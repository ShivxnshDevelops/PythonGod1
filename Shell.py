# Match Cases File 
x = int(input("Enter The Shell No.Of The Atomic Structure :"))


match x:
    # If Case Is 1 Then
    case 1:
        print("The No Of Atoms Can Be Stored In The First Shell Are" , 2*x**2)
    # if Case Is 2 Then
    case 2:
        print("The No Of Atoms Can Be Stored In The Second Shell Are" ,  2*x**2)
    # if Case Is 3 Then
    case 3:
        print("The No Of Atoms Can Be Stored In The Third Shell Are" ,  2*x**2)
    # if Case Is 3 Then
    case 4:
        print("The No Of Atoms Can Be Stored In The Fourth Shell Are" ,  2*x**2)
    case _:
            while(x>4):
                 x = int(input("Please ReEnter The Shell No.Of The Atomic Structure :"))
                 while(x=="1" , "2" , "3" , "4"):
                      match x:
                     # If Case Is 1 Then
                         case 1:
                            print("The No Of Atoms Can Be Stored In The First Shell Are" , 2*x**2)
                            x = x - 1

                     # if Case Is 2 Then
                         case 2:
                             print("The No Of Atoms Can Be Stored In The Second Shell Are" ,  2*x**2)
                             x = x - 2

                     # if Case Is 3 Then
                         case 3:
                             print("The No Of Atoms Can Be Stored In The Third Shell Are" ,  2*x**2)
                             x = x - 3
                    # if Case Is 3 Then
                         case 4:
                             print("The No Of Atoms Can Be Stored In The Fourth Shell Are" ,  2*x**2)
                             x = x - 4

     
    
       

