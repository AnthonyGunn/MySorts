from pkgutil import get_data
from tkinter import N
import time
import argparse
from enum import Enum
from unittest import result
import requirements as rq
import random
import csv
from pathlib import Path
import math

DATA_DIRECTORY = Path('sorting_data')

class PermutationType(Enum):
    UNIFORMLY_DISTRIBUTED = 'random'
    ALMOST_SORTED = 'almost'
    REVERSE_SORTED = 'reverse'

SORTING_ALGORITHMS = {
    'insertion_sort' : rq.insertion_sort,
    'merge_sort' : rq. merge_sort, 
    'shell_sort1' : rq.shell_sort1, 
    'shell_sort2' : rq.shell_sort2, 
    'shell_sort3' : rq.shell_sort3, 
    'shell_sort4' : rq.shell_sort4, 
    'hybrid_sort1' : rq.hybrid_sort1,  
    'hybrid_sort2' : rq.hybrid_sort2,   
    'hybrid_sort3' : rq.hybrid_sort3,  
    }

def fetch_args() -> 'args':
    parser = argparse.ArgumentParser(
        description = 'Benchmark several algorithms'
    )
    parser.add_argument('input_start', type = int,
        help = 'First input size to be passed to the sorting algorithm'
    )
    parser.add_argument('mult_factor', type = int,
        help = 'The factor by which to multiply the input size'
    )
    parser.add_argument('runs', type = int,
        help = 'The number of benchmarks to run'
    )
    parser.add_argument('--permutation', choices = [e.value for e in PermutationType], default = 'random',
        help = 'The input permutation to be sorted'
    )
    parser.add_argument('--algorithm', dest = 'algorithm_name', choices = SORTING_ALGORITHMS.keys(), default = 'insertion_sort',
        help = 'The sorting algoritm to use', required = True,
    )
    parser.add_argument('--num_iterations', dest = 'NUM_ITERATIONS', type = int, default = 1,
        help = 'The number of iterations to run on input size'
    )
    args = parser.parse_args()
    args.permutation = PermutationType(args.permutation)
    args.algorithm = SORTING_ALGORITHMS[args.algorithm_name]
    return args

def generate_list(permutation: PermutationType, size: int) -> list[int]:
    result_list = list(range(size))
    match permutation:
        case PermutationType.UNIFORMLY_DISTRIBUTED:
            random.shuffle(result_list)
        case PermutationType.REVERSE_SORTED:
            result_list.sort(reverse = True)
        case PermutationType.ALMOST_SORTED:
            for i in range(int(2 * math.log2(size))):
                i = random.randint(0, size - 1)
                j = random.randint(0, size - 1)
                result_list[i], result_list[j] = result_list[j], result_list[i]
    return result_list

def run_benchmark(args: 'str') -> None:
    print(f"---TIMES CALCULATED ARE AVERAGED BASED ON {args.NUM_ITERATIONS} ITERATIONS---")
    list_size = args.input_start
    for runs in range(args.runs):
        total_time = 0 

        for num_of_iterations in range(args.NUM_ITERATIONS):
            result_list = generate_list(args.permutation, list_size)
            total_time += benchmark(result_list, args.algorithm)

        avg = int(total_time / args.NUM_ITERATIONS)
        avg_in_seconds = avg * 0.000000001
        avg_time = "{:.2f}".format(avg_in_seconds)
        print(f"Input size: {str(list_size):>30} ... done in {avg_time} seconds")
        save_data(args.permutation, args.algorithm_name, list_size, avg)
        
        list_size *= args.mult_factor

def benchmark(nums: list[int], execute_algorithm: 'function') -> float:
    start_time = time.process_time_ns()
    execute_algorithm(nums)
    end_time = time.process_time_ns()
    return end_time - start_time

def get_data_path(permutation: PermutationType, algorithm_name: str) -> Path:
    directory = DATA_DIRECTORY / algorithm_name
    directory.mkdir(parents = True, exist_ok = True)
    return (directory / permutation.value).with_suffix('.csv')

def save_data(permutation: PermutationType, algorithm_name: str, size: int, elapsed_time: int) -> None:
    path = get_data_path(permutation, algorithm_name)

    with path.open('a') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([size, elapsed_time])

if __name__ == '__main__':
    args = fetch_args()
    run_benchmark(args)
