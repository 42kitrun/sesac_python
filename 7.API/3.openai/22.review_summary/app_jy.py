from dotenv import load_dotenv
import os

from flask import Flask, request, jsonify
from openai import OpenAI

from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

# app = Flask(__name__, static_folder='static', static_url_path='static')
app = Flask(__name__, static_folder='public', static_url_path='')

# openai = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
openai = OpenAI()

parser = StrOutputParser()

reviews = [] # 사용자 후기를 저장할 DB
translation_language ={
    "kor" : "한국어",
    "eng" : "영어",
    "jpn" : "일본어",
    "fra" : "프랑스어",
    "ita" : "이탈리아어"
}


@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/api/reviews', methods=['POST'])
def add_review():
    data = request.get_json()
    rating = data.get('rating')
    opinion = data.get('opinion')
    
    reviews.append({'rating': rating, 'opinion': opinion})
    
    return jsonify({'message':'성공적으로 저장됨'})

@app.route('/api/reviews', methods=['GET'])
def get_reviews():
    return jsonify({'reviews': reviews})

@app.route('/api/ai-summary', methods=['GET','POST'])
def get_ai_summary():
    target_lang = 'kor'
    if request.method == 'POST':
        target_lang = request.form.get('lang','kor')
    else:
        target_lang = request.args.get('lang','kor')
    
    print('언어: ',target_lang)
    
    if not reviews:
        return jsonify({'summary': '리뷰가 없습니다.', 'averageRating': 0.0})

    average_rating = sum(r['rating'] for r in reviews) / len(reviews)
    reviews_text = '\n'.join([f"별점: {r['rating']}, 내용: {r['opinion']}" for r in reviews])
    
    print("리뷰내용 통합: ", reviews_text)
    
    try:
        # 아래도 try catch 로 꼭 감싸야 함.. key가 없거나, 돈이 다 떨어졌거나, 서버가 죽었거나, 여러가지 이유로 요청에 실패할수 있음.
        response = openai.chat.completions.create(
            model='gpt-3.5-turbo',
            messages=[{
                'role': 'user',
                'content': f'다음 리뷰 목록을 기반으로 간결하게 한줄로 요약해 주세요.\n\n{reviews_text}'
            }]
        )
    except:
        return jsonify({'summary': 'OpenAI와의 연결이 원활하지 않습니다', 'averageRating': 0.0})

    summary = response.choices[0].message.content.strip()
    print("요약리뷰내용: ", summary)

    # 미션1. 프런트에서 보낸 언어 "코드값" 으로, 원하는 언어로 매핑을 한다.
    # 미션2. 그걸 기반으로, GPT에게 해당 언어로 요약을 만들어 달라고 한다.
    #       하나의 프롬프트로 할지, 아니면 두번의 스탭으로 나눠서 (한번은 요약, 한번은 번역) 이렇게 할지 고민해보기
    if target_lang != 'kor':
        prompt = PromptTemplate(
        input_variables=['language', 'sentence'],
        template='다음 문장을 {language}로 번역하시오. {sentence}'
        )

        chain = prompt | openai | parser

        inputs = {'language': translation_language[target_lang],
                  'sentence': summary}

        reviews = chain.invoke(inputs)

    return jsonify({'summary': summary, 'averageRating': average_rating})

if __name__ == '__main__':
    app.run(port=5000, debug=True)