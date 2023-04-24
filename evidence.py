

from pojistenec import Pojistenec

class Evidence:
    def __init__(self):
        pass

    def pridat(self):
        print("Zadejte pojištěnce")
        jmeno = input("Zadejte jméno:")
        prijmeni = input("Zadejte přijmění:")
        vek = input("Zadejte věk:")
        tel_cislo = input("Zadejte telefonní číslo:")
        novy_pojistenec = Pojistenec(jmeno, prijmeni, vek, tel_cislo)
        return novy_pojistenec

    def vypsat(self,pojistenci):
        print("\nVýpis všech pojištěnců:")
        for i in pojistenci:
            print(i)

    def vyhledat(self,pojistenci):
        print("\nVyhledávání všech pojištěnců:")
        hledane_jmeno = input("Zadejte jméno:")
        hledane_prijmeni = input("Zadejte přijmení:")
        for i in pojistenci:
            if (hledane_jmeno == i.jmeno) and (hledane_prijmeni == i.prijmeni):
                print(i)
            else:
                print("Pojištěnec nebyl nalezen.")