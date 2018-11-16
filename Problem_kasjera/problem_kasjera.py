def problem_kasjera(zlote_reszta, grosze_reszta):
    zlote = {'Pięćset złotych:':500, 'Dwieście złotych:':200, 'Sto złotych:':100, 'Pięćdziesiąt złotych:':50, 'Dwadzieścia złotych:':20, 'Dziesięć złotych:':10, 'Pięć złotych:':5, 'Dwa złote:':2, 'Złotówka:':1}
    grosze = {'Pięćdziesiąt groszy:':50, 'Dwadzieścia groszy:':20, 'Dziesięć groszy:':10, 'Pięć groszy:':5, 'Dwa grosze:':5, 'Grosz:':1}
    zlote_klucze = tuple(zlote.keys())
    grosze_klucze = tuple(grosze.keys())
    p = i = j = 0
    reszta_dict = {}
    
    while zlote_reszta > 0:
        if zlote_reszta >= zlote[zlote_klucze[i]]:
            p = zlote_reszta // zlote[zlote_klucze[i]]
            zlote_reszta = zlote_reszta - (zlote[zlote_klucze[i]]*p)
            reszta_dict.update({zlote_klucze[i]:p})
        i += 1
        p = 0

    while grosze_reszta > 0:
        if grosze_reszta >= grosze[grosze_klucze[j]]:
            p = grosze_reszta // grosze[grosze_klucze[j]]
            grosze_reszta = grosze_reszta - (grosze[grosze_klucze[j]]*p)
            reszta_dict.update({grosze_klucze[j]:p})
        j += 1
        p = 0
    
    return reszta_dict

def wydrukuj_reszte(reszta):
    print(25*'-')
    print('Tak wydam resztę')
    print(25*'-')
    
    for i, j in reszta.items():
        print(i, j)
        
    print(25*'-')

def pobierz_dane():
    zlote = int(input("Ile złotych należy wydać: "))
    while zlote < 0:
        zlote = int(input("Nie można wydać mniej niż 0 złotych... Podaj jeszcze raz ile złotych mam wydać: "))

    grosze = int(input("Ile groszy należy wydać: "))
    while not(0 <= grosze <= 99):
        grosze = int(input("Ilość groszy do wydania musi być większa lub równa 0 i mniejsza lub równa 99. Podaj jeszcze raz ile groszy mam wydać: "))

    return zlote, grosze

zlote, grosze = pobierz_dane()
reszta = problem_kasjera(zlote, grosze)
wydrukuj_reszte(reszta)
