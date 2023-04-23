import threading # importing thread module
import time # import time module


def countNum():
    print('Sleeping for 2 Seconds')
    time.sleep(2) # sleeping for 2 seconds

start = time.perf_counter() 
t1 = threading.Thread(target=countNum) # creating thread t1 
t2 = threading.Thread(target=countNum) # creating thread t2
t1.start() # starting thread t1
t2.start() # starting thread t2

t1.join() # further execution of program will wait t1 is not finished
t2.join() # further execution of program will wait t2 is not finished

finish = time.perf_counter()
timeTaken = round((finish-start),2)

print(f"Execution Finished in {timeTaken} second(s)")