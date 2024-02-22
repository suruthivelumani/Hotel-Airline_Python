from tabulate import tabulate
import datetime

import mysql.connector

con = mysql.connector.connect(host="localhost", port="3307", user="root", password="", database="sampledbmsdb")

'''if(con):
    print("Connected")
else:
    print("Error")'''



def flight1():
    id=input("Enter ID")
    name=input("Enter your name")
    insert(id,name)

def insert(id,name):
    res = con.cursor()
    sql = "insert into data (id,name) values (%s,%s)"
    user = (id,name)
    try:
        res.execute(sql, user)
        con.commit()
        print("Data Insert Success")
    except:
        con.rollback()

def flight2():
    id=input("Enter ID")
    name=input("Enter your name")
    update(id,name)

def update(id,name):
    res = con.cursor()
    sql = "update data set id=%s, name=%s where id=%s"
    user = (id,name)
    try:
        res.execute(sql, user)
        con.commit()
        print("Data Update Success")
    except:
        con.rollback()

def select():
    res = con.cursor()
    sql = "SELECT ID, NAME from data"
    res.execute(sql)
    # result=res.fetchone()
    # result=res.fetchmany(2)
    result = res.fetchall()
    print(tabulate(result, headers=["ID", "NAME"]))


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
    elif choice == 5:
        print("Thank You for Visiting")
        quit()
    else:
        print("Invalid Selection . Please Try Again !")

    

