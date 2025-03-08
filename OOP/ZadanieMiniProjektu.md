Opis zadania: 
Zadanie dotyczy stworzenia aplikacji do obsługi biura nieruchomości, w którym: 
1. Mamy różne **namespace'y** (czyli pakiety), 
które reprezentują różne części organizacyjne biura nieruchomości. 
2. Musimy używać **wielokrotnego dziedziczenia** wśród klas. 
3. Stosujemy **zmienne prywatne**, **publiczne** oraz **stałe**. 
4. Klasy mają **settery** i **gettery**. 
5. Wszystkie klasy, metody etc., będą nazwane zgodnie z wytycznymi - w **angielskim** jézyku i **snake_case**. 
6. Będą klasy abstrakcyjne, które będą stanowiły szablon do implementacji innych klas. 
7. W kontekście **wielokrotnego dziedziczenia** użyjemy 

**MRO (Method Resolution Order)**, żeby wywołana została ta sama metoda, która występuje w klasie nadrzędnej. 
### Strukturę projektu podzielimy na trzy **namespace'y (pakiety)**: 
1. **person** - klasy związane z osobami pracującymi w biurze nieruchomości. 
2. **property** - klasy związane z nieruchomościami. 
3. **real_estate** - główne klasy związane z obsługą biura nieruchomości.

Każdy z **namespace'ów** będzie zawierał co najmniej jedną klasę i dostępne w niej zmienne oraz metody.
 ### Zadanie: - **`Person`**: Będzie zawierał dane pracownika (imię, nazwisko), a także metodę do obliczania rabatu dla klientów. 
 - **`Property`**: Będzie zawierała informacje o nieruchomości (adres, powierzchnia), 
 a także metodę do wyliczania ceny nieruchomości na podstawie ceny za metr kwadratowy. 
 - **`RealEstateAgent`**: Dziedziczy po klasach `Person` oraz `Property` (wielokrotne dziedziczenie). 
 Będzie zawierał dodatkową metodę do wyliczania prowizji oraz informacje o tym, czy agent jest pracownikiem danej firmy. 
 ### Klasy: 1. **Person** - klasa abstrakcyjna, z metodą `calculate_discount` (oblicz rabat pracownika). 2. **Property** - klasa abstrakcyjna, zawierająca metodę `calculate_price` (oblicz cenę nieruchomości). 3. **RealEstateAgent** - zwykła klasa, która dziedziczy po `Person` i `Property`, implementując wszystkie wymagane metody. Każda klasa będzie miała zmienne publiczne i prywatne, a także settery, gettery i stałe. Za pomocą `MRO` będziemy wywoływać metody z superklas, nawet jeśli nazwy tych metod są takie same. Zaczynamy od struktury katalogów i plików: ``` real_estate/ └── person/ │ ├── __init__.py │ └── person.py ├── property/ │ ├── __init__.py │ └── property.py └── real_estate_agent.py ``` **Teraz przygotuję odpowiednią implementację z opisem.** przez 13 sekund(y)
Opis wymyślonego zadania spełniającego wszystkie warunki:

Mamy do czynienia z biurem nieruchomości. Chcemy odwzorować prosty model obiektowy, w którym występują różne klasy związane z nieruchomościami, osobami oraz dodatkowymi funkcjonalnościami. Kod podzielimy na trzy pakiety (namespace’y):

 - entities – zawierający klasy związane z nieruchomościami (np. bazową klasę abstrakcyjną PropertyBase, od której dziedziczyć będą Apartment i Office).
 - persons – zawierający klasy związane z osobami (np. Person i Owner).
 - utilities – zawierający stałe i różne mixiny/funkcje pomocnicze (np. VatMixin oraz stałe w constants).

W tym modelu:

- Klasa abstrakcyjna PropertyBase (w entities/property_base.py) będzie definiowała interfejs dla różnych typów nieruchomości (abstrakcyjna metoda get_description).
- Klasa Apartment (w entities/apartment.py) będzie dziedziczyć po PropertyBase. Będzie posiadać prywatną zmienną _price, publiczną zmienną rooms_count, seter i geter dla _price, oraz zdefiniowaną metodę get_description zwracającą informacje o nieruchomości (po polsku w f-stringu).
- Klasa Office (w entities/office.py) również będzie dziedziczyć po PropertyBase i będzie posiadać np. informację o powierzchni biura, zwracając opis w metodzie get_description.

W pakiecie persons:

- Klasa Person (w persons/person.py) będzie zwykłą klasą z informacjami o imieniu i nazwisku oraz metodą get_full_info() (metoda zwróci opis osoby).
- Klasa Owner (w persons/owner.py) będzie dziedziczyć po Person i dodatkowo doda informacje, że jest właścicielem nieruchomości (np. przechowa listę nieruchomości).

W pakiecie utilities:

- Plik utilities/constants.py będzie zawierał stałą VAT_RATE.
- Plik utilities/helpers.py będzie zawierał klasę VatMixin z metodą get_full_info().
Następnie wprowadzimy wielokrotne dziedziczenie. Na przykład utworzymy klasę OfficeEmployee w pliku persons/owner.py (lub w osobnym pliku persons/office_employee.py – wybór jest dowolny, zrobimy w owner.py dla uproszczenia), która dziedziczy zarówno po Person, jak i po VatMixin. Obie te klasy (Person oraz VatMixin) będą miały metodę get_full_info(). Dzięki temu zobaczymy działanie MRO – czyli Python zdecyduje, którą metodę get_full_info() wywołać na podstawie kolejności dziedziczenia.

W main.py (poza tymi trzema pakietami) zaimportujemy wszystkie potrzebne klasy, utworzymy obiekty i pokażemy:

- Wykorzystanie wielodziedziczenia (OfficeEmployee dziedziczy po Person i VatMixin).
- Wywołanie metody z łańcucha MRO (będą dwie metody get_full_info() w superklasach, Python wywoła tę, która jest wcześniej w MRO).
- Wykorzystanie klas abstrakcyjnych (PropertyBase), zwykłych klas (Apartment, Office, Person), stałych (VAT_RATE), prywatnych zmiennych (_price w Apartment), setterów i getterów.
- Wypiszemy informacje po polsku za pomocą f-stringów, a nazwy klas, metod i zmiennych pozostaną w angielskim stylu snake_case dla metod i zmiennych oraz PascalCase dla klas.
- Komentarze do każdej linii kodu będą po polsku.