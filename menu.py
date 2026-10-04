import time

def pokaz_menu_glowne(postac, MAXHP, LVL, kredyty):
    print("\n-----------------------------------------")
    print("           STACJA KOSMICZNA")
    print("-----------------------------------------")
    print("Skanuj sektor (Walka ze zwyklym wrogiem) - a")
    time.sleep(0.5)
    print("Odwiedz handlarza (Sklep) - b")
    time.sleep(0.5)
    print("Skok w nadprzestrzen (Walka z BOSSEM - Wymaga 20 LVL) - c")
    time.sleep(0.5)
    print(f"Twoje kredyty = {kredyty}")
    time.sleep(0.5)
    print(f"LVL: {LVL[0]}/{LVL[1]}")
    time.sleep(0.5)
    print(f"KADLUB (HP): {postac[0]}/{MAXHP}")
    time.sleep(0.5)

def zasady_gry():
    print("\nZASADY GRY:")
    print("1. Wcielasz sie w kapitana statku kosmicznego.")
    print("2. Twoim celem jest przetrwanie w kosmosie i pokonanie")
    print("   glownego statku matki obcych (wymagany 20 LVL).")
    print("3. Na swojej drodze spotkasz rozne statki i drony.")
    print("4. W sklepie na stacji kosmicznej mozesz ulepszac bron.")
    print("5. Zawsze pilnuj punktow kadluba (HP).")
    time.sleep(2)
