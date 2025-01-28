import random
import time

def naive_search(l,target):
    for i in range(len(l)):
        if l[i] == target:
            return i
        else:
            return -1
    
def binary_search(l, target, low = None, high = None):
    if low is None:
        low = 0
    if high is None:
        high = len(l) - 1
    
    if high < low:
        return -1
    
    midpoint = (high + low)//2
    
    if l[midpoint] == target:
        return midpoint
    elif l[midpoint] > target:
        return binary_search(l, target, low, midpoint-1)
    else:
        return binary_search(l, target, midpoint + 1, high)

if __name__ == '__main__':
    length = 1000
    sorted_list = set()

    while len(sorted_list) < 1000:
        sorted_list.add(random.randint(-4*length, 4*length))
    sorted_list = sorted(list(sorted_list))

    start = time.time()
    for i in sorted_list:
        result = naive_search(sorted_list, i)
    end = time.time()
    print('Naive search time:', (end - start)/length, 'seconds')

    start = time.time()
    for i in sorted_list:
        result = binary_search(sorted_list, i)
    end = time.time()
    print('binary search time:', (end - start)/length, 'seconds')






