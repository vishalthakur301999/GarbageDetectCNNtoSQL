import mysql.connector

mydb = mysql.connector.connect(
  host="urhost",
  user="uruname",
  passwd="urpass"
)

print(mydb)