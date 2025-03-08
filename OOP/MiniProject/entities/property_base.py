# Importujemy moduły do tworzenia klas abstrakcyjnych
from abc import ABC, abstractmethod

# Definiujemy klasę abstrakcyjną PropertyBase
class PropertyBase(ABC):
    # Definiujemy metodę abstrakcyjną, którą muszą zaimplementować klasy dziedziczące
    @abstractmethod
    def get_description(self):
        # Metoda abstrakcyjna nie ma implementacji
        pass
