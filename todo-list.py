print("""To Do List By Shiv4nsh In Python 
    Enter 1 If You Want To Check The Current ToDo List
    Enter 2 If Want To Add Something In Todo List 
    Enter 3 If You WAnt To Remove Something From The ToDo List""")

t = []
def display():
    """This Function Is Used To Display The No. Of Tasks In Your ToDo List"""
    if not t:
        print("Sorry !! Your ToDo List Is Empty")
    else :
        print("Your Current ToDo List Looks Like This")
        for i , task in enumerate(t , start=1):
            print(f"{i}. {task}")
def add(a):
    """This Function Is Used To Add The Task In The ToDo List"""
    t_list = [a.strip() for item in a.split(",")]
    t.extend(t_list)
    print(f'"{a}" has been added to your To-Do list.')
def delete(a):
    """This Function Is Used To Remove The Task From The ToDo List"""
    c = t.pop(t.index - 1)
    print(f'"{c}" has been removed from your To-Do list.')
while True:
    x = int(input("Enter The Cmds According To The Instructions Given Above :"))
           
    if x==2 or x==3:
        a = input("Enter The Task You Want To Add Or Remove Form The ToDo List :")
        if x==2:
           add(a)
           display()
        else:
           delete(a)
           display()
    elif x==1:
        display()
    else :
        raise ValueError("Invalid Input | Please read The Given Instructions CareFully ")