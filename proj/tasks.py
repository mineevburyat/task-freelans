import queue
from random import random
from .celery import app
from time import sleep

# logger = get_task_logger(__name__)

# @app.task(bind=True)
# def add(self, x, y):
#     logger.info(self.request.id)
@app.task(bind=True)
def add(self,x,y):
  # print(self.request.id)
  for i in range(10):
    i += 1
    sleep(int(15*random()))
    self.update_state(state="PROGRESS", meta={'progress': 10*i})
  return (x + y)
#celery -A proj worker -l INFO -Q celery,priority.high
@app.task(queue='priority.high')
def mul(x, y):
  sleep(34)
  return(x * y)

@app.task
def xsum(numbers):
  sleep(34)
  return sum(numbers)