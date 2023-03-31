class ALFABET_AFN:
    def __init__(self,input):
        self.input=input
    def alfabet(self):
        self.indicator_lambda=False
        self.dictionar = {}
        self.lista_stari = []
        self.lista_muchii = []
        with open(self.input) as f:
            rand = f.readline()
            self.stare_initiala = rand.split()[0]
            rand = f.readline()
            self.stari_finale = rand.split()
            rand = f.readline()
            while rand != "":
                rand = rand.split()
                if rand[0] not in self.lista_stari:
                    self.lista_stari.append(rand[0])
                if rand[1] not in self.lista_muchii:
                    self.indicator_lambda=True
                    self.lista_muchii.append(rand[1])
                if rand[2] not in self.lista_stari:
                    self.lista_stari.append(rand[2])

                d = {}
                ok = 0
                d[rand[1]] = [rand[2]]
                if rand[0] in self.dictionar:
                    if rand[1] in self.dictionar[rand[0]]:
                        l = self.dictionar[rand[0]][rand[1]]
                        l.append(rand[2])
                        d[rand[1]] = l
                        ok = 1
                    d = self.dictionar[rand[0]]
                    if ok == 0:
                        d[rand[1]] = [rand[2]]
                    else:
                        d[rand[1]] = l
                self.dictionar[rand[0]] = d
                rand = f.readline()

        for element in self.lista_stari:
            if element not in self.dictionar:
                self.dictionar[element] = {}
    def get(self,dictionar, stare_curenta, lista, simbol, vizitate):                #obtin λ-inchiderile sau starea urmatoare
        if stare_curenta in vizitate:                                               #verific ca starea curenta sa nu fie deja vizitata
            return
        vizitate.add(stare_curenta)
        if simbol in dictionar[stare_curenta]:
            for element in dictionar[stare_curenta][simbol]:
                if simbol == 'l':
                    if stare_curenta not in lista:
                        lista.append(stare_curenta)
                    self.get(dictionar, element, lista, simbol, vizitate)
            if simbol != 'l' and dictionar[stare_curenta][simbol] not in lista:
                lista.extend(dictionar[stare_curenta][simbol])
        else:
            if stare_curenta not in lista and simbol == 'l':
                lista.append(stare_curenta)

    def transformare(self,stare_curenta, simbol, di, stari_finale, l, l_finale):    #pentru starea curenta, obtin noile muchii, facand
        viz = set()                                                                 #mai intai λ-inchiderile, apoi starile urmatoare si in final, λ-inchiderile
        self.get(di, stare_curenta, l, 'l', viz)                                    #ce ajung sa fie noile stari urmatoare

        for stare in l:                                                             #verific de fiecare data daca starea curenta a devenit finala
            if stare in stari_finale and stare_curenta not in l_finale:
                l_finale.append(stare_curenta)
        l_copie = []
        viz.clear()

        for stare in l:
            self.get(di, stare, l_copie, simbol, viz)

        l.clear()
        viz.clear()
        for stare in l_copie:
            self.get(di, stare, l, 'l', viz)

        for stare in l_finale:
            if stare not in stari_finale:
                stari_finale.append(stare)
        return l

    def verif_automat(self,cuvant_intrare):
        if self.stare_initiala in self.stari_finale and cuvant_intrare == '':
            return True
        else:
            lista_poz = [[self.stare_initiala]]
            lista_pt_afis = []
            for litera in cuvant_intrare:
                j = 0
                while j < len(lista_poz):
                    stare_curenta = lista_poz[j][-1]
                    if litera in self.dictionar[stare_curenta]:
                        copie = lista_poz[j].copy()
                        lista_poz[j] = []
                        for i in self.dictionar[stare_curenta][litera]:
                            lista_noua = copie.copy()
                            lista_noua.append(litera)
                            lista_noua.append(i)
                            lista_poz.insert(j + 1, lista_noua)
                        del lista_poz[j]
                        j += len(self.dictionar[stare_curenta][litera])
                    else:
                        if lista_poz[j] not in lista_pt_afis:
                            lista_pt_afis.append(lista_poz[j])
                            del lista_poz[j]
            accept = False
            for element in lista_poz:
                if element[-1] in self.stari_finale:
                    accept = True
                    break
            if accept == True:
                return True
            return False

class generator:
    ob = ALFABET_AFN('input_generator.txt')                               #folosesc clasa de mai sus pentru a imi genera lista de muchii
    ob.alfabet()
    lista = ob.lista_muchii
    def __init__(self,lungime_max):
        self.lungime_max=lungime_max
        self.lista_cuvinte=[]
        self.l_noua=[]
        if self.ob.stare_initiala in self.ob.stari_finale:
            self.lista_cuvinte.append('\u03BB')                     #verific cuvantul vid
    def back(self, k, l_noua):                                      #alg de backtracking
        if k < self.lungime_max:                                    #conditia cu care verific lungimea maxima a cuvantului
            for i in self.lista:
                new_l_noua = list(l_noua)                           #de fiecare data cand apelez subprog, imi creez o lista noua
                new_l_noua.append(i)                                #cu elementele deja adaugate, la care adaug elementul curent
                cuvant = "".join(new_l_noua)
                if self.ob.verif_automat(cuvant)==True:             #conditia principala
                    self.lista_cuvinte.append(new_l_noua)           #daca cuvantul este acceptat, atunci il adaug in lista de cuvinte
                self.back(k + 1, new_l_noua)
            else:                                                   #cand se termina for-ul, elimina ultimul element adaugat
                if len(self.l_noua) > 0:
                    self.l_noua.pop()
        elif k == self.lungime_max and len(self.l_noua) > 0:
            self.l_noua.pop()

p2=generator(6)
p2.back(0,[])
for cuvant in p2.lista_cuvinte:
    print(*cuvant)