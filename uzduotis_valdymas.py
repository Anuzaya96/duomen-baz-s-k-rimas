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
from uzduotis import engine, Klientas, Uzsakymas, UzsakymoStatusas, UzsakymoEilute, Gaminys

Session = sessionmaker(bind=engine)
session = Session()

while True:
    pasirinkimas = input("1 - a - įveskite klientą\n2 - b - įveskite užsakymą\n3 - c - įveskite užsakymo statusą\n4 - d - įveskite užsakymo eilutę\n5 - e - įveskite gaminį\n6 - f - peržiūrėti klientą\n7 - g - peržiūrėti užsakymą\n8 - h - peržiūrėti užsakymo statusą\n9 - i - peržiūrėti užsakymo eilutę\n10 - j - peržiūrėti gaminį\n11 - k - išeiti iš programos\11") 
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
        prisatymo_adresas = input("Pristatymo adresas")
        uzsakymas = Uzsakymas(suma=suma, prisatymo_adresas=prisatymo_adresas)
        session.add(uzsakymas)
        session.commit()
        
    if pasirinkimas == "c":
        pavadinimas = input("Užsakymo statusas: ")
        uzsakymo_statusas = UzsakymoStatusas(pavadinimas=pavadinimas)
        session.add(uzsakymo_statusas)
        session.commit()

    if pasirinkimas == "d":
        kiekis = input("Gaminių kiekis: ")
        suma = ("Suma: ")
        uzsakymo_eilute = UzsakymoEilute(kiekis=kiekis, suma=suma)
        session.add(uzsakymo_eilute)
        session.commit()

    if pasirinkimas == "e":
        pavadinimas = input("Gamynio pavadinimas: ")
        _1_vnt_kaina = input("Vnt kaina: ")
        _1_vnt_svoris = input("Vnt svoris: ")
        gaminys = Gaminys(pavadinimas=pavadinimas, _1_vnt_kaina=_1_vnt_kaina, _1_vnt_svoris=_1_vnt_svoris)
        session.add(gaminys)
        session.query()

    if pasirinkimas == "f":
        klientai = session.query(Klientas).all()
        for klientas in klientai:
            print(klientas)

    if pasirinkimas == "g":
        uzsakymai = session.query(Uzsakymas).all()
        for uzsakymas in uzsakymai:
            print(uzsakymas)

    if pasirinkimas == "h":
        uzsakymu_statusai = session.query(UzsakymoStatusas).all()
        for uzsakymo_statusas in uzsakymu_statusai:
            print(uzsakymo_statusas)

    if pasirinkimas == "i":
        uzsakymu_eilutes = session.query(UzsakymoEilute).all()
        for uzsakymo_eilute in uzsakymu_eilutes:
            print(uzsakymo_eilute)

    if pasirinkimas =="j":
        gaminiai = session.query(Gaminys).all()
        for gaminys in gaminiai:
            print(gaminys)
    if pasirinkimas =="k":
        print("Viso!")
        break
