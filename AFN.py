def afn(nume_fisier):
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
            ok = 0
            d[rand[1]] = [rand[2]]
            if rand[0] in dictionar:
                if rand[1] in dictionar[rand[0]]:
                    l = dictionar[rand[0]][rand[1]]
                    l.append(rand[2])
                    d[rand[1]] = l
                    ok = 1
                d = dictionar[rand[0]]
                if ok == 0:
                    d[rand[1]] = [rand[2]]
                else:
                    d[rand[1]] = l
            dictionar[rand[0]] = d
            rand = f.readline()

    for element in lista_stari:
        if element not in dictionar:
            dictionar[element] = {}

    cuvant_intrare = input("Introduceti cuvantul=")
    if stare_initiala in stari_finale and cuvant_intrare == '':
        print('Cuvant acceptat\n')
    else:
        lista_poz = [[stare_initiala]]
        lista_pt_afis = []
        for litera in cuvant_intrare:
            j = 0
            while j < len(lista_poz):
                stare_curenta = lista_poz[j][-1]
                if litera in dictionar[stare_curenta]:
                    copie = lista_poz[j].copy()
                    lista_poz[j] = []
                    for i in dictionar[stare_curenta][litera]:
                        lista_noua = copie.copy()
                        lista_noua.append(litera)
                        lista_noua.append(i)
                        lista_poz.insert(j + 1, lista_noua)
                    del lista_poz[j]
                    j += len(dictionar[stare_curenta][litera])
                else:
                    if lista_poz[j] not in lista_pt_afis:
                        lista_pt_afis.append(lista_poz[j])
                        del lista_poz[j]
                    # j+=1
        accept = False
        for element in lista_poz:
            if element[-1] in stari_finale:
                accept = True
                break
        if accept == True:
            print('Cuvant acceptat\n')
            for element in range(len(lista_poz)):

                print('Traseu ', element + 1, ':', sep='')
                print('Starea ', lista_poz[element][0], ' ----', sep='', end='')
                for simbol in range(1, len(lista_poz[element]) - 2, 2):
                    print(lista_poz[element][simbol], '----> Starea ', lista_poz[element][simbol + 1], ' ----', sep='',
                          end='')
                print(lista_poz[element][-2], '----> Starea ', lista_poz[element][-1], sep='')
            if len(lista_pt_afis) != 0:
                j=len(lista_poz)
                print('\nAlte trasee efectuate:')
                for element in range(len(lista_pt_afis)):
                    print('Traseu ', j + 1, ':', sep='')
                    print('Starea ', lista_pt_afis[element][0], ' ----', sep='', end='')
                    for simbol in range(1, len(lista_pt_afis[element]) - 2, 2):
                        print(lista_pt_afis[element][simbol], '----> Starea ', lista_pt_afis[element][simbol + 1],
                              ' ----', sep='',
                              end='')
                    print(lista_pt_afis[element][-2], '----> Starea ', lista_pt_afis[element][-1], sep='')
                    j+=1
        else:
            print('Cuvant respins')
afn('input_afn.txt')