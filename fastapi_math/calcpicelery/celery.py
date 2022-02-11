from celery import Celery
from redis import StrictRedis, Redis

redis_host = '192.168.88.82'

# redisServer = StrictRedis(host=redis_host)
redisServer = Redis(host=redis_host)

app = Celery()


class Config:
  result_expires=3600
  task_track_started=True
  enable_utc=True
  timezone='Asia/Irkutsk'
  broker_url='pyamqp://guest@192.168.88.82/'
  result_backend='redis://'+redis_host+'/0'
  include=['calcpicelery.tasks']

app.config_from_object(Config)

