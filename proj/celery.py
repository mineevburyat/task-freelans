from celery import Celery, Task
from celery.utils.log import get_task_logger
logger = get_task_logger(__name__)
class Config:
  broker_url='pyamqp://guest@192.168.88.82/'
  enable_utc = True
  timezone = 'Asia/Irkutsk'
  result_expires = 3600
  task_track_started = True
  result_backend='redis://192.168.88.82/0'
  result_persistent=True
  include=['proj.tasks']

class DebugTask(Task):
  def __call__(self, *args, ** kwargs):
    logger.info('TASK STARTING: {0.name}[{0.request.id}]'.format(self))
    logger.info('TASK EXPIRES: [{0.request.expires}]'.format(self))
    logger.info('TASK ARG: ({0.request.args}]'.format(self))
    logger.info('TASK INFO: ({0.request.delivery_info}]'.format(self))
    logger.info('TASK CORRELATION: ({0.request.correlation_id}]'.format(self))
    logger.info('TASK REPLY TO: ({0.request.reply_to}]'.format(self))
    return self.run(*args, **kwargs)

app = Celery()
# app.conf.update(
#   broker_url='pyamqp://guest@192.168.88.82/',
#   enable_utc = True,
#   timezone = 'Asia/Irkutsk',
#   result_expires = 3600,
#   task_track_started = True,
#   result_backend='rpc://',
#   include=['proj.tasks'])

app.config_from_object(Config)
app.Task = DebugTask

if __name__ == '__main__':
  app.start()
