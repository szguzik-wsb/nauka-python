# Importujemy klasę Person z tego samego pakietu
from .person import Person
# Importujemy VatMixin z utilities.helpers do wielokrotnego dziedziczenia
from utilities.helpers import VatMixin

# Definiujemy klasę Owner, która dziedziczy po Person
class Owner(Person):
    # Konstruktor przyjmuje imię, nazwisko i listę nieruchomości
    def __init__(self, first_name, last_name, properties_list):
        # Wywołujemy konstruktor klasy bazowej Person
        super().__init__(first_name, last_name)
        # Ustawiamy listę nieruchomości (jako publiczny atrybut)
        self.properties_list = properties_list

    # Metoda zwracająca informacje o właścicielu i jego nieruchomościach
    def get_owner_info(self):
        # Tworzymy opis z wykorzystaniem metody odziedziczonej get_full_info() z Person
        base_info = self.get_full_info()
        # Dodajemy informacje o nieruchomościach (iterujemy po liście)
        props_info = ", ".join([p.get_description() for p in self.properties_list])
        # Zwracamy pełną informację po polsku
        return f"{base_info} Jestem właścicielem następujących nieruchomości: {props_info}"


# Definiujemy klasę OfficeEmployee, która dziedziczy po Person i VatMixin (wielokrotne dziedziczenie)
# Zauważmy, że zarówno Person jak i VatMixin mają metodę get_full_info().
# Dzięki kolejności dziedziczenia (OfficeEmployee(Person, VatMixin)) i MRO, wywołana zostanie najpierw metoda z Person.
class OfficeEmployee(Person, VatMixin):
    # Konstruktor przyjmuje imię i nazwisko pracownika biura
    def __init__(self, first_name, last_name):
        # Wywołujemy konstruktor Person
        super().__init__(first_name, last_name)
        # Nie dodajemy nic więcej, to tylko przykład wielokrotnego dziedziczenia

    # Metoda testująca MRO
    def show_mro_method_result(self):
        # Wywołujemy get_full_info(). Ponieważ w Person i VatMixin są metody o tej nazwie,
        # Python użyje MRO. W kolejności dziedziczenia jest Person, potem VatMixin,
        # więc najpierw sprawdzi Person i znajdzie tam metodę get_full_info() - ją wywoła.
        # Metoda z VatMixin zostanie pominięta przy pierwszym napotkaniu metody w Person.
        # W ten sposób demonstrujemy działanie MRO.
        return self.get_full_info()
