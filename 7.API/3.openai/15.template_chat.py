from dotenv import load_dotenv

from langchain_core.prompts import PromptTemplate  # 이전까지 배운거 <- Completion(instruct)
from langchain_core.prompts import ChatPromptTemplate   # 지금부터 할거 <- QA(Chat 모델)
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.runnables import RunnableLambda

from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
# 여러 번 문답(질문, 재질문)을 주고받을 때 대화의 흐름을 이해하며 적절하게 답변하는 QA: Question-Answering 모델(Chat 모델)
# Chat 모델로 chain 만들기
# 1. 프롬프트 템플릿 생성
prompt = ChatPromptTemplate.from_messages([
    SystemMessage(content="You are a naming consultant for new companies"),
    HumanMessage(content="What is a good name for a {company} that makes {product}?")
])

# 아래는 현업에서 많이 쓰는 축약형
# prompt_short = ChatPromptTemplate.from_messages([
#     ('system', 'You are a naming consultant for new companies'),
#     ('human', 'What is a good name for a {company} that makes {product}?')
# ])

# 2. 모델 생성
llm = ChatOpenAI(model='gpt-3.5-turbo')  # chat 모델중에 하나를 고를것

# 3. 파서 생성
parser = StrOutputParser()

# 4. 입력값 정의 하고 invoke로 호출 3줄로 해도 됨..
# messages = ...
# response = llm.invoke(messages)
# output = parser.invoke(response)
# 위 이런 여러줄의 문장을 LCEL 체이닝으로 처리함..

chain = prompt | llm | parser | RunnableLambda(lambda x: {'response': x})

inputs = {'company': 'high-tech startup', 'product': 'electrical automobile'}
result = chain.invoke(inputs)

print("최종결과:", result)