import multiprocessing
import random
import time
from datetime import datetime


def processTask(processId):
    waitTime = random.uniform(0, 1)  
    time.sleep(waitTime)
    print(f"Process {processId} finished at {datetime.now().strftime('%H:%M:%S.%f')}")

if __name__ == "__main__":

    processes = [multiprocessing.Process(target=processTask, args=(i,)) for i in range(1, 4)]
    
    for process in processes:
        process.start()
    
    for process in processes:
        process.join()
