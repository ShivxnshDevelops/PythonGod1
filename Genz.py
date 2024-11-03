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
        print("Invailid Shell No. | ErrOr 404 | Command Not Found")

    
       

