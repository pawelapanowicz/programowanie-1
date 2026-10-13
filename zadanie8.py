wysokosc_choinki = input("Podaj wysokość choinki: ")
for i in range(int(wysokosc_choinki)):
    print(" " * (int(wysokosc_choinki) - i + 1) + "*" * (2 * i + 1))