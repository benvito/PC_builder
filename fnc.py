import pandas as pd



class Build:
    def __init__(self, motherboard=None, cpu=None, gpu=None, psu=None, ram=None, sum_price=None):
        self.MB_per = 10
        self.CPU_per = 30
        self.GPU_per = 35
        self.PSU_per = 10
        self.RAM_per = 15
        self.motherboard_price = None
        self.cpu_price = None
        self.gpu_price = None

        self.motherboard = motherboard
        self.cpu = cpu
        self.gpu = gpu
        self.psu = psu
        self.ram = ram
        self.sum_price = sum_price
    def set_price(self):
        self.motherboard_price = (int((self.sum_price / 100) * (self.MB_per - 2)), int((self.sum_price / 100) * self.MB_per))
        self.cpu_price = (int((self.sum_price / 100) * (self.CPU_per - 5)), int((self.sum_price / 100) * self.CPU_per))
        self.gpu_price = (int((self.sum_price / 100) * (self.GPU_per - 5)), int((self.sum_price / 100) * self.GPU_per))
    


class Motherboard:
    def __init__(self, name='None', price=0, socket='None', ram='None', category='None'):
        self.name = name
        self.price = price
        self.socket = socket
        self.category = category
        self.ram = ram


class Cpu:
    def __init__(self, name='None', price=0, mark=0, tdp=0, cores=0, socket='None', category='None'):
        self.name = name
        self.price = price
        self.mark = mark
        self.tdp = tdp
        self.cores = cores
        self.socket = socket
        self.category = category


class Gpu:
    def __init__(self, name='None', price=0, mark3D=0, mark2D=0, tdp=0, category='None'):
        self.name = name
        self.price = price
        self.mark3D = mark3D
        self.mark2D = mark2D
        self.tdp = tdp
        self.category = category



