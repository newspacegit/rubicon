import psycopg2

conn = psycopg2.connect(database="rubicondb", user="rubicon",password="Rub1coN",host="10.77.150.34")
print("Opened database successfully")
ctable = "CREATE TABLE USERS (UserID int, LastName varchar(255),FirstName varchar(255));"
ins = "INSERT INTO USERS(UserID,LastName,FirstName) VALUES(1,'Petrov','Ivan');"
sel = "SELECT * FROM USERS;"
cur = conn.cursor()
cur.execute(sel)
for row in cur:
    print(row)
conn.commit()
print("Tables Create")



