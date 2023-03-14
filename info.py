import json as js
dicti = {}
with open("columns.json") as json:
    dicti = js.load(json)


print([i for i in dicti.keys()])
tp = input('>>>')
print([i for i in dicti[tp].keys()])
tp2 = input('>>>')
print([i for i in dicti[tp][tp2].keys()])
tp3 = input('>>>')
print(dicti[tp][tp2][tp3])