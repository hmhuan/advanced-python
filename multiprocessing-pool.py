from multiprocessing import Pool
import time
def cube(number):
    return number ** 3

if __name__ == '__main__':
    numbers = range(1000)
    p = Pool()


    start = time.time()
    result_2 = []
    for iv, number in enumerate(numbers):
        result_2.append(cube(number))
    end = time.time()
    print(end - start)

    start = time.time()
    result = p.map(cube, numbers)
    end = time.time()
    p.close()
    p.join()
    print(end - start)
    
    start = time.time()
    result_1 = map(cube, numbers)
    end = time.time()
    print(end - start)