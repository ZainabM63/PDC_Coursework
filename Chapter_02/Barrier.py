# Barrier.py
from random import randrange
from threading import Barrier, Thread
from time import ctime
from do_something import do_something  # Import CPU-bound function

num_runners = 3
finish_line = Barrier(num_runners)
runners = ['Huey', 'Dewey', 'Louie']

def runner():
    name = runners.pop()
    out_list = []
    
    # Simulate CPU-bound work instead of sleep
    work_size = randrange(10000, 50000)  # adjust size to simulate randomness
    do_something(work_size, out_list)
    
    print('%s reached the barrier at: %s | Work done: %d items' %
          (name, ctime(), len(out_list)))
    finish_line.wait()

def main():
    threads = []
    print('START RACE!!!!')
    for i in range(num_runners):
        threads.append(Thread(target=runner))
        threads[-1].start()
    for thread in threads:
        thread.join()
    print('Race over!')

if __name__ == "__main__":
    main()
