import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.font_manager as fm

# ✅ 한글 폰트 설정 (NanumGothic.otf 파일이 같은 폴더에 있어야 함)
font_path = "./NanumGothic.otf"
fontprop = fm.FontProperties(fname=font_path)
plt.rcParams['font.family'] = fontprop.get_name()

# ✅ 페이지 제목
st.title("사고유형 대분류별 총 피해자 수 시각화")

# ✅ CSV 업로드 받기
uploaded_file = st.file_uploader("CSV 파일을 업로드하세요", type="csv")

if uploaded_file is not None:
    try:
        # ✅ CSV 읽기 (한글 파일이므로 cp949 인코딩 사용)
        df = pd.read_csv(uploaded_file, encoding='cp949')

        # ✅ 공백 제거
        df.columns = df.columns.str.strip()

        # ✅ 숫자형 변환
        cols = ['사망자수', '중상자수', '경상자수']
        df[cols] = df[cols].apply(pd.to_numeric, errors='coerce')

        # ✅ 총 피해자 수 계산
        df['총피해자수'] = df[cols].sum(axis=1)

        # ✅ 사고유형 대분류별 집계
        grouped = df.groupby('사고유형대분류')['총피해자수'].sum().sort_values(ascending=False)

        # ✅ 그래프 시각화
        st.subheader("사고유형 대분류별 총 피해자 수")

        fig, ax = plt.subplots(figsize=(12, 6))
        sns.barplot(x=grouped.index, y=grouped.values, palette='Reds', ax=ax)

        ax.set_title('사고유형 대분류별 총 피해자 수', fontproperties=fontprop)
        ax.set_xlabel('사고유형대분류', fontproperties=fontprop)
        ax.set_ylabel('총 피해자 수', fontproperties=fontprop)
        ax.grid(True)

        # ✅ 눈금 라벨 폰트 적용 + 회전
        for label in ax.get_xticklabels():
            label.set_fontproperties(fontprop)
            label.set_rotation(45)

        st.pyplot(fig)

    except Exception as e:
        st.error(f"오류가 발생했습니다: {e}")
