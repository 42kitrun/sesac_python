from langchain_core.prompts import PromptTemplate
from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

llm = OpenAI() # 필요시 모델, 키, 온도 등을 설정한다
# 여기는 사용자가 입력한 문장의 뒷부분을 이어서 텍스트(문장, 단어 등)를 생성하는 Completion 모델(instruct)이 필요하겠다
template = "You are a naming consultant. Suggest a name for a company that makes {product}"

prompt = PromptTemplate(
    input_variables=['product'],
    template=template
)

print("새 회사 이름을 생성하는 서비스 입니다. 종료하려면 'quit' 또는 'exit' 를 입력하세요\n")
while True:
    product = input("제품/서비스를 입력하세요: ").strip()
    if product in {"quit", "exit"}:
        print("종료합니다.")
        break
    
    filled_prompt = prompt.format(product=product)
    response = llm.invoke(filled_prompt)
    print("생성된 회사명: ", response.strip())