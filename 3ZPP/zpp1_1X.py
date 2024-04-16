def vytvor_osobu(jmeno, prijmeni, adresa, den, mesic, rok, telefon, email):
    return {
        "jmeno": jmeno,
        "prijmeni": prijmeni,
        "adresa": adresa,
        "den": den,
        "mesic": mesic,
        "rok": rok,
        "telefon": telefon,
        "email": email
    }
    
def vloz(s, o):
    s.append(o)
    
def tisk(s):
    for osoba in s:
        tisk_osoby(osoba)
        
def najdi_osobu(kde,co,s):
    return

def nejmladsi(s):
    return

def tisk_osoby(o):
    print(f"Jméno: {o['jmeno']}, Příjmení: {o['prijmeni']}, Adresa: {o['adresa']}, Datum narození: {o['den']}.{o['mesic']}.{o['rok']}, Telefon: {o['telefon']}, Email: {o['email']}")

seznam_osob=[]
o1 = vytvor_osobu("Alice", "Pokorna", "Holicka 62", 2, 1, 1992, "214 145 478", "alice.pokorna@email.cz")
o2 = vytvor_osobu("Pavel", "Novak", "tr. 17 listopadu 24", 13, 1, 1992, "654 784 478", "pavel.novak@seznam.cz")
o3 = vytvor_osobu("Ales", "Maly", "Holicka 62", 6, 5, 1989, "772 847 457", "ales.maly@upol.cz")
vloz(seznam_osob, o1)
vloz(seznam_osob, o2)
vloz(seznam_osob, o3)
tisk(seznam_osob)

"""
if (najdi_osobu("jmeno", "Alice", seznam_osob)):
    print("Alice nalezena.\n")
else: 
    print("Alice nenalezena.\n")

if (najdi_osobu("prijmeni", "Novotny", seznam_osob)):
    print("Novotny nalezen.\n")
else: 
    print("Novotny nenalezen.\n")

o = nejmladsi(seznam_osob)
print("Nejmladsi osobou v seznamu je ", tisk_osoby(o))
"""