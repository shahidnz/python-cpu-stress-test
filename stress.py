from multiprocessing import Pool
from multiprocessing import cpu_count
import argparse
import math


def stress(x):
    while True:
        for i in range(1, int(math.sqrt(x)) + 1):
            if x % i == 0:
                x**x
        x**x


def parse_cmd_args():
    parser = argparse.ArgumentParser(description='CPU and Memory stresser'
                                                 'made in python')
    parser.add_argument('-m', '--memory', type=int, default=1024,
                        help='The amount of memory in megabytes to eat',
                        required=False)
    parser.add_argument('-c', '--cores', type=int, default=cpu_count(),
                        help='The amount of logical cores to stress',
                        required=False)
    args = parser.parse_args()
    return args

MB = 1024*1024

if __name__ == '__main__':

    cores = parse_cmd_args().cores
    mem_eat = "a" * MB * parse_cmd_args().memory
    print(f"Stressing {cores} cores")
    pool = Pool(cores)
    pool.map(stress, range(cores))
