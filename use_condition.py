import threading
import time


def fun(condition):
    time.sleep(1)

    condition.acquire()
    print('thread 1 acquire lock')

    condition.notify()

    condition.wait()
    print('thread 1 acquire lock again')
    condition.release()


def func2(condition):
    condition.acquire()
    print('thread 2 acquire lock')
    condition.wait()
    print('thread 2 acquire lock again')
    condition.notify()
    condition.release()


if __name__ == '__main__':
    def worker(n, sema):
        # Wait to be signaled
        sema.acquire()

        # Do some work
        print('Working', n)


    # Create some threads
    sema = threading.Semaphore(0)
    nworkers = 10
    for n in range(nworkers):
        t = threading.Thread(target=worker, args=(n, sema,))
        t.start()
