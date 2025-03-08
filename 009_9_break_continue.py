for liczba in range(10):
    if liczba == 5:
        break  # Przerwij, gdy liczba wynosi 5
    print(liczba)

for liczba in range(10):
    if liczba % 2 == 0:  # Pomijaj liczby parzyste
        continue
    print(liczba)
