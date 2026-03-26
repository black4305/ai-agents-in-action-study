import os
from openai import OpenAI
from dotenv import load_dotenv

# .env 파일에 저장된 비밀값을 불러온다.
load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')

# API 키가 설정됐는지 확인한다.
if not api_key:
    raise ValueError("API 키 없음 - .env 파일을 확인하세요.")
# API 키로 client를 생성한다.
client = OpenAI(api_key=api_key)

def ask_chatgpt(user_message):
    response = client.chat.completions.create(
        model='gpt-5.4-nano', # 요청에 응답하는 데 사용할 모델의 ID
        messages=[
            {'role': 'system', 'content': '당신은 유능한 어시스턴트입니다.'}, # 시스템 메시지(시스템 프롬프트)
            {'role': 'user', 'content': user_message} # 사용자 역할 메시지
        ],
        # 가변성을 설정하는 온도 (gpt-5-nano 모델의 경우 기본값인 1만 가능하다는 에러가 있어. 0.7이었는데, 1로 변경)
        temperature=1, # 후행 쉼표(trailing comma): 나중에 인자 추가 시 diff를 깔끔하게 유지하기 위한 Python 관행
    )
    return response.choices[0].message.content

user = "조선인민민주공화국의 수도는?"
response = ask_chatgpt(user)
print(response)