from itertools import permutations
import matplotlib.pyplot as plt
import csv
from benchmark import PermutationType, get_data_path
from collections import defaultdict
import numpy as np
from sklearn.metrics import r2_score

def load_data(algorithm_name : str, permutation : PermutationType) -> defaultdict:
    path = get_data_path(permutation, algorithm_name)
    data = defaultdict(list)
    with path.open() as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data[int(row[0])].append(int(row[1]))
    return data

def load_avg_data(algorithm_name : str, permutation : PermutationType):
    data = load_data(algorithm_name, permutation)
    sizes, avg_times = list(), list()
    
    for size, elapsed_time in sorted(data.items()):
        sizes.append(size)
        avg_times.append(sum(elapsed_time) / len(elapsed_time))
    return sizes[3:], avg_times[3:]

def add_to_plot(algorithm_name: str, permutation: PermutationType) -> None:
    sizes, avg_times = load_avg_data(algorithm_name, permutation)
    
    x, y = sizes, avg_times
    logx, logy = np.log(x), np.log(y)

    m, b = np.polyfit(logx, logy, 1)
    fit = np.poly1d((m, b))
    expected_y = fit(logx)
    r2 = r2_score(logy, expected_y)

    p = plt.loglog(x, y, '.', base = 2)
    plt.loglog(x, np.exp(expected_y), '--', base = 2, 
        label = f'{algorithm_name} ({permutation}) : {m:0.5} log x + {b:.5}, r^2 = {r2:.5}',
        color = p[-1].get_color()
    )
    plt.legend(bbox_to_anchor = (.47, 1.1), loc = 'upper center')
    plt.ylabel('Elapsed time in nanoseconds')
    plt.xlabel('Input size (n, # of elements)')

if __name__ == '__main__':
    plt.figure(num = 1, figsize = (8, 5), dpi = 150, facecolor = 'w', edgecolor = 'k')
    add_to_plot('hybrid_sort1', PermutationType.UNIFORMLY_DISTRIBUTED)
    add_to_plot('hybrid_sort1', PermutationType.REVERSE_SORTED)
    add_to_plot('hybrid_sort1', PermutationType.ALMOST_SORTED)    
    plt.show()

