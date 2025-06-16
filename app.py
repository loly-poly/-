import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.font_manager as fm

# ✅ 한글 폰트 수동 등록
font_path = "./NanumGothic.otf"
fontprop = fm.FontProperties(fname=font_path)
plt.rcParams['font.family'] = fontprop.get_name()

st.title("사고유형별 총 피해자 수 시각화")

uploaded_file = st.file_uploader("CSV 파일을 업로드하세요", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file, encoding='cp949')
    df.columns = df.columns.str.strip()

    cols = ['사망자수', '중상자수', '경상자수']
    df[cols] = df[cols].apply(pd.to_numeric, errors='coerce')
    df['총피해자수'] = df[cols].sum(axis=1)

    grouped = df.groupby('사고유형대분류')['총피해자수'].sum().sort_values(ascending=False)

    st.subheader("사고유형 대분류별 총 피해자 수")

    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(x=grouped.index, y=grouped.values, palette='Reds', ax=ax)
    ax.set_title('사고유형 대분류별 총 피해자 수', fontproperties=fontprop)
    ax.set_xlabel('사고유형대분류', fontproperties=fontprop)
    ax.set_ylabel('총 피해자 수', fontproperties=fontprop)
    ax.tick_params(axis='x', rotation=45)
    ax.grid(True)

    st.pyplot(fig)
