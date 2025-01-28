 #a flow of execution.Like a seperate order of instructions.
# however each flow takes turn running into concurrency.
#GIL = Global interpreter lock
#allows only one thread to hold the control the python interpreter
#cpu bound : program/task spend most of their time waiting for internal events(cpu intensive use
#multiprocessing)
#i/o bound : program/task spend most of their time waiting for external events(user input web 
# scrapping use multithreading) 



import time 
import threading 

def breakfast():
    time.sleep(3)
    print("you ate breakfast")
    

def coffee():
    time.sleep(4)
    print("you drank coffee ")
    

def study():
    time.sleep(4) 
    print("you finished studying")

x = threading.Thread(target = breakfast, args = ())
x.start()

y = threading.Thread(target = coffee, args = ())
y.start()

z = threading.Thread(target = study, args = ())
z.start()
    

#breakfast()
#coffee()
#study()

print(threading.activeCount())
print(threading.enumerate())
print(time.perf_counter())