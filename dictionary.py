import pandas as pd
import json as js

dict = {
    "cpu": {
        "id" : {
            "desc" : "unique number", 
            "dtype" : "int", 
        },
        "name" :{
            "desc" : "name of the CPU's", 
            "dtype" : "string", 
        },
        "cores" :{
            "desc" : "num of CPU's cores", 
            "dtype" : "int", 
        },
        "threads" :{
            "desc" : "num of CPU's threads", 
            "dtype" : "int", 
        },
        "base_freq" :{
            "desc" : "base CPU's frequency in MHz", 
            "dtype" : "int", 
        },
        "turbo_freq" :{
            "desc" : "turbo CPU's frequency in MHz", 
            "dtype" : "int", 
        },
        "price" :{
            "desc" : "CPU price", 
            "dtype" : "float", 
        },
        
    },
    "gpu":{
        "id" : {
            "desc" : "unique number", 
            "dtype" : "int", 
        },
        "name" :{
            "desc" : "name of the GPU's(model)", 
            "dtype" : "string", 
        },
        "Architecture" :{
            "desc" : "The GPU architecture used on the graphics card.", 
            "dtype" : "string", 
        },
        "best_res" :{
            "desc" : "Best Resolution. The best Screensize for reducing bottleneck to a minimum.", 
            "dtype" : "string", 
        },
        "boost_clock" :{
            "desc" : "the MHz speed of the graphics card", 
            "dtype" : "int", 
        },
        "core speed" :{
            "desc" : "the speed of the graphics card", 
            "dtype" : "int", 
        },
        "DX" :{
            "desc" : "What DirectX can the graphics card support", 
            "dtype" : "float", 
        },
        "price" :{
            "desc" : "GPU price", 
            "dtype" : "float", 
        }
        
    },
    "disk":{
        "id" : {
            "desc" : "unique number", 
            "dtype" : "int", 
        },
        "name" :{
            "desc" : "model", 
            "dtype" : "string", 
        },
        "type" :{
            "desc" : "Drive type", 
            "dtype" : "string", 
        },
        "capacity" :{
            "desc" : "Storage Capacity, in gigabytes (GB)", 
            "dtype" : "float", 
        },
        "mark" :{
            "desc" : "Disk Rating, higher is better", 
            "dtype" : "int", 
        },
        "rank" :{
            "desc" : "Benchmark Rank", 
            "dtype" : "int", 
        },
        "price" :{
            "desc" : "Last seen market price, in USD ($)", 
            "dtype" : "float", 
        }
        
    },
}


with open("columns.json", "w") as json:
    js.dump(dict, json)

