from concurrent.futures import ThreadPoolExecutor
from time import sleep
 
def return_after_5_secs(message):
    sleep(5)
    return message
 
pool = ThreadPoolExecutor(3)
 
future = pool.submit(return_after_5_secs, ("hello"))
print(future.done())
sleep(2)
print(future.done())
# если done fulse, то result заблокирует поток
print(future.result()) 
sleep(5)
print(future.done())
print(future.result())