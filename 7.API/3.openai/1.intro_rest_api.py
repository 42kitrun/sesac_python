from dotenv import load_dotenv
import os
import requests, json

load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

response = requests.post('https://api.openai.com/v1/chat/completions',
    json = {
        'model':'gpt-4o',
        # 'input':'Write a one-sentence bedtime story about a unicorn'
        'messages':[
            # {"role": "user",
            #  "content":"잠자리에 들기 전에 양에 대한 스토리를 한문장 말해주시오."
            # }
            {"role": "user",
             "content":"오늘 저녁 메뉴는?"
            }
        ]
    },
    headers={
        'Content-Type':'application/json',
        'Authorization':f'Bearer {OPENAI_API_KEY}',
    }
)

response_data = response.json()
print(response_data['choices'][0]['message']['content'])
# https://api.openai.com/v1/responses =>>> print(response_data['output'][0]['content'][0]['text'])

