"""функция долговременного вычисления в отдельном потоке с сохранением результатов и промежуточных значений в процессе вычислений.
Основная идея передать функции аргументы и так же ссылку на список с индексом, где будут хранится результаты.
Функцию запустить как поток"""

# percentwork = 0
# result [{"pi":float, "percentwork":float},{}]
def calcPi(decimal:int):
  accuracy = {2: 1000, 3: 10000, 4: 100000, 5: 1000000, 6: 10000000, 7: 100000000, 8: 1000000000, 9:10000000000}
  print(decimal)
  if decimal > 9:
    decimal = 9
  if decimal < 2:
    decimal = 2
  summa = 1
  percent = 0
  # global percentwork
  _halfpercent = accuracy[decimal] * 0.005
  _maxrange = accuracy[decimal]
  for i in range(1,_maxrange):
    summa += pow(-1, i) / (2*i + 1)
    if i % _halfpercent == 0:
      percent += 0.5
      
  percent = 100
  return round(summa * 4, decimal)
  

# print(calcPi(5))
# print(percentwork)

