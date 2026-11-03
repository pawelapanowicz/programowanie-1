studenci = input("Podaj liczbę studentów: ")

for i in range(int(studenci)):
    student = input("Podaj nazwisko studenta: ")
    punkty_studenta = input("Podaj liczbę punktów studenta: ")
    print("Student:", student, "uzyskał ocenę:", end=" ")
    if int(punkty_studenta) >= 90:
        print("5.0")
    elif int(punkty_studenta) >= 80:
        print("4.5")
    elif int(punkty_studenta) >= 70:
        print("4.0")
    elif int(punkty_studenta) >= 60:
        print("3.5")
    elif int(punkty_studenta) >= 50:
        print("3.0")
    else:
        print("2.0")
