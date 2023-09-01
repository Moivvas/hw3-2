from timeit import timeit
from multiprocessing import Pool, cpu_count
import time


def factorize(*numbers):
    main_divide_list = []
    for num in numbers:
        divide_list = [i for i in range(1, num + 1) if num % i == 0]
        main_divide_list.append(divide_list)
    return main_divide_list

def super_factorize(*numbers):
    main_divide_list = []
    for num in numbers:
        divide_list = [i for i in range(1, num + 1) if num % i == 0]
        main_divide_list.append(divide_list)
    return main_divide_list

if __name__ == '__main__':
    
    execution_time = timeit(lambda: factorize(128, 255, 23243503, 52345674), number=1)
    print(f"Execution time: {execution_time} seconds")
    
    pool = Pool(cpu_count())
    execution_time_super_factorize = timeit(lambda: pool.map(super_factorize, [128, 255, 23243503, 52345674]), number=1)
    print(f"Execution time of super_factorize: {execution_time_super_factorize} seconds")
