import process_image
import time
import os
import psutil

t1 = time.time()

occupied_grids = process_image.main("20x20_600p/t4.jpg")
planned_path = process_image.main("20x20_600p/t4.jpg")
print ("Occupied Grids : ")
print (planned_path)

t2 = time.time()

print()
pid = os.getpid()
py = psutil.Process(pid)
memoryUse = py.memory_info()[0]/2.**30
print('Memory Use:', memoryUse)
print("Time Elapsed: ", t2-t1)