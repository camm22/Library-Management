from math import sqrt

def open_books_avec_strip():
    livres = open_books()
    for i in range(len(livres)):
        livres[i] = livres[i].strip('\n')
    return livres

def open_books():
    books = open("books.txt", "r", encoding='utf-8')
    livres = books.readlines()
    books.close()
    return livres

def Liste_pseudo():
    liste_lecteurs = open_readers_list()
    liste_pseudo = []
    for i in range(len(liste_lecteurs)):
        liste_pseudo.append(liste_lecteurs[i][0])
    return liste_pseudo

def write_books(livres):
    books = open("books.txt", "w", encoding='utf-8')
    for element in livres:
        books.write(element)
    books.close()

def open_readers():
    readers = open("readers.txt", "r", encoding='utf-8')
    liste_lecteurs = readers.readlines()
    readers.close()
    return liste_lecteurs

def open_booksread():
    booksread = open("booksread.txt", "r", encoding='utf-8')
    liste_lecture = booksread.readlines()
    booksread.close()
    return liste_lecture

def open_readers_list():
    liste_lecteurs = open_readers()
    for i in range(len(liste_lecteurs)):
        liste_lecteurs[i] = liste_lecteurs[i].strip('\n')
        a = liste_lecteurs[i].split(',')
        liste_lecteurs[i] = a
    return liste_lecteurs

def open_booksread_list():
    liste_lecture = open_booksread()
    for i in range(len(liste_lecture)):
        liste_lecture[i] = liste_lecture[i].strip('\n')
        a = liste_lecture[i].split(',')
        liste_lecture[i] = a
    return liste_lecture

def Write_readers_and_booksread (liste_lecteurs, liste_lecture):
    readers = open("readers.txt", "w", encoding='utf-8')
    booksread = open("booksread.txt", "w", encoding='utf-8')

    for element in liste_lecteurs:
        readers.write(element)
    for element in liste_lecture:
        booksread.write(element)

    readers.close()
    booksread.close()

def Trier(livres_lus):
    for i in range(len(livres_lus)):
        livres_lus[i] = int(livres_lus[i])
    l =[]
    while len(livres_lus) != 0:
        l.append(str(min(livres_lus)))
        livres_lus.remove(min(livres_lus))
    return l

def Matrice():
    M = open("matrice.txt", "r", encoding='utf-8')
    matrice = M.readlines()
    for i in range(len(matrice)):
        matrice[i] = matrice[i].strip('\n')
        l = matrice[i].split(' ')
        matrice[i] = l
    M.close()
    return matrice

def Afficher_matrice(matrice):
    M = open("matrice.txt","w",encoding='utf-8')
    for i in range (len(matrice)):
        l = ""
        for j in range(len(matrice[i])):
            l += str(matrice[i][j])
            if j != len(matrice[i])-1:
                l += " "
            else:
                l += "\n"
        M.write(l)
    M.close()

def Ajouter_ligne_matrice(notes,livres_lus):
    matrice = Matrice()
    l=[]

    for i in range(1,len(matrice[0])+1):
        if str(i) in livres_lus:
            l.append(notes[livres_lus.index(str(i))])
        else:
            l.append('0')
    matrice.append(l)
    Afficher_matrice(matrice)

def Supprimer_ligne_matrice(position):
    matrice = Matrice()
    del matrice[position]
    Afficher_matrice(matrice)

def Ajouter_colonne_matrice():
    matrice = Matrice()
    for i in range(len(matrice)):
        matrice[i].append('0')
    Afficher_matrice(matrice)

def Supprimer_colonne_matrice(position):
    matrice = Matrice()
    for i in range(len(matrice)):
        del matrice[i][position]
    Afficher_matrice(matrice)

def Modifier_colonne_matrice(position,notes,livres_lus):
    matrice = Matrice()
    l = []
    for i in range(1,len(matrice[position])+1):
        if str(i) in livres_lus:
            l.append(notes[livres_lus.index(str(i))])
        else:
            l.append('0')
    matrice[position] = l
    Afficher_matrice(matrice)

def Notes(position):
    matrice = Matrice()
    notes = []
    for i in range(len(matrice[position])):
        if matrice[position][i] != '0':
            notes.append(matrice[position][i])
    return notes

def Similarité_Cosinus(debut, pos, matrice):
    num = 0
    for i in range(len(matrice[0])):
        num += matrice[debut][i] * matrice[pos][i]

    somme1=0
    somme2=0
    for i in range(len(matrice[0])):
        somme1 += matrice[debut][i] ** 2
        somme2 += matrice[pos][i] ** 2

    dem = sqrt(somme1) * sqrt(somme2)
    res = num / dem
    res = round(res,2)
    return res

def Matrice_similarité():
    matrice = Matrice()
    for i in range(len(matrice)):
        for j in range(len(matrice[i])):
            matrice[i][j] = int(matrice[i][j])

    matrice_simi = []
    for i in range(len(matrice)):
        l = []
        for j in range(len(matrice)):
            l.append(0)
        matrice_simi.append(l)


    for debut in range(len(matrice_simi)):
        for i in range(debut, len(matrice_simi)+1):
            if i == len(matrice_simi):
                i -= 1

            res = Similarité_Cosinus(debut, i, matrice)
            matrice_simi[debut][i] = res
            matrice_simi[i][debut] = res

    return matrice_simi

def Suggestion(position):
    liste_val = []
    matrice_simi = Matrice_similarité()

    for i in range(len(matrice_simi[position])):
        if i == position:
            liste_val.append(-1)
        else:
            liste_val.append(matrice_simi[position][i])

    posi = liste_val.index(max(liste_val))

    liste_lecture = open_booksread_list()
    lectures1 = liste_lecture[position]
    lectures2 = liste_lecture[posi]
    del lectures1[0]
    del lectures2[0]

    liste_suggestion = []
    for element in lectures2:
        if element not in lectures1:
            liste_suggestion.append(element)

    return liste_suggestion
