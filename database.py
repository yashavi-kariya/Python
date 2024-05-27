# import mysql.connector
# mydb=mysql.connector.connect(host='localhost',user='root',password='')
# print(mydb)

#creating database
# import mysql.connector
# mydb=mysql.connector.connect(host='localhost',user='root',password='')
# mycursor=mydb.cursor()
# mycursor.execute('CREATE DATABASE mypy')

# creating table
# import mysql.connector
# mydb=mysql.connector.connect(host='localhost',user='root',password='',database='mypy')
# mycursor=mydb.cursor()
# mycursor.execute('CREATE table stud_data(roll int,name varchar(25))')

#showing database
# import mysql.connector
# mydb=mysql.connector.connect(host='localhost',user='root',password='',database='mypy')
# mycursor=mydb.cursor()
# mycursor.execute('SHOW DATABASES')
# for i in mycursor:
# 	print(i)

# inserting the database

# import mysql.connector
# mydb=mysql.connector.connect(host='localhost',user='root',password='',database='mypy')
# my_insert_query='INSERT into stud_data (roll,name)values(%s,%s)'
# record_to_insert=[(1,'sunday'),(2,'monday'),(3,'tuesday')]
# cursor=mydb.cursor()
# cursor.executemany(my_insert_query,record_to_insert)
# # mycursor=mydb.cursor()
# mydb.commit()
# print('record inserted successfully')
# mydb.close()

# display the records

# import mysql.connector
# mydb=mysql.connector.connect(host='localhost',user='root',password='',database='mypy')
# mycursor=mydb.cursor()
# mycursor.execute('SELECT * FROM stud_data')
# myresult=mycursor.fetchall()
# for i in myresult:
# 	print(i)

# update

# import mysql.connector
# mydb=mysql.connector.connect(host='localhost',user='root',password='',database='mypy')
# mycursor=mydb.cursor()
# mycursor.execute("UPDATE stud_data SET name='friday' WHERE roll=2")
# mydb.commit()
# mydb.close()


# delete record
import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='',database='mypy')
mycursor=mydb.cursor()
mycursor.execute("DELETE FROM stud_data WHERE roll=3")
mydb.commit()
mydb.close()



