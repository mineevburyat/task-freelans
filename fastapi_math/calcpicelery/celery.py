from celery import Celery

app = Celery(broker='pyamqp://guest@192.168.88.82/', backend='rpc://', include=['calcpicelery.tasks'])


class Config:
  result_expires=3600
  task_track_started=True
  enable_utc=True
  timezone='Asia/Irkutsk'

app.config_from_object(Config)

