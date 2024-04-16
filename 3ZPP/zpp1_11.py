class abc:
    def __init__(self):
        self.slovnik = []

    def pridej_polozku(self, den, mesic, rok, castka, kategorie):
        self.slovnik.append({"den": den, "mesic": mesic, "rok": rok, "castka": castka, "kategorie": kategorie})
    
    def prehled(self, mesic, rok):
        soucet = {}
        for slovo in self.slovnik:
            if slovo["mesic"] == mesic and slovo["rok"] == rok:
                kategorie = slovo["kategorie"]
                castka = slovo["castka"]
                if kategorie in soucet:
                    soucet[kategorie] = soucet[kategorie] + castka
                else:
                    soucet[kategorie] = castka
        return soucet
        
        
        
cba = abc()
cba.pridej_polozku(15,10,2022,150,"jídlo")
cba.pridej_polozku(16,11,2022,250,"jídlo")
cba.pridej_polozku(17,11,2022,300,"bydlení")
cba.pridej_polozku(18,11,2022,500,"jídlo")
cba.pridej_polozku(19,11,2022,150,"domáctnost")
vysledek = cba.prehled(11,2022)
print(vysledek)