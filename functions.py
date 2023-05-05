import pandas as pd
import random

class Build:
    def __init__(self, motherboard=None, cpu=None, gpu=None, psu=None, ram=None, sum_price=None, rom=None, cfg=None, mode='first'):
        self.motherboard_price = None
        self.cpu_price = None
        self.gpu_price = None
        self.rom_price = None
        self.ram_price = None
        self.psu_price = None
        self.cfg = cfg
        self.sum_price=sum_price
        self.mode = mode

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
    
    def getCPUnMB(self):
        dfCPU = pd.read_csv("data/CPU.csv")
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
        to_price_MB.sort_values('ramFreq')

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

    def getROM(self):
        dfROM = pd.read_csv("data/ROM.csv")
        if self.cfg == "Gaming":
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

        self.rom = Rom(name=rom['driveName'].values[0],
                       type=rom['type'].values[0],
                       capacity=rom['diskCapacity'].values[0],
                       mark=rom['diskMark'].values[0],
                       rank=rom['rank'].values[0],
                       price=rom['price'].values[0])

    def build(self):
        self.getCPUnMB()
        self.getGPU()
        self.getROM()
        
    
    def out(self):
        return f"""🧠CPU: {self.cpu.name}
            Socket: {self.cpu.socket}
            Cores: {self.cpu.cores}
            TDP: {self.cpu.tdp}
            Benchmark: {self.cpu.mark}
            Price: {self.cpu.price}
🖥 GPU: {self.gpu.name}
            TDP: {self.gpu.tdp}
            Benchmark3D: {self.gpu.mark3D}
            Benchmark2D: {self.gpu.mark2D}
            Price: {self.gpu.price}
🎛Motherboard: {self.motherboard.name}
            Form-factor: {self.motherboard.formFactor}
            Socket: {self.motherboard.socket}
            Chipset: {self.motherboard.chipset}
            RAM Type: {self.motherboard.ramType}
            RAM slots: {self.motherboard.ramSlots}
            RAM Frequency: {self.motherboard.ramFreq}
            RAM max: {self.motherboard.maxRam}
            Power PINS: {self.motherboard.powerPin}
            Price: {self.motherboard.price}
📀ROM: {self.rom.name}
            Type: {self.rom.type}
            Capacity: {self.rom.capacity}
            Benchmark: {self.rom.mark}
            Price: {self.rom.price}
🔧Settings:
            CFG: {self.cfg}
            Mode: {self.mode}
"""
    #сделать итоговую цену и очередной режим

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
    def __init__(self, name=None, type=None, capacity=0, price=0, mark=0, rank=0):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.price = price
        self.mark = mark
        self.rank = rank
    