import multiprocessing
from threading import Thread, Event
import threading
import time

exitFlag = 0


class MyThread(threading.Thread):
    def __init__(self, thread_id, name, counter):
        super(MyThread, self).__init__()
        print(super(MyThread, self))
        self.thread_id = thread_id
        self.name = name
        self.counter = counter


# def loop():
#     print(f'thread {threading.current_thread().name} is running')
#     n = 0
#     while n < 5:
#         n = n + 1
#         print(f'thread {threading.current_thread().name} >>> {n}')
#         time.sleep(1)
#
#     print(f'thread {threading.current_thread().name} ended')
#
#
# print(f'thread {threading.current_thread().name} is running')
# t = threading.Thread(target=loop, name='LoopThread')
# t.start()
# t.join()
# print(f'thread {threading.current_thread().name} ended')

def countdown(n, started_evt):
    print('countdown starting')
    started_evt.set()
    while n > 0:
        print('T-minus', n)
        n -= 1
        time.sleep(5)



class CountdownTask:
    def __init__(self):
        self.__running = True

    def terminate(self):
        self.__running = False

    def run(self, n):
        while self.__running and n > 0:
            print('T-minus', n)
            n -= 1
            time.sleep(5)


started_evt = Event()
print('launching countdown')
t = Thread(target=countdown, args=(10, started_evt))
t.start()

started_evt.wait()
print('countdown is running')

