import mysql.connector

dataBase = mysql.connector.connect(
    host="localhost",  # Replace with your server's hostname or IP address
    user="root",
    passwd="Password1234",
)

# Rest of your code to interact with the database

cursorObject = dataBase.cursor()


cursorObject.execute("CREATE DATABASE elderco")

print("All Done!")