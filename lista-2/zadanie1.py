lista = []
ilosc = int(input("Ile produktów chcesz dodać? "))
for i in range(ilosc):
    produkt = input(f"Podaj nazwę produktu {i+1}: ")
    lista.append(produkt)
print("Lista:", lista)
print("Liczba produktów:", len(lista))
usunac = input("Produkt do usunięcia: ")
if usunac in lista:
    lista.remove(usunac)
    print("Nowa lista:", lista)