
# Thread Synchronization Examples in Python
### (Lock, RLock, Semaphore, Condition, Barrier, and Event)

This project demonstrates how different thread synchronization mechanisms in Python (`threading` module) control concurrent access to shared resources using a common computational function `do_something.py`.

---

## Synchronization Mechanisms Tested

### 1. Lock
**Purpose:** Ensures that only one thread modifies the shared resource (`out_list`) at a time.

**Behavior Observed:**
Thread 0 started.  
Thread 0 finished.  
Thread 1 started.  
Thread 1 finished.  
Thread 2 started.  
Thread 2 finished.  
Length of list (Lock): 21

**Result:** Safe access to the shared list; total length = 21 (expected).

---

### 2. RLock (Reentrant Lock)
**Purpose:** Allows the same thread to acquire the lock multiple times safely.

**Behavior Observed:**  
Similar to Lock — sequential thread completion and consistent results.

**Result:** Safe and consistent access; total length = 21.

---

### 3. Semaphore
**Purpose:** Controls access to a resource by limiting the number of threads allowed to run concurrently.

**Behavior Observed:**
Thread 0 waiting for permit...  
Thread 0 started.  
Thread 1 waiting for permit...  
Thread 2 waiting for permit...  
Thread 1 started.  
Thread 0 finished.  
Thread 1 finished.  
Thread 2 started.  
Thread 2 finished.  
Length of list (Semaphore): 21

**Result:** Threads run in controlled batches; list remains consistent.

---

### 4. Condition
**Purpose:** Enables threads to wait for a certain condition to be met before proceeding.

**Behavior Observed:**
Thread 0 notifying condition.  
Thread 1 notifying condition.  
Thread 2 notifying condition.  
Monitor: Current length = 7  
Monitor: Current length = 14  
Monitor: Current length = 21

**Result:** All threads signal the condition, and the monitor accurately tracks progress.

---

### 5. Barrier
**Purpose:** Synchronizes a fixed number of threads, making them wait until all threads reach a certain point.

**Behavior Observed:**
```

START RACE!!!!
Louie reached the barrier at: Tue Jan  6 20:35:03 2026 | Work done: 15636 items
Dewey reached the barrier at: Tue Jan  6 20:35:03 2026 | Work done: 37112 items
Huey reached the barrier at: Tue Jan  6 20:35:03 2026 | Work done: 32758 items
Race over!

```

**Result:** All threads completed their CPU-bound tasks before crossing the barrier; race synchronization successful.

---

### 6. Event
**Purpose:** Allows threads to signal each other for event-driven coordination.

**Behavior Observed:**
```

2026-01-06 20:35:29,858 Thread-1          INFO     Producer added item: 23 | Work done: 5000 items
2026-01-06 20:35:29,862 Thread-2          INFO     Consumer processed item: 23 | Work done: 5000 items
2026-01-06 20:35:30,864 Thread-1          INFO     Producer added item: 2 | Work done: 5000 items
2026-01-06 20:35:30,864 Thread-2          INFO     Consumer processed item: 2 | Work done: 5000 items
2026-01-06 20:35:31,867 Thread-1          INFO     Producer added item: 7 | Work done: 5000 items
2026-01-06 20:35:31,880 Thread-2          INFO     Consumer processed item: 7 | Work done: 5000 items
2026-01-06 20:35:32,883 Thread-1          INFO     Producer added item: 26 | Work done: 5000 items
2026-01-06 20:35:32,888 Thread-2          INFO     Consumer processed item: 26 | Work done: 5000 items
2026-01-06 20:35:33,886 Thread-1          INFO     Producer added item: 44 | Work done: 5000 items
2026-01-06 20:35:33,901 Thread-2          INFO     Consumer processed item: 44 | Work done: 5000 items

````

**Result:** Producer and Consumer threads successfully coordinated using the Event; CPU-bound tasks executed and items processed sequentially.

---

## Comparative Evaluation (Markdown table)
| Synchronization Type | Main Use                                  | Behavior                      | Safety | Best For                         |
|----------------------|-------------------------------------------|-------------------------------|--------|----------------------------------|
| Lock                 | Prevents simultaneous access              | Sequential execution          | Safe   | General thread safety            |
| RLock                | Reentrant version of Lock                 | Similar to Lock               | Safe   | Nested locking scenarios         |
| Semaphore            | Limits concurrent access                  | Controlled parallelism        | Safe   | Managing limited resources       |
| Condition            | Waits for specific conditions/signals     | Event-driven coordination     | Safe   | Producer-consumer models         |
| Barrier              | Waits for all threads to reach a point   | Threads synchronized at barrier | Safe   | Race or checkpoint scenarios     |
| Event                | Signal threads for coordination           | Event-driven signaling        | Safe   | Producer-consumer or notifications |

---

## Unified Conclusion

All six synchronization mechanisms — Lock, RLock, Semaphore, Condition, Barrier, and Event — successfully maintained data integrity during concurrent execution. Each method produced the expected results and prevented race conditions. Choose the primitive that matches your concurrency requirement:

- **Lock/RLock:** Simple mutual exclusion  
- **Semaphore:** Limit concurrent access to resources  
- **Condition:** Coordination via signals  
- **Barrier:** Synchronize threads at a checkpoint  
- **Event:** Thread signaling for event-driven workflows  

---

## How to Run

Execute each file separately to observe the synchronization behavior:

```bash
python Chapter_02/Lock.py
python Chapter_02/RLock.py
python Chapter_02/Semaphore.py
python Chapter_02/Condition.py
python Chapter_02/Barrier.py
python Chapter_02/Event.py
````

---

```
# CPU-bound work is provided by do_something.py
# Ensure do_something.py is in the same folder as these scripts
```

