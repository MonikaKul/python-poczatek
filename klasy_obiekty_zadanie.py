class Produkt:
    pass

class Zamowienie:
    pass

class Jablka:
    pass

class Ziemniaki:
    pass

if __name__ == '__main__':
    jablko_czerwone = Jablka()
    jablko_zielone = Jablka()

    ziemniak_maly = Ziemniaki()
    ziemniak_duzy = Ziemniaki()

    wazne_zamowienie = Zamowienie()

print(jablko_zielone, jablko_czerwone)
print(ziemniak_duzy, ziemniak_maly)

print("type(jablko_zielone:", type(jablko_zielone))
print("type(jablko_czerwone:", type(jablko_czerwone))
print("type(ziemniak_maly:", type(ziemniak_maly))
print("type(ziemniak_duzy:", type(ziemniak_duzy))

wszystkie_zamowienia = [Zamowienie(), Zamowienie(), Zamowienie()]
print(wszystkie_zamowienia)
print(wszystkie_zamowienia[0])

produkty = {
    "Jablko": Produkt(),
    "Chleb": Produkt(),
    "Mleko": Produkt
}

print(produkty)