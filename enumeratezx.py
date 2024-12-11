x = {"7e" , "Hex" , "Br" , "Rx"}
for i , name in enumerate(x , start=1):
    print(f"{i} {name}")
a = list(x)
a.append("JK")
print(a)
a = tuple(a)
for i , name in enumerate(a , 1):
    print(f"{i} . {name}")