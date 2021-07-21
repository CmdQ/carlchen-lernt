import sqlite3
from sqlite3.dbapi2 import Cursor

prerequisites = """
DROP TABLE IF EXISTS Books;
CREATE TABLE Books (
    BuchID integer primary key,
    Titel text,
    AusgeliehenVon text,
    Kundennummer integer
);
INSERT INTO Books VALUES
    (123, "Bürgerliches Gesetzbuch", "Magdalena Mustermann", 12345),
    (137, "Die Physiker", NULL, NULL),
    (55, "Darm mit Charme", NULL, NULL),
    (42, "Die Verwandlung", "Jan Modal", 75135),
    (23, "Der Prozess", "Jan Modal", 75135);
"""

con = sqlite3.connect("buecher.db")

while True:
    buch = input("Buchtitel? ")
    if buch == "quit":
        break

    cursor = con.cursor()
    result = cursor.execute("SELECT AusgeliehenVon FROM Books WHERE Titel=?", [buch]).fetchone()
    if not result:
        print("Dieses Buch gibt es nicht.")
    elif result[0] is None:
        print("Das Buch ist nicht verliehen.")
    else:
        print(f"Das Buch wurde ausgeliehen von {result[0]}.")
