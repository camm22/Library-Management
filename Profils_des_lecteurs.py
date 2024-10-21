from Function import*

def Profils():
    livres = open_books_avec_strip()

    while 1:
        print("\nQue voulez-vous faire ?\n\n 1-Créer un nouveau lecteur\n 2-Afficher un lecteur\n 3-Modifier un lecteur\n 4-Supprimer un lecteur")

        liste_pseudo = Liste_pseudo()

        choix = input(':')
        while choix not in ['1', '2', '3', '4', 'q']:
            choix = input('Réponse inappropirée :')

        if choix == '1':
            pseudo = input('\nSaisir le pseudo du nouveau lecteur :')
            while pseudo == '' or ' ' in pseudo or pseudo in liste_pseudo:
                if pseudo in liste_pseudo:
                    pseudo = input("Ce pseudo existe déjà, veuillez le ressaisir :")
                else:
                    pseudo = input('Veuillez ressaisir votre pseudo (réponse inappropriée) :')

            print("\nEst-ce ?\n 1-Un homme\n 2-Une femme\n 3-Autre")
            genre=input(':')
            while genre not in ['1', '2', '3']:
                genre = input("Réponse inappropirée :")

            print("\nQuel âge a-t-il ?\n 1-Moin de 18 ans\n 2-Entre 18 ans et 25 ans\n 3-Plus de 25 ans")
            age=input(":")
            while age not in ['1', '2', '3']:
                age = input("Réponse inappropirée :")

            print("\nQuel est son style de lecture ?\n 1-Science-fiction\n 2-Biographie\n 3-Horreur\n 4-Romance\n 5-Fable\n 6-Histoire\n 7-Comédie")
            style=input(':')
            while style not in ['1', '2', '3', '4', '5', '6', '7']:
                style = input("Réponse inappropirée :")


            print("\nQuels livres a-t-il déjà lu ?\n*Appuyer directement sur entrer si vous n'en n'avez pas lus sinon écrivez-les à la suite séparés par des espaces*\n")
            for i in range(1,len(livres)+1):
                print(str(i)+'-'+livres[i-1])
            livres_lus = [s for s in input(':').split()]
            l = []
            for j in range(1,i+1):
                l.append(str(j))
            for j in range(len(livres_lus)):
                while livres_lus[j] not in l or livres_lus.count(livres_lus[j])>1:
                    if j == 0:
                        prem = "er"
                    else:
                        prem = "ième"
                    print("Veuillez ressaisir le", j+1,prem, "livre que vous avez lu (réponse inappropriée)", end=' ')
                    livres_lus[j]=input(':')

            if len(livres_lus) != 0:
                livres_lus = Trier(livres_lus)
                print("\nVeuillez noter les livres que vous avez lus en leurs attribuant une note entre 1 (je n'ai pas aimé) et 5 (exellent): ")
                notes = []
                for k in livres_lus:
                    print(" ."+livres[int(k)-1], end=' ')
                    note = input(':')
                    while note not in ['1','2','3','4','5']:
                        print("Veuillez ressaisir votre note pour", livres[int(k)-1],"(réponse inappropriée)", end=' ')
                        note = input(':')
                    notes.append(note)
            else:
                notes = []

            Ajouter_lecteur(pseudo, genre, age, style, livres_lus)
            Ajouter_ligne_matrice(notes,livres_lus)
            print("\nLe profil '"+pseudo+"' a bien été créé.")

        elif choix == '2':
            recherche = input("\nQuel est le pseudo du profil que vous voulez consulter ? :")
            while recherche not in liste_pseudo:
                recherche = input("Ce pseudo n'existe pas veuillez le ressaisir :")
            Afficher_lecteur(recherche,livres)

        elif choix == '3':
            recherche = input("\nQuel est le pseudo du profil que vous voulez modifier? :")
            while recherche not in liste_pseudo:
                recherche = input("Ce pseudo n'existe pas veuillez le ressaisir :")

            position = liste_pseudo.index(recherche)
            liste_pseudo.remove(recherche)

            liste_lecteurs = open_readers_list()

            pseudo = liste_lecteurs[position][0]
            genre = liste_lecteurs[position][1]
            age = liste_lecteurs[position][2]
            style = liste_lecteurs[position][3]

            liste_lecture = open_booksread_list()
            livres_lus = liste_lecture[position]

            del livres_lus[0]

            notes = Notes(position)

            while 1:
                print("\nQue voulez-vous modifier ?\n 1-Pseudo\n 2-Genre\n 3-Age\n 4-Style\n 5-Livres lus\n 6-Terminer")
                choix2 = input(':')
                while choix2 not in ['1','2','3','4','5','6']:
                    choix2 = input('Réponse inappropirée :')

                if choix2 == '1':
                    pseudo = input('\nSaisir le nouveau pseudo : ')
                    while pseudo == '' or ' ' in pseudo or pseudo in liste_pseudo:
                        if pseudo in liste_pseudo:
                            pseudo = input("Ce pseudo existe déjà, veuillez le ressaisir :")
                        else:
                            pseudo = input('Veuillez ressaisir votre pseudo (réponse inappropriée) : ')

                elif choix2 == '2':
                    print("\nRessaisir le genre :\n 1-Homme\n 2-Femme\n 3-Autre")
                    genre=input(':')
                    while genre not in ['1', '2', '3']:
                        genre = input("Réponse inappropirée :")

                elif choix2 == '3':
                    print("\nRessaisir l'âge :\n 1-Moin de 18 ans\n 2-Entre 18 ans et 25 ans\n 3-Plus de 25 ans")
                    age=input(":")
                    while age not in ['1', '2', '3']:
                        age = input("Réponse inappropirée :")

                elif choix2 == '4':
                    print("\nRessaisir son style de lecture ?\n 1-Science-fiction\n 2-Biographie\n 3-Horreur\n 4-Romance\n 5-Fable\n 6-Histoire\n 7-Comédie")
                    style=input(':')
                    while style not in ['1', '2', '3', '4', '5', '6', '7']:
                        style = input("Réponse inappropirée :")

                elif choix2 == '5':
                    print("\nRessaisir les livres déjà lus :\n*Appuyer directement sur entrer si vous n'en n'avez pas lus sinon écrivez-les à la suite séparés par des espaces*\n")
                    for i in range(1,len(livres)+1):
                        print(str(i)+'-'+livres[i-1])
                    livres_lus = [s for s in input(':').split()]
                    l=[]
                    for j in range(1,i+1):
                        l.append(str(j))
                    for j in range(len(livres_lus)):
                        while livres_lus[j] not in l or livres_lus.count(livres_lus[j])>1:
                            if j == 0:
                                prem = "er"
                            else:
                                prem = "ième"
                            print("veuillez ressaisir le", j+1, prem, "livre que vous avez lus (réponse inapproprié)", end=' ')
                            livres_lus[j]=input(':')

                    if len(livres_lus) != 0:
                        livres_lus = Trier(livres_lus)
                        print("\nVeuillez noter les livres que vous avez lus en leurs attribuant une note entre 1 (je n'ai pas aimé) et 5 (exellent): ")
                        notes = []
                        for k in livres_lus:
                            print(" ."+livres[int(k)-1], end=' ')
                            note = input(':')
                            while note not in ['1','2','3','4','5']:
                                print("Veuillez ressaisir votre note pour", livres[int(k)-1],"(réponse inapproprié)", end=' ')
                                note = input(':')
                            notes.append(note)
                    else:
                        notes = []

                elif choix2 == '6':
                    break

            Modifier_colonne_matrice(position, notes, livres_lus)
            Modifier_lecteur(pseudo, genre, age, style, livres_lus, position)
            print("\nLe profil '"+pseudo+"' a bien été modifié.")

        elif choix == '4':
            recherche = input("\nQuel est le pseudo du profil que vous voulez supprimer ? :")
            while recherche not in liste_pseudo:
                recherche = input("Ce pseudo n'existe pas veuillez le ressaisir :")

            position = liste_pseudo.index(recherche)

            Supprimer_lecteur(position)
            Supprimer_ligne_matrice(position)
            print("\nLe profil '"+recherche+"' a bien été supprimé.")

        elif choix == 'q':
            break

def Ajouter_lecteur (pseudo, genre, age, style, livres_lus):
    readers = open('readers.txt', 'a',encoding='utf-8')
    lecteur = pseudo+','+genre+','+age+','+style+'\n'
    readers.write(lecteur)
    readers.close()

    booksread = open('booksread.txt', 'a', encoding='utf-8')
    lecteur = pseudo
    for livre in livres_lus:
        lecteur += ','
        lecteur += livre
    lecteur += '\n'
    booksread.write(lecteur)
    booksread.close()


def Afficher_lecteur(recherche,livres):
    liste_lecteurs = open_readers_list()
    liste_lecture = open_booksread_list()

    for i in range(len(liste_lecteurs)):
        if recherche == liste_lecteurs[i][0]:
            lecteur = liste_lecteurs[i]

    for i in range(len(liste_lecture)):
        if recherche == liste_lecture[i][0]:
            lecture = liste_lecture[i]

    print("\n------Profile de "+recherche+"------")
    print("-Genre : ",end='')
    if lecteur[1] == '1':
        print("homme")
    elif lecteur[1] == '2':
        print("femme")
    elif lecteur[1] == '3':
        print("non spécifié")

    print("-Age : ",end='')
    if lecteur[2]=='1':
        print("moin de 18 ans")
    elif lecteur[2]=='2':
        print("entre 18 ans et 25 ans")
    elif lecteur[2]=="3":
        print("plus de 25 ans")

    print("-Style : ",end='')
    if lecteur[3]=='1':
        print("Science-fiction")
    elif lecteur[3]=='2':
        print("Biographie")
    elif lecteur[3]=='3':
        print("Horreur")
    elif lecteur[3]=='4':
        print("Romance")
    elif lecteur[3]=='5':
        print("Fable")
    elif lecteur[3]=='6':
        print("Histoire")
    elif lecteur[3]=='7':
        print("Comédie")

    if len(lecture) == 1:
        print("-Cet utilisateur n'a pas lu de livre.")
    else:
        print("-Livres lus :")
        for i in range(1,len(lecture)):
            print(" ."+livres[int(lecture[i]) - 1])

def Modifier_lecteur (pseudo, genre, age, style, livres_lus, position):
    liste_lecteurs = open_readers()
    liste_lecture = open_booksread()

    liste_lecteurs[position] = pseudo+','+genre+','+age+','+style+'\n'

    lecteur = pseudo
    for livre in livres_lus:
        lecteur += ','
        lecteur += livre
    lecteur += '\n'
    liste_lecture[position] = lecteur

    Write_readers_and_booksread(liste_lecteurs, liste_lecture)

def Supprimer_lecteur (position):
    liste_lecteurs = open_readers()
    liste_lecture = open_booksread()

    del liste_lecteurs[position]
    del liste_lecture[position]

    Write_readers_and_booksread(liste_lecteurs, liste_lecture)
