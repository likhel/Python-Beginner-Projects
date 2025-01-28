import time
print(time.ctime(0)) #converts  a time  expressed in seconds since epoch into readable strings 
print(time.time())  #returns current time in seconds from epoch(when your computer thinks the time began or reference point)
print(time.ctime(time.time())) 

time_object = time.localtime()
time_object = time.gmtime()
print(time_object)
timestamp = time.strftime('%B %d %Y',time_object)
print(timestamp)
time1 = '2020 April 20'
time_object1 = time.strptime(time1,'%Y %B %d')
print(time_object1)

time_tuple = (2032,6,7,9,0,7,0,0,0)   #year,month,day,hours,minutes,seconds,day of the week,day of the month,dst
time_string = time.asctime(time_tuple)
print(time_string)
time_string1 = time.mktime(time_tuple)
print(time_string1)
'''timestamp=(time.strftime('%H:%M:%S'))
print(timestamp)
timestamp=int(time.strftime('%H'))
print("The time is: ", timestamp)

if((timestamp<=12 and timestamp>=5)):
    print("Good Morning!")
elif((timestamp>=12 and timestamp<17)): 
    print("Good Afternoon!")  
elif((timestamp>=18 and timestamp<=20 )): 
    print("Good Evening")
else:
    print("Good night")'''
