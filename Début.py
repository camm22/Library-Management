from Profils_des_lecteurs import*
from Visiter_le_dépôt_des_livres import*
from Recommandation import*

print("\n###########################################\n###-Système de recommandation de livres-###\n###########################################")
print("\n*Vous pouvez quitter le programme ou revenir en arrière à tout moment en entrant 'q'*")

while 1:
    print("\nMenu :\n\n 1-Gérer le profil des lecteurs\n 2-Gérer le dépôt des livres\n 3-Recommandation")

    choix = input(':')
    while choix not in ['1','2','3','q']:
        choix = input('Réponse inappropirée :')

    if choix == '1':
        Profils()
    elif choix == '2':
        Visiter_le_depot()
    elif choix == '3':
        Recommandation()
    elif choix == 'q':
        print("\n*Vous avez quitté le programme*")
        break
