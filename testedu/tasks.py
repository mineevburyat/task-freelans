from celery import Celery
from time import sleep

# app = Celery('tasks', broker='pyamqp://guest@192.168.88.43//')
app = Celery('hello', backend='rpc://', broker='pyamqp://guest@192.168.88.82//')
app.conf.update(task_serializer = 'json',
accept_content=['json'],
result_serializer='json',
timezone='Asia/Irkutsk',
enable_utc=True)



@app.task
def add(x,y):
  return (x + y)


@app.task
def hello():
  sleep(50)
  return 'hello world!'

