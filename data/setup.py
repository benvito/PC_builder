import pandas as pd

data = pd.read_csv('CPU_benchmark_v4.csv')

data.drop(columns=['Cpu Value', 'Thread Mark', 'Thread Value'], axis=1)
