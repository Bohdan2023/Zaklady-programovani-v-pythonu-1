userinput = input("rimskecislo:")
userinput = userinput.upper()

roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

import re
vzor = "^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"

if re.search(vzor, userinput):

    arabikcislo = 0
    minulerimskecislo = 0
    spravnyroman = True

    for numeral in userinput:
        if numeral in roman:
            aktualnivalue = roman[numeral]
            if aktualnivalue > minulerimskecislo:
                arabikcislo += aktualnivalue - 2 * minulerimskecislo
            else:
                arabikcislo += aktualnivalue
            minulerimskecislo = aktualnivalue
        else:
            spravnyroman = False
            break
    if spravnyroman:
        print(arabikcislo)
else:
    print("neni spravne romanske cislo")