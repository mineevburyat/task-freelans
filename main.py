from fastapi import FastAPI
import uvicorn
from monitoring import *
from shema import CommonInfo

app = FastAPI()

hostconf = getInfo()
@app.get('/', response_model=CommonInfo)
async def home():
    return updateInfo(hostconf)

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