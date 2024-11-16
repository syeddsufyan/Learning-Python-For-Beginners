import sqlite3
conn = sqlite3.connect('test.db')
print("Database Create Succussfully")

conn.execute("CREATE TABLE IF NOT EXISTS  COMPANY(p_id INTEGER PRIMARY KEY, p_name TEXT NOT NULL, price REAL, quantity INTEGER)");
print("Table Has Been Created");

conn.execute("INSERT INTO COMPANY(p_name,price,quantity) VALUES('AutoCAD', 200, 20)");
conn.execute("INSERT INTO COMPANY(p_name,price,quantity) VALUES('Quick Hill', 330, 12)");
print("Company data has been inserted")

update = conn.execute("UPDATE COMPANY SET quantity=quantity+5, price=2131 WHERE p_id=1");
update = conn.execute("UPDATE COMPANY SET quantity=quantity+5, price=2131 WHERE p_id=2");
for row in update:
	print(row[0])
	print(row[1])
	print(row[2])
	print(row[3])
print("Update Has Been Selected")

query = conn.execute("SELECT * FROM COMPANY")
for row in query:
	print(row[0])
	print(row[1])
	print(row[2])
	print(row[3])
print("Data Has Been Selected")

