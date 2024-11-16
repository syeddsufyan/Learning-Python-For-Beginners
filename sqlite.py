import sqlite3
try:
	# creating db using this
	sqliteConnection = sqlite3.connect('SQLite_Python.db')
# 	# when create table any db using this
	cur = sqliteConnection.cursor()
# 	# then insert everything inset update delete etc 
# 	# now execute
	print("Database Created And Succussfully Connect To Sqlite")
	sqlite_select_query = "select sqlite_version();"
	cur.execute(sqlite_select_query)
	record = cur.fetchall()
	print("SQLite Database Version is: ", record)
	cur.close()
except sqlite3.Error as error:
	print("Error While Connecting To Sqlite", error)
try:
	sqliteConnection = sqlite3.connect('SQLite_Python.db')
	sqlite_create_table_qurey = '''CREATE TABLE IF NOT EXISTS SqliteDb_developers(
			id INTEGER PRIMARY KEY,
			name TEXT NOT NULL,
			email TEXT NOT NULL
	UNIQUE,
			joining_data datetime
			salary REAL NOT NULL);'''
	cursor = sqliteConnection.cursor()
	print('Succussfully Created To Sqlite')
	cursor.execute(sqlite_create_table_qurey)
	print("Sqlite Table Created")
	cursor.close()
except sqlite3.Error as error:
	print("Error While Creating a Sqlite Table", error)		
finally:
	if (sqliteConnection):
		sqliteConnection.close()
		print("Sqlite Connection In Closed")

# CREATE TABLE
conn = sqlite3.connect('test.db')
print("Open Database Succussfully")
conn.execute('''CREATE TABLE IF NOT EXISTS COMPANY (ID INT PRIMARY KEY,
		NAME TEXT NOT NUll,
		AGE INT NOT NULL,
		ADDRESS CHAR(50),
		SALARY REAL);''')
print("Table Created Succussfully")
conn.close()

# INSERT
try:
	conn = sqlite3.connect('test.db')
	print("Open Database Succussfully")
	conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
					VALUES (1, 'Paul', 32, 'California', 2000.00)");
	conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
					VALUES(2,'Allen',25,'Texas',15000.00)");
	conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
					VALUES(3,'Teeddy',23,'Norway',20000.00)");
	conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
					VALUES(4,'Mark',25,'Rich-Mond', 650000.00)");
	conn.commit()
	print("Record Has Been Added")
	conn.close()
except:
	print("Username Aleady Exists")
	

# # SELECT

# connect = sqlite3.connect('test.db')
# print("Opened Database Succussfully")
# cursor = connect.execute("SELECT id, name, address, salary FROM COMPANY")
# for row in cursor:
# 	print("ID =", row[0])
# 	print("Name =", row[1])
# 	print("Address =", row[2])
# 	print("Salary =", row[3], "\n")
# print("Operation  Done Succussfully")
# connect.close()

# # UPDATE

# conn = sqlite3.connect('test.db')
# print("Open Database Succussfully")
# conn.execute("UPDATE COMPANY SET SALARY=25000.00 WHERE ID=1")
# conn.commit()
# print("Total number of rows updated", conn.total_changes)
# cursor = conn.execute("SELECT id, name, address, salary FROM COMPANY")
# for row in cursor:
# 	print("ID =", row[0])
# 	print("Name =", row[1])
# 	print("Address =", row[2])
# 	print("Salary =", row[3])


# conn = sqlite3.connect('test.db')
# print("Open Database Succussfully")
# conn.execute("DELETE FROM COMPANY WHERE ID=2;")
# conn.commit()
# print("Total number of rows deleted:", conn.total_changes)
# cursor = conn.execute("SELECT id, name, address, salary FROM COMPANY")
# for row in cursor:
# 	print("ID =", row[0])
# 	print("Name =", row[1])
# 	print("Address =", row[2])
# 	print("Salary =", row[3], "\n")
# print("Operation Done Succussfully")
# conn.close
from employee_class import Employee

conn = sqlite3.connect('emloyee.db')
# clean db
conn = sqlite3.connect(':memory:')
print("Emloyee Database Has Been Created")

c = conn.cursor()

c.execute("""CREATE TABLE emloyees(first text, last text, pay integer)""")
print("Emloyees Table Has Been Created")

def insert_emp(emp):
	with conn:
		c.execute("INSERT INTO emloyees VALUES (:first, :last, :pay)",{'first':emp.first, 'last':emp.last, 'pay':emp.pay})

def get_emps_by_name(lastname):
	c.execute("SELECT * FROM emloyees WHERE last=:last", {'last':lastname})
	return c.fetchall()

def update_pay(emp, pay):
	with conn:
		c.execute("""UPDATE emloyees SET pay=:pay WHERE first=:first AND last=:last""",
				{'first':emp.first, 'last':emp.last, 'pay':pay})

def remove_emp(emp):
	with conn:
		c.execute("DELETE FROM emloyees WHERE first=:first AND last=:last", {'first':emp.first, 'last':emp.last})


emp_1 = Employee("John", "Doe", 90000)
emp_2 = Employee("Jane", "Doe", 100000)

insert_emp(emp_1)
insert_emp(emp_2)

emps = get_emps_by_name('Doe')
print(emps)

update_pay(emp_2, 95000)
remove_emp(emp_1)

emps = get_emps_by_name('Doe')
print(emps)
# c.execute("INSERT INTO emloyees(first, last, pay) VALUES ('Ahmed', 'Muhammad', 70)")
# print("Emloyees Table Record Inserted")
# conn.commit()

# c.execute("SELECT * FROM emloyees WHERE first='Ahmed'")
# print(c.fetchall())

# c.execute("INSERT INTO emloyees VALUES ('{}', '{}', '{}')".format(emp_1.first, emp_1.last, emp_1.pay))
# print("Emloyees Table Record Inserted")
# conn.commit()

# c.execute("INSERT INTO emloyees VALUES (?, ?, ?)",(emp_1.first, emp_1.last, emp_1.pay))
# print("Emloyees Table Record Inserted")
# conn.commit()

# c.execute("SELECT * FROM emloyees WHERE first=? AND last=?", ('Azian', 'Khan'))
# print(c.fetchall())


# c.execute("INSERT INTO emloyees VALUES (:first, :last, :pay)",
# 	{'first':emp_2.first, 'last':emp_2.last, 'pay':emp_2.pay})
# print("Emloyees Table Record Inserted")
# conn.commit()

# c.execute("SELECT * FROM emloyees WHERE first=:first_key AND last=:last_key", {'first_key':'Kashif', 'last_key':'Ali'})
# print(c.fetchall())


conn.close()