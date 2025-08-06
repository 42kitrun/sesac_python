from dotenv import load_dotenv
import os

from flask import Flask, request, jsonify
from openai import OpenAI

load_dotenv()

# app = Flask(__name__, static_folder='static', static_url_path='static')
app = Flask(__name__, static_folder='public', static_url_path='')
# openai = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
openai = OpenAI()

reviews = [] # 사용자 후기를 저장할 DB

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

@app.route('/api/ai-summary', methods=['GET'])
def get_ai_summary():
    target_lang = request.args.get('lang', 'ko')
    lang_name_map = {
        'ko': '한국어',
        'en': '영어',
        'ja': '일본어',
        'zh': '중국어',
        'fr': '프랑스어',
        'it': '이탈리아어',
    }
    
    lang_name = lang_name_map.get(target_lang, '한국어')
    print(f'언어: {target_lang}, 언어명: {lang_name}')
    
    # 미션1. 프런트에서 보낸 언어 "코드값" 으로, 원하는 언어로 매핑을 한다.
    # 미션2. 그걸 기반으로, GPT에게 해당 언어로 요약을 만들어 달라고 한다.
    #       하나의 프롬프로 할지, 아니면 두번의 스탭으로 나눠서 (한번은 요약, 한번은 번역) 이렇게 할지 고민해보기...
    
    if not reviews:
        return jsonify({'summary': '리뷰가 없습니다.', 'averageRating': 0.0})

    average_rating = sum(r['rating'] for r in reviews) / len(reviews)
    reviews_text = '\n'.join([f"별점: {r['rating']}, 내용: {r['opinion']}" for r in reviews])
    
    print("리뷰내용 통합: ", reviews_text)
    
    # 아래도 try catch 로 꼭 감싸야 함.. key가 없거나, 돈이 다 떨어졌거나, 서버가 죽었거나, 여러가지 이유로 요청에 실패할수 있음.
    response_summary = openai.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=[{
            'role': 'user',
            'content': f'다음 리뷰 목록을 기반으로 간결하게 요약해 주세요.\n\n{reviews_text}'
        }] # 어떻게 잘 이 문장을 만들것이냐? 프롬프트 엔지니어링.
    )
    
    summary = response_summary.choices[0].message.content.strip()
    print("요약내용: ", summary)
    
    response_translated = openai.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=[{
            'role': 'system', 'content': 'You are a professional language translator.',
            'role': 'user',
            'content': f'다음 문장을 {lang_name}로 번역하여 해당 언어로만 출력해 주세요.\n\n{summary}'
        }], # 어떻게 잘 이 문장을 만들것이냐? 프롬프트 엔지니어링.
        temperature=0.2
    )
    
    final_text = response_translated.choices[0].message.content.strip()
    print("요약번역내용: ", final_text)
    return jsonify({'summary': final_text, 'averageRating': average_rating})

if __name__ == '__main__':
    app.run(port=5000, debug=True)