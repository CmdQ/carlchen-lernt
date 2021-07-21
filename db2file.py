import sqlite3

con = sqlite3.connect("database.db")

cursor = con.cursor()
with open("employees.txt", "w") as f:
    for row in cursor.execute("SELECT * FROM Employees"):
        #print(f"{row[0]},{row[1]},{row[2]}", file=f)
        f.write(f"{row[0]},{row[1]},{row[2]}\n")

con.close()
