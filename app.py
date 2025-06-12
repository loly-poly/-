import matplotlib.pyplot as plt
import seaborn as sns
from google.colab import files
uploaded = files.upload()
df = pd.read_csv("한국도로교통공단_사고유형별 교통사고 통계_20231231.csv", encoding='cp949')  
df.head()
df['총피해자수'] = df['사망자수'] + df['중상자수'] + df['경상자수']

df.columns = df.columns.str.strip()

# 숫자형 컬럼 변환
cols = ['사망자수', '중상자수', '경상자수',]
df[cols] = df[cols].apply(pd.to_numeric, errors='coerce')

# 총 피해자 수 계산
df['총피해자수'] = df[cols].sum(axis=1)

# 사고유형 대분류별 집계
grouped = df.groupby('사고유형대분류')['총피해자수'].sum().sort_values(ascending=False)

# 시각화
plt.figure(figsize=(12,6))
sns.barplot(x=grouped.index, y=grouped.values, palette='Reds')
plt.title('사고유형 대분류별 총 피해자 수')
plt.xlabel('사고유형대분류')
plt.ylabel('총 피해자 수')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()
