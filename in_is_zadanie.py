lista_zakupow = input("Wprowadź nazwy produktów, rozdziel je za pomocą ptzecinka: ")
lista_zakupow_rozdzielenie = lista_zakupow.split(",")
if "chleb" in lista_zakupow_rozdzielenie or "bułki" in lista_zakupow_rozdzielenie:
    print("Kupujesz pieczywo")