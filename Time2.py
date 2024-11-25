import time
import datetime as dt


name = input("Enter Your Name :")
Recenttime = time.strftime('%H :%M')
x= int(time.strftime("%H"))




if(x>=0 and x<12):
    print("Good Morning" , name , "the Time Right Now is" , Recenttime)
elif(x>=12 and x<18):
    print("Good Afternoon" , name , "the Time Right Now is" , Recenttime)

elif(x>=18 and x<0):
    print("Good Evening" , name , "the Time Right Now is" , Recenttime)
else:
    print("Good Night" , name , "the Time Right Now is" , Recenttime)