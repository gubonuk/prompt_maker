import streamlit as st

def translate_or_keep(text: str) -> str:
    """
    TRANSLATION_DICT에 있는 한글 키를 선택했으면 영어로 번역,
    없으면 그대로 사용.
    """
    TRANSLATION_DICT = {
        "행복하다": "happy",
        "슬프다": "sad",
        "화려하다": "fancy",
        "차분하다": "calm",
        "날고 있다": "flying",
        "뛰고 있다": "running",
        "웃고 있다": "smiling",
        "울고 있다": "crying",
        "놀라고 있다": "surprised",
        "숲": "in a forest",
        "미래 도시": "in a futuristic city",
        "우주": "in space",
        "바다": "by the sea",
        "사막": "in a desert",
        "도시 거리": "on a city street",
        "농촌 마을": "in a rural village",
        "산속": "in the mountains",
        "하늘 위": "in the sky",
        "햇빛": "lit by sunlight",
        "네온": "lit by neon lights",
        "달빛": "lit by moonlight",
        "캠프파이어": "lit by a campfire",
        "촛불": "lit by candlelight",
        "별빛": "lit by starlight",
        "전구 빛": "lit by bulb light",
        "자연광": "lit by natural light",
        "스포트라이트": "lit by a spotlight",
        "따뜻한 색조": "with warm tones",
        "차가운 색조": "with cool tones",
        "네온 색상": "with neon colors",
        "파스텔 색감": "with pastel colors",
        "모노크롬": "in monochrome",
        "컬러풀": "with colorful tones",
        "황금빛": "with golden hues",
        "회색빛": "with grayish tones",
        "강렬한 대비": "with high contrast",
        "눈높이": "viewed from eye level",
        "조감도": "viewed from above",
        "저각도": "viewed from below",
        "일반적인 시야": "viewed from a normal perspective",
        "멀리서": "viewed from afar",
        "근접해서": "viewed up close",
        "뒤에서": "viewed from behind",
        "옆에서": "viewed from the side",
        "움직이는 시점": "from a moving perspective",
        "느와르": "in a noir style",
        "사이버펑크": "in a cyberpunk style",
        "픽셀 아트": "in pixel art style",
        "스팀펑크": "in steampunk style",
        "초현실주의": "in surrealist style",
        "미니멀리즘": "in minimalist style",
        "고전적": "in a classic style",
        "현대적": "in a modern style",
        "추상적": "in an abstract style",
        "레트로": "in a retro style"
    }
    return TRANSLATION_DICT.get(text, text)  # 사전에 없으면 그대로 반환

def main():
    st.title("GPT O1 Pro - 프롬프트 생성기 (Streamlit 버전)")

    # 메인 주제
    main_subject = st.text_input("메인 주제 (한글/영어 모두 가능)", value="")

    # 각 카테고리별 옵션 및 선택
    desc_option = st.selectbox("설명 (선택)", options=["", "행복하다", "슬프다", "화려하다", "차분하다", "날고 있다", "뛰고 있다", "웃고 있다", "울고 있다", "놀라고 있다"], index=0)
    desc_custom = st.text_input("설명 (직접 입력)", value="")
    desc = desc_custom if desc_custom.strip() else desc_option

    env_option = st.selectbox("주변 환경 (선택)", options=["", "숲", "미래 도시", "우주", "바다", "사막", "도시 거리", "농촌 마을", "산속", "하늘 위"], index=0)
    env_custom = st.text_input("주변 환경 (직접 입력)", value="")
    env = env_custom if env_custom.strip() else env_option

    light_option = st.selectbox("조명 (선택)", options=["", "햇빛", "네온", "달빛", "캠프파이어", "촛불", "별빛", "전구 빛", "자연광", "스포트라이트"], index=0)
    light_custom = st.text_input("조명 (직접 입력)", value="")
    light = light_custom if light_custom.strip() else light_option

    color_option = st.selectbox("색감 (선택)", options=["", "따뜻한 색조", "차가운 색조", "네온 색상", "파스텔 색감", "모노크롬", "컬러풀", "황금빛", "회색빛", "강렬한 대비"], index=0)
    color_custom = st.text_input("색감 (직접 입력)", value="")
    color = color_custom if color_custom.strip() else color_option

    persp_option = st.selectbox("관점 (선택)", options=["", "눈높이", "조감도", "저각도", "일반적인 시야", "멀리서", "근접해서", "뒤에서", "옆에서", "움직이는 시점"], index=0)
    persp_custom = st.text_input("관점 (직접 입력)", value="")
    persp = persp_custom if persp_custom.strip() else persp_option

    style_option = st.selectbox("스타일 (선택)", options=["", "느와르", "사이버펑크", "픽셀 아트", "스팀펑크", "초현실주의", "미니멀리즘", "고전적", "현대적", "추상적", "레트로"], index=0)
    style_custom = st.text_input("스타일 (직접 입력)", value="")
    style = style_custom if style_custom.strip() else style_option

    # 번역된 결과
    desc_translated = translate_or_keep(desc) if not desc_custom.strip() else desc
    env_translated = translate_or_keep(env) if not env_custom.strip() else env
    light_translated = translate_or_keep(light) if not light_custom.strip() else light
    color_translated = translate_or_keep(color) if not color_custom.strip() else color
    persp_translated = translate_or_keep(persp) if not persp_custom.strip() else persp
    style_translated = translate_or_keep(style) if not style_custom.strip() else style

    # 만들기 버튼
    if st.button("만들기"):
        prompt_parts = [main_subject.strip(), desc_translated, env_translated, light_translated, color_translated, persp_translated, style_translated]
        prompt_parts = [part for part in prompt_parts if part]  # 빈 값 제거

        final_prompt = ", ".join(prompt_parts)
        if final_prompt:
            final_prompt += "."

        st.subheader("생성된 프롬프트:")
        st.write(final_prompt)

if __name__ == "__main__":
    main()
