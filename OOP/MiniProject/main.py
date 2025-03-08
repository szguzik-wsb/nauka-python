# Importujemy klasy z poszczególnych pakietów
from entities.apartment import Apartment
from entities.office import Office
from persons.owner import Owner, OfficeEmployee

# Komentarze do każdej linii po polsku:

# Tworzymy obiekt Apartment z ceną i liczbą pokoi
apartment = Apartment(price=300000, rooms_count=3)
# Tworzymy obiekt Office z powierzchnią
office = Office(area=120)

# Tworzymy listę nieruchomości, których właścicielem jest dana osoba
properties = [apartment, office]

# Tworzymy obiekt Owner, przekazując imię, nazwisko oraz listę nieruchomości
owner = Owner(first_name="Jan", last_name="Kowalski", properties_list=properties)

# Wywołujemy metodę get_owner_info, aby sprawdzić opis właściciela i jego nieruchomości
print(owner.get_owner_info())
# Przykładowy wynik:
# "Nazywam się Jan Kowalski. Jestem właścicielem następujących nieruchomości: Mieszkanie: liczba pokoi = 3, cena = 300000 PLN, Biuro: powierzchnia = 120 m2"

# Tworzymy pracownika biura (OfficeEmployee) dziedziczącego po Person i VatMixin
employee = OfficeEmployee(first_name="Anna", last_name="Nowak")

# Wywołujemy show_mro_method_result, aby zobaczyć, którą metodę get_full_info() wybierze MRO
print(employee.show_mro_method_result())
# Oczekiwany wynik:
# "Nazywam się Anna Nowak."
# Zostanie użyta metoda get_full_info() z klasy Person, ponieważ jest pierwsza w MRO.
# Metoda z VatMixin o tej samej nazwie nie zostanie użyta w tym wypadku.

# Wyjaśnienie:
# MRO to kolejność przeszukiwania metod w klasach bazowych.
# W tym przypadku OfficeEmployee(Person, VatMixin) oznacza, że Python najpierw sprawdzi Person,
# a dopiero potem VatMixin. Ponieważ Person ma metodę get_full_info(), to tę metodę wywoła.
# Gdybyśmy zmienili kolejność dziedziczenia na OfficeEmployee(VatMixin, Person),
# wtedy pierwsza byłaby metoda z VatMixin.
