import pandas as pd
import random, os

class Build:
    def __init__(self, motherboard=None, cpu=None, gpu=None, psu=None, ram=None, sum_price=None, rom=None, cfg=None, mode='first', ID=None, gpuCFG='None', cpuCfg='None'):
        self.motherboard_price = None
        self.cpu_price = None
        self.gpu_price = None
        self.rom_price = None
        self.ram_price = None
        self.psu_price = None
        self.cfg = cfg
        self.sum_price=sum_price
        self.mode = mode
        self.ID = ID
        self.gpuCFG = gpuCFG
        self.cpuCFG = cpuCfg

        if cfg == "Gaming":
            self.MB_per = 13
            self.CPU_per = 13
            self.GPU_per = 35
            self.PSU_per = 11
            self.RAM_per = 11
            self.ROM_per = 9
            self.Other_per = 8
        elif cfg == "Working":
            self.MB_per = 13
            self.CPU_per = 26
            self.GPU_per = 22
            self.PSU_per = 9
            self.RAM_per = 13
            self.ROM_per = 10
            self.Other_per = 7
        elif cfg == "Graphics":
            self.MB_per = 11
            self.CPU_per = 13
            self.GPU_per = 37
            self.PSU_per = 10
            self.RAM_per = 12
            self.ROM_per = 10
            self.Other_per = 7
        else:
            self.MB_per = 10
            self.CPU_per = 10
            self.GPU_per = 10
            self.PSU_per = 10
            self.RAM_per = 10
            self.ROM_per = 10
            self.Other_per = 10

        self.motherboard = motherboard
        self.cpu = cpu
        self.gpu = gpu
        self.psu = psu
        self.ram = ram
        self.rom = rom
        self.sum_price = sum_price
    def set_price(self):
        self.motherboard_price = (int((self.sum_price / 100) * (self.MB_per - 2)), int((self.sum_price / 100) * self.MB_per))
        self.cpu_price = (int((self.sum_price / 100) * (self.CPU_per - 30)), int((self.sum_price / 100) * self.CPU_per))
        self.gpu_price = (int((self.sum_price / 100) * (self.GPU_per - 30)), int((self.sum_price / 100) * self.GPU_per))
        self.rom_price = (int((self.sum_price / 100) * (self.ROM_per - 30)), int((self.sum_price / 100) * self.ROM_per))
        self.ram_price = (int((self.sum_price / 100) * (self.RAM_per - 30)), int((self.sum_price / 100) * self.RAM_per))
        self.psu_price = (int((self.sum_price / 100) * (self.PSU_per - 30)), int((self.sum_price / 100) * self.PSU_per))
        self.other_price = int((self.sum_price / 100) * self.Other_per)
    
    def getCPUnMB(self):
        dfCPU = pd.read_csv("data/CPU.csv")
        if self.cpuCFG == 'AMD':
            to_price_CPU = dfCPU[(dfCPU['price'] > self.cpu_price[0]) & (dfCPU['price'] < self.cpu_price[1]) & (dfCPU['brnd'] == 'AMD')]
        elif self.cpuCFG == 'Intel':
            to_price_CPU = dfCPU[(dfCPU['price'] > self.cpu_price[0]) & (dfCPU['price'] < self.cpu_price[1]) & (dfCPU['brnd'] == 'Intel')]
        else:
            to_price_CPU = dfCPU[(dfCPU['price'] > self.cpu_price[0]) & (dfCPU['price'] < self.cpu_price[1])]
        to_price_CPU.sort_values('cpuValue')

        if self.mode == 'random':
            randomTMP = random.randint(1, 7)
            cpu = to_price_CPU.iloc[[randomTMP]]
            while len(cpu['cpuName'].values[0]) < 4:
                randomTMP -= 1
        else:
            cpu = to_price_CPU.head(1)


        try:
            cpu = cpu.drop(columns='Unnamed: 0')
        except:
            pass
        
        self.cpu = Cpu(name=cpu['cpuName'].values[0], 
                       price=cpu['price'].values[0], 
                       mark=cpu['cpuMark'].values[0], 
                       tdp=cpu['TDP'].values[0], 
                       cores=cpu['cores'].values[0], 
                       socket=cpu['socket'].values[0], 
                       category=cpu['category'].values[0])
        
        dfMB = pd.read_csv("data/MB.csv")
        to_price_MB = dfMB[(dfMB['price'] > self.ram_price[0]) & (dfMB['price'] < self.ram_price[1]) & (self.cpu.socket == dfMB["socket"])]
        
        to_price_MB = to_price_MB.sort_values('price', ascending=False)

        mb = to_price_MB.head(1)

        try:
            cpu = cpu.drop(columns='Unnamed: 0')
        except:
            pass
        
        self.motherboard = Motherboard(name=mb['name'].values[0],
                                       formFactor= mb['formFactor'].values[0],
                                       socket= mb['socket'].values[0],
                                       chipset= mb['chipset'].values[0],
                                       ramType= mb['ramType'].values[0],
                                       ramSlots= mb['ramSlots'].values[0],
                                       ramFreq= mb['ramFreq'].values[0],
                                       maxRam= mb['maxRam'].values[0],
                                       powerPin= mb['powerPin'].values[0],
                                       price= mb['price'].values[0])

    def getGPU(self):
        dfGPU = pd.read_csv("data/GPU.csv")
        print(dfGPU.head())
        if self.gpuCFG == 'NVIDIA':
            to_price_GPU = dfGPU[(dfGPU['price'] > self.gpu_price[0]) & (dfGPU['price'] < self.gpu_price[1]) & (dfGPU['brnd'] == 'NVIDIA')]
        elif self.gpuCFG == 'AMD':
            print('AMD')
            to_price_GPU = dfGPU[(dfGPU['price'] > self.gpu_price[0]) & (dfGPU['price'] < self.gpu_price[1]) & (dfGPU['brnd'] == 'AMD')]
        else:
            to_price_GPU = dfGPU[(dfGPU['price'] > self.gpu_price[0]) & (dfGPU['price'] < self.gpu_price[1])]
        to_price_GPU.sort_values('gpuValue')

        if self.mode == 'random':
            randomTMP = random.randint(1, 7)
            gpu = to_price_GPU.iloc[[randomTMP]]
            while len(gpu['gpuName'].values[0]) < 4:
                randomTMP -= 1
        else:
            gpu = to_price_GPU.head(1)

        try:
            gpu = gpu.drop(columns='Unnamed: 0')
        except:
            pass
        
        self.gpu = Gpu(name=gpu['gpuName'].values[0], 
                       price=gpu['price'].values[0], 
                       mark3D=gpu['G3Dmark'].values[0], 
                       mark2D=gpu['G2Dmark'].values[0], 
                       tdp=gpu['TDP'].values[0],                        
                       category=gpu['category'].values[0])

    def getROM(self, dbl=False, remainder=0):
        dfROM = pd.read_csv("data/ROM.csv")
        if self.cfg == "Gaming" and dbl:
            to_price_ROM = dfROM[(dfROM['price'] <= remainder) & (dfROM['type'] == 'SSD') & (dfROM['diskCapacity'] > 1000)]
            if len(to_price_ROM['type'].values) == 0:
                to_price_ROM = dfROM[(dfROM['price'] <= remainder) & (dfROM['diskCapacity'] > 2000)]
        elif self.cfg == "Gaming" and not dbl:
            to_price_ROM = dfROM[(dfROM['price'] > self.rom_price[0]) & (dfROM['price'] < self.rom_price[1]) & (dfROM['type'] == 'SSD')]
            if len(to_price_ROM['type'].values) == 0:
                to_price_ROM = dfROM[(dfROM['price'] > self.rom_price[0]) & (dfROM['price'] < self.rom_price[1])]
        else:
            to_price_ROM = dfROM[(dfROM['price'] > self.rom_price[0]) & (dfROM['price'] < self.rom_price[1])]
        to_price_ROM.sort_values('driveValue')

        rom = to_price_ROM.head(1)

        try:
            cpu = cpu.drop(columns='Unnamed: 0')
        except:
            pass
        if not dbl:
            self.rom = Rom(name=rom['driveName'].values[0],
                        type=rom['type'].values[0],
                        capacity=rom['diskCapacity'].values[0],
                        mark=rom['diskMark'].values[0],
                        rank=rom['rank'].values[0],
                        price=rom['price'].values[0])
        elif dbl:
            self.rom = Rom(name=rom['driveName'].values[0],
                        type=rom['type'].values[0],
                        capacity=rom['diskCapacity'].values[0],
                        mark=rom['diskMark'].values[0],
                        rank=rom['rank'].values[0],
                        price=rom['price'].values[0])
        else:
            print('Что то пошло не так')

    def getTDP(self):
        open(f'{os.getcwd()}\\userdata\\{self.ID}\\TDP.txt', 'a+').write(str(self.cpu.tdp + self.gpu.tdp + 300))

    def getPSU(self):
        dfPSU = pd.read_csv("data/PSU.csv")

        to_price_PSU = dfPSU[(dfPSU['price'] > self.psu_price[0]) & (dfPSU['price'] < self.psu_price[1]) & (dfPSU['power'] > int(open(f'{os.getcwd()}\\userdata\\{self.ID}\\TDP.txt').read()[0:-2]))]
        try:
            os.remove(f'{os.getcwd()}\\userdata\\{self.ID}\\TDP.txt')
        except:
            print('rm err')

        to_price_PSU.sort_values('value')

        psu = to_price_PSU.head(1)

        self.psu = Psu(name=psu['name'].values[0],
                       formFactor=psu['formFactor'].values[0],
                       power=psu['power'].values[0],
                       fan=psu['fan'].values[0],
                       pin=psu['pin'].values[0],
                       gpuPin=psu['GPUpin'].values[0],
                       price=psu['price'].values[0]
                       )

    def getRAM(self, dbl=False, remainder=0):
        dfRAM = pd.read_csv('data/RAM.csv')

        if dbl:
            to_price_RAM = dfRAM[(dfRAM['price'] > self.ram_price[0]) & (dfRAM['price'] < self.ram_price[1]) & (dfRAM['type'] == self.motherboard.ramType) 
                                 & (dfRAM['count'] == 2 if self.motherboard.ramSlots == 2 else dfRAM['count'] == 4) & (dfRAM['capacity'] >= 16 if self.motherboard.ramSlots == 2 else dfRAM['capacity'] == 8)]
        else:
            to_price_RAM = dfRAM[(dfRAM['price'] > self.ram_price[0]) & (dfRAM['price'] < self.ram_price[1]) & (dfRAM['type'] == self.motherboard.ramType)]

        to_price_RAM.sort_values('value')

        ram = to_price_RAM.head(1)

        self.ram = Ram(name=ram['name'].values[0],
                       count=ram['count'].values[0],
                       capacity=ram['capacity'].values[0],
                       freq=ram['freq'].values[0],
                       timings=ram['timings'].values[0],
                       formFactor=ram['formFactor'].values[0],
                       type=ram['type'].values[0],
                       price=ram['price'].values[0]
                       )


    def build(self):
        self.getCPUnMB()
        self.getGPU()
        self.getROM()
        self.getTDP()
        self.getPSU()
        self.getRAM()
        tmpPrice = self.cpu.price + self.gpu.price + self.motherboard.price + self.rom.price + self.psu.price + int(self.ram.price)
        if tmpPrice < self.sum_price:
            remainder = self.sum_price - tmpPrice
            if remainder > self.other_price:
                remainder -= self.other_price
                if remainder > 3000:
                    self.getROM(dbl=True, remainder=remainder/2)
                    self.getRAM(dbl=True, remainder=remainder/2)
        
    
    def out(self):
        return f"""🧠Процессор: `{self.cpu.name}`
            Сокет: {self.cpu.socket}
            Ядер: {self.cpu.cores}
            Потребление: {self.cpu.tdp}W
            Benchmark: {self.cpu.mark}
            Цена: {self.cpu.price}
🖥Видеокарта: `{self.gpu.name}`
            Потребление: {self.gpu.tdp}W
            Benchmark3D: {self.gpu.mark3D}
            Benchmark2D: {self.gpu.mark2D}
            Цена: {self.gpu.price}
🎛Материнская плата: `{self.motherboard.name}`
            Форм фактор: {self.motherboard.formFactor}
            Сокет: {self.motherboard.socket}
            Чипсет: {self.motherboard.chipset}
            Тип ОЗУ: {self.motherboard.ramType}
            Кол-во слотов ОЗУ: {self.motherboard.ramSlots}
            Максимальная частота ОЗУ: {self.motherboard.ramFreq}
            Максимальное кол-во ОЗУ: {self.motherboard.maxRam}
            Power PINS: {self.motherboard.powerPin}
            Цена: {self.motherboard.price}
⏱️Оперативная память: `{self.ram.name}`
            Тип: {self.ram.type}
            Кол-во: {self.ram.count}
            Кол-во памяти: {self.ram.capacity}
            Частота: {self.ram.freq}
            Тайминги: {self.ram.timings}
            Форм фактор: {self.ram.formFactor}
            Цена: {self.ram.price}
📀Накопитель: `{self.rom.name}`
            Тип: {self.rom.type}
            Ёмкость: {self.rom.capacity}
            Benchmark: {self.rom.mark}
            Цена: {self.rom.price}
🔌Блок питания: `{self.psu.name}`
            Форм фактор: {self.psu.formFactor}
            Мощность: {self.psu.power}W
            Кулер: {self.psu.fan}
            PIN: {self.psu.pin}
            GPU PIN: {self.psu.gpuPin}
            Цена: {self.psu.price}
🚬На остаточные комплектующие: {self.other_price}
🔧Твои настройки:
            Конфиг: {self.cfg}
            Режим: {self.mode}
💵Цена: {round(self.cpu.price + self.gpu.price + self.motherboard.price + self.rom.price + self.psu.price + int(self.ram.price), 1)} руб
"""

class Motherboard:
    def __init__(self, name=None, formFactor=None, socket=None, chipset=None, ramType=None, ramSlots=0, ramFreq=0, maxRam=0, powerPin=None, price=0, category=None):
        self.name = name
        self.formFactor = formFactor
        self.socket = socket
        self.chipset = chipset
        self.ramType = ramType
        self.ramSlots = ramSlots
        self.ramFreq = ramFreq
        self.price = price
        self.category = category
        self.maxRam = maxRam
        self.powerPin = powerPin


class Cpu:
    def __init__(self, name=None, price=0, mark=0, tdp=0, cores=0, socket=None, category=None):
        self.name = name
        self.price = price
        self.mark = mark
        self.tdp = tdp
        self.cores = cores
        self.socket = socket
        self.category = category


class Gpu:
    def __init__(self, name=None, price=0, mark3D=0, mark2D=0, tdp=0, category=None):
        self.name = name
        self.price = price
        self.mark3D = mark3D
        self.mark2D = mark2D
        self.tdp = tdp
        self.category = category


class Rom:
    def __init__(self, name=None, type=None, capacity=0, price=0, mark=0, rank=0, count=1):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.price = price
        self.mark = mark
        self.rank = rank
        self.count = count
    

class Psu:
    def __init__(self, name=None, formFactor=None, power=None, fan=None, pin=None, gpuPin=None, price=None):
        self.name = name
        self.formFactor = formFactor
        self.power = power
        self.fan = fan
        self.pin = pin
        self.gpuPin = gpuPin
        self.price = price

class Ram:
    def __init__(self, name=None, count=None, capacity=None, freq=None, timings=None, formFactor=None, type=None, price=None):
        self.name = name
        self.count = count
        self.capacity = capacity
        self.freq = freq
        self.timings = timings
        self.formFactor = formFactor
        self.type = type
        self.price = price
        