from celery import Celery
from time import sleep

# app = Celery('tasks', broker='pyamqp://guest@192.168.88.43//')
app = Celery('hello', backend='rpc://', broker='pyamqp://guest@192.168.88.43//')

# @app.task
# def add(x,y):
#   return (x + y)


@app.task
def hello():
  sleep(50)
  return 'hello world!'