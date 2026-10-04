import random

wrog = []

def uszkodzony_dron():
    wrog[:] = ["Uszkodzony Dron Zwiadowczy", random.randint(30, 50), random.randint(10, 20)]

def kosmiczny_pirat():
    wrog[:] = ["Kosmiczny Pirat", random.randint(50, 70), random.randint(20, 30)]

def elitarny_mysliwiec():
    wrog[:] = ["Elitarny Mysliwiec Obcych", random.randint(10, 30), random.randint(5, 10)]

def straznik_sektora():
    wrog[:] = ["Pradawny Straznik Sektora", random.randint(200, 300), random.randint(40, 60)]

def losuj_wroga():
    los = random.randint(1, 100)
    if los <= 50:
        elitarny_mysliwiec()
    elif los <= 80:
        uszkodzony_dron()
    elif los <= 99:
        kosmiczny_pirat()
    else:
        straznik_sektora()
    return wrog

boss = []

def gwiezdny_niszczyciel():
    boss[:] = ["Gwiezdny Niszczyciel", random.randint(1000, 8000), 200]

def okret_matka():
    boss[:] = ["Okret Matka Obcych", random.randint(8000, 80000), 400]

def losuj_bossa():
    lo = random.randint(1, 100)
    if lo <= 99:
        gwiezdny_niszczyciel()
    else:
        okret_matka()
    return boss
