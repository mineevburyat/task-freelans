from multiprocessing import Pool
import time
import random

def f(x):
    return x*x

def worker(number):
    sleep = random.randrange(1, 10)
    time.sleep(sleep)
    print("I am Worker {}, I slept for {} seconds".format(number, sleep))
    return number*number


if __name__ == '__main__':
    p = Pool(4)
    print(p)
    print(p.map(worker, [1,2,3,4,5,6,7,8]))