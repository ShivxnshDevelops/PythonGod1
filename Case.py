Wel = "Welcome To The Program , The Author Of The Program Is ShivxnshDevelops"
print(Wel.center(50))

x = input("\nEnter The String Of which You Wanna Change The Something :")
print("""Enter 1 If You Want To Change it In Upper Case \nEnter 2 If You Want To Change it In Lower Case \nEnter 3 If You Want To Remve Any Special Characters \nEnter 4 if You Want To Replace The String With Something \nEnter 5 If You Want To Use The Captalize Case \nEnter 6 If You Want Find The first Occurence Of Any Str
    \nEnter 7 If You Want to know That Your Str Is AlphaNumeric Or Not \nEnter 8 If You Want To Know Thar Your Str is Printable Or Not \nEnter 9 If You Want To Know That Your Str Contain Spaces \nEnter 10 If You Want Know That Your Str Is Captialized \nEnter 11 If You want To Swap The Case Of Your  Str \nEnter 12 If You Want To CHange Your Str Into Justified case""")


K = input("\nEnter The Value According to The Instructions Given Above :")

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
elif K=="6" :
    q = input("Enter The Str Of Which You Want To Find The first Occurence :")
    print("The First Occurence Of The String You Given Is" , x.find(q))
    if x.find(q)=="-1" :
        print("The Str you Entered Is Not Present In The Original Str")
elif K=="7" :
    if x.isalnum()==True :
        print("Yes , Your Str Is AlphaNumeric")
    else :
        print("No , Your Is Not AlphaNumeric")
elif K=="8" :
    if x.isprintable()==True :
        print("Yes , All Characters Of Your String Are Prinatble")
    else :
        print("No , Not All The Characters Of Your Str Are Printable ")
elif K=="9" :
    if x.isspace()==True :
        print("Yes , Your Str Contain Spaces")
    else :
        print("No , Your Str Didn't Contain Any Spaces")
elif K=="10":
    if x.istitle()==True :
        print("Yes , Your Str Is Captialized")
    else :
        print("No , Your Str Is Not Captailized")
elif K=="11":
    print(x.swapcase())
elif K=="12":
    print(x.title())

else :
    print("The Value You Entered Is InVailid \n Kindly Read The Instructions Carefully <3")

# The Strings Are Inmutable SO The Str Which Is Formed Aftr is New AND the Old Str isd not changed

