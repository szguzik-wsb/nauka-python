# Definiujemy klasę Person, która reprezentuje osobę
class Person:
    # Konstruktor przyjmuje imię i nazwisko
    def __init__(self, first_name, last_name):
        # Ustawiamy imię
        self.first_name = first_name
        # Ustawiamy nazwisko
        self.last_name = last_name

    # Metoda zwracająca pełne informacje o osobie
    def get_full_info(self):
        # Zwracamy opis osoby po polsku z imieniem i nazwiskiem
        return f"Nazywam się {self.first_name} {self.last_name}."
