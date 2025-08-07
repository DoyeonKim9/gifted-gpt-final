#  🎁 Gifted-GPT

**Gifted-GPT**는 사용자의 말투와 상황을 바탕으로  
GPT를 활용해 **기념일 메시지**와 **선물 추천**을 자동으로 생성해주는 Streamlit 기반 미니 프로젝트입니다.

---

## ✨ Features

- 🎈 **관계 선택**: 친구 / 연인 / 가족 / 직장 동료 중 선택
- 💌 **기념일 종류 입력**: 생일, 입학, 승진 등 자유 입력
- 🗣️ **말투 선택**: 친근한 / 격식 있는 / 다정한 / 웃긴 톤 중 선택
- 📝 **사용자 말투 예시 입력**: 자연스러운 대화 스타일 반영
- 💡 **키워드 입력 (선택사항)**: 메시지나 선물에 포함될 키워드 입력 가능
- 🎁 **GPT 기반 추천**:
  - 상황과 말투에 맞는 **선물 3가지 추천**
  - 서로 다른 전략(prompt)을 통해 생성된 **메시지 2종 추천**

---

## 🛠 Tech Stack

- **Frontend**: [Streamlit](https://streamlit.io/)
- **LLM API**: [OpenAI GPT-4 Turbo](https://platform.openai.com/)
- **언어**: Python

---

## 🚀 Getting Started

1. 이 레포를 클론합니다.

```bash
# 1. Clone the repository
git clone https://github.com/DoyeonKim9/gifted-gpt-final.git
cd gifted-gpt-final

# 2. Install dependencies
pip install -r requirements.txt

# 3. Set your OpenAI API key
export OPENAI_API_KEY=your-api-key

# 4. Run the app (예: Streamlit 기준)
streamlit run GiftedGpt.py
