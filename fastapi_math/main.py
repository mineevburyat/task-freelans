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
import json


app = FastAPI()

@app.get('/')
async def home():
    return {'about': "Подсчет числа пи методом Лейбница. Подробнее: /docs"}

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
    redis_answer = redisServer.get('celery-task-meta-'+task_id)
    if redis_answer is None:
        return {'error': "task id is wrong"}
    redis_answer = redis_answer.decode('utf-8')
    task_status = json.loads(redis_answer)
    return task_status

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level="info")
