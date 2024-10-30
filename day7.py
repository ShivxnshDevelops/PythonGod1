a = int(input("Enter The First Value :"))
b = int(input("Enter The Second Value :"))
c = input("Enter The Specific Operator For The Operation :")

if c == "+" :
    print("The Addition Of The Values :", a+b)
elif c == '-' :
    print("The Subtraction Of The Values :",a-b)
elif c == '*':
    print("The Multipliucation Of The Values :", a*b)
elif c == "/" :
    print("The Division Of The Values :" , a/b)
elif c == '//' :
    print("The Quotient Of The Values :" , a//b)
elif c == '**' :
    print("The Exponent Of Yhe Values :", a**b)
elif c == '%':
    print("The Modulus Of The Values :", a%b)
else :
    print("-------------invailid Operator---------------")

print("Thanks For Using Our Calculator , Credit Goes To ShivxnshDevelops")