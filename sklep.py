def obsluga(postac, kredyty, MAXHP,
          laser, ulepszony_laser,
          dzialo, miotacz,
          pancerz_weglowy, pancerz_tytanowy, ekwipunek):

    print("\n--- HANDLARZ Z CZARNEGO RYNKU ---")
    print("Laser bojowy 50 kredytow - a")
    print("Ulepszony laser bojowy 100 kredytow - b")
    print("Dzialo plazmowe 250 kredytow - c")
    print("Miotacz antymaterii 1500 kredytow - d")
    print("Zestaw naprawczy 30 kredytow - e")
    print("Duzy zestaw naprawczy 60 kredytow - f")
    print("Wzmocnienie weglowe 200 kredytow - g")
    print("Tarcza tytanowa 1500 kredytow - h")
    print(f"Twoje kredyty = {kredyty}")
    inp = input("> ")

    if inp == "a":
        if laser == 0:
            print("\nKupiles juz te bron!")
        elif kredyty >= 50:
            postac[1] += laser
            kredyty -= 50
            laser = 0
            print("Kupiono Laser bojowy. Atak +20")
        else:
            print("\nNie masz wystarczajaco kredytow!")

    elif inp == "b":
        if ulepszony_laser == 0:
            print("\nKupiles juz te bron!")
        elif kredyty >= 100:
            postac[1] += ulepszony_laser
            kredyty -= 100
            ulepszony_laser = 0
            print("Kupiono Ulepszony laser. Atak +20")
        else:
            print("\nNie masz wystarczajaco kredytow!")

    elif inp == "c":
        if dzialo == 0:
            print("\nKupiles juz te bron!")
        elif kredyty >= 250:
            postac[1] += dzialo
            kredyty -= 250
            dzialo = 0
            print("Kupiono Dzialo plazmowe. Atak +40")
        else:
            print("\nNie masz wystarczajaco kredytow!")

    elif inp == "d":
        if miotacz == 0:
            print("\nKupiles juz te bron!")
        elif kredyty >= 1500:
            postac[1] += miotacz
            kredyty -= 1500
            miotacz = 0
            print("Kupiono Miotacz antymaterii. Atak +1500")
        else:
            print("\nNie masz wystarczajaco kredytow!")

    elif inp == "e":
        if kredyty >= 30:
            kredyty -= 30
            print("Dodac do ladowni - a")
            print("Uzyc - b")
            x = input("> ")
            if x == "a":
                ekwipunek[0] += 1
                print("Zestaw naprawczy dodany do ladowni")
            elif x == "b":
                postac[0] = min(postac[0] + 40, MAXHP)
                print(f"Uzyto zestawu! Masz teraz {postac[0]} Kadluba")
        else:
            print("\nNie masz wystarczajaco kredytow!")

    elif inp == "f":
        if kredyty >= 60:
            kredyty -= 60
            print("Dodac do ladowni - a")
            print("Uzyc - b")
            x = input("> ")
            if x == "a":
                ekwipunek[1] += 1
                print("Duzy zestaw naprawczy dodany do ladowni")
            elif x == "b":
                postac[0] = min(postac[0] + 80, MAXHP)
                print(f"Uzyto duzego zestawu! Masz teraz {postac[0]} Kadluba")
        else:
            print("\nNie masz wystarczajaco kredytow!")

    elif inp == "g":
        if pancerz_weglowy == 0:
            print("\nKupiles juz to ulepszenie!")
        elif kredyty >= 200:
            MAXHP += 200
            kredyty -= 200
            pancerz_weglowy = 0
            print("Kupiono Wzmocnienie weglowe! MAX Kadlub +200")
        else:
            print("\nNie masz wystarczajaco kredytow!")

    elif inp == "h":
        if pancerz_tytanowy == 0:
            print("\nKupiles juz to ulepszenie!")
        elif kredyty >= 1500:
            MAXHP += 800
            kredyty -= 1500
            pancerz_tytanowy = 0
            print("Kupiono Tarcze tytanowa! MAX Kadlub +800")
        else:
            print("\nNie masz wystarczajaco kredytow!")

    else:
        print("\nNieznana opcja!")

    return (postac, kredyty, MAXHP,
            laser, ulepszony_laser,
            dzialo, miotacz,
            pancerz_weglowy, pancerz_tytanowy, ekwipunek)
