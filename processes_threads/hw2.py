import threading
import time
import signal
import sys

sem = threading.Semaphore()
shutdown_flag = threading.Event()


class SignalHandler:
    def __init__(self, workers):
        self.workers = workers

    def __call__(self, signum, frame):
        shutdown_flag.set()

        for worker in self.workers:
            worker.join()

        sys.exit(0)


def fun1():
    while not shutdown_flag.is_set():
        sem.acquire()
        print(1)
        sem.release()
        time.sleep(0.25)

    sem.release()


def fun2():
    while not shutdown_flag.is_set():
        sem.acquire()
        print(2)
        sem.release()
        time.sleep(0.25)

    sem.release()


def test():
    print('Starting main program')

    t1 = threading.Thread(target=fun1)
    t2 = threading.Thread(target=fun2)

    handler = SignalHandler([t1, t2])
    signal.signal(signal.SIGINT, handler)

    t1.start()
    t2.start()

    while True:
        time.sleep(0.5)


if __name__ == '__main__':
    test()
