import pandas as pd
from functions import Build, Cpu
import json as js

alina = Build(sum_price=200000, cfg="Gaming")
alina.set_price()
print(alina.__dict__)


df_CPU = pd.read_csv('data/CPU_benchmark_v4.csv') # открываем датасет с цпу
df_CPU = df_CPU.dropna () # здесь удалила незаполненные строки чтоб работало все нормально
df_CPU = df_CPU.reset_index(drop=True)
df_CPU = df_CPU.drop(['cpuValue','threadMark','threadValue','powerPerf','testDate'], axis=1)


len_df_CPU = len(df_CPU)
CPU_variable = {}
for i in range(len_df_CPU):
  if alina.cpu_price[0] <= (df_CPU['price'][i] * 78) <= alina.cpu_price[1]: 
    # print(i,' ',df_CPU.cpuName[i])
    CPU_variable.update({df_CPU.cpuName[i]: {'price': float(df_CPU['price'][i]), 'cpuMark': int(df_CPU['cpuMark'][i]),'TDP': float(df_CPU['TDP'][i]),'cores': int(df_CPU['cores'][i]),'socket': df_CPU['socket'][i],'category': df_CPU['category'][i] }})
# print(CPU_variable)


with open("CPU.json", "w") as json:
    js.dump(CPU_variable, json) #записала в json
with open("CPU.json") as json:
   dict_cpu = js.load(json)
print(dict_cpu)


list_cpuMark = []
for i in dict_cpu.keys():
    list_cpuMark.append(dict_cpu[i].get("cpuMark"))
for i in dict_cpu.keys():
   if max(list_cpuMark) == dict_cpu[i].get("cpuMark"):
      print(i)
      break #сравнение по cpuMark


cpu = Cpu(name=i, price = dict_cpu[i].get("price"), mark = dict_cpu[i].get("cpuMark"), tdp = dict_cpu[i].get("TDP"), cores = dict_cpu[i].get("cores"), socket = dict_cpu[i].get("socket"), category = dict_cpu[i].get("category"))
print(cpu.__dict__) #записала процессор 



df_MB = pd.read_csv('data/MB_DF.csv') # открываем датасет с материнками
df_MB = df_MB.dropna () # чистим
df_MB = df_MB.reset_index(drop=True)
df_MB = df_MB.drop(['maxRam','powerPin','link'], axis=1)


len_df_MB = len(df_MB)
MB_variable = {}
for i in range(len_df_MB):
  if alina.motherboard_price[0] <= (df_MB['price'][i]) <= alina.motherboard_price[1]: 
    if df_MB['socket'][i] == cpu.socket: #вот тут надо править
      print(df_MB.name[i])
      MB_variable.update({df_MB.name[i]: {'price': float(df_MB['price'][i]), 'formFactor': df_MB['formFactor'][i],'socket': df_MB['socket'][i],'chipset': df_MB['chipset'][i],'ramType': df_MB['ramType'][i],'ramSlots': int(df_MB['ramSlots'][i]), 'ramFreq': int(df_MB['ramFreq'][i]) }})
print(MB_variable)
   
   
# with open("MB.json", "w") as json:
#     js.dump(MB_variable, json) #записала в json



# ПРИМЕЧАНИЯ:
# записи сокетов в датасетах цпу и мб. различаются надо их привести к одному виду чтоб сравнить или че нибудь другое придумать
# прайс в цпу в долларах а в мб. в рублях
# сравнить материнки
# ну и там пошло поехало, проц вроде вывела по самому высокому cpuMark и записала пока в класс Cpu
 