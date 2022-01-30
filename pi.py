import time, sched

class LeibnicPi:
  accuracy = {2: 1000, 3: 10000, 4: 100000, 5: 1000000, 6: 10000000, 7: 100000000, 8: 1000000000}
  def __init__(self, decimals: int):
    if decimals > 8 or decimals < 2:
      raise ValueError("Rnge from 2 to 8 inclusive")
    self.summa = 1
    self.percentwork = 0
    self._halfpercent = LeibnicPi.accuracy[decimals] * 0.005
    self.maxrange = LeibnicPi.accuracy[decimals]
    self.decimals = decimals
    self.calcFlag = False
  
  def calcPi(self):
    self.calcFlag = True
    for i in range(1, self.maxrange):
      self.summa += pow(-1, i) / (2*i + 1)
      if i % self._halfpercent == 0:
        self.percentwork += 0.5
    self.calcFlag = False
    self.percentwork = 100
  
  def getPercentWork(self):
    return(self.percentwork)

  def getPi(self):
    return round(self.summa * 4, self.decimals)

  def getCalcFlag(self):
    return self.calcFlag

Pi7decimals = LeibnicPi(6)
Pi7decimals.calcPi()
print(Pi7decimals.getPi())