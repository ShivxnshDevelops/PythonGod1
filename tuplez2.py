# How to Mainupulate A Tuple 

x = ("Shiv4nsh Dalal" , "Yash dalla " , "Dixit Ji" , "palva" , "baba ji" , "Marwadhi" , "Kinder Joy" )

t = list(x)
t.append("Mai Hun Pappu Pelu") , 
print(t , len(t))
t.append("app kahe to appki lelu")
t.append("kya")
print(t)
x = tuple(t)
print(x)

tup = (4 , 5 ,6 ,5, 3 , 2 , 1 ,5 ,4)
n = list(tup)
n.pop(3) , print(n)
print(n.count(5))
print(n.index(5, 1 , 6))