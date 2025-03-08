# Pobieranie imienia i wieku od użytkownika

imie = input("Podaj swoje imię: ")

wiek_str = input("Podaj swój wiek: ")

# Rzutowanie wieku na typ liczbowy (int)
wiek = int(wiek_str)

# Formatowanie i wyświetlanie danych
print(f"Witaj, {imie.upper()}! Za rok będziesz miał(a) {wiek + 1} lat.") 