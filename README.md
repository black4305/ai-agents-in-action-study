# AI 에이전트 인 액션 - 학습 프로젝트

> **"AI 에이전트 인 액션: 설계와 구현, 배포까지, 그동안 궁금했던 AI 에이전트 개발의 모든 것"** 교재의 예제 코드를 실습하고 학습하기 위한 프로젝트입니다.

## 도서 정보

| 항목 | 내용 |
|------|------|
| **원서** | AI Agents in Action (Manning Publications) |
| **저자** | Micheal Lanham |
| **역자** | 류광, 307번역랩 |
| **출판사** | 위키북스 (생성형 AI 프로그래밍 시리즈_018) |
| **출판일** | 2025년 7월 10일 |
| **ISBN** | 9791158396176 |
| **페이지** | 380쪽 |

## 목차 및 챕터 구성

이 프로젝트는 교재의 챕터별 예제 코드를 정리한 구조입니다. (1장은 이론 중심이므로 코드 없음)

### 02장. LLM의 능력 발휘 (`chapter_02/`)
프롬프트 엔지니어링의 기초와 LLM 연동 방법을 다룹니다.
- OpenAI API 연결 및 대화 관리
- 프롬프트 엔지니어링 기법 (페르소나 설정, Few-shot 학습, 단계별 지시 등)
- JSON 형식의 구조화된 출력 생성
- 로컬 LLM 서버 (LM Studio) 연동

### 03장. GPT 어시스턴트 활용 (`chapter_03/`)
OpenAI Assistants API를 활용한 어시스턴트 구축과 대규모 데이터 처리를 다룹니다.
- 커스텀 액션 어시스턴트 설계
- 데이터 탐색 어시스턴트 (Data Scout)
- 작업 관리 어시스턴트 (Task Organizer)
- 구텐베르크 프로젝트 텍스트 데이터 활용

### 04장. 다중 에이전트 시스템 살펴보기 (`chapter_04/`)
AutoGen과 CrewAI 프레임워크를 활용한 멀티 에이전트 시스템을 구축합니다.
- AutoGen: 에이전트 간 통신, 코드 리뷰 에이전트, 그룹 협업
- CrewAI: 팀 기반 워크플로우, 계층적 에이전트 구조
- 이미지 이해 및 비전 작업

### 05장. 행동을 통한 에이전트 기능 강화 (`chapter_05/`)
Microsoft Semantic Kernel(SK) 프레임워크를 활용한 지능형 애플리케이션 개발을 다룹니다.
- SK 함수 및 스킬 정의
- 병렬 함수 실행
- 시맨틱/네이티브 함수 통합
- 외부 서비스 연동 (TMDB 영화 추천)
- SK 콘솔 앱 프로젝트 구조

### 06장. 자율 어시스턴트 구축 (`chapter_06/`)
에이전트 계획 및 의사결정을 위한 행동 트리(Behavior Tree) 구조를 학습합니다.
- py_trees 라이브러리를 활용한 행동 트리 구현
- 조건-행동 패턴 및 상태 기반 관리

### 07장. 에이전트 플랫폼의 구축과 활용 (`chapter_07/`)
실시간 스트리밍 채팅 애플리케이션을 구축합니다.
- ChatGPT 클론 구현 (일반 응답 / 스트리밍 응답)
- 실시간 사용자 인터페이스 개발

### 08장. 에이전트의 기억과 지식 (`chapter_08/`)
벡터 데이터베이스, 임베딩, RAG(검색 증강 생성) 패턴을 다룹니다.
- ChromaDB 벡터 데이터베이스 활용
- 문서 임베딩 및 유사도 검색
- LangChain을 활용한 문서 로딩, 청킹, 압축 검색
- Semantic Kernel 시맨틱 메모리 구현

### 09장. 프롬프트 흐름을 이용한 효과적인 에이전트 프롬프팅 (`chapter_09/`)
Microsoft Prompt Flow 프레임워크를 활용한 LLM 워크플로우를 설계합니다.
- Q-러닝 에이전트와 시맨틱 메모리
- DAG 기반 워크플로우 설계
- Jinja2 템플릿을 활용한 프롬프트 구성
- 배치 처리 및 평가 메트릭

### 10장. 에이전트의 추론과 평가 (`chapter_10/`)
복잡한 추론을 위한 고급 프롬프팅 기법을 학습합니다.
- 프롬프트 체이닝 (Prompt Chaining)
- Zero-shot Chain-of-Thought 프롬프팅
- 자기 일관성(Self-Consistency) 평가
- 다단계 추론 워크플로우

### 11장. 에이전트의 계획과 피드백 (`chapter_11/`)
OpenAI Assistants API의 고급 기능과 다양한 UI 프레임워크를 활용한 배포를 다룹니다.
- Assistants API 고급 기능 (스트리밍, 파일 처리)
- Gradio를 활용한 챗봇 UI 구축
- Streamlit을 활용한 어시스턴트 관리 및 플레이그라운드
- 웹캠 등 멀티모달 입력 통합

## 기술 스택

- **언어**: Python
- **LLM**: OpenAI GPT 시리즈
- **에이전트 프레임워크**: AutoGen, CrewAI, Semantic Kernel
- **벡터 DB**: ChromaDB
- **워크플로우**: Microsoft Prompt Flow
- **UI**: Gradio, Streamlit
- **기타**: LangChain, py_trees

## 시작하기

### 사전 요구사항
- Python 3.10 이상
- OpenAI API 키

### 설치 및 실행

```bash
# 저장소 클론
git clone https://github.com/black4305/ai-agents-in-action-study.git
cd ai-agents-in-action-study

# 가상환경 생성 및 활성화
python -m venv .venv
source .venv/bin/activate  # macOS/Linux

# 환경 변수 설정
cp .env.example .env
# .env 파일에 OPENAI_API_KEY 등 API 키 입력
```

> 각 챕터별로 필요한 패키지가 다를 수 있으므로, 챕터 디렉토리 내의 안내를 참고하세요.

## 프로젝트 구조

```
ai-agents-in-action-study/
├── chapter_02/          # LLM의 능력 발휘
├── chapter_03/          # GPT 어시스턴트 활용
├── chapter_04/          # 다중 에이전트 시스템
├── chapter_05/          # 행동을 통한 에이전트 기능 강화
├── chapter_06/          # 자율 어시스턴트 구축
├── chapter_07/          # 에이전트 플랫폼 구축과 활용
├── chapter_08/          # 에이전트의 기억과 지식
├── chapter_09/          # 프롬프트 흐름을 이용한 프롬프팅
├── chapter_10/          # 에이전트의 추론과 평가
├── chapter_11/          # 에이전트의 계획과 피드백
├── .gitignore
└── README.md
```

## 참고 자료

- [원서 (Manning Publications)](https://www.manning.com/books/ai-agents-in-action)
- [교보문고 (한국어판)](https://product.kyobobook.co.kr/detail/S000216967209)
- [위키북스 도서 페이지](https://wikibook.co.kr/ai-agents/)
- [원서 공식 예제 코드 (GitHub)](https://github.com/cxbxmxcx/GPT-Agents)

## 라이선스

이 프로젝트는 학습 목적으로 작성되었으며, 교재의 예제 코드에 대한 저작권은 원저자 및 출판사에 있습니다.
