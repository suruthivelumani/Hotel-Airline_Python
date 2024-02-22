from tabulate import tabulate
import datetime

import mysql.connector

con = mysql.connector.connect(host="localhost", port="3307", user="root", password="", database="trialdb")
'''if(con):
    print("Connected")
else:
    print("Error")'''

while True:
    print("--------------------------------------------------------------------------------")
    print("WELCOME TO GOA TOURISM")
    print("We aim to assist you in planning a comfortable and fun trip to Goa. ") 
    print("Enjoy your Visit! ")
    print("--------------------------------------------------------------------------------")
    print("     1)  Flight Booking")
    print("     2)  Hotel Booking")
    print("     3)  Update Flight Booking")
    print("     4)  Update Hotel Booking")
    print("     5)  View Flight Booking")
    print("     6)  View Hotel Booking")
    print("     7)  Delete Flight Booking")
    print("     8)  Delete Hotel Booking")
    print("     9)  Exit")
    choice = int(input("Enter Your Choice : "))
    if (choice == 1):
        flight1();break;}
 case 2:
{ hotel1();break;}
  case 3: exit(0);
}
}while((n==1)||(n==2));
getch();
}