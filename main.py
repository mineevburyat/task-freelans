from fastapi import FastAPI
import uvicorn
import psutil
import platform

def getHostName():
    """Return str - hostname"""
    return "hostname"

def getDiskInfo():
    """Return list with obj {str(root), str(fstype), num(% usage)}"""
    return [{"root":"C:\\", "fstype": "ntfs", "usage": 90}, 
            {"root":"D:\\", "fstype":"ntfs", "usage": 15}]

def getCPUcount():
    """Return number of logical CPU"""
    return 8

def getCPUInfo():
    """Return list with obj {}"""
    pass

app = FastAPI()
"""route:
/ - answer common info: hostname, CPU count, Disk count, process count;
/cpu - answer detailed information about cpu: usage common and usege logical cpu separately;
/disk - answer detailed information about disks: usage space on all disk;
/proc - answer datailed information abaut processes: pid, owner, time"""
@app.get('/')
async def root():
    return "common info"

@app.get('/cpu')
async def root():
    return "cpu datailed info"

@app.get('/disk')
async def root():
    return "disks datailed info"

@app.get('/proces')
async def root():
    return "processes datailed info"

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info")