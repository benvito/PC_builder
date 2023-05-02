import pandas as pd

priceCPU = (5000, 6000)
priceGPU = (2000, 3000)
priceMB = (5000, 7000)
priceROM = (1000, 3000)

dfCPU = pd.read_csv("data/CPU.csv")
dfGPU = pd.read_csv("data/GPU.csv")
dfMB = pd.read_csv("data/MB.csv")
dfROM = pd.read_csv("data/ROM.csv")

tmpCPU = dfCPU[(dfCPU['price'] > priceCPU[0]) & (dfCPU['price'] < priceCPU[1])]
tmpGPU = dfGPU[(dfGPU['price'] > priceGPU[0]) & (dfGPU['price'] < priceGPU[1])]
tmpMB = dfMB[(dfMB['price'] > priceMB[0]) & (dfMB['price'] < priceMB[1])]
tmpROM = dfROM[(dfROM['price'] > priceROM[0]) & (dfROM['price'] < priceROM[1])]

#




print(tmpCPU.head())

