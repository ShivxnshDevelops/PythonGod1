def name():
    try:
        l=["Shiv4nsh" , "Y4SH" , "Anuj" , "Roh4n" ]
        x = int(input("enter The Index You WAnt To Print :"))
        print(f"Your Demanded String Is {l[x-1]}")
        return 1
    except:
        print("Something Happend TO The Program")
        return 0
    finally:
        print("Thanks For Using The Program \n Author - Shiv4nsh")

n = name()
print(n)