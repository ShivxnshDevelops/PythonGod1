print("""To Do List By Shiv4nsh In Python 
    Enter 1 If You Want To Check The Current ToDo List
    Enter 2 If Want To Add Something In Todo List 
    Enter 3 If You WAnt To Remove Something From The ToDo List
    Enter 4 To Terminate The Program""")

t = {""}
t.clear()
# Display Function 
def display():
    """This Function Is Used To Display The No. Of Tasks In Your ToDo List"""
    if not t:
        print("Sorry !! Your ToDo List Is Empty")
    else :
        print("Your Current ToDo List Looks Like This")
        for i , task in enumerate(t , start=1):
            print(f"{i}. {task}")

# Add Function
def add(a):
    """This Function Is Used To Add The Task In The ToDo List"""
    
    t.update(a.strip()  for a in a.split(","))
    print(f'"{a}" has been added to your To-Do list.')

# Remove Function
def delete(a):
    """This Function Is Used To Remove The Task From The ToDo List"""
    c = t.remove(a)
    print(f'"{c}" has been removed from your To-Do list.')

# Main Loop 
while True:
    x = int(input("Enter The Cmds (1/2/3/4): "))
           
    if x==2 or x==3:
        if x==2:
           a = input("Enter The Task You Want To Add In The ToDo List :")
           add(a)
           display()
        else:
           a = input("Enter The Task You Want To Remove Form The ToDo List :")
           delete(a)
           display()
    elif x==1:
        display()
    elif x==4:
        print("The Program Is Terminated ")
        break
    else :
        raise ValueError("Invalid Input | Please read The Given Instructions CareFully ")