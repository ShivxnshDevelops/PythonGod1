print("This File Is For Learning DocStrings In Python \nAuthor Of The Progrm - Shiv4nsh")
def factorial(a):
    '''This Function Used For The Factorial Of The Intger/Number in Python'''
    if(a==0 or a==1):
        return 1
    else :
        return a * factorial(a-1)
    
a = int(input("Enter The Value For The Factorial :"))
print(factorial(a))
print(factorial.__doc__)