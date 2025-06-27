import pandas as pd

data = pd.read_csv('data.csv')

filtered_data = data[data['age'] >= 18]
mean_height = filtered_data['height'].mean()

print('평균키 : ',mean_height)
