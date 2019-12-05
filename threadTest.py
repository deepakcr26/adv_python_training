import threading
import time

SEP = "_"*50


class MyThread(threading.Thread):
    def __init__(self, threadID, name, counter=100, delay=3):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.delay = delay

    def run(self):
        print("Starting {}".format(self.name))
        # threadLock.acquire()
        print_time(self.name, self.delay, 3)
        print("Timer item for {} is completed".format(self.name))
        print(SEP)
        print("Beginning the displaying of characters for: {} ".format(self.name))
        display_char(self.counter, self.name)
        # threadLock.release()
        print(SEP)
        print("Finished {} Thread".format(self.name))


class MyThread2(threading.Thread):
    def __init__(self, threadID, name, counter=10, delay=1):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.delay = delay

    def run(self):
        print("Welecome to MyThread2, Here you will find a different and unique experience")
        while self.counter:
            print("Process: {} is performing an action".format(self.name))
            time.sleep(1)
            self.counter -= 1


def print_time(threadName, delay, counter):
    while counter:
        time.sleep(delay)
        print("{}: {}".format(threadName, time.ctime(time.time())))
        counter -= 1


def display_char(counter, char):
    while counter:
        print(char)
        counter -= 1


threadLock = threading.Lock()


threads = []
thread1 = MyThread(1, "X", 1100)
thread2 = MyThread2(2, "YYY", 1000)

thread1.start()
thread2.start()

threads.append(thread1)
threads.append(thread2)

for t in threads:
    t.join()
print("Exiting MainThread")
