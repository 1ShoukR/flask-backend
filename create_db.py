import mysql.connector


mydb = mysql.connector.connect(host='localhost', user='root', passwd = 'Rahmin12')



my_cursor = mydb.cursor()

my_cursor.execute('CREATE DATABASE to_do_list_v2')



my_cursor.execute('SHOW DATABASES')

for db in my_cursor:
    print(db)