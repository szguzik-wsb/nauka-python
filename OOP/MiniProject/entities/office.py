# Importujemy klasę bazową PropertyBase
from .property_base import PropertyBase

# Definiujemy klasę Office, która dziedziczy po PropertyBase
class Office(PropertyBase):
    # Konstruktor przyjmuje powierzchnię biura (m2)
    def __init__(self, area):
        # Ustawiamy publiczny atrybut area
        self.area = area

    # Implementacja metody abstrakcyjnej get_description
    def get_description(self):
        # Zwracamy opis biura po polsku, uwzględniając powierzchnię
        return f"Biuro: powierzchnia = {self.area} m2"
