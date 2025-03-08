# Definiujemy klasę bazową (superklasę)
class Animal:
    # Konstruktor przypisujący imię zwierzęcia
    def __init__(self, name):
        self.name = name

    # Przykładowa metoda zwracająca informację o zwierzęciu
    def info(self):
        return f"Nazywam się {self.name} i jestem zwierzęciem."

# Definiujemy klasę Cat dziedziczącą po klasie Animal
class Cat(Animal):  
    # Konstruktor przyjmuje imię kota i wywołuje konstruktor klasy bazowej
    def __init__(self, name):
        # Wywołujemy konstruktor klasy Animal, aby zainicjalizować name
        super().__init__(name)
    
    # Dodajemy nową metodę, specyficzną dla klasy Cat
    def make_sound(self):
        return "Miau!"
    
    # Możemy również nadpisać metodę info, jeśli chcemy zmienić jej zachowanie
    def info(self):
        # Korzystamy z metody bazowej i dodajemy coś od siebie
        bazowa_info = super().info()
        return bazowa_info + " Jestem kotem i lubię mruczeć."

# Tworzymy obiekt klasy Cat
my_cat = Cat("Mruczek")

# Wywołujemy metodę info odziedziczoną i nadpisaną w klasie Cat
print(my_cat.info())  
# Wywołujemy metodę specyficzną dla Cat
print(my_cat.make_sound())  
