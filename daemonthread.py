import time
import threading

def timer():
    print()
    print()
    count = 0
    while True:
        time.sleep(1)
        count = count+1
        print(f" \ntime taken :{count}")
        


y = threading.Thread(target = timer, daemon = True)
y.start()

user = input("enter the password ")


