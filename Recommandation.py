from Function import*

def Recommandation():
    while 1:
        liste_pseudo = Liste_pseudo()
        livres = open_books_avec_strip()

        print("\nQue voulez-voulez vous faire ?\n\n 1-Noter un livre\n 2-Suggérer un livre")
        choix = input(':')
        while choix not in ['1', '2', 'q']:
            choix = input('Réponse inappropirée :')

        if choix == '1':
            pseudo  = input("\nEntrer votre pseudo :")
            while pseudo not in liste_pseudo:
                pseudo = input("Ce pseudo n'existe pas, veuillez le ressaisir :")

            position = liste_pseudo.index(pseudo)
            liste_lecture = open_booksread_list()
            livres_lus = liste_lecture[position]
            del livres_lus[0]
            notes = Notes(position)

            l_veri = []
            for i in range(len(livres_lus)):
                l_veri.append(str(i+1))

            if len(livres_lus) == 0:
                print("\nCe lecteur n'a pas encore lu de livre.")
            else:
                print("\nVoici les livres que vous pouvez noter :")
                for i in range(len(livres_lus)):
                    print(" "+str(i+1)+"-"+livres[int(livres_lus[i])-1])

                while 1:
                    cible = input("\nQuel livre voulez-vous noter ? (entrer 'q' pour revenir en arrière) :")
                    while cible not in l_veri and cible != 'q':
                        cible = input("Veuillez ressaisir votre livre (réponse inappropriée) :")

                    if cible == 'q':
                        break

                    note = input("\nAttribuer-lui sa note sur 5 :")
                    while note not in ['1', '2', '3', '4', '5']:
                        note = input("Veuillez ressaisir votre note (réponse inappropriée) :")

                    notes[int(cible)-1] = note
                    Modifier_colonne_matrice(position, notes, livres_lus)

        elif choix == '2':
            pseudo  = input("\nEntrer votre pseudo :")
            while pseudo not in liste_pseudo:
                pseudo = input("Ce pseudo n'existe pas, veuillez le ressaisir :")
            position = liste_pseudo.index(pseudo)

            liste_suggestion = Suggestion(position)

            if len(liste_suggestion) == 0:
                print("\nNous ne pouvons pas vous suggérer de livre mais nous vous conseillons d'essayer d'en choisir un par vous même.")
            else:
                print("\nSuggestion :")
                for i in range(len(liste_suggestion)):
                    print(' '+str(i+1)+'-'+livres[int(liste_suggestion[i])-1])

                print("\nVoulez-vous lire et noter l'un de ces livres ?\n 1-Oui\n 2-Non")
                choix3= input(':')
                while choix3 not in ['1','2']:
                    choix3 = input('Réponse inappropirée :')

                if choix3 == '1':
                    w = []
                    for i in range(len(liste_suggestion)):
                        w.append(str(i+1))

                    lu = input("\nLe quel ? :")
                    while lu not in w:
                        lu = input("Réponse inaproppriée :")

                    note = input("\nDonnez lui sa note sur 5 :")
                    while note not in ['1', '2', '3', '4', '5']:
                        note = input("Réponse inapropprié (vous ne pouvez que lui donner une note comprise entre 1 et 5) :")

                    liste_lecture = open_booksread_list()

                    livres_lus = liste_lecture[position]
                    del livres_lus[0]

                    livres_lus.append(liste_suggestion[int(lu)-1])

                    livres_lus = Trier(livres_lus)

                    pos2 = livres_lus.index(liste_suggestion[int(lu)-1])

                    notes = Notes(position)
                    notes.insert(pos2,note)

                    liste_lecture = open_booksread()
                    lecteur = pseudo
                    for livre in livres_lus:
                        lecteur += ','
                        lecteur += livre
                    lecteur += '\n'
                    liste_lecture[position] = lecteur
                    booksread = open("booksread.txt", "w", encoding='utf-8')
                    for element in liste_lecture:
                        booksread.write(element)
                    booksread.close()

                    Modifier_colonne_matrice(position, notes, livres_lus)

                elif choix3 == '2':
                    pass

        elif choix == 'q':
            break
