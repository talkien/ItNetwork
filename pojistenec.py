class Pojistenec: #Třída reprezentuje pojistěnou osobu"
    def __init__(self, jmeno, prijmeni, vek, telefon):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.telefon = telefon

    def __str__(self): #textová reprezentace
        return f"Jméno: {self.jmeno}, Příjmení: {self.prijmeni}, Věk: {self.vek}, Telefonní číslo: {self.telefon}"
