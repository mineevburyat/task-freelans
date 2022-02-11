from turtle import back
from celery.result import AsyncResult
from unicodedata import decimal
from fastapi import FastAPI, Path
import uvicorn
# from fastapi_math import calcpicelery
from pifunc import calcPi
from shema import *

from calcpicelery.tasks import calcPi as celeryCalcPi
# from redis import StrictRedis
from calcpicelery.celery import redisServer


app = FastAPI()

@app.get('/')
async def home():
    return "Подсчет числа пи методом Лейбница"

@app.get('/blocprocess/leibnic/{decimal}')
async def leibnic_method_calc(decimal: int):
    return {'pi': calcPi(decimal)}

@app.get('/nonblocprocess/leibnic/{decimal}')
async def leibnic_method_calc_from_celery(decimal: int):
    result = celeryCalcPi.delay(decimal)
    print(result)
    return {'task_id': result.id,
            'get_status_byredis': 'celery-task-meta-' + result.id}

@app.get("/tasks/{task_id}")
def get_status(task_id: str):
    return redisServer.get('celery-task-meta-' + task_id)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level="info")
