import mysql.connector

mydb = mysql.connector.connect(host="localhost", port="3307", user="root", password="", database="dbmsdb")

mycursor = mydb.cursor()

sql = "UPDATE data SET name = 'thanikjg' WHERE id = 1"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")


        sql = "update data set name=%s, date=%s, airport_d=%s, duration=%s, airport_a=%s, count=%s, amount=%s where id=%s"
        user = (self.fname, self.date, self.fdept, self.fdur, self.farvl, self.nooftickets,self.fbill,self.fid)
        try:
            res.execute(sql, user)
            con.commit()
            print("Data Update Success")
        except:
            con.rollback()



'''from tabulate import tabulate
import datetime

import mysql.connector

con = mysql.connector.connect(host="localhost", port="3307", user="root", password="", database="dbmsdb")

if(con):
    print("Connected")
else:
    print("Error")



def flight1():
    id=input("Enter ID")
    name=input("Enter your name")
    date=input("Enter date of travel")
    insert(id,name,date)

def insert(id,name,date):
    res = con.cursor()
    sql = "insert into data (id,name,date) values (%s,%s,%s)"
    user = (id,name,date)
    try:
        res.execute(sql, user)
        con.commit()
        print("Data Insert Success")
    except:
        con.rollback()

def flight2():
    id=input("Enter ID")
    name=input("Enter your name")
    date=input("Enter date of travel")
    update(id,name,date)

def update(id,name,date):
    res = con.cursor()
    sql = "update data set name=%s, date=%s where id=%s"
    user = (id,name,date)
    try:
        res.execute(sql, user)
        con.commit()
        print("Data Update Success")
    except:
        con.rollback()

def select():
    res = con.cursor()
    sql = "SELECT ID, NAME, DATE from data"
    res.execute(sql)
    # result=res.fetchone()
    # result=res.fetchmany(2)
    result = res.fetchall()
    print(tabulate(result, headers=["ID", "NAME", "DATE"]))


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
    print("--------------------------------------------------------------------------------")
    print("WELCOME TO GOA TOURISM")
    print("We aim to assist you in planning a comfortable and fun trip to Goa. ") 
    print("Enjoy your Visit! ")
    print("--------------------------------------------------------------------------------")
    print("     1)  Flight Booking")
    print("     2)  Update Flight Booking")
    print("     3)  View Flight Booking")
    print("     4)  Delete Flight Booking")
    print("     5)  Exit")
    choice = int(input("Enter Your Choice : "))
    if choice == 1:
        flight1()
    elif choice ==2 :
        flight2()
    elif choice==3:
        select()
    elif choice==4:
        id = int(input("Enter The Id to Delete : "))
        delete(id)
    
'''
