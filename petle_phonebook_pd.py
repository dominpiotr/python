phonebook = {}
while True:
    print(f"""
    x wyjście z programu
    a dodanie do książki
    d usuwanie kontaktu
    v wyświetlenie""")
    wej = input("Co chcesz zrobić (podaj literkę) ")
    try:
        if wej == "x":
            break
        elif wej == "a":
            telefon = input("nr telefonu: ")
            nazwa = input("nazwa: ")
            phonebook[nazwa] = telefon
        elif wej == "v":
            if not phonebook:
                print("Zero kontaktów")
            for nazwa, telefon in phonebook.items():
                print(f"Kontakt {nazwa} : {telefon}")
        elif wej == "d":
            nazwa = input("Podaj nazwę kontaktu do usunięcia: ")
            del phonebook[nazwa]
    except KeyError:
        print(f"Nie ma kontaktu {nazwa}")
    except Exception as e:
        print("Wystąpił błąd: ", e)
