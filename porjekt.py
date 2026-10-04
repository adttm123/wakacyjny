import json
import os

class Uzytkownik:
    def __init__(self, login, haslo, rola):
        self.login = login
        self.haslo = haslo
        self.rola = rola

    def to_dict(self):
        return {"login": self.login, "haslo": self.haslo, "rola": self.rola}

class Admin(Uzytkownik):
    def __init__(self, login, haslo):
        super().__init__(login, haslo, "admin")
        
    def zmien_dane_uzytkownika(self, uzytkownik, nowe_haslo, nowa_rola):
        uzytkownik.haslo = nowe_haslo
        uzytkownik.rola = nowa_rola

class Pracownik(Uzytkownik):
    def __init__(self, login, haslo, rola):
        super().__init__(login, haslo, rola)

class Produkt:
    def __init__(self, nazwa, ilosc, cena):
        self.nazwa = nazwa
        self.ilosc = ilosc
        self.cena = cena

    def to_dict(self):
        return {"nazwa": self.nazwa, "ilosc": self.ilosc, "cena": self.cena}

class Firma:
    def __init__(self, plik_danych):
        self.plik_danych = plik_danych
        self.uzytkownicy = []
        self.produkty = []
        self.finanse = 0.0
        self.wczytaj_dane()

    def wczytaj_dane(self):
        try:
            if not os.path.exists(self.plik_danych):
                self.generuj_dane_poczatkowe()
                
            with open(self.plik_danych, 'r', encoding='utf-8') as f:
                dane = json.load(f)
                
            self.finanse = float(dane.get("finanse", 0.0))
            
            self.uzytkownicy = []
            for u in dane.get("uzytkownicy", []):
                if u["rola"] == "admin":
                    self.uzytkownicy.append(Admin(u["login"], u["haslo"]))
                else:
                    self.uzytkownicy.append(Pracownik(u["login"], u["haslo"], u["rola"]))
                    
            self.produkty = []
            for p in dane.get("produkty", []):
                self.produkty.append(Produkt(p["nazwa"], p["ilosc"], p["cena"]))
                
        except json.JSONDecodeError:
            print("Blad odczytu pliku JSON. Tworzenie nowej bazy danych.")
            self.generuj_dane_poczatkowe()
        except Exception as e:
            print(f"Wystapil nieoczekiwany blad: {e}")

    def zapisz_dane(self):
        dane = {
            "finanse": self.finanse,
            "uzytkownicy": [u.to_dict() for u in self.uzytkownicy],
            "produkty": [p.to_dict() for p in self.produkty]
        }
        try:
            with open(self.plik_danych, 'w', encoding='utf-8') as f:
                json.dump(dane, f, indent=4)
        except Exception as e:
            print(f"Blad podczas zapisu danych: {e}")

    def generuj_dane_poczatkowe(self):
        self.finanse = 10000.0
        self.uzytkownicy = [
            Admin("admin", "admin123"),
            Pracownik("jan", "jan123", "sprzedawca"),
            Pracownik("anna", "anna123", "magazynier")
        ]
        self.produkty = [
            Produkt("Laptop", 5, 3000.0),
            Produkt("Myszka", 20, 100.0),
            Produkt("Klawiatura", 10, 200.0)
        ]
        self.zapisz_dane()

    def znajdz_uzytkownika(self, login, haslo):
        for u in self.uzytkownicy:
            if u.login == login and u.haslo == haslo:
                return u
        return None

    def generuj_raport(self):
        nazwa_pliku = "raport.txt"
        try:
            with open(nazwa_pliku, 'w', encoding='utf-8') as f:
                f.write("=== RAPORT FIRMOWY ===\n")
                f.write(f"Stan finansow: {self.finanse} PLN\n\n")
                
                f.write("--- Pracownicy ---\n")
                for u in self.uzytkownicy:
                    f.write(f"Login: {u.login} | Rola: {u.rola}\n")
                    
                f.write("\n--- Stan Magazynu ---\n")
                for p in self.produkty:
                    f.write(f"Produkt: {p.nazwa} | Ilosc: {p.ilosc} szt. | Cena jednostkowa: {p.cena} PLN\n")
                    
            print(f"Raport zostal pomyslnie wygenerowany do pliku {nazwa_pliku}")
        except Exception as e:
            print(f"Blad przy generowaniu raportu: {e}")

def menu_admin(firma, zalogowany_admin):
    while True:
        print("\n--- MENU ADMINISTRATORA ---")
        print("1. Wyswietl uzytkownikow")
        print("2. Zmien dane uzytkownika")
        print("3. Generuj raport txt")
        print("4. Wyloguj")
        wybor = input("Wybierz opcje: ")

        if wybor == '1':
            for u in firma.uzytkownicy:
                print(f"Login: {u.login}, Rola: {u.rola}")
        elif wybor == '2':
            login_zmiana = input("Podaj login uzytkownika do modyfikacji: ")
            cel = next((u for u in firma.uzytkownicy if u.login == login_zmiana), None)
            if cel:
                nowe_haslo = input("Podaj nowe haslo: ")
                nowa_rola = input("Podaj nowa role (admin/sprzedawca/magazynier): ")
                zalogowany_admin.zmien_dane_uzytkownika(cel, nowe_haslo, nowa_rola)
                firma.zapisz_dane()
                print("Dane uzytkownika zostaly zaktualizowane.")
            else:
                print("Nie znaleziono takiego uzytkownika.")
        elif wybor == '3':
            firma.generuj_raport()
        elif wybor == '4':
            break
        else:
            print("Nieprawidlowa opcja.")

def menu_pracownik(firma, zalogowany_pracownik):
    while True:
        print(f"\n--- MENU PRACOWNIKA ({zalogowany_pracownik.rola.upper()}) ---")
        print("1. Wyswietl stan magazynu i finanse")
        print("2. Zamow towar (Kup)")
        print("3. Sprzedaj towar")
        print("4. Wyloguj")
        wybor = input("Wybierz opcje: ")

        if wybor == '1':
            print(f"\nStan firmowego konta: {firma.finanse} PLN")
            for i, p in enumerate(firma.produkty):
                print(f"{i+1}. {p.nazwa} - {p.ilosc} szt. (Cena: {p.cena} PLN)")
                
        elif wybor == '2':
            if zalogowany_pracownik.rola not in ['sprzedawca', 'magazynier']:
                print("Brak uprawnien do zamawiania towaru.")
                continue
                
            nazwa = input("Podaj nazwe produktu do zamowienia: ")
            cel = next((p for p in firma.produkty if p.nazwa.lower() == nazwa.lower()), None)
            if cel:
                try:
                    ilosc = int(input("Podaj ilosc do zamowienia: "))
                    koszt = ilosc * cel.cena
                    if firma.finanse >= koszt:
                        firma.finanse -= koszt
                        cel.ilosc += ilosc
                        firma.zapisz_dane()
                        print(f"Pomyslnie zamowiono. Nowy stan konta: {firma.finanse} PLN")
                    else:
                        print("Firma nie ma wystarczajacych srodkow.")
                except ValueError:
                    print("Blad: Ilosc musi byc liczba calkowita.")
            else:
                print("Nie znaleziono takiego produktu.")

        elif wybor == '3':
            if zalogowany_pracownik.rola != 'sprzedawca':
                print("Tylko sprzedawca moze sprzedawac towar klientom.")
                continue
                
            nazwa = input("Podaj nazwe produktu do sprzedazy: ")
            cel = next((p for p in firma.produkty if p.nazwa.lower() == nazwa.lower()), None)
            if cel:
                try:
                    ilosc = int(input("Podaj ilosc do sprzedazy: "))
                    if cel.ilosc >= ilosc:
                        cel.ilosc -= ilosc
                        firma.finanse += (ilosc * cel.cena)
                        firma.zapisz_dane()
                        print(f"Pomyslnie sprzedano. Nowy stan konta: {firma.finanse} PLN")
                    else:
                        print("Brak wystarczajacej ilosci towaru w magazynie.")
                except ValueError:
                    print("Blad: Ilosc musi byc liczba calkowita.")
            else:
                print("Nie znaleziono takiego produktu.")
                
        elif wybor == '4':
            break
        else:
            print("Nieprawidlowa opcja.")

def main():
    firma = Firma("dane.json")
    
    while True:
        print("\n=== SYSTEM ZARZADZANIA FIRMA ===")
        print("Zaloguj sie, aby kontynuowac lub wpisz 'wyjdz'.")
        login = input("Login: ")
        
        if login.lower() == 'wyjdz':
            print("Zamykanie programu...")
            break
            
        haslo = input("Haslo: ")
        
        uzytkownik = firma.znajdz_uzytkownika(login, haslo)
        
        if uzytkownik:
            print(f"Pomyslnie zalogowano jako {uzytkownik.login}.")
            if isinstance(uzytkownik, Admin):
                menu_admin(firma, uzytkownik)
            else:
                menu_pracownik(firma, uzytkownik)
        else:
            print("Bledny login lub haslo.")

if __name__ == "__main__":
    main()
