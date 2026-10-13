czas_parkowania = input("Podaj czas parkowania (h): ")
if int(czas_parkowania) <= 0:
    print("Nieprawidłowe dane")
elif int(czas_parkowania) <= 1:
    print("Opłata za parking: 5 zł")
elif int(czas_parkowania) <= 3:
    print("Opłata za parking: 12 zł")
elif int(czas_parkowania) <= 6:
    print("Opłata za parking: 20 zł")
else:
    print("Opłata za parking: 30 zł")