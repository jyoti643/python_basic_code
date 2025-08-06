import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="admin@123",
  database="information"
)

mycursor = mydb.cursor()
# mycursor.execute("CREATE DATABASE information")

# mycursor.execute("SHOW DATABASES")
# for x in mycursor:
#   print(x)

# mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
# print(mydb)

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = ("John", "kandivali")
val=[("reem","borivali"),("riya","khar"),("reena","grant road")]
#mycursor.execute(sql, val)
mycursor.executemany(sql, val)
mydb.commit()

print(mycursor.rowcount, "record inserted.")