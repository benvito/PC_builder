import pandas as pd

class Build:
    def __init__(self, motherboard=None, cpu=None, gpu=None, psu=None, ram=None, sum_price=None, rom=None, cfg=None):   
        self.motherboard_price = None
        self.cpu_price = None
        self.gpu_price = None
        self.rom_price = None
        self.ram_price = None
        self.psu_price = None

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
    def sorter(self):
        dfCPU = pd.read_csv("data/CPU.csv")
        dfGPU = pd.read_csv("data/GPU.csv")
        dfMB = pd.read_csv("data/MB.csv")
        dfROM = pd.read_csv("data/ROM.csv")

        tmpCPU = dfCPU[(dfCPU['price'] > self.cpu_price[0]) & (dfCPU['price'] < self.cpu_price[1])]
        tmpGPU = dfGPU[(dfGPU['price'] > self.gpu_price[0]) & (dfGPU['price'] < self.gpu_price[1])]
        tmpMB = dfMB[(dfMB['price'] > self.ram_price[0]) & (dfMB['price'] < self.ram_price[1])]
        tmpROM = dfROM[(dfROM['price'] > self.rom_price[0]) & (dfROM['price'] < self.rom_price[1])]

        tmpCPU.sort_values('cpuValue')
        tmpGPU.sort_values('gpuValue')
        tmpMB.sort_values('ramFreq')
        tmpROM.sort_values('diskMark')

        print(tmpCPU)
        print(tmpGPU)
        print(tmpMB)
        print(tmpROM)
        
        
        

    


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
    


tmp = Build(sum_price=60000, cfg='Gaming')
tmp.set_price()
tmp.sorter()
