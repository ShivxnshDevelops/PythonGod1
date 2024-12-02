import random
import string

# Coding The Messeage Into Secret Code :

def encode(a):
    if (len(a)<3):
        print(a[1]+a[0])
    elif (len(a)>3):
        l = a[1:]+a[0]
        if (len(l)>7):
            print(l)
        else:
            k = 3
            rnd = "".join(random.choice(string.ascii_lowercase, ))
            rndx = "".join(random.choice(string.ascii_lowercase)) 
            Code = rnd+l+rndx
            print(f"The Secret Code Of Your Given Message {Code}")

def decode(a):
    if (len(a)<3):
        print(a[1]+a[0])
    elif (len(a)>3):
        l = a[0]+a[1:]
        print(l)

print("If Want To EnCode The Messeage Then Press $ \nIf YOu WAnt To Decode The Messegae Then Press # :")
z = input("Enter The Cmds After Reading The Instructions CareFully ( $ / # ) : ")
try:
    if z=="$":
        norm = input("The Messeage You Wannt To Encode :")
        encode(norm)
    elif z=="#":
        norm = input("The Messeage You Wannt To Decode :")
        decode(norm)

except:
    raise ValueError("The Cmds Should Not BE Other Than '$' Or '#'")
finally:
    print("Tysm !! For Using The Program ")