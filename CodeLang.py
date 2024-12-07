import random
import string

# Coding The Messeage Into Secret Code :

def encode(a):
    '''Function To Encode The Messeage Into Secret Code'''

    if (len(a)<3):
        # If The Code Is Less Than Three Character Then It Just Reverse The Msg
        print(a[1]+a[0])
        
    elif (len(a)>3):
        Encoded_msg = a[1:]+a[0]  
        Code_Prefix = "".join(random.choice(string.ascii_lowercase)for _ in range(3))
        Code_suffix = "".join(random.choice(string.ascii_lowercase)for _ in range(3))
        Encrypted_Msg = Code_Prefix+Encoded_msg+Code_suffix
        print(f"The Encrypted Messeage :{Encrypted_Msg}")

# Decoding The Messeage Into Real World Language

def decode(a):
    '''Function To Decode The Encrypted Messeage'''
    if (len(a)<3):
        # If The Code Is Less Than Three Character Then It Just Reverse The Msg
        print(a[1]+a[0])

    elif (len(a)>3):
       
        
            core = a[2:-3]
            print(core)
            og_msg = core[len(core) -1] + core[1:len(core) - 1] 
           
            print(f"The Decoded Messeage Of Your Secret {og_msg}")
        

print("If Want To EnCode The Messeage Then Press $ \nIf YOu WAnt To Decode The Messegae Then Press # \nIf You Want o Terminate Then Program Enter '&'")
z = input("Enter The Cmds After Reading The Instructions CareFully ( $ / # / & ) : ")

try:
    if z=="$":
        a = input("The Messeage You Wannt To Encode :")
        encode(a)
            
    elif z=="#":
        a = input("The Messeage You Wannt To Decode :")
        decode(a)
    elif z=="&":
        print("The Program Has Been Succesfully Terminated")
            
except Exception as e:
    print(f"Error : {e}")
finally:
    print("Tysm !! For Using The Program ")