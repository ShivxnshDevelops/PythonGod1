print("This Program Is Used To Find Out The Electricity Bill Of your Home/House \nAuthor - Shiv4nsh Develops")
def bill(a , b , c):
    print("The Electricity Bill Of Your Building Is - " , "₹", (b - a)*c , 
          "\nThe Total Unit Electricity You Have Used In Last Month - " , (b-a) , "Kwh")
def joulecnverter(a , b):
  print("The Units Electricity You Have Used Into Joules -" , (b-a)*(3.6 *  10**6))


a = int(input("Enter No. Of Units Electricity You Have Used Previos Month - "))
b = int(input("Enter No. Of Units Electricity You Have Used This Month - "))
c = int(input("Enter Rate Of Electricity Per Unit - "))

bill(a , b , c)

x = input("Do You Want To Convert The Units Electricity Which You Have Used Into Joules ? \nType Yes Or No - ")
if x=="Yes":
   joulecnverter(a , b)
elif x=="No":
   print("Okay !! Thanks For Using The Program")
else :
   print("Invalid Input | ErrOr 404")