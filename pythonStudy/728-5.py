import modi_plus
import pandas as pd
from datetime import datetime
import time
import matplotlib.pyplot as plt

# 모듈 번들 초기화
bundle = modi_plus.MODIPlus()

# 환경 모듈 할당
environment = bundle.envs[0]

# 데이터 저장을 위한 리스트 초기화
data = {
    'Time': [],
    'Temperature': [],
    'Humidity': [],
    'Light Intensity': []
}

# 5초 간격으로 데이터 수집 (예: 5번 수집)
for _ in range(5):
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    temperature = environment.temperature
    humidity = environment.humidity
    light_intensity = environment.intensity

    print(temperature)
    print(humidity)
    print(light_intensity)

    # 수집한 데이터 리스트에 추가
    data['Time'].append(current_time)
    data['Temperature'].append(temperature)
    data['Humidity'].append(humidity)
    data['Light Intensity'].append(light_intensity)

    # 5초 대기
    time.sleep(5)

# DataFrame 생성
df = pd.DataFrame(data)

# 엑셀 파일 불러오기
input_file = 'environment_data.xlsx'
ds = pd.read_excel(input_file)

# 시간 데이터를 datetime 형식으로 변환

# DataFrame을 엑셀 파일로 내보내기
if(ds.empty):
  output_file = 'environment_data.xlsx'
  df.to_excel(output_file, index=False, engine='openpyxl')
  print(f"Data has been written to {output_file}")
else:
   ds['Time'] = pd.to_datetime(ds['Time'])
   plt.figure(figsize=(10, 5))
   plt.plot(ds['Time'], ds['Light Intensity'], marker='o', linestyle='-')
   plt.xlabel('Time')
   plt.ylabel('Light Intensity')
   plt.title('Light Intensity over Time')
   plt.grid(True)
   plt.xticks(rotation=45)
   plt.tight_layout()  
   # 그래프 보여주기
   plt.show()

