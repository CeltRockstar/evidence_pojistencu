
from evidence import Evidence

evidence = Evidence()

seznam_pojistencu = []     #založí seznam do kterého se ukládají pojištěnci

pokracovat = True         #cyklus se opakuje dokud nenastane volba akce Konec

while pokracovat:
    print("\n")
    print(">>>>Evidence pojištěnců<<<<\n")
    print("1 - Nový pojištěnec")
    print("2 - Výpis všech pojištěnců")
    print("3 - Vyhledat pojištěnce")
    print("4 - Konec\n")
    akce = int(input("Zvol akci a stiskni ENTER: "))

    if akce == 1:
        novy_pojistenec = evidence.pridat()
        seznam_pojistencu.append(novy_pojistenec)
        print("Nový pojištěnec byl vložen do databáze. Pokračujte stisknutím ENTER...")
        input()
    elif akce == 2:
        evidence.vypsat(seznam_pojistencu)
        print("Pro návrat do menu stiskněte ENTER...")
        input()
    elif akce == 3:
        evidence.vyhledat(seznam_pojistencu)
        print("Pro návrat do menu stiskněte ENTER...")
        input()
    elif akce == 4:
        pokracovat = False
        print("Děkujeme za použití evidence pojištěnců.")
    else:
        print("Neplatné zadání.")
        pokracovat = True
