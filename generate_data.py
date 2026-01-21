import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os

# 确保文件夹存在
if not os.path.exists('data'):
    os.makedirs('data')

np.random.seed(42)
start_date = datetime(2024, 1, 1)
dates = [start_date + timedelta(days=i) for i in range(30)]

data = {
    'date': dates,
    'temperature': np.random.normal(25, 5, 30),
    'humidity': np.random.normal(60, 10, 30),
    'pm25': np.random.normal(50, 20, 30),
    'location': ['站点A']*15 + ['站点B']*15
}

df = pd.DataFrame(data)
df['humidity'] = df['humidity'].clip(0, 100)
df['pm25'] = df['pm25'].clip(0, 500)

df.to_csv('data/sensor_data.csv', index=False, encoding='utf-8')
print("数据已生成：data/sensor_data.csv")