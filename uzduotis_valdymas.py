#Ivesti klienta
#Ivesti uzsakyma
#Ivesti uzsakymo statusa
#Ivesti uzsakymo eilute
#Ivesti gamini
#Perziureti klienta
#Perziureti uzsakyma
#Perziureti suzsakymo statusa
#Perziureti uzsakymo eilute
#Perziureti gamini
from sqlalchemy.orm import sessionmaker
from uzduotis import engine, Klientas, Uzsakymas, Uzsakymo_statusas, Uzsakymo_eilute, Gaminys

Session = sessionmaker(bind=engine)
session = Session()

while True:
    pasirinkimas = input("1 - a - įveskite klientą\n2 - b - įveskite užsakymą\n3 - c - įveskite užsakymo statusą\n4 - d - įveskite užsakymo eilutę\n5 - e - įveskite gaminį\n6 - f - peržiūrėti klientą\n7 - g - peržiūrėti užsakymą\n8 - h - peržiūrėti užsakymo statusą\n9 - i - peržiūrėti užsakymo eilutę\n10") 
    if pasirinkimas == "a":
        vardas = input("Įveskite vardą: ")
        pavarde = input("Įveskite pavardę: ")
        tel_nr = input("Įveskite telefomo numerį +370")
        adresas = input("Įveskite adresą: ")
        klientas = Klientas(vardas=vardas, pavarde=pavarde, tel_nr=tel_nr, adresas=adresas)
        session.add(klientas)
        session.commit()

    if pasirinkimas == "b":
        suma = input("Suma")
        prisatymo_adresas = ("Pristatymo adresas")
        
    if pasirinkimas == "c":
        pavadinimas = 


    if pasirinkimas == "d"
    if pasirinkimas == "e"
    if pasirinkimas == "f"
    if pasirinkimas == "g"
    if pasirinkimas == "h"
    if pasirinkimas == "i"
