import sqlite3

dataBase = sqlite3.connect('ARU_Submarine_Project_Data_Base.db')
print("Data Based Opened")


# def CreateDonationsTable():
#     dataBase.execute('''
#     CREATE TABLE IF NOT EXISTS Donations(
#     DonationID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
#     IBAN CHAR(26) NOT NULL,
#     NameSurname TEXT NOT NULL,
#     DonationAmount FLOAT NOT NULL
#     )
#     ''')
#
#
def CreateTicketsReceivedTable():
    dataBase.execute('''
    CREATE TABLE TicketsReceived(
    TicketID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    IdentityNo TEXT NOT NULL,
    NameSurname TEXT NOT NULL,
    TripDate TEXT NOT NULL,
    Location TEXT NOT NULL,
    ClassType TEXT NOT NULL,
    IBAN CHAR(26) NOT NULL
    )''')

def CreateManager():
    dataBase.execute('''
    CREATE TABLE Managers(
    ManagerID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Username TEXT NOT NULL,
    Password TEXT NOT NULL
    )''')
#
#
def CreateIdeasTable():
    dataBase.execute('''
    CREATE TABLE IF NOT EXISTS Ideas(
    IdeaID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    NameSurname TEXT NOT NULL,
    Idea TEXT NOT NULL
    )''')


def CreateTripAdviceTable():
    dataBase.execute('''
        CREATE TABLE IF NOT EXISTS TripAdvices(
        TripAdvicesID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        NameSurname TEXT NOT NULL,
        CityName TEXT NOT NULL,
        StateName TEXT NOT NULL,
        LocationsAndReasons TEXT NOT NULL
    )''')


# def CreatingAllTables():
#     CreateIdeasTable()
    # CreateDonationsTable()
    # CreateTicketsReceivedTable()
    # CreateTripAdviceTable() #Already created
# def insertManager(ID,username,password):
#     dataBase.execute(''' INSERT INTO Managers(ManagerID,Username,Password) VALUES(?,?,?)''', (ID,username,password))
#     dataBase.commit()
#
# def insertIdea(ID, NameSurname, Idea):
#     dataBase.execute('''INSERT INTO Ideas(IdeaID,NameSurname,Idea) VALUES(?,?,?)''',
#                      (ID, NameSurname, Idea))
#     dataBase.commit()  # To Applying the Changes
#
#
# def insertDonation(ID, IBAN, NameSurname, Price):
#     dataBase.execute('''INSERT INTO Donations(DonationID,IBAN,NameSurname,DonationAmount) VALUES(?,?,?,?)''',
#                      (ID, IBAN, NameSurname, Price))
#     dataBase.commit()  # To Applying the Changes
#
#
# def insertTripAdvice(ID, NameSurname, City, State, Reason):
#     dataBase.execute('''INSERT INTO TripAdvice(AdviceID,NameSurname,City,State,Reasons) VALUES(?,?,?,?,?)''',
#                      (ID, NameSurname, City, State, Reason))
#     dataBase.commit()  # To Applying the Changes
#
#
# def insertTicket(TicketID, IdentityNo, NameSurname, Date, Location, Class, IBAN):
#     dataBase.execute('''INSERT INTO TicketsReceived(TicketID,IdentityNo,NameSurname,Date,Location,Class,IBAN)
#     VALUES(?,?,?,?,?,?,?)''',
#                      (TicketID, IdentityNo, NameSurname, Date, Location, Class, IBAN))
#     dataBase.commit()  # To Applying the Changes
#
#
# FunctionName(); #Already Created
# insertDonation(1, "9197919791979197955245", "MustafaBerat", 550)
# insertIdea(1, "MustafaBerat", "I think Istanbul is very nice but also i need to see the sea of Izmir")
# insertTicket(1, "26476490554", "MustafaBerat", 2019 - 12 - 16, "Istanbul", "Standard", "9197919791979197954245")
# insertManager(1,"mustafaberat","mustafaberat")
dataBase.close()
print("Data Base Closed")
