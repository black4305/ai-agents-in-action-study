# 다양한 프롬프트 엔지니어링 전술들의 사용법을 이해하는데 도움이 되는 다양한 프롬프트 예시를 포함한 코드

import os
import json

# prompt_utils.py에 정의된 prompt_llm 함수를 가져온다.
# prompt_llm()은 내부적으로 OpenAI API를 호출하는 함수인데,
# model 파라미터의 기본값이 "gpt-5.4-nano"로 설정되어 있다.
# 즉, 호출할 때 model을 따로 지정하지 않으면 이 기본값이 사용된다.
from prompt_utils import prompt_llm

def list_text_files_in_directory(directory):
    text_files = []
    for filename in os.listdir(directory):
        if filename.startswith('_'):
            continue
        if filename.endswith(".jsonl"):
            text_files.append(filename)
    return text_files

def load_and_parse_json_file(file_path):
    data = []
    with open(file_path, 'r', encoding='utf-8') as file:
        json_text = ""
        for line in file:
            line = line.strip()
            json_text += line
            if line == "]":
                try:
                    json_data = json.loads(json_text)
                    data.append(json_data)
                except json.JSONDecodeError as e:
                    print(f"Error decoding JSON: {json_text}")
                    print(e)
                json_text = ""    
    return data


# 메인 함수
# 1) prompts 폴더의 모든 jsonl 파일을 불러오고, 그 중 하나를 사용자가 선택하게 함
# 2) 특정 jsonl 파일을 선택하면, 그 파일에 담긴 프롬프트를 LLM에 요청하고 응답을 출력
def main():
    directory = "prompts"
    text_files = list_text_files_in_directory(directory) # 주어진 폴더(이 코드에선 prompts)의 모든 파일을 모으는 역할

    if not text_files:
        print("No text files found in the directory.")
        return
    
    def print_available():
        print("Available prompt tactics:")
        for i, filename in enumerate(text_files, start=1):
            print(f"{i}. {filename}")

    while True:
        try:
            # 파일 목록을 선택지로 출력
            print_available()

            # 사용자의 선택을 입력 받음
            choice = int(input("Enter the number of the prompt tactic to run (or 0 to exit): "))
            if choice == 0:
                break
            elif 1 <= choice <= len(text_files):
                selected_file = text_files[choice - 1]
                file_path = os.path.join(directory, selected_file)
                
                # 해당 프롬프트 파일을 파싱해서 메시지들을 만듦
                prompts = load_and_parse_json_file(file_path)
                print(f"Running prompts for {selected_file}")                
                for i, prompt in enumerate(prompts):
                    print(f"PROMPT {i+1} -------------------------------------------------")
                    print(prompt)
                    print(f"REPLY -------------------------------------------------")
                    
                    # OpenAI 모델 사용
                    print(prompt_llm(prompt))

                    # 로컬 LLM 사용
                    # print(prompt_llm(prompt, 
                    #                  model="local-model", 
                    #                  base_url="http://localhost:1234/v1",
                    #                  api_key="not used"))
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()


# =============================================================================
# [개념 정리]
# =============================================================================
#
# 1. 파싱(Parsing)이란?
# --------------------
# "파싱"은 텍스트 데이터를 읽어서, 프로그램이 이해할 수 있는 구조로 변환하는 것이다.
#
# 예를 들어, 아래와 같은 텍스트가 있다고 하자:
#   '{"role": "user", "content": "안녕"}'
#
# 이건 사람 눈에는 데이터처럼 보이지만, 파이썬 입장에서는 그냥 "문자열 한 덩어리"일 뿐이다.
# 여기서 json.loads()를 쓰면:
#   {"role": "user", "content": "안녕"}  ← 파이썬 딕셔너리(dict)
# 이렇게 키-값으로 접근 가능한 구조로 바뀐다.
#
# 이 변환 과정 자체를 "파싱"이라고 부른다.
# 위 코드의 load_and_parse_json_file() 함수가 하는 일이 바로 이것이다:
#   파일의 텍스트 → json.loads() → 파이썬 리스트/딕셔너리
#
#
# 2. JSONL vs JSON
# ----------------
# JSON (.json)
#   - 파일 전체가 하나의 JSON 구조 (보통 하나의 객체 {} 또는 배열 [])
#   - 예시:
#       [
#         {"role": "system", "content": "너는 도우미야"},
#         {"role": "user", "content": "안녕"}
#       ]
#
# JSONL (.jsonl) — JSON Lines
#   - 한 줄에 하나의 독립된 JSON 객체가 들어간다.
#   - 줄바꿈(\n)이 구분자 역할을 한다.
#   - 예시:
#       {"role": "system", "content": "너는 도우미야"}
#       {"role": "user", "content": "안녕"}
#
# 왜 JSONL을 쓸까?
#   - 한 줄씩 읽으면서 처리할 수 있어서, 대용량 데이터에 유리하다.
#   - JSON은 파일 전체를 한 번에 메모리에 올려야 하지만,
#     JSONL은 한 줄씩 읽고 버릴 수 있다.
#   - LLM 학습 데이터, 로그, 프롬프트 모음 등에서 자주 쓰인다.
#
# 참고: 이 프로젝트의 prompts/ 폴더에 있는 .jsonl 파일들은
#       각각 하나의 프롬프트 전술(tactic)에 해당하는 메시지 배열을 담고 있다.
# =============================================================================