from module import *
hallgatok:list[Hallgato] = []
file = open(file='course.txt', mode='r', encoding='utf-8')
for s in file: hallgatok.append(Hallgato(s))

print(f'hallgatók száma: {len(hallgatok)}')

f2:int = 0
for h in hallgatok:
    f2 += h.eredmenyek['backend']
print(f'hallgatók átlaga backend tt-ből: {f2/len(hallgatok)}%')

f3:int = 0
for i in range(len(hallgatok)):
    if hallgatok[i].osszeredmeny > hallgatok[f3].osszeredmeny:
        f3 = i
print(f'legjobb tanuló: {hallgatok[f3].nev}')

print('akik már kifizették:')
for h in hallgatok:
    if h.befizetes >= 2600:
        print(f'\t- {h.nev}')

f5:str = input('írj be egy nevet: ')
for h in hallgatok:
    if h.nev == f5:
        if h.vanbukas:
            print('\taz alábbi tt-kből kell javítóvizsgát tenie: ')
            for k, v in h.eredmenyek.items():
                if v <= 50: print(f'\t\t{k}: ({v}%-os eredmény)')
        else: print('\tnem kell javítóvizsgát tennie semmiből')
        break
else: print('\tnincs ilyen nevű hallgató')