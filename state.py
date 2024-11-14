print("Enter S For Simple Program \nEnter Pro For Advanced Program ")
z = input("Enter The Command According To The Instructions Given Above : ")
if z =="S" :
    i = int(input("Enter The Value From Which The Counting You Wanna Start : "))
    K = int(input("Enter The Value From Which The Counting You Wanna End : "))
    while True :
        print(i)
        i = i + 1
        if (K <= i):
            break 

 
elif z =="Pro":
    i = int(input("Enter The Value From Which The Counting You Wanna Start : "))
    S = int(input("Enter The Value From Which The You Wanna Step Up / Leave  : "))
    K = int(input("Enter The Value From Which The Counting You Wanna End : "))
    while True :
        print(i)
        i = i + 1
        if (K == S):
            continue 













# for i in range(100):
#     print(i)
#     i = i + 1
#     if (i == "100") :
#         break
# print("The Program Ends Here ")

