from multiprocessing import Process, Value, Array
from multiprocessing import Lock
import os
import time
from multiprocessing import Queue


def square_numbers():
    for i in range(1000):
        result = i * i
    print(result)
    pass


def add_element_to_array(arr, lock):
    for _ in range(10000):
        for i in range(len(arr)):
            # with lock: # use with context instead of lock.acquire() and lock.release()
            arr[i] += 1

def make_double(numbers, queue):
    for i in numbers:
        queue.put(i * i)
    pass

def make_negative(numbers, queue):
    for i in numbers:
        queue.put(-i)
    pass

if __name__ == '__main__':
    processes = []
    num_procs = os.cpu_count()
    lock = Lock()

    for i in range(num_procs):
        process = Process(target=square_numbers)
        processes.append(process)
        pass

    for process in processes:
        process.start()

    for process in processes:
        process.join()

    shared_arr_1 = Array('i', [0, 1, 20])
    shared_arr_2 = Array('i', [1, 2, 3])
    shared_arr_3 = Array('i', [1, 5, 10])
    print(shared_arr_1[:])
    print(shared_arr_2[:])
    print(shared_arr_3[:])

    process_1 = Process(target=add_element_to_array, args=(shared_arr_1, lock))
    process_2 = Process(target=add_element_to_array, args=(shared_arr_2, lock))
    process_3 = Process(target=add_element_to_array, args=(shared_arr_3, lock))

    process_1.start()
    process_2.start()
    process_3.start()

    process_1.join()
    process_2.join()
    process_3.join()

    print(shared_arr_1[:])
    print(shared_arr_2[:])
    print(shared_arr_3[:])

    numbers = [1, 2, 3, 4, 5, 6]
    q = Queue()
    process_1 = Process(target=make_double, args=(numbers, q))
    process_2 = Process(target=make_negative, args=(numbers, q))

    process_1.start()
    process_2.start()

    process_1.join()
    process_2.join()

    while not q.empty():
        print(q.get())
        pass
    

