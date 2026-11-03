kwota = input("Ile odkładasz tygodniowo?: ")
tygodnie = input("Przez ile tygodni?: ")
suma = 0
for i in range(1, int(tygodnie) + 1):
    suma = suma + float(kwota)
    print("Tydzień", i, ":", suma, "zł")
print("Łączne oszczędności:", suma, "zł")