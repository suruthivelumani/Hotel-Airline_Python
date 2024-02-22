
from tabulate import tabulate
import datetime

import mysql.connector

con = mysql.connector.connect(host="localhost", port="3307", user="root", password="", database="goadb")
'''if(con):
    print("Connected")
else:
    print("Error")'''

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
        self.n = 0

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
        #self.fid = int(input("Enter ID : "))
        self.fname = input("Enter your Name : ")
        f = 1
        while f == 1:
            self.date = input("Enter Date of travel : ")
            date_format = '%Y-%m-%d'
            flag = 1
            while (flag == 1):
                try:
                    dateObject = datetime.datetime.strptime(self.date, date_format)
                
                    d = datetime.datetime.now().date()
                    if self.date >= str(d):
                        flag = 0
                    else:
                        self.date = input("Invalid Date!!!\nRe-enter valid date.. : ")
                        flag = 1
                    f=0
                except ValueError:
                    print("Incorrect data format, should be YYYY-MM-DD")
                    self.date = input("Enter Date of travel : ")
        #f1=1
        #while f1==1:
        print("Choose your departure airport : ")
        print("  1)   Indira Gandhi International Airport, Delhi")
        print("  2)   Chhatrapati Shivaji International Airport, Mumbai")
        print("  3)   Kempegowda International Airport, Bangalore")
        print("  4)   Chennai International Airport, Chennai")
        print("  5)   Netaji Subhas Chandra Bose International Airport, Kolkata")
        print("  6)   Rajiv Gandhi International Airport, Hyderabad")
        print("  7)   Cochin International Airport, Kochi")
        print("  8)   Sardar Vallabhbhai Patel International Airport, Ahmedabad")
        print("  9)   Lokpriya Gopinath Bordoloi International Airport, Guwahati")
        n=int(input("Enter your Departure Airport (1 - 9) : "))
        if(n==1 or n==2 or n==3 or n==4 or n==5 or n==6 or n==7 or n==8 or n==9):
            self.ftype=n
                #f1=0
           # break
        else:
            self.ftype=int(input("Invalid Selection. Please Try Again ! Select any number between 1 to 9 : "))
            #break
            
        #print("Press any number between 1 and 9:")
        #self.ftype = int(input())
        #self.ftype = int(input("Press any number between 1 and 9 : "))
        self.nooftickets = int(input("Enter no. of tickets : "))
        self.fprice1()

#inserting into the database

        res = con.cursor()
        sql = "insert into booking (name,date, airport_d,duration ,airport_a,count,amount) values (%s,%s,%s,%s,%s,%s,%s)"
        user = (self.fname, self.date, self.fdept, self.fdur, self.farvl, self.nooftickets,self.fbill)
        try:
            res.execute(sql, user)
            con.commit()
            print("Data Insert Success")
        except:
            con.rollback()




    def fshowinfo(self):
       ''' print("ID                             :  " + self.fid)
        print("Name                      :  " + self.fname)
        print("No of tickets          :  " + str(self.nooftickets))
        print("Date of travel        :  " + self.date)
        print("Departure              :  " + self.fdept)
        print("Arrival                     :  " + self.farvl)
        print("Duration                 :  " + self.fdur)
        print("Bill                           :  " + str(self.fbill))'''
       res = con.cursor()
       sql = "SELECT id,name,date, airport_d,duration ,airport_a,count,amount from booking"
       res.execute(sql)
        # result=res.fetchone()
        # result=res.fetchmany(2)
       result = res.fetchall()
       print(tabulate(result, headers=["ID", "NAME", "DATE OF TRAVEL","DEPARTURE","DURATION", "ARRIVAL", "NO. OF TICKETS", "AMOUNT"]))



    def retfid(self):
        return self.fid

    def fmod(self):
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
                
                    d = datetime.datetime.now().date()
                    if self.date >= str(d):
                        flag = 0
                    else:
                        self.date = input("Invalid Date!!!\nRe-enter valid date.. : ")
                        flag = 1
                    f=0
                except ValueError:
                    print("Incorrect data format, should be YYYY-MM-DD")
                    self.date = input("Enter Date of travel : ")
        #f1=1
        #while f1==1:
        print("Choose your departure airport : ")
        print("  1)   Indira Gandhi International Airport, Delhi")
        print("  2)   Chhatrapati Shivaji International Airport, Mumbai")
        print("  3)   Kempegowda International Airport, Bangalore")
        print("  4)   Chennai International Airport, Chennai")
        print("  5)   Netaji Subhas Chandra Bose International Airport, Kolkata")
        print("  6)   Rajiv Gandhi International Airport, Hyderabad")
        print("  7)   Cochin International Airport, Kochi")
        print("  8)   Sardar Vallabhbhai Patel International Airport, Ahmedabad")
        print("  9)   Lokpriya Gopinath Bordoloi International Airport, Guwahati")
        n=int(input("Enter your Departure Airport (1 - 9) : "))
        if(n==1 or n==2 or n==3 or n==4 or n==5 or n==6 or n==7 or n==8 or n==9):
            self.ftype=n
                #f1=0
           # break
        else:
            self.ftype=int(input("Invalid Selection. Please Try Again ! Select any number between 1 to 9 : "))
            #break
            
        #print("Press any number between 1 and 9:")
        #self.ftype = int(input())
        #self.ftype = int(input("Press any number between 1 and 9 : "))
        self.nooftickets = int(input("Enter no. of tickets : "))
        self.fprice1()

#updating into the database
        res = con.cursor()
        sql = "update booking set name=%s, date=%s, airport_d=%s, duration=%s, airport_a=%s, count=%s, amount=%s where id=%s"
        user = (self.fname, self.date, self.fdept, self.fdur, self.farvl, self.nooftickets,self.fbill,self.fid)
        try:
            res.execute(sql, user)
            con.commit()
            print("Data Update Success")
        except:
            con.rollback()

def fbook():
    flight = Flight()
    flight.fgetinfo()
    print("Booking over")
    print("Thank you for using our service!")

def fmodify():
    flight = Flight()
    flight.fmod()
    print("Booking modified")
    print("Thank you for using our service!")

def fcancel():
    gid = input("Enter ID to cancel booking: ")
    res = con.cursor()
    sql = "delete from booking where id=%s"
    user = (gid,)
    try:
        res.execute(sql, user)
        con.commit()
        print("Data Delete Success")
    except:
        con.rollback()
    print("Booking cancelled")
    print("Thank you for using our service!")

def fview():    
    res = con.cursor()
    sql = "SELECT id,name,date, airport_d,duration ,airport_a,count,amount from booking"
    res.execute(sql)
    # result=res.fetchone()
    # result=res.fetchmany(2)
    result = res.fetchall()
    print(tabulate(result, headers=["ID", "NAME", "DATE OF TRAVEL","DEPARTURE","DURATION", "ARRIVAL", "NO. OF TICKETS", "AMOUNT"]))
    print("Booking viewed")
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
        self.name = input("Enter your name : ")
        f = 1
        while f == 1:
            self.checkindate = input("Enter check-in date : ")
            date_format = '%Y-%m-%d'
            flag = 1
            while (flag == 1):
                try:
                    dateObject = datetime.datetime.strptime(self.checkindate, date_format)
                
                    d = datetime.datetime.now().date()
                    if self.checkindate >= str(d):
                        flag = 0
                    else:
                        self.checkindate = input("Invalid Date!!!\nRe-enter valid date.. : ")
                        flag = 1
                    f=0
                except ValueError:
                    print("Incorrect data format, should be YYYY-MM-DD")
                    self.checkindate = input("Enter Date of check-in : ")       

            self.checkoutdate = input("Enter check-out date : ")
            date_format = '%Y-%m-%d'
            flag = 1
            while (flag == 1):
                try:
                    dateObject = datetime.datetime.strptime(self.checkoutdate, date_format)
                    flag=0
                except ValueError:
                    print("Incorrect data format, should be YYYY-MM-DD")
                    self.checkoutdate = input("Enter outdate : ")

            if self.checkindate > self.checkoutdate:
                f=1
                print("Enter correct indate and outdate")
            else:
                f=0
        
        self.noofdays = int(input("Enter number of days of stay:"))
        self.noofrms = int(input("Enter number of rooms:"))
        print("Choose the room type:")
        print("     1) Standard")
        print("     2) Executive")
        print("     3) Club")
        n=int(input("Press 1, 2, or 3 : "))
        if(n==1 or n==2 or n==3):
            self.rtype=n
           # break
        else:
            self.rtype=int(input("Invalid Selection. Please Try Again ! Select any number between 1 to 3 : "))
            #break
        self.price()   

        #inserting into the database

        res = con.cursor()
        sql = "insert into booking_h (name,checkindate, checkoutdate,noofdays ,noofrooms,rmtype,rbill) values (%s,%s,%s,%s,%s,%s,%s)"
        user = (self.name, self.checkindate, self.checkoutdate, self.noofdays, self.noofrms, self.rtype,self.rbill)
        try:
            res.execute(sql, user)
            con.commit()
            print("Data Insert Success")
        except:
            con.rollback()


    def hshowinfo(self):
        '''print("ID                         :", self.id)
        print("Name                       :", self.name)
        print("Check-in date              :", self.checkindate)
        print("Check-out date             :", self.checkoutdate)
        print("Number of days             :", self.noofdays)
        print("Number of rooms            :", self.noofrms)
        print("Room type                  :", self.rmtype)
        print("Total bill                 :", self.rbill)'''

        res = con.cursor()
        sql = "SELECT id,name,checkindate, checkoutdate,noofdays ,noofrooms,rmtype,rbill from booking_h"
        res.execute(sql)
        # result=res.fetchone()
        # result=res.fetchmany(2)
        result = res.fetchall()
        print(tabulate(result, headers=["ID", "NAME", "CHECKIN DATE","CHECKOUT DATE","DURATION", "NO. OF ROOMS", "ROOM TYPE", "AMOUNT"]))
    

    def retid(self):
        return self.id

    def hmod(self):
        self.id= int(input("Enter ID to modify hotel booking : "))
        self.name = input("Enter your name : ")
        f = 1
        while f == 1:
            self.checkindate = input("Enter check-in date : ")
            date_format = '%Y-%m-%d'
            flag = 1
            while (flag == 1):
                try:
                    dateObject = datetime.datetime.strptime(self.checkindate, date_format)
                
                    d = datetime.datetime.now().date()
                    if self.checkindate >= str(d):
                        flag = 0
                    else:
                        self.checkindate = input("Invalid Date!!!\nRe-enter valid date.. : ")
                        flag = 1
                    f=0
                except ValueError:
                    print("Incorrect data format, should be YYYY-MM-DD")
                    self.checkindate = input("Enter Date of check-in : ")        

            self.checkoutdate = input("Enter check-out date : ")
            date_format = '%Y-%m-%d'
            flag = 1
            while (flag == 1):
                try:
                    dateObject = datetime.datetime.strptime(self.checkoutdate, date_format)
                    flag=0
                except ValueError:
                    print("Incorrect data format, should be YYYY-MM-DD")
                    self.checkoutdate = input("Enter outdate : ")

            if self.checkindate > self.checkoutdate:
                f=1
                print("Enter correct indate and outdate")
            else:
                f=0
        
        self.noofdays = int(input("Enter number of days of stay:"))
        self.noofrms = int(input("Enter number of rooms:"))
        print("Choose the room type:")
        print("     1) Standard")
        print("     2) Executive")
        print("     3) Club")
        n=int(input("Press 1, 2, or 3 : "))
        if(n==1 or n==2 or n==3):
            self.rtype=n
           # break
        else:
            self.rtype=int(input("Invalid Selection. Please Try Again ! Select any number between 1 to 3 : "))
            #break
        self.price()

        #updating into the database
        res = con.cursor()
        sql = "update booking_h set name=%s, checkindate=%s, checkoutdate=%s, noofdays=%s, noofrooms=%s, rmtype=%s, rbill=%s where id=%s"
        user = (self.name, self.checkindate, self.checkoutdate, self.noofdays, self.noofrms, self.rmtype,self.rbill,self.id)
        try:
            res.execute(sql, user)
            con.commit()
            print("Data Update Success")
        except:
            con.rollback()


def hbook():
    h = Hotel()
    h.hgetinfo()
    print("Booking over")
    print("Thank you for using our service!")

def hmodify():
    h = Hotel()
    h.hmod()
    print("Booking modified")
    print("Thank you for using our service!")


def hview():
    h = Hotel()
    h.hshowinfo()
    print("Booking viewed")
    print("Thank you for using our service!")

def hcancel():
    h = Hotel()
    sid = input("Enter ID to cancel booking: ")

    res = con.cursor()
    sql = "delete from booking_h where id=%s"
    user = (sid,)
    try:
        res.execute(sql, user)
        con.commit()
        print("Data Delete Success")
    except:
        con.rollback()
    print("Booking cancelled")
    print("Thank you for using our service!")

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