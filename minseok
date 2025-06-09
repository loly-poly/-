!pip install koreanize-matplotlib
import koreanize_matplotlib
import pandas as pd
import matplotlib.pyplot as plt
import chardet
from google.colab import files

# 1. 파일 업로드
uploaded = files.upload()
filename = list(uploaded.keys())[0]

# 2. 인코딩 감지
with open(filename, 'rb') as f:
    result = chardet.detect(f.read(10000))
    detected_encoding = result['encoding']
    print(f"감지된 인코딩: {detected_encoding}")

# 3. 데이터 읽기
df = pd.read_csv(filename, encoding=detected_encoding)

# 4. 컬럼명이 숫자라면 컬럼명 직접 지정
expected_columns = ['날짜', '역명', '승차총승객수', '하차총승객수']

if all(isinstance(col, int) for col in df.columns):
    print("컬럼명이 숫자 형태입니다. 컬럼명을 직접 지정합니다.")
    df.columns = expected_columns

print(df.columns)
print(df.head())

# 5. 역명 문자열 변환 및 총 이용객 수 계산 (일일 단위)
df['역명'] = df['역명'].astype(str)
df['총이용객수'] = df['승차총승객수'] + df['하차총승객수']

# 6. 역-날짜별 일일 이용객수가 가장 많은 날 (최대값) 구하기
max_daily = df.groupby('역명')['총이용객수'].max()

# 7. Top 5 역 추출 (일일 최대 이용객수 기준)
top5 = max_daily.sort_values(ascending=False).head(5)

# 8. 시각화
plt.figure(figsize=(10, 5))
bars = plt.bar(top5.index, top5.values, color='mediumseagreen')

plt.title('2025년 4월 일일 이용객수가 가장 많은 지하철역 Top 5')
plt.xlabel('지하철역')
plt.ylabel('일일 이용객 수 (최대값)')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.5)

for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 5000, f'{yval:,}',
             ha='center', va='bottom', fontsize=10)

plt.tight_layout()
plt.show()

# 9. 결과 출력
print(top5)
