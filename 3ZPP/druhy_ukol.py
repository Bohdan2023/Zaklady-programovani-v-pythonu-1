def vytvor_osobu(jmeno, prijmeni, adresa, den, mesic, rok, telefon, email):
    o = {
        "jmeno": jmeno,
        "prijmeni": prijmeni,
        "adresa": adresa,
        "den": den,
        "mesic": mesic,
        "rok": rok,
        "telefon": telefon,
        "email": email
    }
    return o

def vloz(s, o):
    s.append(o)

def najdi_osobu(kde, co, s):
    for osoba in s:
        jmeno = osoba["jmeno"]
        prijmeni = osoba["prijmeni"]
        adresa = osoba["adresa"]
        den = osoba["den"]
        mesic = osoba["mesic"]
        rok = osoba["rok"]
        telefon = osoba["telefon"]
        email = osoba["email"]
        if co in [jmeno , prijmeni, adresa, den, mesic, rok, telefon, email]:
            return True
        else:
            return False
        
def nejmladsi(s):
    if not s:
        return None
    x = s[0]
    
    for osoba in s:
        if(osoba["rok"], osoba["mesic"], osoba["den"]) > (x ["rok"], x["mesic"], x["den"]):
            x = osoba
    return x

def tisk_osoby(o):
    print(o)

def tisk(s):
    print(s)

seznam_osob = []

o1 = vytvor_osobu("Alice", "Pokorna", "Holicka 62", 2, 1, 1992, "214 145 478", "alice.pokorna@email.cz")
o2 = vytvor_osobu("Pavel", "Novak", "tr. 17 listopadu 24", 13, 1, 1992, "654 784 478", "pavel.novak@seznam.cz")
o3 = vytvor_osobu("Ales", "Maly", "Holicka 62", 6, 5, 1989, "772 847 457", "ales.maly@upol.cz")
vloz(seznam_osob, o1)
vloz(seznam_osob, o2)
vloz(seznam_osob, o3)
tisk(seznam_osob)

if najdi_osobu("jmeno", "Alice", seznam_osob):
    print("Alice nalezena.\n")
else: 
    print("Alice nenalezena.\n")

if najdi_osobu("prijmeni", "Novotny", seznam_osob):
    print("Novotny nalezen.\n")
else: 
    print("Novotny nenalezen.\n")
    
nejmladsi_osoba = nejmladsi(seznam_osob)
print("Nejmladsi osobou v seznamu je:")
tisk_osoby(nejmladsi_osoba)