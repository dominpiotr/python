typ_samochodu = "pieszo"
wiek = int(input("podaj swój wiek: "))

if wiek < 18:
    typ_samochodu = "pieszo"
elif (wiek > 25 and wiek < 59):
    typ_samochodu = "mały"
elif wiek < 60:
    typ_samochodu = "samochód rodzinny"
else:
    typ_samochodu = "kabriolet"


print(f"sugeruję:{typ_samochodu}")
