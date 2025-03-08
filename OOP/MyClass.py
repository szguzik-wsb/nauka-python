# Definicja nowej klasy o nazwie MyClass
class MyClass:
    # Konstruktor klasy, wywoływany podczas tworzenia instancji
    def __init__(self, name):
        # Inicjalizacja atrybutu / właściwości 'name' dla danej instancji
        self.name = name    

    # Przykładowa metoda instancji        
    def greet(self):
        # Metoda wypisuje tekst powitalny, używając atrybutu 'name'
        return f"Cześć, jestem {self.name}!"
    
# Służy do sprawdzania, czy dany plik jest uruchamiany bezpośrednio, 
# czy też importowany jako moduł w innym skrypcie.
if __name__ == "__main__":
    # Tworzymy instancję klasy MyClass z parametrem "Jan"
    obj = MyClass("Jan")
    # Wywołujemy metodę greet i wypisujemy jej wynik
    print(obj.greet())    
