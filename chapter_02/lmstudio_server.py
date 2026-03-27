from openai import OpenAI

# LM Studio에서 모델 다운로드 후 서버를 실행해야함
client = OpenAI(base_url="http://localhost:1234/v1", api_key="not-needed")

completion = client.chat.completions.create(
  model="Nvidia/Nemotron-3-Nano-4B", # 아무 이름이나 가능
  messages=[
    {"role": "system", "content": "항상 라임을 맞춰서 응답하세요."},
    {"role": "user", "content": "너는 누구니?"} # 원하는 메시지로 변경 가능
  ],
  temperature=0.4,
)

# 응답 전체 출력
print(completion.choices[0].message)

# 문제가 없다면 LM Studio의 Developer Logs에서 확인 가능