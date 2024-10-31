import time
import datetime as dt
import pytz


name = input("Enter Your Name :")
Recenttime = time.strftime('%H :%M')
recenttime = time.strftime("%H")



print("India ' s Code is Ind \n America ' s Code is USA")

z = pytz.timezone("Europe/France")

x = str(input("Enter The Country Code :"))

if x=="Ind" :
    if recenttime=="> 12" or "< 4" :
        print("Good Morning" , name ,"The Time Right Now Is " , Recenttime)
    elif recenttime=="12" :
        print("Good Afternoon" , name , "The Time Right Now Is" , Recenttime)
    elif recenttime=="< 12" or "> 18" :
        print("Good Evening" , name , "The Time Right Now Is" , Recenttime)
    else : 
        print("Good Night" , name , "The Time Right Now is " , Recenttime) 



elif x=="USA":
        if z=="> 12" or "< 4" :
            print("Good Morningh" , name ,"The Time Right Now Is " , Recenttime)
        elif z=="12" :
            print("Good Afternoon" , name , "The Time Right Now Is" , Recenttime)
        elif z=="< 12" or "> 18" :
            print("Good Evening" , name , "The Time Right Now Is" , Recenttime)
        else : 
            print("Good Night" , name , "The Time Right Now is " , Recenttime)