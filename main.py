from fastapi import FastAPI, Path
import uvicorn
from monitoring import *
from shema import CommonInfo

app = FastAPI()

hostconf = getInfo()
@app.get('/', response_model=CommonInfo)
async def home():
    return updateInfo(hostconf)

@app.get('/memory')
async def virtual_memory():
    return getMemory()

@app.get('/partitions')
async def disk_partitions():
    return getPartList()

@app.get('/interfaces')
async def get_if_stats():
    return getInterfaceList()

# @app.get('/disk')
# async def disk_io_counters():
#     return "phisical disk counter"

# @app.get('/cpu/times')
# async def cpu_time():
#     return {"user": 22, "system": 12, "idle": 78}

# @app.get('/cpu/percent')
# async def cpu_percent():
#     return {"user": 22, "system": 12, "idle": 78}

# @app.get('/cpu/times_percent')
# async def cpu_times_percent():
#     return {"user": 22, "system": 12, "idle": 78}

# @app.get('/cpu/{id}/percent')
# async def cpu_core_load(id: int = Path(..., description='cpu id', ge=0, lt=hostconf.cpu_core)):
#     return {"cpu{id}".format(id=id):psutil.cpu_percent(percpu=True)[id]}

# @app.get('/cpu/{id}/times')
# async def cpu_core_load(id: int = Path(..., title='cpu id', ge=0, lt=hostconf.cpu_core)):
#     return {"cpu{id}".format(id=id):psutil.cpu_percent(percpu=True)[id]}

# @app.get('/cpu/{id}/times_percent')
# async def cpu_core_load(id: int = Path(..., title='cpu id', ge=0, lt=hostconf.cpu_core)):
#     return {"cpu{id}".format(id=id):psutil.cpu_percent(percpu=True)[id]}

# @app.get('/partitions/{mountpoint}')
# async def disk_usage(mountpoint: str):
#     return "disks datailed info"

# @app.get('/ifstatus')
# async def root():
#     return "processes datailed info"

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info")