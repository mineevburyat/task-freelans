"""функция долговременного вычисления в отдельном потоке с сохранением результатов и промежуточных значений в процессе вычислений.
Основная идея передать функции аргументы и так же ссылку на список с индексом, где будут хранится результаты.
Функцию запустить как поток"""

# percentwork = 0
# result [{"pi":float, "percentwork":float},{}]
def calcPi(decimal:int, result:list, index:int):
  accuracy = {2: 1000, 3: 10000, 4: 100000, 5: 1000000, 6: 10000000, 7: 100000000, 8: 1000000000, 9:10000000000}
  if decimal > 9:
    decimal = 9
  if decimal < 2:
    decimal = 2
  summa = 1
  # global percentwork
  _halfpercent = accuracy[decimal] * 0.005
  _maxrange = accuracy[decimal]
  for i in range(1,_maxrange):
    summa += pow(-1, i) / (2*i + 1)
    if i % _halfpercent == 0:
      result[index]["percentwork"] += 0.5
      result[index]["pi"] = round(summa*4, decimal)
  result[index]["percentwork"] = 100
  result[index]["pi"] = round(summa * 4, decimal)
  return 0

# print(calcPi(5))
# print(percentwork)

from threading import Thread
from time import sleep

if __name__ == "__main__":
  print("Hello from main Process")
  THREDNUMBER = 6
  result = []
  threadslist = []
  for i in range(THREDNUMBER):
    result.append({"pi":0, "percentwork":0})
    thread = Thread(target=calcPi, args=(2+i, result, i), daemon=True)
    thread.setName("findPIto{d}decimal".format(d=i+2))
    threadslist.append(thread)
    thread.start()

  continiusFlag = True
  while continiusFlag:
    sleep(1)
    i = 0
    for thread in threadslist:
      if thread.is_alive():
        print("Поток {name} идентификатор {ident} : процент выполнения: {percent}. Промежуточное значение pi: {pi}".
            format(name=thread.getName(), ident=thread.ident, percent=result[i]["percentwork"], pi=result[i]["pi"]))
      i += 1
      # print(dir(thread))
  print(result[0]["pi"])