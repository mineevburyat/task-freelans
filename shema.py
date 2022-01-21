from pydantic import BaseModel, Field
from typing import List
# from xmlrpc.client import Boolean, boolean
import datetime


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
    upstatus: bool
    speed: int


class CommonInfo(BaseModel):
    hostname: str
    uptime: datetime.timedelta
    cpu_core: int
    cpu_load: float
    memory: Memory = None
    disks: List [Disk] = None
    iflist: List [Interface] = None
