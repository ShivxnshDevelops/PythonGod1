Wel = "Welcome To The Program , The Author Of The Program Is ShivxnshDevelops"
print(Wel.center(50))

x = input("\nEnter The String Of which You Wanna Change The Something :")
print("""1: If You Want To Change it In Upper Case \n2: If You Want To Change it In Lower Case \n3: If You Want To Remove Any Special Characters \n4: if You Want To Replace The String With Something else.\n5: If You Want To Use The Captalize Case""")


K = input("Enter The Value According to The Instructions Given Above :")

if K=="1" :
    print(x.upper())
elif K=="2" :
    print(x.lower())
elif K=="3" :
    z = input("Enter The Special Character Which You wanna Remove")
    print(x.rstrip(z))
elif K=="4" :
    a = input("Enter The Original Str Which You Want To Replace : ")
    n = input("Enter The str Which You Want To Replace With The Original ")
    print(x.replace( a , n))
elif K=="5" :
    print(x.capitalize())
else :
    print("The Value You Entered Is InVailid \n Kindly Read The Instructions Carefully <3")

# The Strings Are Inmutable SO The Str Which Is Formed Aftr is New AND the Old Str isd not changed
