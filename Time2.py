import time
import datetime as dt


name = input("Enter Your Name :")
Recenttime = time.strftime('%H :%M')
recenttime = time.strftime("%H")




if recenttime=="<=4" or "<12" :
    print("Good Morningh" , name ,"The Time Right Now Is " , Recenttime)
elif recenttime==">=12" or "< 16" :
     print("Good Afternoon" , name , "The Time Right Now Is" , Recenttime)
elif recenttime==">=16" or "< 20" :
    print("Good Evening" , name , "The Time Right Now Is" , Recenttime)
elif recenttime==">= 20" or "> 4" : 
    print("Good Night" , name , "The Time Right Now is " , Recenttime) 
else :
    input("Enter 1 To Retry The Program")
    for i in range():
        RuntimeError


