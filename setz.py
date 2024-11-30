z = {"Yash " , "SHiv4nsh" , "Divyansh"}
x = {"Anuj" , "Arjun"}
print(type(z) and type(x))
print(z.union(x))
z.update(x)
print(z)
n = z.intersection(x)
print(n)
q = {"K" , "Unnati" , "Pryanshi" , "Kairavi"}
e = {"K" , "nitya"}
a = {"K"}
t = q.symmetric_difference(e)
# q.intersection_update(e)
print(t)
print(q.difference(e))
print(q.isdisjoint(e))
print(q.issuperset(a))
print(a.issubset(q))

print(q) 
del t
print(t) # T is ALready Deleted so it throws error
q.discard("K")
q.remove("K2") #It Raises Error But Discard Doesnt
q.clear() # TO clear whole set but dont want to delete
print(q)