from .celery import app
from time import sleep


@app.task(bind=True)
def calcPi(self, decimal:int):
  accuracy = {2: 1000, 3: 10000, 4: 100000, 5: 1000000, 6: 10000000, 7: 100000000, 8: 1000000000, 9:10000000000}
  sleepConst = { 2: 2, 3: 1, 4: 1, 5: 0.5}
  # print(decimal)
  if decimal > 9:
    decimal = 9
  if decimal < 2:
    decimal = 2
  summa = 1
  percent = 0
  sleepVar = 0
  # percentwork
  _halfpercent = accuracy[decimal] * 0.005
  _maxrange = accuracy[decimal]
  # slepping for speed calc
  if decimal < 6:
    sleepVar = sleepConst[decimal]
  for i in range(1,_maxrange):
    summa += pow(-1, i) / (2*i + 1)
    if i % _halfpercent == 0:
      percent += 0.5
      self.update_state(state="PROGRESS", meta={'percent': percent, 'current_pi': summa * 4})
      sleep(sleepVar)
  return round(summa * 4, decimal)
