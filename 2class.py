import pandas as pd
from functions import Build

alina = Build()
alina.cpu_price = 7000 # к примеру цена на цпу вышла 7к


df_CPU = pd.read_csv('CPU_benchmark_v4.csv') # открываем датасет с цпу
df_CPU.head()


df_CPU = df_CPU.dropna () # здесь удалила незаполненные строки чтоб работало все нормально
df_CPU = df_CPU.reset_index(drop=True)
df_CPU



len_df_CPU = len(df_CPU)
CPU_variable = {}
for i in range(len_df_CPU):
  if df_CPU['price'][i] - 500 <= alina.cpu_price <= df_CPU['price'][i] + 500: # к примеру цена варьируется +- 500
    name  = df_CPU.cpuName[i]
    CPU_variable.update({df_CPU.cpuName[i]: {'price': float(df_CPU['price'][i]), 'cpuMark': int(df_CPU['cpuMark'][i]), 'cpuValue':float(df_CPU['cpuValue'][i]), 'threadMark':int(df_CPU['threadMark'][i]),'threadValue': float(df_CPU['threadValue'][i]),'TDP': float(df_CPU['TDP'][i]),'powerPerf': float(df_CPU['powerPerf'][i]),'cores': int(df_CPU['cores'][i]),'testDate': int(df_CPU['testDate'][i]),'socket': df_CPU['socket'][i],'category': df_CPU['category'][i] }})
print(CPU_variable)



import json as js
with open("CPU.json", "w") as json:
    js.dump(CPU_variable, json) #записала в json