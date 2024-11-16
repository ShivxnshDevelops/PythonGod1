def name(a , bb ="You Have Logined As"):
    print(bb , a)

b = input("Enter N If You Wanna Login AS Guset \nEnter User IF You Wanna Login With Your Username :")

if b=="User":
    a=input("Enter Your Username :") 
    name(a)
else :
    name(a="Guest User 01")


    