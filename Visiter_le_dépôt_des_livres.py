from Function import*

def Visiter_le_depot():
    while 1:
        livres = open_books_avec_strip()

        print("\nQue voulez-vous faire ?\n\n 1-Afficher la liste des livres\n 2-Ajouter un livre\n 3-Modifier le titre d'un livre\n 4-Supprimer un livre")
        choix = input(':')
        while choix not in ['1', '2', '3', '4', 'q']:
            choix = input('Réponse inappropirée :')

        if choix == '1':
            print("\nVoici la liste des livres :\n")
            for i in range(1,len(livres)+1):
                print(str(i)+'-'+livres[i-1])

        elif choix == '2':
            titre = input("\nEntrer le titre du livre que vous voulez ajouter :")
            while titre == '' or len(titre) == titre.count(' ') or titre in livres:
                if titre in livres:
                    titre = input("Ce livre existe déjà, veuillez le ressaisir :")
                else:
                    titre = input("Veuillez ressaisir le titre du livre (réponse inappropriée) :")
            Ajouter_livre(titre)
            Ajouter_colonne_matrice()
            print("\nLe livre '"+titre+"' a bien été ajouté au dépôt.")


        elif choix == '3':
            recherche = input("\nQuel est le titre du livre que vous voulez modifier :")
            while recherche not in livres:
                recherche = input("Ce livre n'existe pas veuillez le ressaisir :")

            position = livres.index(recherche)
            livres.remove(recherche)

            titre = input("\nSaisir le nouveau titre du livre :")
            while titre == '' or len(titre) == titre.count(' ') or titre in livres:
                if titre in livres:
                    titre = input("Ce titre existe déjà, veuillez le ressaisir :")
                else:
                    titre = input("Veuillez ressaisir le titre du livre (réponse inappropriée) :")

            Modifier_livre(position,titre)
            print("\nLe livre '"+recherche+"' a bien été modifié (nouveau titre du livre : '"+titre+"').")

        elif choix == '4':
            recherche = input("\nQuel est le titre du livre que vous voulez supprimer :")
            while recherche not in livres:
                recherche = input("Ce livre n'existe pas veuillez le ressaisir :")

            position = livres.index(recherche)
            Maj_booksread(position)
            Supprimer_livre(position)
            Supprimer_colonne_matrice(position)

            print("\nLe livre '"+recherche+"'a bien été supprimé.")

        elif choix == 'q':
            break

def Ajouter_livre(titre):
    books = open("books.txt", "a", encoding='utf-8')
    books.write(titre+'\n')
    books.close()

def Modifier_livre(position,titre):
    livres = open_books()
    livres[position] = titre + '\n'
    write_books(livres)

def Supprimer_livre(position):
    livres = open_books()
    del livres[position]
    write_books(livres)

def Maj_booksread(position):
    liste_lecture = open_booksread()
    for i in range(len(liste_lecture)):
        liste_lecture[i] = liste_lecture[i].strip('\n')
        b = liste_lecture[i].split(',')
        liste_lecture[i] = b

    for i in range(len(liste_lecture)):
        veri = True
        for j in range(1,len(liste_lecture[i])):
            if veri == True:
                if liste_lecture[i][j] == str(position+1):
                    del liste_lecture[i][j]
                    veri = False

    for i in range(len(liste_lecture)):
        for j in range(1,len(liste_lecture[i])):
            if int(liste_lecture[i][j]) > position + 1:
                val = int(liste_lecture[i][j]) - 1
                liste_lecture[i][j] = str(val)

    for i in range(len(liste_lecture)):
        lec=''
        for j in range(len(liste_lecture[i])):
            lec += liste_lecture[i][j]
            if j != len(liste_lecture[i])-1:
                lec += ','
        lec += '\n'
        liste_lecture[i] = lec

    booksread = open("booksread.txt", "w", encoding='utf-8')
    for element in liste_lecture:
        booksread.write(element)
    booksread.close()
