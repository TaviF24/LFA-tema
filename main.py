from emoji import emojize
import copy
class AFD:
    def __init__(self,input):
        self.input=input
    def afd(self):
        dictionar = {}
        lista_stari = []
        lista_muchii = []
        with open(self.input) as f:
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
            print('Cuvant acceptat', emojize(':smiling_face_with_sunglasses:'), '\n')
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
                print('Cuvant acceptat', emojize(':smiling_face_with_sunglasses:'), '\n')
            else:
                print("Cuvant respins", emojize(':face_with_raised_eyebrow:'))

class AFN:
    def __init__(self,input):
        self.input=input
    def afn(self):
        dictionar = {}
        lista_stari = []
        lista_muchii = []
        with open(self.input) as f:
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
            print('Cuvant acceptat', emojize(':smiling_face_with_sunglasses:'), '\n')
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
                print('Cuvant acceptat', emojize(':smiling_face_with_sunglasses:'), '\n')
                for element in range(len(lista_poz)):

                    print('Traseu ', element + 1, ':', sep='')
                    print('Starea ', lista_poz[element][0], ' ----', sep='', end='')
                    for simbol in range(1, len(lista_poz[element]) - 2, 2):
                        print(lista_poz[element][simbol], '----> Starea ', lista_poz[element][simbol + 1], ' ----',
                              sep='',
                              end='')
                    print(lista_poz[element][-2], '----> Starea ', lista_poz[element][-1], sep='')
                if len(lista_pt_afis) != 0:
                    j = len(lista_poz)
                    print('\nAlte trasee efectuate:')
                    for element in range(len(lista_pt_afis)):
                        print('Traseu ', j + 1, ':', sep='')
                        print('Starea ', lista_pt_afis[element][0], ' ----', sep='', end='')
                        for simbol in range(1, len(lista_pt_afis[element]) - 2, 2):
                            print(lista_pt_afis[element][simbol], '----> Starea ', lista_pt_afis[element][simbol + 1],
                                  ' ----', sep='',
                                  end='')
                        print(lista_pt_afis[element][-2], '----> Starea ', lista_pt_afis[element][-1], sep='')
                        j += 1
            else:
                print('Cuvant respins', emojize(':face_with_raised_eyebrow:'))

class ALFABET_AFN:
    def __init__(self,input):
        self.input=input
    def alfabet(self):
        self.indicator_lambda = False
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
                    self.indicator_lambda = True
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

class GENERATOR:
    ob = ALFABET_AFN('input_generator.txt')                               #folosesc clasa de mai sus pentru a imi genera lista de muchii
    ob.alfabet()
    lista = ob.lista_muchii
    def __init__(self,lungime_max):
        if self.ob.indicator_lambda == True:                            #verific daca automatul este un λ-NFA
            dictionar_copie = copy.deepcopy(self.ob.dictionar)

            for mini_dictionar in dictionar_copie:                      #transform vechiul dictionar ce contine λ, intr-unul ce nu are,
                for cheie in self.ob.lista_muchii:                      #luand fiecare stare cu fiecare muchie
                    if cheie != 'l':
                        l = []
                        l_finale = []
                        self.ob.dictionar[mini_dictionar][cheie] = self.ob.transformare(mini_dictionar, cheie, dictionar_copie,
                                                                              self.ob.stari_finale, l, l_finale)
                    elif cheie == 'l' and cheie in self.ob.dictionar[mini_dictionar]:
                        self.ob.dictionar[mini_dictionar].pop(cheie)

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
def meniu():
    print('START: Apasati 1','EXIT: Apasati 0',sep='\n')
    tasta=int(input())
    if tasta!=1:
        print('SFARSIT',emojize(':slightly_frowning_face:'))
    else:
        print('\nBuna alegere',emojize(':thumbs_up:'))
        print('Pentru a schimba inputul, verificati fisierele input_afd.txt, input_afn.txt si input_generator.txt\n')
        print('Ce doriti sa efectuati?\n','AFD: Apasati 1\n','AFN: Apasati 2\n','GENERAREA TUTUROR CUVINTELOR ACCEPTATE CU O LUNGIME MAXIMA N: Apasati 3\n','Nimic, la revedere',emojize(':waving_hand:'),': Apasati 0',sep='')
        tasta = int(input())
        while tasta!=0:
            if tasta==1:
                ob1 = AFD("input_afd.txt")
                ob1.afd()
            elif tasta==2:
                ob2 = AFN("input_afn.txt")
                ob2.afn()
            else:
                nr_max=int(input("Introduceti lungimea maxima= "))
                ob3=GENERATOR(nr_max)
                ob3.back(0,[])
                for cuvant in ob3.lista_cuvinte:
                    print(''.join(cuvant))
            print('\nMai doriti sa efectuati altceva?\n','Inca un AFD: Apasati 1\n','Inca un AFN: Apasati 2\n','GENERAREA TUTUROR CUVINTELOR ACCEPTATE CU O LUNGIME MAXIMA N: Apasati 3\n','Nu, la revedere',emojize(':waving_hand:'),': Apasati 0',sep='')
            tasta = int(input())
        print("SFARSIT",emojize(':grinning_face:'))

meniu()