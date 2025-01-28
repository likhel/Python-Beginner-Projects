#multiprocessing = running task in parallel in a different cpu cores,bypasses GIL used for thread
#multiprocessing = better for cpu bound tasks
#multithreading = better for io bound task

# main_module.py

# main_module.py

import time

def main():
    from multiprocessing import Process

    # Import 'counter' function conditionally inside the 'main()' function to avoid circular imports
    from counter_module import counter

    a = Process(target=counter, args=(100000,))
    a.start()
    a.join()
    print("time taken:", time.perf_counter())

if __name__ == '__main__':
    main()
