import time
import datetime as dt
import pytz


name = input("Enter Your Name :")
Recenttime = time.strftime('%H :%M')
recenttime = time.strftime("%H")







if recenttime=="> 12" or "< 4" :
        print("Good Morning" , name ,"The Time Right Now Is " , Recenttime)
elif recenttime=="12" :
        print("Good Afternoon" , name , "The Time Right Now Is" , Recenttime)
elif recenttime=="< 12" or "> 18" :
        print("Good Evening" , name , "The Time Right Now Is" , Recenttime)
else : 
        print("Good Night" , name , "The Time Right Now is " , Recenttime) 



