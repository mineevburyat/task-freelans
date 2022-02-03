from celery import Celery

app = Celery('calcpicelery', broker='pyamqp://guest@192.168.88.82/', backend='rpc://', include=['calcpicelery.tasks'])

app.conf.update(result_expires=3600, )

if __name__ == '__main__':
  app.start()