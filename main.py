from fastapi import FastAPI, Path
import uvicorn
from monitoring import *
from shema import *

app = FastAPI()

hostconf = getInfo()
@app.get('/', response_model=CommonInfo)
async def home():
    return updateInfo(hostconf)

@app.get('/memory', response_model=Memory)
async def virtual_memory():
    return getMemory()

@app.get('/partitions', response_model=List[Partitions])
async def disk_partitions():
    return getPartList()

@app.get('/interfaces', response_model=List[Interface])
async def get_if_stats():
    return getInterfaceList()

@app.get('/disk', response_model=List[PhisicalDisks])
async def disk_io_counters():
    return {"disks": getPhisicalDisk()}

@app.get('/cpu/times', response_model=Dict[str, CPUTimes])
async def cpu_times():
    return getCPUTimes()

@app.get('/cpu/times_percent', response_model=Dict[int, CPUTimesPersent])
async def cpu_times_percent():
    return getCPUTimesPercent()

@app.get('/cpu/percent', response_model=CPUPercent)
async def cpu_percent():
    return getCPUPercent()

@app.get('/cpu/{id}/percent', response_model=NameFloat)
async def cpu_core_load(id: int = Path(..., description='cpu id', ge=0, lt=hostconf.cpu_core)):
    return getCPUPercent(id)

@app.get('/cpu/{id}/times_percent', response_model=NameDict)
async def cpu_core_timespercent(id: int = Path(..., description='cpu id', ge=0, lt=hostconf.cpu_core)):
    return getCPUTimesPercent(id)

@app.get('/partitions/usage', response_model=List[PartInfo])
async def partition_usage():
    return getPartitionUsage()

# @app.get('/ifstatus')
# async def root():
#     return "processes datailed info"

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info")