import sqlite3

try:
    sql_connect = sqlite3.connect('sqlile_moja.db')
    cursor = sql_connect.cursor()
    print("Baza połączona")
except sqlite3.Error as e:
    print("Błąd połączena z bazą", e)
finally:
    if sql_connect:
        sql_connect.close()
        print("Baza zamknięta")
