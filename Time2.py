import time
import datetime as dt


name = input("Enter Your Name :")
Recenttime = time.strftime('%H :%M')
recenttime = int(time.strftime("%H"))




if recenttime == "<= 4" and "> 12":
    print("Good Morning" , name , "the Time Right Now is" , Recenttime)
elif recenttime ==  ">= 12"and "> 17":
    print("Good AfterNoon" , name , "the Time Right Now is" , Recenttime)
elif recenttime == ">= 17"and ">20":
    print("Good Evening" , name , "the Time Right Now is" , Recenttime)
else :
    print("Good Night" , name , "the Time Right Now is" , Recenttime)

