print("This File Is For Learning DocStrings In Python \nAuthor Of The Progrm - Shiv4nsh")
def factorial(a):
    if(a==0 or a==1):
        return 1
    else :
        a * factorial(a-1)
a = int(input("Enter The Value For The Factorial : "))
factorial(a)