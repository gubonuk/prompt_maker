import streamlit as st
def main():
    st.title("GPT O1 Pro - 프롬프트 생성기 (Streamlit 버전)")

    # 도움말(Help) Expander
    with st.expander("도움말"):
        st.markdown(
            "**[사용법]**\n\n"
            "1. **메인 주제**: 원하는 대상(한글/영어) 입력.\n"
            "2. 각 카테고리에 대해 선택하거나 직접 입력.\n"
            "3. **[만들기]** 버튼을 누르면 프롬프트가 생성됩니다."
        )

    # 메인 주제
    main_subject = st.text_input("메인 주제 (한글/영어 모두 가능)", value="")

    # 각 카테고리별 옵션 및 입력 UI
    desc_option = st.selectbox("설명", options=["행복하다", "슬프다", "화려하다", "차분하다", "날고 있다", "뛰고 있다", "웃고 있다", "울고 있다", "놀라고 있다"])
    env_option = st.selectbox("주변 환경", options=["숲", "미래 도시", "우주", "바다", "사막", "도시 거리", "농촌 마을", "산속", "하늘 위"])
    light_option = st.selectbox("조명", options=["햇빛", "네온", "달빛", "캠프파이어", "촛불", "별빛", "전구 빛", "자연광", "스포트라이트"])
    color_option = st.selectbox("색감", options=["따뜻한 색조", "차가운 색조", "네온 색상", "파스텔 색감", "모노크롬", "컬러풀", "황금빛", "회색빛", "강렬한 대비"])
    persp_option = st.selectbox("관점", options=["눈높이", "조감도", "저각도", "일반적인 시야", "멀리서", "근접해서", "뒤에서", "옆에서", "움직이는 시점"])
    style_option = st.selectbox("스타일", options=["느와르", "사이버펑크", "픽셀 아트", "스팀펑크", "초현실주의", "미니멀리즘", "고전적", "현대적", "추상적", "레트로"])

    # 선택된 값을 확인
    st.markdown("### 선택된 옵션")
    st.write(f"**설명**: {desc_option}")
    st.write(f"**주변 환경**: {env_option}")
    st.write(f"**조명**: {light_option}")
    st.write(f"**색감**: {color_option}")
    st.write(f"**관점**: {persp_option}")
    st.write(f"**스타일**: {style_option}")

    # 만들기 버튼
    if st.button("만들기"):
        # 번역 또는 그대로 유지
        desc_translated = translate_or_keep(desc_option)
        env_translated = translate_or_keep(env_option)
        light_translated = translate_or_keep(light_option)
        color_translated = translate_or_keep(color_option)
        persp_translated = translate_or_keep(persp_option)
        style_translated = translate_or_keep(style_option)

        # 필요한 부분만 쉼표로 연결
        prompt_parts = [main_subject.strip()] if main_subject.strip() else []
        prompt_parts.extend([
            desc_translated,
            env_translated,
            light_translated,
            color_translated,
            persp_translated,
            style_translated
        ])

        final_prompt = ", ".join(prompt_parts)
        if final_prompt:
            final_prompt += "."

        st.subheader("생성된 프롬프트:")
        st.write(final_prompt)


if __name__ == "__main__":
    main()
