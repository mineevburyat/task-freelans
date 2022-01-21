from xmlrpc.client import Boolean
from fastapi import FastAPI
import uvicorn
import psutil, datetime, socket
from pydantic import BaseModel, Field
from typing import List

class Memory(BaseModel):
	total: int
	available: int
	percent: float
	used: int
	free: int

class Disk(BaseModel):
	device: str = Field(..., max_length=25, min_length=1)
	mountpoint: str = Field(..., min_length=1)
	fstype: str
	opts: str

class Interface(BaseModel):
    name: str
    upstatus: Boolean
    speed: int


class CommonInfo(BaseModel):
    hostname: str
    uptime: datetime.timedelta
    cpu_core: int
    cpu_load: float
    memory: Memory
    disks: List [Disk]
    iflist: List [Interface] = None

app = FastAPI()

mem = Memory(**psutil.virtual_memory()._asdict())

disks = []
for disk in psutil.disk_partitions():
	disks.append(Disk(**disk._asdict()))
interfaces = []
for if_name, if_status in psutil.net_if_stats().items():
    interface = Interface(name=if_name, upstatus=if_status.isup, speed=if_status.speed)
    interfaces.append(interface)

commoninfo = CommonInfo(hostname = socket.gethostname(),
    uptime = datetime.datetime.now() - datetime.datetime.fromtimestamp(psutil.boot_time()), 
    cpu_core = psutil.cpu_count(True),
    cpu_load = psutil.cpu_percent(interval=1),
    memory = mem,
    disks=disks,
    iflist = interfaces)

@app.get('/', response_model=CommonInfo)
async def home():
    commoninfo.uptime = datetime.datetime.now() - datetime.datetime.fromtimestamp(psutil.boot_time())
    commoninfo.cpu_load = psutil.cpu_percent()
    return commoninfo

@app.get('/cpu/{id}')
async def root():
    return "cpu datailed info"

@app.get('/disk/{mountpoint}')
async def root():
    return "disks datailed info"

@app.get('/ifstatus')
async def root():
    return "processes datailed info"

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info")