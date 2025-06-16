!pip install matplotlib seaborn

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from google.colab import files

# ✅ 한글 폰트 설정 (koreanize-matplotlib 대신)
plt.rcParams['font.family'] = 'NanumGothic'

# ✅ 파일 업로드
uploaded = files.upload()

# ✅ 데이터 불러오기
df = pd.read_csv("한국도로교통공단_사고유형별 교통사고 통계_20231231.csv", encoding='cp949')

# ✅ 공백 제거
df.columns = df.columns.str.strip()

# ✅ 숫자형 컬럼 변환
cols = ['사망자수', '중상자수', '경상자수']
df[cols] = df[cols].apply(pd.to_numeric, errors='coerce')

# ✅ 총 피해자 수 계산
df['총피해자수'] = df[cols].sum(axis=1)

# ✅ 사고유형 대분류별 집계
grouped = df.groupby('사고유형대분류')['총피해자수'].sum().sort_values(ascending=False)

# ✅ 시각화
plt.figure(figsize=(12,6))
sns.barplot(x=grouped.index, y=grouped.values, palette='Reds')
plt.title('사고유형 대분류별 총 피해자 수')
plt.xlabel('사고유형대분류')
plt.ylabel('총 피해자 수')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()
