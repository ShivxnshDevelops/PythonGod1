print("This Project Is To USe Recursion in Python By Creating Fibonacci Series \nAuthor - Shiv4nsh")

def fibonacci(a):
    if a==0:
        return 0
    elif a==1:
        return 1
    else:
        return fibonacci(a-1) + fibonacci(a-2)
a = int(input("Enter The Value To Find The Fibonacci Of The Value :"))
print(f"The Fibonacci Of {a} is {fibonacci(a)}")