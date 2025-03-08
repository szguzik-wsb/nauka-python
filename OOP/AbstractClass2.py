# Importujemy klasy i dekoratory do tworzenia klas abstrakcyjnych
from abc import ABC, abstractmethod

# Definiujemy klasę abstrakcyjną Pojazd, dziedziczącą po ABC
class Pojazd(ABC):
    # Zmienna klasowa określająca nazwę pojazdu (ogólna)
    name = "Pojazd"
    
    # Definiujemy abstrakcyjną metodę my_name_is, którą będą musiały zaimplementować klasy potomne
    @abstractmethod
    def my_name_is(self):
        # Pusta metoda, wymagana do zaimplementowania w klasach dziedziczących
        pass

# Definiujemy klasę Samochod, dziedziczącą po klasie abstrakcyjnej Pojazd
class Samochod(Pojazd):
    # Zmienna klasowa określająca markę samochodu
    brand = "Fiat"
    # Zmienna klasowa informująca o tym, że jest to samochód osobowy
    type_of_vehicle = "samochod osobowy"
    
    # Implementacja metody my_name_is wymaganej przez klasę bazową
    def my_name_is(self):
        # Zwracamy nazwę pojazdu oraz informację o marce i typie
        return f"Jestem {self.name}, marka: {self.brand}, rodzaj: {self.type_of_vehicle}"

# Definiujemy klasę Samolot, dziedziczącą po Pojazd
class Samolot(Pojazd):
    # Konstruktor, który przyjmuje linię lotniczą i ustawia ją w prywatnej zmiennej
    def __init__(self, airline):
        # Prywatny atrybut przechowujący informację o linii lotniczej
        self._airline = airline

    # Implementacja metody my_name_is wymaganej przez klasę bazową
    def my_name_is(self):
        # Zwracamy nazwę pojazdu oraz linię lotniczą do której należy samolot
        return f"Jestem {self.name}, należę do linii lotniczych: {self._airline}"

    # Publiczny setter dla prywatnej zmiennej _airline
    def set_airline(self, airline):
        # Ustawiamy wartość prywatnej zmiennej _airline na tę podaną w argumencie
        self._airline = airline

    # Publiczny getter dla prywatnej zmiennej _airline
    def get_airline(self):
        # Zwracamy aktualną wartość prywatnej zmiennej _airline
        return self._airline


# Przykładowe użycie:

# Tworzymy obiekt klasy Samochod
car = Samochod()
# Wywołujemy metodę my_name_is, która została zdefiniowana w klasie Samochod
print(car.my_name_is())  # "Jestem Pojazd, marka: Fiat, rodzaj: samochod osobowy"

# Tworzymy obiekt klasy Samolot, przypisując mu linię lotniczą "LOT"
plane = Samolot("LOT")
# Wywołujemy metodę my_name_is, która została zdefiniowana w klasie Samolot
print(plane.my_name_is())  # "Jestem Pojazd, należę do linii lotniczych: LOT"

# Zmieniamy linię lotniczą za pomocą settera
plane.set_airline("Lufthansa")
# Sprawdzamy nową linię lotniczą za pomocą gettera
print(plane.get_airline())  # "Lufthansa"
print(plane.my_name_is())   # "Jestem Pojazd, należę do linii lotniczych: Lufthansa"
