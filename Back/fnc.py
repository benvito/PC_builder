import os
import Back.builder as func

def init(message):
    try:
        if not os.path.exists(f'{os.getcwd()}\\userdata\\{message.chat.id}'):
            os.makedirs(f'{os.getcwd()}\\userdata\\{message.chat.id}')
    except Exception as e:
        print(f'[{message.chat.id}] Error with create user folder({e})')
    if 'name.txt' not in os.listdir(f'{os.getcwd()}\\userdata\\{message.chat.id}'):
        open(f'{os.getcwd()}\\userdata\\{message.chat.id}\\name.txt', 'a+').write(f'Username: {message.from_user.username}\nName: {message.from_user.first_name} {message.from_user.last_name}')
    if 'mode.txt' not in os.listdir(f'{os.getcwd()}\\userdata\\{message.chat.id}'):
        open(f'{os.getcwd()}\\userdata\\{message.chat.id}\\mode.txt', 'a+').write(f'first')
    if 'cpu.txt' not in os.listdir(f'{os.getcwd()}\\userdata\\{message.chat.id}'):
        open(f'{os.getcwd()}\\userdata\\{message.chat.id}\\cpu.txt', 'a+').write('nan')
    if 'gpu.txt' not in os.listdir(f'{os.getcwd()}\\userdata\\{message.chat.id}'):
        open(f'{os.getcwd()}\\userdata\\{message.chat.id}\\gpu.txt', 'a+').write('nan')
    return f'Здравствуй, {message.from_user.first_name}! Рады видеть вас в PC Builder – боте, который поможет вам подобрать оптимальную конфигурацию компьютера на любой бюджет.'

def priceCFG(message):
    bld = func.Build(sum_price=int(open(f'{os.getcwd()}\\userdata\\{message.chat.id}\\price.txt', 'r').read()), cfg=open(f'{os.getcwd()}\\userdata\\{message.chat.id}\\cfg.txt', 'r').read())
    bld.set_price()
    return f'''💵Расчет цены:
            Материнская плата до {bld.motherboard_price[1]} руб
            Процессор до {bld.cpu_price[1]} руб
            Видеокарта до {bld.gpu_price[1]} руб
            Накопитель до {bld.rom_price[1]} руб
            Оперативная память до {bld.ram_price[1]} руб
            Блок питания до {bld.psu_price[1]} руб
            На остальное до {bld.other_price} руб
    '''

def build(message):
    builder = func.Build(sum_price=int(open(f'{os.getcwd()}\\userdata\\{message.chat.id}\\price.txt', 'r').read()),
                                            cfg=open(f'{os.getcwd()}\\userdata\\{message.chat.id}\\cfg.txt', 'r').read(),
                                            mode=open(f'{os.getcwd()}\\userdata\\{message.chat.id}\\mode.txt', 'r').read(),
                                            gpuCFG=open(f'{os.getcwd()}\\userdata\\{message.chat.id}\\gpu.txt', 'r').read(),
                                            cpuCfg=open(f'{os.getcwd()}\\userdata\\{message.chat.id}\\cpu.txt', 'r').read(),
                                            ID=message.chat.id)
    builder.set_price()
    builder.build()
    
    return builder.out()