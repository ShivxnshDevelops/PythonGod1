l = ["Wakatime" , "Github" , "Other things"]
m = [10 , 7 , 5 , 9 , 8 , 4 , 5 ,6 ,7 ]

# a = input("Enter The Thing You Want To ADd In List")
# l.append(a)
print(l)
# m.sort(reverse=True)
print(m)
print(m.index(4))
m.sort()
# k = l + m
# print(k)
l.extend(m)
n = l.copy()
print( n )
print(len(l))
print(m.count(5))
x = m
x[0] 