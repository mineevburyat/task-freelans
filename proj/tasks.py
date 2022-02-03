from .celery import app
from time import sleep


@app.task
def add(x,y):
  sleep(19)
  return (x + y)

@app.task
def mul(x, y):
  sleep(34)
  return(x * y)

@app.task
def xsum(numbers):
  sleep(34)
  return sum(numbers)