import streamlit as st
from openai import OpenAI

# 🔑 OpenAI API Key (환경변수로 저장 권장)
import os
from dotenv import load_dotenv

load_dotenv("openaiAPI.env") # .env 파일에서 환경변수 로드
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

# Streamlit 앱 설정
st.title("🎁기념일 메시지, 선물 추천 프롬프트")
st.markdown("어떻게 말하고 뭘 선물할지 고민될 때, 너의 말투로 축하 메시지와 선물까지 추천해줄게!")

# 사용자 입력
relation = st.selectbox("🎈 누구에게 보내나요?", ["친구", "연인", "가족", "직장 동료"])
event = st.text_input("💌 기념일 종류 (예: 생일, 입학, 승진 등)")
tone = st.selectbox("🗣️ 말투 톤", ["친근한", "격식 있는", "다정한", "웃긴"])
user_style = st.text_area("📝 너의 상황과, 말투 예시 (사용자 상황, 대상과 사용자와의 관계, 대상의 취향 등 자유롭게 작성)")
keyword = st.text_input("💡 포함하고 싶은 키워드 (선택사항)")

def generate_prompts(relation, event, tone, user_style, keyword):
    prompts = []

    # A. 선물 추천
    prompts.append(f"""
다음 예시를 참고해서 이벤트와 대상에 맞는 선물을 세가지 정도 추천해줘.
말투 예시: "{user_style}"
대상: {relation}
이벤트: {event}
""")

    # B. 규칙 기반
    prompts.append(f"""
아래 예시를 규칙으로 메시지를 작성해줘
- 말투 예시: "{user_style}"
- 대상: {relation}
- 이벤트: {event}
- 키워드: {keyword}
- 말투 톤: {tone}
메시지는 3문장 이내로 문맥에 맞고 자연스럽게 써줘.
""")

    # C. 역할 기반 설정
    prompts.append(f"""
너가 사용자가 됐다고 몰입하고, 대상과의 관계와 말투를 생각해서
다음 정보를 참고해 메시지를 아주 자연스럽게 작성해줘.
- 말투 예시: "{user_style}"
- 대상: {relation}
- 이벤트: {event}
- 말투 톤: {tone}
- 키워드: {keyword}
""")

    return prompts

if st.button("✨ 프롬프트 추천 시작"):
    if not user_style or not event:
        st.warning("⚠️ 말투 예시와 기념일 종류는 꼭 입력해주세요!")
    else:
        prompts = generate_prompts(relation, event, tone, user_style, keyword)

        labels = ["🎁 선물 추천", "💌 메시지1 추천", "💌 메시지2 추천"]
        for i, prompt in enumerate(prompts):
            with st.spinner(f"프롬프트 {labels[i]} 실행 중..."):
                res = client.chat.completions.create(
                    model="gpt-4-turbo",
                    messages=[{"role": "user", "content": prompt}],
                    temperature = 0.3
                )
                output = res.choices[0].message.content

            st.subheader(f"{labels[i]} 결과")
            st.markdown(output)  # 자동 줄바꿈!
            st.divider()
