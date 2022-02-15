from fastapi import FastAPI, Path
import uvicorn
from shema import *

from calcpicelery.tasks import calcPi as celeryCalcPi
# from redis import StrictRedis

# import json
import json
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
    return {'id': result.id}

@app.get("/tasks/{task_id}")
def get_status(task_id: str):
    try:
        with open('results/' + task_id, 'rb') as f:
            fresults = json.load(f)
    except FileNotFoundError:
        return {'error': "tasks not found"}
    
    return {**fresults}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level="info")
