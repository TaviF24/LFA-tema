def afd(nume_fisier):
    dictionar = {}
    lista_stari = []
    lista_muchii = []
    with open(nume_fisier) as f:
        rand = f.readline()
        stare_initiala = rand.split()[0]
        rand = f.readline()
        stari_finale = rand.split()
        rand = f.readline()
        while rand != "":
            rand = rand.split()
            if rand[0] not in lista_stari:
                lista_stari.append(rand[0])
            if rand[1] not in lista_muchii:
                lista_muchii.append(rand[1])
            if rand[2] not in lista_stari:
                lista_stari.append(rand[2])

            d = {}
            d[rand[1]] = rand[2]
            if rand[0] in dictionar:
                d = dictionar[rand[0]]
                d[rand[1]] = rand[2]
            dictionar[rand[0]] = d
            rand = f.readline()

    for element in lista_stari:
        if element not in dictionar:
            dictionar[element] = {}
    cuvant_intrare = input("Introduceti cuvantul=")
    if cuvant_intrare == "" and stare_initiala in stari_finale:
        print('Cuvant acceptat\n')
    else:
        stare_curenta = stare_initiala
        print('Starea', stare_curenta, sep=' ', end='')
        try:
            for litera in cuvant_intrare:
                print(' ------', litera, '-----> ', end="")
                stare_curenta = dictionar[stare_curenta][litera]
                print('Starea', stare_curenta, sep=' ', end='')
        except:
            stare_curenta = False
        if stare_curenta == False:
            print('Nu exista')
        else:
            print()
        if stare_curenta in stari_finale:
            print('Cuvant acceptat\n')
        else:
            print('Cuvant respins')

afd('input_afd.txt')