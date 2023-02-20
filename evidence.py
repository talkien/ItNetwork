from pojistenec import Pojistenec

class EvidencePojistenych: #třída reprezentující evidenci pojištěných
    def __init__(self): #Konstruktor vytváří seznam pojištěných"
        self.seznam_pojistencu = []

    def pridej_pojistence(self, jmeno=None, prijmeni=None, vek=None, telefon=None): #Metoda přidá novou pojištěnou osobu
        while True:
            if not jmeno:
                jmeno = input("Zadejte jmeno: ")
                if not jmeno.isalpha():
                    print("\nProsím zadejte platné jméno\n")
                    jmeno = None
                    continue
                elif len(jmeno) > 150:
                    print("\nZadané jméno je příliš dlouhé\n")
                    jmeno = None
                    continue
            if not prijmeni:
                prijmeni = input("Zadejte příjmení: ")
                if not prijmeni.isalpha():
                    print("\nProsím zadejte platné příjmení\n")
                    prijmeni = None
                    continue
                elif len(prijmeni) > 150:
                    print("\nZadané příjmení je příliš dlouhé\n")
                    prijmeni = None
                    continue
            if not vek:
                while True:
                    try:
                        vek = int(input("Zadejte vek: "))
                        if vek > 199:
                            print("Zadaný věk je příliš vysoký\n")
                            vek = None
                            continue
                        break
                    except ValueError:
                        print("Prosím zadajte platný věk\n")
            if not telefon:
                while True:
                    telefon = input("Zadejte telefonní číslo: ")
                    if telefon.isnumeric() and len(telefon)==9:
                        break
                    else:
                        print("\nProsím zadejte platné telefonní číslo\n")
            break
        self.seznam_pojistencu.append(Pojistenec(jmeno, prijmeni, vek, telefon))
        print("\nNová osoba přidána")
        

    def vypis_pojistence(self): #Vypíše všechny uložené pojištěné osoby
        for i, pojistenec in enumerate(self.seznam_pojistencu):
            print(f"\n{i+1}. {pojistenec}")
            

    def vyhledej_pojistence(self, jmeno=None, prijmeni=None): #Vyhledá uloženou pojištěnou osobu podle jména a/nebo příjmení
        vyhledani_pojistenci = []
        for osoba in self.seznam_pojistencu:
            if jmeno and prijmeni:
                if jmeno.lower() == osoba.jmeno.lower() and prijmeni.lower() == osoba.prijmeni.lower():
                    vyhledani_pojistenci.append(osoba)
            elif jmeno and jmeno.lower() == osoba.jmeno.lower():
                vyhledani_pojistenci.append(osoba)
            elif prijmeni and prijmeni.lower() == osoba.prijmeni.lower():
                vyhledani_pojistenci.append(osoba)
        if vyhledani_pojistenci:
            for i, osoba in enumerate(vyhledani_pojistenci):
                print(f"{i+1}. {osoba}")
                
        else:
            print("\nOsoba nenalezena")
            

    def run(self):
        while True:
            print("--------------------")
            print("Evidence pojištěných")
            print("--------------------")
            print("1. Přidej novou osobu")
            print("2. Vypiš všechny osoby")
            print("3. Vyhledej osobu")
            print("4. Konec")

            choice = input("Zvolte možnost 1-4: ")

            if choice == "1":
                self.pridej_pojistence()
                input("Stiskněte libovolnou klávesu pro pokračování...")
            elif choice == "2":
                self.vypis_pojistence()
                input("Stiskněte libovolnou klávesu pro pokračování...")
            elif choice == "3":
                jmeno = input("Zadejte jméno: ")
                prijmeni = input("Zadejte příjmení: ")
                self.vyhledej_pojistence(jmeno, prijmeni)
                input("Stiskněte libovolnou klávesu pro pokračování...")
            elif choice == "4":
                break
            else:
                print("\nChybná volba. Zvolte číslo od 1 do 4.")

