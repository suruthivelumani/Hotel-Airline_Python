'''class flight:
    def __init__(self,):'''
        
'''a=open("E:\\python\\room.txt","r")
        print(a.read())'''



class flight:
    def __init__(self,):



def flight1():
    while True:
        print("  1) Book  Ticket(s)")
        print("  2) Modify Booking")
        print("  3) Cancel Booking")
        print("  4) View Booking")
        print("  5) Exit")
        n = int(input("Enter Your Choice : "))   
        if(n==1):
            fbook()
            break
        elif(n==2):
            fmodify()
            break
        elif(n==3):
            fcancel()
            break
        elif(n==4):
            fview()
            break
        elif(n==5):
            print("Thank You for Visiting")
            exit(0)
        else:
            print("Invalid Selection . Please Try Again !")









def hotel1():
    while True:
        print("  1) Book  Room(s)")
        print("  2) Modify Booking")
        print("  3) Cancel Booking")
        print("  4) View Booking")
        print("  5) Exit")
        m = int(input("Enter Your Choice : "))   
        if(m==1):
            hbook()
            break
        elif(m==2):
            hmodify()
            break
        elif(m==3):
            hcancel()
            break
        elif(m==4):
            hview()
            break
        elif(m==5):
            print("Thank You for Visiting")
            exit(0)
        else:
            print("Invalid Selection . Please Try Again !")





while True:
    print("--------------------------------------------------------------------------------")
    print("WELCOME TO GOA TOURISM")
    print("We aim to assist you in planning a comfortable and fun trip to Goa. ") 
    print("Enjoy your Visit! ")
    print("--------------------------------------------------------------------------------")
    print("     1)  Flight Booking")
    print("     2)  Hotel Booking")
    print("     3)  Exit")
    choice = int(input("Enter Your Choice : "))
    if choice == 1:
        flight1()
    elif choice ==2 :
        hotel1()
    elif choice==3:
        print("Thank You for Visiting")
        quit()
    else:
        print("Invalid Selection . Please Try Again !")