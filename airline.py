from tabulate import tabulate
import datetime

import mysql.connector

con = mysql.connector.connect(host="localhost", port="3307", user="root", password="", database="hoteldb")
'''if(con):
    print("Connected")
else:
    print("Error")'''


class basicuser:

    def __init__(self, rt='', s=0, p=0, r=0, t=0, a=1800, name='', address='', cindate='', coutdate='', roomnumber=''):

        print("\n\n*****WELCOME TO WORLD OF AIR TRAVEL*****\n")

        self.rt = rt

        self.r = r

        self.t = t

        self.p = p

        self.s = s
        self.a = a
        self.name = name
        self.address = address
        self.cindate = cindate
        self.coutdate = coutdate
        self.roomnumber = roomnumber

    def inputdata(self,name, address, age, indate, outdate, roomnumber):
        self.name = name
        self.address = address
        self.age=age
        self.cindate = indate
        self.coutdate = outdate
        self.roomnumber=roomnumber

class hotel (basicuser):
    def roomrent(self):  # sel1353

        print("We have the following rooms for you:-")

        print("1.  type A---->rs 6000 PN\-")

        print("2.  type B---->rs 5000 PN\-")

        print("3.  type C---->rs 4000 PN\-")

        print("4.  type D---->rs 3000 PN\-")

        x = int(input("Enter Your Choice Please->"))

        n = int(input("For How Many Nights Did You Stay:"))

        if (x == 1):

            print("you have opted room type A")

            self.s = 6000 * n

        elif (x == 2):

            print("you have opted room type B")

            self.s = 5000 * n

        elif (x == 3):

            print("you have opted room type C")

            self.s = 4000 * n

        elif (x == 4):
            print("you have opted room type D")

            self.s = 3000 * n

        else:

            print("please choose a room")

        print("your room rent is =", self.s, "\n")

    def restaurentbill(self):

        print("*****RESTAURANT MENU*****")

        print("1.water----->Rs20", "2.tea----->Rs10", "3.breakfast combo--->Rs90", "4.lunch---->Rs110",
              "5.dinner--->Rs150", "6.Exit")

        while (1):

            c = int(input("Enter your choice:"))

            if (c == 1):
                d = int(input("Enter the quantity:"))
                self.r = self.r + 20 * d

            elif (c == 2):
                d = int(input("Enter the quantity:"))
                self.r = self.r + 10 * d

            elif (c == 3):
                d = int(input("Enter the quantity:"))
                self.r = self.r + 90 * d

            elif (c == 4):
                d = int(input("Enter the quantity:"))
                self.r = self.r + 110 * d

            elif (c == 5):
                d = int(input("Enter the quantity:"))
                self.r = self.r + 150 * d

            elif (c == 6):
                break;
            else:
                print("Invalid option")

        print("Total food Cost=Rs", self.r, "\n")

    def laundrybill(self):
        print("******LAUNDRY MENU*******")

        print("1.Shorts----->Rs3", "2.Trousers----->Rs4", "3.Shirt--->Rs5", "4.Jeans---->Rs6", "5.Girlsuit--->Rs8",
              "6.Exit")

        while (1):

            e = int(input("Enter your choice:"))

            if (e == 1):
                f = int(input("Enter the quantity:"))
                self.t = self.t + 3 * f

            elif (e == 2):
                f = int(input("Enter the quantity:"))
                self.t = self.t + 4 * f

            elif (e == 3):
                f = int(input("Enter the quantity:"))
                self.t = self.t + 5 * f

            elif (e == 4):
                f = int(input("Enter the quantity:"))
                self.t = self.t + 6 * f

            elif (e == 5):
                f = int(input("Enter the quantity:"))
                self.t = self.t + 8 * f
            elif (e == 6):
                break;
            else:

                print("Invalid option")

        print("Total Laundary Cost=Rs", self.t, "\n")

    def gamebill(self):
        print("******GAME MENU*******")

        print("1.Table tennis----->Rs60", "2.Bowling----->Rs80", "3.Snooker--->Rs70", "4.Video games---->Rs90",
              "5.Pool--->Rs50==6", "6.Exit")

        while (1):

            g = int(input("Enter your choice:"))

            if (g == 1):
                h = int(input("No. of hours:"))
                self.p = self.p + 60 * h

            elif (g == 2):
                h = int(input("No. of hours:"))
                self.p = self.p + 80 * h

            elif (g == 3):
                h = int(input("No. of hours:"))
                self.p = self.p + 70 * h

            elif (g == 4):
                h = int(input("No. of hours:"))
                self.p = self.p + 90 * h

            elif (g == 5):
                h = int(input("No. of hours:"))
                self.p = self.p + 50 * h
            elif (g == 6):
                break;

            else:

                print("Invalid option")

        print("Total Game Bill=Rs", self.p, "\n")

    def display(self):
        print("******HOTEL BILL******")
        print("Customer details:")
        print("Customer name:", self.name)
        print("Customer address:", self.address)
        print("Check in date:", self.cindate)
        print("Check out date", self.coutdate)
        print("Room no.", self.roomnumber)
        print("Your Room rent is:", self.s)
        print("Your Food bill is:", self.r)
        print("Your laundary bill is:", self.t)
        print("Your Game bill is:", self.p)

        self.rt = self.s + self.t + self.p + self.r

        print("Your sub total bill is:", self.rt)


def menu():
    print("1.Basic user")
    print("2.Luxurious")
    i=int(input())
    if i==1:
        a=basicuser()
        while (1):
            print("1.Enter Customer Data")
            print("2.EXIT")
            b = int(input("\nEnter your choice:"))
            if (b == 1):
                name = input("Enter Name : ")
                address = input("Enter address: ")
                age = int(input("Enter Age : "))
                f = 1
                while f == 1:
                    indate = input("Enter indate : ")
                    date_format = '%Y-%m-%d'
                    flag = 1
                    while (flag == 1):
                        try:
                            dateObject = datetime.datetime.strptime(indate, date_format)
                            flag = 0
                            d = datetime.datetime.now().date()
                            if indate == str(d):
                                flag = 0
                            else:

                                indate = input("Enter today's date..")
                                flag = 1
                        except ValueError:
                            print("Incorrect data format, should be YYYY-MM-DD")
                            indate = input("Enter indate : ")

                    outdate = input("Enter outdate : ")
                    date_format = '%Y-%m-%d'
                    flag = 1
                    while (flag == 1):
                        try:
                            dateObject = datetime.datetime.strptime(outdate, date_format)
                            flag = 0
                        except ValueError:
                            print("Incorrect data format, should be YYYY-MM-DD")
                            outdate = input("Enter outdate : ")

                    if indate > outdate:
                        f = 1
                        print("Enter correct indate and outdate")
                    else:
                        f = 0
                roomnumber = int(input("Enter roomnumber : "))
                insert(name, address, age, indate, outdate, roomnumber)
                a.inputdata(name, address, age, indate, outdate, roomnumber)

            if (b == 2):
                quit()
            else:
                print("Invalid")
    else:
        a = hotel()

        while (1):
            print("1.Enter Customer Data")

            print("2.Calculate rommrent")

            print("3.Calculate restaurant bill")

            print("4.Calculate laundry bill")

            print("5.Calculate gamebill")

            print("6.Show total cost")

            print("7.EXIT")

            b = int(input("\nEnter your choice:"))
            if (b == 1):
                name = input("Enter Name : ")
                address = input("Enter address: ")
                age = int(input("Enter Age : "))
                f = 1
                while f == 1:
                    indate = input("Enter indate : ")
                    date_format = '%Y-%m-%d'
                    flag = 1
                    while (flag == 1):
                        try:
                            dateObject = datetime.datetime.strptime(indate, date_format)
                            flag = 0
                            d = datetime.datetime.now().date()
                            if indate == str(d):
                                flag = 0
                            else:

                                indate = input("Enter today's date..")
                                flag = 1
                        except ValueError:
                            print("Incorrect data format, should be YYYY-MM-DD")
                            indate = input("Enter indate : ")

                    outdate = input("Enter outdate : ")
                    date_format = '%Y-%m-%d'
                    flag = 1
                    while (flag == 1):
                        try:
                            dateObject = datetime.datetime.strptime(outdate, date_format)
                            flag = 0
                        except ValueError:
                            print("Incorrect data format, should be YYYY-MM-DD")
                            outdate = input("Enter outdate : ")

                    if indate > outdate:
                        f = 1
                        print("Enter correct indate and outdate")
                    else:
                        f = 0
                roomnumber = int(input("Enter roomnumber : "))
                insert(name, address, age, indate, outdate, roomnumber)
                a.inputdata(name, address, age, indate, outdate, roomnumber)

            if (b == 2):
                a.roomrent()

            if (b == 3):
                a.restaurentbill()

            if (b == 4):
                a.laundrybill()

            if (b == 5):
                a.gamebill()

            if (b == 6):
                a.display()

            if (b == 7):
                quit()
            else:
                print("Invalid")


def insert(name, address, age, indate, outdate, roomnumber):
    res = con.cursor()
    sql = "insert into data (name,address, age,indate ,outdate,roomnumber) values (%s,%s,%s,%s,%s,%s)"
    user = (name, address, age, indate, outdate, roomnumber)
    try:
        res.execute(sql, user)
        con.commit()
        print("Data Insert Success")
    except:
        con.rollback()


def update(name, address, age, indate, outdate, roomnumber, id):
    res = con.cursor()
    sql = "update data set name=%s, address=%s, age=%s, indate=%s, outdate=%s, roomnumber=%s where id=%s"
    user = (name, address, age, indate, outdate, roomnumber, id)
    try:
        res.execute(sql, user)
        con.commit()
        print("Data Update Success")
    except:
        con.rollback()



def select():
    res = con.cursor()
    sql = "SELECT ID, NAME, ADDRESS,AGE, INDATE, OUTDATE, ROOMNUMBER from data"
    res.execute(sql)
    # result=res.fetchone()
    # result=res.fetchmany(2)
    result = res.fetchall()
    print(tabulate(result, headers=["ID", "NAME", "ADDRESS","AGE", "INDATE", "OUTDATE", "ROOMNUMBER"]))


def delete(id):
    res = con.cursor()
    sql = "delete from data where id=%s"
    user = (id,)
    try:
        res.execute(sql, user)
        con.commit()
        print("Data Delete Success")
    except:
        con.rollback()



while True:
    print("1.Insert Data")
    print("2.Update Data")
    print("3.Select Data")
    print("4.Delete Data")
    print("5.Hotel Menu")
    print("6.Exit")
    choice = int(input("Enter Your Choice : "))
    if choice == 1:
        name = input("Enter Name : ")
        address=input("Enter address: ")
        age = int(input("Enter Age : "))
        f=1
        while f==1:
            indate = input("Enter indate : ")
            date_format = '%Y-%m-%d'
            flag=1
            while (flag==1):
                try:
                    dateObject = datetime.datetime.strptime(indate, date_format)
                    flag=0
                    d = datetime.datetime.now().date()
                    if indate == str(d):
                        flag=0
                    else:

                        indate=input("Enter today's date..")
                        flag=1
                except ValueError:
                    print("Incorrect data format, should be YYYY-MM-DD")
                    indate = input("Enter indate : ")

            outdate = input("Enter outdate : ")
            date_format = '%Y-%m-%d'
            flag = 1
            while (flag == 1):
                try:
                    dateObject = datetime.datetime.strptime(outdate, date_format)
                    flag=0
                except ValueError:
                    print("Incorrect data format, should be YYYY-MM-DD")
                    outdate = input("Enter outdate : ")

            if indate > outdate:
                f=1
                print("Enter correct indate and outdate")
            else:
                f=0

        roomnumber = int(input("Enter roomnumber : "))
        insert(name, address, age, indate, outdate, roomnumber)
    elif choice == 2:
        id =int(input("Enter The Id : "))
        name = input("Enter Name : ")
        address = input("Enter address: ")
        age = int(input("Enter Age : "))
        f = 1
        while f == 1:
            indate = input("Enter indate : ")
            date_format = '%Y-%m-%d'
            flag = 1
            while (flag == 1):
                try:
                    dateObject = datetime.datetime.strptime(indate, date_format)
                    flag = 0
                    d = datetime.datetime.now().date()
                    if indate == str(d):
                        flag = 0
                    else:

                        indate = input("Enter today's date..")
                        flag = 1
                except ValueError:
                    print("Incorrect data format, should be YYYY-MM-DD")
                    indate = input("Enter indate : ")

            outdate = input("Enter outdate : ")
            date_format = '%Y-%m-%d'
            flag = 1
            while (flag == 1):
                try:
                    dateObject = datetime.datetime.strptime(outdate, date_format)
                    flag = 0
                except ValueError:
                    print("Incorrect data format, should be YYYY-MM-DD")
                    outdate = input("Enter outdate : ")

            if indate > outdate:
                f = 1
                print("Enter correct indate and outdate")
            else:
                f = 0
        roomnumber = int(input("Enter roomnumber : "))
        update(name, address, age, indate, outdate, roomnumber, id)
    elif choice == 3:
        select()
    elif choice == 4:
        id = int(input("Enter The Id to Delete : "))
        delete(id)
    elif choice == 5:
        menu()
    elif choice == 6:
        quit()
    else:
        print("Invalid Selection . Please Try Again !")
