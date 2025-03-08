# Definiujemy klasę o nazwie MyClass
class MyClass:
    # Zmienna klasowa (atrybut klasy), wspólna dla wszystkich instancji
    class_variable = 0
    
    # Konstruktor, wywoływany przy tworzeniu obiektu
    def __init__(self, name):
        # Atrybut instancji przypisany do konkretnego obiektu
        self.name = name

    # Metoda pozwalająca zwiększyć class_variable
    def increment_class_variable(self):
        # Zmieniamy wartość zmiennej klasowej
        MyClass.class_variable += 1


# Tworzymy dwie instancje klasy
obj1 = MyClass("Obiekt1")
obj2 = MyClass("Obiekt2")

# Początkowo class_variable ma wartość 0
print("Początkowa wartość class_variable:", MyClass.class_variable)

# Zwiększamy class_variable wywołując metodę na pierwszym obiekcie
obj1.increment_class_variable()
print("class_variable po increment_class_variable na obj1:", MyClass.class_variable)

# Wartość class_variable zmieniła się również dla drugiej instancji
obj2.increment_class_variable()
print("class_variable po increment_class_variable na obj2:", MyClass.class_variable)
