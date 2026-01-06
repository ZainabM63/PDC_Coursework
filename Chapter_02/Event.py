# Event.py
import logging
import threading
import time
import random
from do_something import do_something  # Import CPU-bound function

LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

items = []
event = threading.Event()

class Consumer(threading.Thread):
    def run(self):
        while True:
            event.wait()  # Wait for producer to signal
            out_list = []
            do_something(5000, out_list)  # simulate CPU-heavy work on consumer side
            if items:
                item = items.pop()
                logging.info('Consumer processed item: {} | Work done: {} items'
                             .format(item, len(out_list)))
            event.clear()  # reset event for next item

class Producer(threading.Thread):
    def run(self):
        for i in range(5):
            item = random.randint(0, 100)
            items.append(item)
            out_list = []
            do_something(5000, out_list)  # simulate CPU-heavy work on producer side
            logging.info('Producer added item: {} | Work done: {} items'
                         .format(item, len(out_list)))
            event.set()
            time.sleep(1)

if __name__ == "__main__":
    t1 = Producer()
    t2 = Consumer()

    t1.start()
    t2.start()

    t1.join()
    t2.join()
