import sqlite3
#to create database
database = sqlite3.connect("movieShop.db")
cur = database.cursor()

def createTable():
    query = """CREATE TABLE movieShopDetails(movieTitle Text, movieType Text, clientName Text, clientPNumber Text,
    clientEAddress Text, amountCharged Text, dateBorrowed Text, status Text)"""
    database.execute(query)
    database.commit()
    
#function to leand movie
def lendMovie(record):
    record = ( mT, mTy, cN, cPN, cEA,aC, dB)
    query = """INSERT INTO  movieShopDetails(movieTitle, movieType, clientName,clientPNumber, 
    clientEAddress ,amountCharged, dateBorrowed,  status) VALUES (?,?,?,?,?,?,?,"pending")"""
    database.execute(query, record)
    database.commit()

    
def viewPendingLending():
   
    query = """SELECT movieTitle, movieType, clientName,clientPNumber,clientEAddress ,amountCharged, dateBorrowed, status FROM movieShopDetails
    WHERE status == 'pending';"""
    cursor = database.execute(query)
    for row in cursor:
        for i in range(0,8):
            print(row[i])
    
def viewCanceledTransactions():
    query = """SELECT movieTitle, movieType, clientName,clientPNumber,clientEAddress ,amountCharged, dateBorrowed, status
    FROM movieShopDetails
    WHERE status="CANCELED";"""
    cursor = cur.execute(query)
    details = cur.fetchall()
    if details == []:
        print("NO TRANSACTIONS")
    else:
        for row in details:
            for i in range(0,8):
                print(row[i])

def  viewReturnedTransactions():
    query = """SELECT movieTitle, movieType, clientName,clientPNumber,clientEAddress ,amountCharged, dateBorrowed FROM movieShopDetails
    WHERE status="RETURNED";"""
    cursor = cur.execute(query)
    details = cur.fetchall()
    if details == []:
        print("NO TRANSACTIONS")
    else:
        for row in cursor:
            for i in range(0,8):
                print(row[i])
def update(record):
    record = (s, )
    query ="""UPDATE movieShopDetails SET status = 'RETURNED' WHERE movieTitle = ? """
    database.execute(query, record)
    database.commit()
def update2(record):
    record = (s, )
    query ="""UPDATE movieShopDetails SET status = 'CANCELED' WHERE movieTitle = ? """
    database.execute(query, record)
    database.commit()
def viewSummary():
    query = """SELECT * FROM movieShopDetails   ;"""
    cursor = database.execute(query)
    for row in cursor:
        if row[7] == 'pending':
            v=0
            v+=1
            print("number of pending", v)
        if row[7] == 'CANCELED':
            b=0
            b+=1
            print("number of canceled", b)
        if row[7] == 'RETURNED':
            a=0
            a+=1
            print("number of returned",a)
       

def viewEarning():
    query = """SELECT * FROM movieShopDetails   ;"""
    cursor = database.execute(query)
    for row in cursor:
        if row[7] == 'RETURNED':
            a=0
            a+=1
            print("amount earned", a*25.54)

c =0
while(c!=9):
    print("1. Lend movie: ")
    print("2. View Pending Lending: ")
    print("3. View Canceled Transactions:")
    print("4. View Returned Transactions:")
    print("5. Return a movie:")
    print("6. Cancel Transaction: ")
    print("7. View Summary:")
    print("8. View earning:")
    c = int(input("enter choice"))
    if(c==1):
        mT = input("enter movie title")
        mTy = input("enter movie type")
        cN = input("enter client name")
        cPN = input("enter client phone number")
        cEA = input("enter the client email address")
        aC = input("enter the amount charged")
        dB = input("enter date borrowed")
        record = ( mT,mTy,  cN, cPN, cEA,aC, dB)
        lendMovie(record)
    if (c==2):
        viewPendingLending()
    if (c==3):
        viewCanceledTransactions()
    if(c==4):
        viewReturnedTransactions()
    if(c==5):
        viewPendingLending()
        s = input("enter movie title to update")
        record = (s,)
        update(record)
    
    if(c==6):
        viewPendingLending()
        s = input("enter movie title to update")
        record = (s,)
        update2(record)
    if (c==7):
        viewSummary()
    if(c==8):
        viewEarning()




