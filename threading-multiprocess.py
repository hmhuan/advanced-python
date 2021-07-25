from threading import Thread
from multiprocessing import Process
import os

def sum_numbers():
    result = 0
    for i in range(10000):
        result += i
        pass
    print(result)
    pass


if __name__ == "__main__":
    threads = []
    num_threads = 10

    print("threading...")
    print(os.cpu_count())

    for i in range(num_threads):
        thread = Thread(target=sum_numbers)
        threads.append(thread)
        pass

    for thread in threads:
        thread.start()
        pass

    for thread in threads:
        thread.join()
        pass
