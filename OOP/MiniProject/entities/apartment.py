# Importujemy klasę bazową PropertyBase
from .property_base import PropertyBase

# Definiujemy klasę Apartment, która dziedziczy po klasie abstrakcyjnej PropertyBase
class Apartment(PropertyBase):
    # Konstruktor przyjmujący cenę i liczbę pokoi
    def __init__(self, price, rooms_count):
        # Ustawiamy prywatną zmienną _price
        self._price = price
        # Ustawiamy publiczną zmienną rooms_count
        self.rooms_count = rooms_count

    # Definiujemy setter dla prywatnej zmiennej _price
    def set_price(self, new_price):
        # Ustawiamy nową wartość _price
        self._price = new_price

    # Definiujemy getter dla prywatnej zmiennej _price
    def get_price(self):
        # Zwracamy aktualną wartość _price
        return self._price

    # Implementacja metody abstrakcyjnej get_description
    def get_description(self):
        # Zwracamy opis mieszkania po polsku, uwzględniając cenę i liczbę pokoi
        return f"Mieszkanie: liczba pokoi = {self.rooms_count}, cena = {self._price} PLN"
