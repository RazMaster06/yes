import os
import sqlite3
from sqlite3 import Error

#main()
def main():

    add_dog_to_table()
    list_dog_table()


def list_dog_table():
    #DB Connect
    sqliteConnection = sqlite3.connect("dogs.db")
    cursor = sqliteConnection.cursor()

    sqlite_select_query = """SELECT * from dogs ORDER BY namn"""
    cursor.execute(sqlite_select_query)
    records = cursor.fetchall()

    for row in records:
        print(f"ID: {row[0]} NAMN: {row[1]} RAS: {row[2]}")

    cursor.close()
    sqliteConnection.close()

def add_dog_to_table():
    os.system('cls' if os.name == 'nt' else 'clear')
    hundnamn = input("Mata in hund namn: ")
    hundras = input("Hund ras: ")

    sqliteConnection = sqlite3.connect('dogs.db')
    cursor = sqliteConnection.cursor()
    sqlite_insert_query = f"""INSERT INTO dogs
                        (namn, ras)
                        VALUES
                        ('{hundnamn}', '{hundras}')"""
    
    cursor.execute(sqlite_insert_query)
    sqliteConnection.commit()
    print("Closed")
    #Stänga av
    cursor.close()

    sqliteConnection.close()



main()