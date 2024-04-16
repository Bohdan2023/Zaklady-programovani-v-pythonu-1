def do_stredu(text): 
    result = "" 
    for i in range(0, len(text), 2): 
        result = result + text[i] 
    for j in range(len(text) - 1, 0, -2): 
        result = result + text[j] 
    return result 
print(do_stredu("Python")) 

def vlozeni_do_textu(text,vloz): 
    i=1 
    while i <= len(text): 
        text = text[:i] + vloz + text[i:] 
        i = i + len(vloz) + 1
    print(text) 
vlozeni_do_textu('Python', 'abc')

def eratosthenovo_sito(n):
  n = n + 1
  sito = [True] * n
 
  for i in range(2, n):
    if sito[i]:
      for j in range(i**2, n, i):
        sito[j] = False
 
  prvocisla = [1]
  for i in range(2, n):
    if sito[i]:
      prvocisla.append(i)
  return prvocisla
print(eratosthenovo_sito(100))