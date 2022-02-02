from threading import Thread, Lock
from multiprocessing import Process, Lock as PLock

class SharedObject(object):
    def __init__(self, property):
        self.property = property

def some_func(shared_obj, lock):
    lock.acquire()
    shared_obj.property += 1
    print(shared_obj.property, lock.release())

if __name__ == '__main__':
    # работа с потоками:
    lock = Lock()
    shared_obj = SharedObject(0)
    for thread_number in range(5):
        thread = Thread(target=some_func, args=(shared_obj, lock))
        thread.start()
    # 1 2 3 4 5

    # работа с процессами:
    lock = PLock()
    shared_obj = SharedObject(0)
    for process_number in range(5):
        process = Process(target=some_func, args=(shared_obj, lock))
        process.start()
    # 1 1 1 1 1
