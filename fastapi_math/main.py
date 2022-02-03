from unicodedata import decimal
from fastapi import FastAPI, Path
import uvicorn
from pifunc import calcPi
from shema import *
from calcpicelery import tasks

app = FastAPI()

@app.get('/')
async def home():
    return "Подсчет числа пи методом Лейбница"

@app.get('/blocprocess/leibnic/{decimal}')
async def leibnic_method_calc(decimal: int):
    return {'pi': calcPi(decimal)}

@app.get('/nonblocprocess/leibnic/{decimal}')
async def leibnic_method_calc(decimal: int):
    result = tasks.calcPi.delay(decimal)
    print(result)
    return {'task_id': result.id}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level="info")