x = input("Enter The String Of which You Wanna Change The Something :")
print("""Enter 1 If You Want To Change it In Upper Case \nEnter 2 If You Want To Change it In Lower Case \nEnter 3 If You Want To Remve Any Special Characters \nEnter 4 if You Want To Replace The String With Something""")


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

else :
    print("The Value You Entered Is InVailid \n Kindly Read The Instructions Carefully <3")

# The Strings Are Inmutable SO The Str Which Is Formed Aftr is New AND the Old Str isd not changed