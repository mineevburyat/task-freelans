from fastapi import FastAPI, Path
import uvicorn
# from fastapi_math import calcpicelery
from shema import *

from calcpicelery.tasks import calcPi as celeryCalcPi
# from redis import StrictRedis
from calcpicelery.celery import redisServer
# import json
import pickle
import datetime


app = FastAPI()

@app.get('/')
async def home():
    return {'about': "Подсчет числа пи методом Лейбница. Подробнее: /docs"}

@app.get('/leibnic')
async def about_function():
    return {'about': "укажите число цифр после запятой"}

@app.get('/leibnic/{decimal}')
async def leibnic_method_calc_from_celery(decimal: int):
    result = celeryCalcPi.delay(decimal)
    timenow = datetime.datetime.now()
    try: 
        with open('data.pickle', 'rb') as f:
            fresult = pickle.load(f)
    except FileNotFoundError:
        fresult = {}
    fresult[result.id] = {'status': result.status, 'result': result.result, 'starttime':timenow.strftime('%c')}
    with open('data.pickle', 'wb') as f:
        pickle.dump(fresult, f)
    return {'task_id': result.id, **fresult}

@app.get("/tasks/{task_id}")
def get_status(task_id: str):
    try:
        with open('data.pickle', 'rb') as f:
            fresults = pickle.load(f)
    except FileNotFoundError:
        return {'error': "tasks not started yet"}
    if fresults[task_id] is None:
        return {'error': "task id is wrong"}
    return fresults[task_id]

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level="info")
