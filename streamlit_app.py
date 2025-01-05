import streamlit as st

# 콤보박스(Selectbox)에서 선택 시 한글 → 영어로 매핑되는 사전
TRANSLATION_DICT = {
    "행복하다": "happy",
    "화려하다": "fancy",
    "날고 있다": "flying",
    "숲": "in a forest",
    "미래 도시": "in a futuristic city",
    "우주": "in space",
    "햇빛": "lit by sunlight",
    "네온": "lit by neon lights",
    "달빛": "lit by moonlight",
    "따뜻한 색조": "with warm tones",
    "차가운 색조": "with cool tones",
    "네온 색상": "with neon colors",
    "눈높이": "viewed from eye level",
    "조감도": "viewed from above",
    "저각도": "viewed from below",
    "느와르": "in a noir style",
    "사이버펑크": "in a cyberpunk style",
    "픽셀 아트": "in pixel art style"
}

# 콤보박스에 표시할 기본 리스트 (사전 key 들)
COMBO_VALUES = list(TRANSLATION_DICT.keys())


def translate_or_keep(text: str) -> str:
    """
    TRANSLATION_DICT에 있는 한글 키를 선택했으면 영어로 번역,
    없으면(직접 입력하거나 사전에 없는 항목) 그대로 사용.
    """
    text = text.strip()
    if text in TRANSLATION_DICT:
        return TRANSLATION_DICT[text]
    return text  # 사전에 없으면 그대로 사용


def main():
    st.title("GPT O1 Pro - 프롬프트 생성기 (Streamlit 버전)")

    # 도움말(Help) Expander
    with st.expander("도움말"):
        help_text = (
            "**[사용법]**\n\n"
            "1. **메인 주제**: 원하는 대상(한글/영어) 입력.\n"
            "2. **설명/주변환경/조명/색감/관점/스타일**: Selectbox에서 선택하거나 직접 한글 입력.\n"
            "   - Selectbox 목록에 있는 항목은 자동으로 영어로 변환.\n"
            "   - 없는 항목은 그대로 사용.\n"
            "3. **[만들기]** 버튼을 누르면 아래에 완성된 프롬프트가 표시.\n\n"
            "**[스타일 예시]**\n"
            " - 느와르(Noir): 어두운 톤과 강렬한 대비를 특징으로 하는 고전 탐정 영화 스타일\n"
            " - 사이버펑크(Cyberpunk): 미래적 기술과 네온 색이 강조된 디스토피아 세계\n"
            " - 픽셀 아트(Pixel Art): 도트 기반 레트로 스타일 그래픽\n"
            " - 스팀펑크(SteamPunk): 증기기관 기반 19세기 산업혁명 세계관\n"
            " - 초현실주의(Surrealism): 현실과 비현실 경계가 무너진 환상적 장면 표현\n"
            " - 미니멀리즘(Minimalism): 단순화된 요소로 구성, 불필요한 디테일 배제\n"
        )
        st.markdown(help_text)

    # 메인 주제
    main_subject = st.text_input("메인 주제 (한글/영어 모두 가능)", value="")

    # 설명(Selectbox & 직접입력)
    desc_option = st.selectbox("설명 (선택)", options=[""] + COMBO_VALUES, index=0)
    desc_custom = st.text_input("설명 (직접입력)", value="")
    # 콤보박스 선택이 비어있고 직접 입력이 있으면 직접 입력 사용, 그 외 콤보박스 우선
    desc = desc_custom if (desc_option == "" and desc_custom != "") else desc_option

    # 주변 환경
    env_option = st.selectbox("주변 환경 (선택)", options=[""] + COMBO_VALUES, index=0)
    env_custom = st.text_input("주변 환경 (직접입력)", value="")
    env = env_custom if (env_option == "" and env_custom != "") else env_option

    # 조명
    light_option = st.selectbox("조명 (선택)", options=[""] + COMBO_VALUES, index=0)
    light_custom = st.text_input("조명 (직접입력)", value="")
    light = light_custom if (light_option == "" and light_custom != "") else light_option

    # 색감
    color_option = st.selectbox("색감 (선택)", options=[""] + COMBO_VALUES, index=0)
    color_custom = st.text_input("색감 (직접입력)", value="")
    color = color_custom if (color_option == "" and color_custom != "") else color_option

    # 관점
    persp_option = st.selectbox("관점 (선택)", options=[""] + COMBO_VALUES, index=0)
    persp_custom = st.text_input("관점 (직접입력)", value="")
    persp = persp_custom if (persp_option == "" and persp_custom != "") else persp_option

    # 스타일
    style_option = st.selectbox("스타일 (선택)", options=[""] + COMBO_VALUES, index=0)
    style_custom = st.text_input("스타일 (직접입력)", value="")
    style_ = style_custom if (style_option == "" and style_custom != "") else style_option

    # 만들기 버튼
    if st.button("만들기"):
        # 번역 또는 그대로 유지
        desc_translated = translate_or_keep(desc)
        env_translated = translate_or_keep(env)
        light_translated = translate_or_keep(light)
        color_translated = translate_or_keep(color)
        persp_translated = translate_or_keep(persp)
        style_translated = translate_or_keep(style_)

        # 필요한 부분만 쉼표로 연결
        prompt_parts = []

        if main_subject.strip():
            prompt_parts.append(main_subject.strip())
        if desc_translated.strip():
            prompt_parts.append(desc_translated.strip())
        if env_translated.strip():
            prompt_parts.append(env_translated.strip())
        if light_translated.strip():
            prompt_parts.append(light_translated.strip())
        if color_translated.strip():
            prompt_parts.append(color_translated.strip())
        if persp_translated.strip():
            prompt_parts.append(persp_translated.strip())
        if style_translated.strip():
            prompt_parts.append(style_translated.strip())

        final_prompt = ", ".join(prompt_parts)
        if final_prompt:
            final_prompt += "."

        st.subheader("생성된 프롬프트:")
        st.write(final_prompt)


if __name__ == "__main__":
    main()
