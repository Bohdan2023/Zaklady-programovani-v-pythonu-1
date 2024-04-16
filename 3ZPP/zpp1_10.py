def rozklad_cisla(n, limit = None):
    if limit is None:
        limit = n
    rozklady = []
    momentalni_rozklad = []
        
    def rozklad(zustatek, zacatek):
        if zustatek == 0:
            rozklady.append(momentalni_rozklad[:])
            return
        for i in range(zacatek, min(zustatek, limit) + 1):
            momentalni_rozklad.append(i)
            rozklad(zustatek - i, i)
            momentalni_rozklad.pop()
            
    rozklad(n , 1)
    return rozklady

cislo = int(input("cislo:"))
rozklad_variants = rozklad_cisla(cislo)
print(f"varianty rozkladu cisla {cislo}:")
for rozklad in rozklad_variants:
    print(rozklad)