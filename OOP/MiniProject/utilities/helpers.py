# Importujemy stałą VAT_RATE
from .constants import VAT_RATE

# Definiujemy klasę VatMixin, która może być stosowana jako dodatek do innych klas
class VatMixin:
    # Metoda zwracająca informację z uwzględnieniem VAT
    def get_full_info(self):
        # Zwracamy informację po polsku, uwzględniając, że klasa bazowa mogłaby tu coś dodać
        return f"Informacje z VAT: obecna stawka VAT to {VAT_RATE * 100}%."
