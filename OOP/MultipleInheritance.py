# Definiujemy klasę School, która przechowuje informację o nazwie szkoły
class School:
    # Konstruktor przyjmuje nazwę szkoły
    def __init__(self, school_name):
        # Ustawiamy atrybut instancji z nazwą szkoły
        self.school_name = school_name

    # Metoda zwracająca informacje o szkole
    def school_info(self):
        # Zwracamy napis z nazwą szkoły
        return f"I attend the school: {self.school_name}"


# Definiujemy klasę Person, która przechowuje informację o imieniu i wieku osoby
class Person:
    # Konstruktor przyjmuje imię i wiek osoby
    def __init__(self, name, age):
        # Ustawiamy atrybuty instancji: imię i wiek
        self.name = name
        self.age = age

    # Metoda zwracająca informacje o osobie
    def person_info(self):
        # Zwracamy napis z imieniem i wiekiem
        return f"My name is {self.name}, I am {self.age} years old."
    
    def school_info(self):
        # Zwracamy napis z nazwą szkoły
        return f"I attend the school: {self.school_name}"


# Definiujemy klasę Student, która dziedziczy po klasach School i Person (wielokrotne dziedziczenie)
class Student(School, Person):
    # Konstruktor przyjmuje nazwę szkoły, imię, wiek i poziom klasy (np. "6B")
    def __init__(self, school_name, name, age, class_level):
        # Wywołujemy konstruktor klasy School
        School.__init__(self, school_name)
        # Wywołujemy konstruktor klasy Person
        Person.__init__(self, name, age)

        # Ustawiamy atrybut instancji z poziomem klasy ucznia
        self.class_level = class_level

    # Metoda zwracająca połączone informacje o uczniu
    def student_info(self):
        # Łączymy informacje z klasy Person, School i dodajemy poziom klasy ucznia
        return f"{self.person_info()} {self.school_info()} and I am in class {self.class_level}."


# Przykładowe użycie:
# Tworzymy obiekt klasy Student, podając nazwę szkoły, imię, wiek i poziom klasy
student = Student("Elementary School No. 5", "Anna", 12, "6B")

# Wywołujemy metodę student_info, aby zobaczyć połączone informacje
print(student.student_info())
# print(student.school_info())
# Przykładowy wynik:
# "My name is Anna, I am 12 years old. I attend the school: Elementary School No. 5 and I am in class 6B."
