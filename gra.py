import random
import time
import statki as s
from statki import postac
import sklep as y
import wrogowie as p
import menu as i
import wirus as w

kredyty = 0
MAXHP = 200
EXP = 0
LVL = [0, 50]
Ekwipunek = [0, 0]

# Moduly ze statystykami z wrogow
PA = 1
PF = 1
PK = 1
PL = 1
PKa = 1

# Zmienne sklepowe
laser = 20
ulepszony_laser = 20
dzialo = 40
miotacz = 1500
pancerz_weglowy = 10
pancerz_tytanowy = 10

print("--- KOSMICZNA ODDYSEJA 3000 ---")
time.sleep(0.5)
i.zasady_gry()

print("\nWybierz swoj statek:")
time.sleep(0.5)
print("Lekki Mysliwiec  - a")
time.sleep(0.5)
print("Ciezki Krazownik  - b")
time.sleep(0.5)
print("Statek Szturmowy - c")
time.sleep(0.5)
print("Prototyp X-99  - d")
time.sleep(0.5)

inp = input("> ")

if inp == "a":
    s.lekki_mysliwiec()
elif inp == "b":
    s.ciezki_krazownik()
elif inp == "c":
    s.statek_szturmowy()
elif inp == "d":
    s.prototyp()
else:
    print("Zla opcja, domyslnie przydzielono Lekki Mysliwiec.")
    time.sleep(0.5)
    s.lekki_mysliwiec()

while postac[0] > 0:
    i.pokaz_menu_glowne(postac, MAXHP, LVL, kredyty)
    potwor = p.losuj_wroga()
    boss = p.losuj_bossa()
    inp = input("> ")
    
    if inp == "a":
        print(f"\nSkanery wykryly: {potwor[0]}! Ma {potwor[1]} HP i {potwor[2]} sily ostrzalu.")
        time.sleep(0.5)
        print("\nOtworz ogien! - a")
        time.sleep(0.5)
        print("Wymijaj! (Ucieczka) - b")
        time.sleep(0.5)
        inp = input("> ")

        if inp == "a":
            print(f"\n--- WALKA Z {potwor[0].upper()} ---")
            time.sleep(0.5)
            while potwor[1] > 0 and postac[0] > 0:
                time.sleep(0.5)
                print(f"Twoj Kadlub: {postac[0]}")
                time.sleep(0.5)
                print(f"HP wroga ({potwor[0]}): {potwor[1]}")
                time.sleep(0.5)
                postac[0] -= potwor[2]
                potwor[1] -= postac[1]
                time.sleep(0.5)

            if potwor[1] <= 0 and postac[0] > 0:
                zdobyte = random.randint(10, 100)
                zdobyt = random.randint(2, 10)
                kredyty += zdobyte
                LVL[0] += zdobyt
                if LVL[0] >= LVL[1]:
                    EXP += 1
                    LVL[0] -= LVL[1]
                    LVL[1] += 5
                print(f"\nZniszczyles {potwor[0]}! Zdobywasz {zdobyte} kredytow i {zdobyt} expa")
                time.sleep(0.5)

                if potwor[0] == "Kosmiczny Pirat":
                    l = random.randint(1,100)
                    if l <= 10 and PA > 0:
                        print("Znalazles porzucony Modul Ataku. +20 do Ataku")
                        time.sleep(0.5)
                        postac[1] += 20
                        PA -= 1
                        time.sleep(0.5)
                    elif l >=99 and PF > 0:
                        print("Znalazles Rdzen Antymaterii. +100 do Ataku")
                        time.sleep(0.5)
                        postac[1] += 100
                        PF -= 1
                        time.sleep(0.5)
                elif potwor[0] == "Pradawny Straznik Sektora":
                    g = random.randint(1,100)
                    if g == 100:
                        if PK > 0:
                            print("Wydobyto Rdzen Nieskonczonosci. +100 do MAX KADLUBA")
                            time.sleep(0.5)
                            MAXHP += 100
                            PK -= 1
                            time.sleep(0.5)

                print(f"Masz teraz {kredyty} kredytow.")
                time.sleep(0.5)
                print(f"Poziom (LVL): {EXP}")
                time.sleep(0.5)
            elif postac[0] <= 0:
                print("\nTwoj statek zostal zniszczony...")
                time.sleep(0.5)
                break

        elif inp == "b":
            print("Inicjacja manewru wymijajacego...")
            time.sleep(0.5)
            if random.randint(0, 1) == 1:
                print("Udalo ci sie zgubic poscig!")
                time.sleep(0.5)
            else:
                print(f"Manewr nieudany! {potwor[0]} trafia ciebie w silniki!")
                time.sleep(0.5)
                postac[0] -= potwor[2]
                print(f"{potwor[0]} zadaje ci {potwor[2]} obrazen!")
                time.sleep(0.5)

    elif inp == "b":
        (postac, kredyty, MAXHP,
        laser, ulepszony_laser,
        dzialo, miotacz,
        pancerz_weglowy, pancerz_tytanowy, Ekwipunek) = y.obsluga(
            postac, kredyty, MAXHP,
            laser, ulepszony_laser,
            dzialo, miotacz,
            pancerz_weglowy, pancerz_tytanowy, Ekwipunek
        )

    elif inp == "c":
        if EXP < 20:
            print("Musisz miec 20 LVL aby skoczyc do sektora Bossa.")
            time.sleep(0.5)
        else:
            while boss[1] > 0 and postac[0] > 0:
                print(f"Twoj Kadlub: {postac[0]}/{MAXHP}  HP Bossa: {boss[1]}")
                time.sleep(0.5)
                print(f"Ladownia: Zestawy:{Ekwipunek[0]} Duze Zestawy:{Ekwipunek[1]}")
                time.sleep(0.5)
                print("\nPelny Ostrzal - a")
                time.sleep(0.5)
                print("Otworz Ladownie (Ulecz) - e")
                time.sleep(0.5)
                inp = input("> ")
                
                if inp == "a":
                        print(f"\n--- TRWA BITWA Z {boss[0]} ---")
                        time.sleep(0.5)
                        while boss[1] > 0 and postac[0] > 0:
                            time.sleep(0.5)
                            print(f"Twoj Kadlub: {postac[0]}")
                            time.sleep(0.5)
                            print(f"HP Bossa: {boss[1]}")
                            time.sleep(0.5)
                            postac[0] -= boss[2]
                            boss[1] -= postac[1]
                            time.sleep(0.5)
                        
                        if boss[1] <= 0 and postac[0] > 0:
                                zdoby = random.randint(100, 1000)
                                zdob = random.randint(20, 100)
                                kredyty += zdoby
                                LVL[0] += zdob
                                if LVL[0] >= LVL[1]:
                                    EXP += 1
                                    LVL[0] -= LVL[1]
                                    LVL[1] += 5
                                print(f"\nZniszczyles {boss[0]}! Sektor czysty. Zbierasz {zdoby} kredytow.")
                                time.sleep(0.5)
                                
                                if boss[0] == "Gwiezdny Niszczyciel":
                                    k = random.randint(1,100)
                                    if k <= 10 and PL > 0:
                                        print("Znalazles Zloty Modul. +200 do Ataku")
                                        time.sleep(0.5)
                                        postac[1] += 200
                                        PL -= 1
                                    elif k >=99 and PKa > 0:
                                        print("Znalazles Rdzen Supernowej! +1000 do Ataku")
                                        time.sleep(0.5)
                                        postac[1] += 1000
                                        PKa -= 1
                                elif boss[0] == "Okret Matka Obcych":
                                    time.sleep(0.5)
                                    print("--- GRATULACJE WYGRALES!!! ---")
                                    time.sleep(0.5)
                                    print("Gre tworzyli:")
                                    time.sleep(0.5)
                                    print("Kod: Kapitan")
                                    time.sleep(0.5)
                                    print("Projekt misji: Kapitan")
                                    time.sleep(0.5)
                                    print("Silnik fizyczny: Brak")
                                    time.sleep(0.5)
                                    print("Rezyser: Kapitan")
                                    time.sleep(0.5)
                                    print("Budzet: 0 Kredytow")
                                    time.sleep(0.5)
                                    print("Dziekujemy za zagranie w nasza gre sci-fi!")
                                    time.sleep(0.5)
                elif inp == "e":
                    print("Zestaw naprawczy - a")
                    time.sleep(0.5)
                    print("Duzy zestaw naprawczy - b")
                    time.sleep(0.5)
                    inp = input("> ")
                    if inp == "a" and Ekwipunek[0] > 0:
                        Ekwipunek[0] -= 1
                        postac[0] += 40
                        postac[0] = min(postac[0], MAXHP)
                        print("Uzyto zestawu naprawczego! +40 HP")
                        time.sleep(0.5)
                    elif inp == "b" and Ekwipunek[1] > 0:
                        Ekwipunek[1] -= 1
                        postac[0] += 80
                        postac[0] = min(postac[0], MAXHP)
                        print("Uzyto duzego zestawu naprawczego! +80 HP")
                        time.sleep(0.5)
                    else:
                        print("Brak zestawow lub zla opcja!")
                        time.sleep(0.5)
    
    elif inp == "TajnyKod":
        print("Wlaczanie tajnego protokolu...")
        w.fake_hack()
