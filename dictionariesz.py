print("This FIle Is For The Disctionaries In The Python \nAuthor of The Program - Shiv4nsh ")

dic = {
    "Shiv4nsh":"Back-End" ,
    "Y4SH.exe":"Back-End"
}
dx = {
    "Name":"Team Dxrk" ,
    "Founding Year": 2026 ,
    "Investers" : "Arjun , Anuj , Divyansh" ,
    "GFX Master" : "Arjun" ,
    "VFX Master" : "Anuj" ,
    "Developers":"Shiv4nsh $ Y4SH.exe" ,
    "Marketing Head":"Divyansh"
    }
print(type(dic))
print(dic["Shiv4nsh"]) # it throws error if you enter wrong key
print(dic.get("Shiv4nsh2")) # it doesnt throw error if you enter wrong key
# dic.update(dx)
print(dx)
# dx.pop("Name")
dx.popitem() # It Removes The Last Keyy Of Any Dict Without ANy Argument
# del dx | It Deletes The Entire Dict
del dx["Name"] #It deletes Specific Key
print(dx)