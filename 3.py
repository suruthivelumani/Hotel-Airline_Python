import os
import datetime

class Flight:
    def __init__(self):
        self.fprice = 0
        self.ftype = 0
        self.fbill = 0
        self.nooftickets = 0
        self.fname = ""
        self.farvl = "Goa International Airport, Goa"
        self.fdept = ""
        self.date = ""
        self.fdur = ""
        self.fid = ""

    def fprice1(self):
        if self.ftype == 1:
            self.fdept = "Indira Gandhi International Airport, Delhi"
            self.fprice = 4215
            self.fdur = "2 hrs 40 mins"
        elif self.ftype == 2:
            self.fdept = "Chhatrapati Shivaji International Airport, Mumbai"
            self.fprice = 2549
            self.fdur = "1 hrs 20 mins"
        elif self.ftype == 3:
            self.fdept = "Kempegowda International Airport, Bangalore"
            self.fprice = 2690
            self.fdur = "1 hrs 20 mins"
        elif self.ftype == 4:
            self.fdept = "Chennai International Airport, Chennai"
            self.fprice = 3311
            self.fdur = "2 hrs 5 mins"
        elif self.ftype == 5:
            self.fdept = "Netaji Subhas Chandra Bose International Airport, Kolkata"
            self.fprice = 8994
            self.fdur = "3 hrs 15 mins"
        elif self.ftype == 6:
            self.fdept = "Rajiv Gandhi International Airport, Hyderabad"
            self.fprice = 2880
            self.fdur = "1 hrs 30 mins"
        elif self.ftype == 7:
            self.fdept = "Cochin International Airport, Kochi"
            self.fprice = 5942
            self.fdur = "2 hrs 55 mins"
        elif self.ftype == 8:
            self.fdept = "Sardar Vallabhbhai Patel International Airport, Ahmedabad"
            self.fprice = 3410
            self.fdur = "1 hrs 55 mins"
        elif self.ftype == 9:
            self.fdept = "Lokpriya Gopinath Bordoloi International Airport, Guwahati"
            self.fprice = 10268
            self.fdur = "5 hrs 20 mins"
        self.fbill = self.fprice * self.nooftickets

    def fgetinfo(self):
        self.fid = int(input("Enter ID : "))
        self.fname = input("Enter your Name : ")
        f = 1
        while f == 1:
            self.date = input("Enter Date of travel : ")
            date_format = '%Y-%m-%d'
            flag = 1
            while (flag == 1):
                try:
                    dateObject = datetime.datetime.strptime(self.date, date_format)
                    flag = 0
                    d = datetime.datetime.now().date()
                    if self.date == str(d):
                        flag = 0
                    else:
                        self.date = input("Enter today's date..")
                        flag = 1
                except ValueError:
                    print("Incorrect data format, should be YYYY-MM-DD")
                    self.date = input("Enter indate : ")

        print("Choose your departure airport:")
        print("  1)   Indira Gandhi International Airport, Delhi")
        print("  2)   Chhatrapati Shivaji International Airport, Mumbai")
        print("  3)   Kempegowda International Airport, Bangalore")
        print("  4)   Chennai International Airport, Chennai")
        print("  5)   Netaji Subhas Chandra Bose International Airport, Kolkata")
        print("  6)   Rajiv Gandhi International Airport, Hyderabad")
        print("  7)   Cochin International Airport, Kochi")
        print("  8)   Sardar Vallabhbhai Patel International Airport, Ahmedabad")
        print("  9)   Lokpriya Gopinath Bordoloi International Airport, Guwahati")
        print("Press any number between 1 and 9:")
        self.ftype = int(input())
        print("Enter no. of tickets:")
        self.nooftickets = int(input())
        self.fprice1()

    def fshowinfo(self):
        print("ID                             :  " + self.fid)
        print("Name                      :  " + self.fname)
        print("No of tickets          :  " + str(self.nooftickets))
        print("Date of travel        :  " + self.date)
        print("Departure              :  " + self.fdept)
        print("Arrival                     :  " + self.farvl)
        print("Duration                 :  " + self.fdur)
        print("Bill                           :  " + str(self.fbill))

    def retfid(self):
        return self.fid

    def fmod(self):
        self.fname = input("Enter your Name : ")
        f = 1
        while f == 1:
            self.date = input("Enter Date of travel : ")
            date_format = '%Y-%m-%d'
            flag = 1
            while (flag == 1):
                try:
                    dateObject = datetime.datetime.strptime(self.date, date_format)
                    flag = 0
                    d = datetime.datetime.now().date()
                    if self.date == str(d):
                        flag = 0
                    else:
                        self.date = input("Enter today's date..")
                        flag = 1
                except ValueError:
                    print("Incorrect data format, should be YYYY-MM-DD")
                    self.date = input("Enter indate : ")

        print("Choose your departure airport:")
        print("  1)   Indira Gandhi International Airport, Delhi")
        print("  2)   Chhatrapati Shivaji International Airport, Mumbai")
        print("  3)   Kempegowda International Airport, Bangalore")
        print("  4)   Chennai International Airport, Chennai")
        print("  5)   Netaji Subhas Chandra Bose International Airport, Kolkata")
        print("  6)   Rajiv Gandhi International Airport, Hyderabad")
        print("  7)   Cochin International Airport, Kochi")
        print("  8)   Sardar Vallabhbhai Patel International Airport, Ahmedabad")
        print("  9)   Lokpriya Gopinath Bordoloi International Airport, Guwahati")
        print("Press any number between 1 and 9:")
        self.ftype = int(input())
        print("Enter no. of tickets:")
        self.nooftickets = int(input())
        self.fprice1()


def fbook():
    flight = Flight()
    flight.fgetinfo()
    print("Booking over")
    print("Thank you for using our service!")

def fmodify():
    gid = input("Enter ID to modify booking: ")
    flight = Flight()
    if flight.retfid() == gid:
        flight.fmod()
    print("Booking modified")
    print("Thank you for using our service!")

def fcancel():
    gid = input("Enter ID to cancel booking: ")
    fin = open("flight.dat", "rb")
    fout = open("tempf.dat", "ab")
    while True:
        try:
            flight = Flight()
            flight.__dict__ = fin.read(512)
            if flight.retfid() != gid:
                fout.write(flight.__dict__)
        except EOFError:
            break
    fin.close()
    fout.close()
    os.remove("flight.dat")
    os.rename("tempf.dat", "flight.dat")
    print("Booking cancelled")
    print("Thank you for using our service!")

def fview():
    gid = input("Enter ID to view booking: ")
    fin = open("flight.dat", "rb")
    while True:
        try:
            flight = Flight()
            flight.__dict__ = fin.read(512)
            if flight.retfid() == gid:
                flight.fshowinfo()
        except EOFError:
            break
    fin.close()
    print("Booking viewed")
    print("Thank you for using our service!")
class Hotel:
    def __init__(self):
        self.name = "NULL"
        self.rmtype = ""
        self.id = ""
        self.rtype = 0
        self.noofrms = 0
        self.noofdays = 0
        self.rprice = 0
        self.rbill = 0
        self.checkindate = ""
        self.checkoutdate = ""

    def price(self):
        if self.rtype == 1:
            self.rmtype = "Standard"
            self.rprice = 3658
        elif self.rtype == 2:
            self.rmtype = "Executive"
            self.rprice = 7544
        elif self.rtype == 3:
            self.rmtype = "Club"
            self.rprice = 12432
        self.rbill = self.rprice * self.noofrms * self.noofdays

    def hgetinfo(self):
        print("Enter ID:")
        self.id = input()
        print("Enter your name:")
        self.name = input()
        print("Enter check-in date (dd/mm/yy):")
        self.checkindate = input()
        print("Enter check-out date (dd/mm/yy):")
        self.checkoutdate = input()
        print("Enter number of days of stay:")
        self.noofdays = int(input())
        print("Enter number of rooms:")
        self.noofrms = int(input())
        print("Choose the room type:")
        print("     1) Standard")
        print("     2) Executive")
        print("     3) Club")
        print("Press 1, 2, or 3")
        self.rtype = int(input())
        self.price()

    def hshowinfo(self):
        print("ID                         :", self.id)
        print("Name                       :", self.name)
        print("Check-in date              :", self.checkindate)
        print("Check-out date             :", self.checkoutdate)
        print("Number of days             :", self.noofdays)
        print("Number of rooms            :", self.noofrms)
        print("Room type                  :", self.rmtype)
        print("Total bill                 :", self.rbill)

    def retid(self):
        return self.id

    def hmod(self):
        print("Enter your name:")
        self.name = input()
        print("Enter check-in date (dd/mm/yy):")
        self.checkindate = input()
        print("Enter check-out date (dd/mm/yy):")
        self.checkoutdate = input()
        print("Enter number of days of stay:")
        self.noofdays = int(input())
        print("Enter number of rooms:")
        self.noofrms = int(input())
        print("Choose the room type:")
        print("     1) Standard")
        print("     2) Executive")
        print("     3) Club")
        print("Press 1, 2, or 3")
        self.rtype = int(input())
        self.price()


def hbook():
    h = Hotel()
    fout = open("hotel.dat", "ab")
    h.hgetinfo()
    fout.write(h.__dict__)
    fout.close()
    print("Booking over")
    print("Thank you for using our service!")

def hmodify():
    h = Hotel()
    sid = input("Enter ID to modify booking: ")
    f = open("hotel.dat", "r+b")
    while True:
        data = f.read(h.__sizeof__())
        if not data:
            break
        h.__dict__ = data
        if h.retid() == sid:
            h.hmod()
            f.seek(-h.__sizeof__(), 1)
            f.write(h.__dict__)
    f.close()
    print("Booking modified")
    print("Thank you for using our service!")

def hview():
    h = Hotel()
    sid = input("Enter ID to view booking: ")
    fin = open("hotel.dat", "rb")
    while True:
        data = fin.read(h.__sizeof__())
        if not data:
            break
        h.__dict__ = data
        if h.retid() == sid:
            h.hshowinfo()
    fin.close()
    print("Booking viewed")
    print("Thank you for using our service!")

def hcancel():
    h = Hotel()
    sid = input("Enter ID to cancel booking: ")
    fin = open("hotel.dat", "rb")
    fout = open("temph.dat", "wb")
    while True:
        data = fin.read(h.__sizeof__())
        if not data:
            break
        h.__dict__ = data
        if h.retid() != sid:
            fout.write(h.__dict__)
    fin.close()
    fout.close()
    os.remove("hotel.dat")
    os.rename("temph.dat", "hotel.dat")
    print("Booking cancelled")
    print("Thank you for using our service!")








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




