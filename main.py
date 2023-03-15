import fnc

import telebot



bld = fnc.Build(sum_price=40000)
bld.set_price()
print(bld.motherboard_price)
print(bld.cpu_price)
print(bld.gpu_price)

