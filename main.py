taches = []


def afficher_menu():
    print("\n=== GESTION DES TÂCHES ===")
    print("1. Ajouter une tâche")
    print("2. Afficher les tâches")
    print("3. Rechercher une tâche")
    print("0. Quitter")


def ajouter_tache():
    titre = input("Titre de la tâche : ").strip()

    while titre == "":
        print("Erreur : le titre ne peut pas être vide.")
        titre = input("Titre de la tâche : ").strip()

    taches.append(titre)
    print("Tâche ajoutée avec succès.")


def afficher_taches():
    if len(taches) == 0:
        print("Aucune tâche dans la liste.")
        return

    print("\n--- Liste des tâches ---")

    for i, tache in enumerate(taches, start=1):
        print(f"{i}. {tache}")


def rechercher_tache():
    mot_cle = input("Mot-clé à rechercher : ").strip()

    if mot_cle == "":
        print("Erreur : le mot-clé ne peut pas être vide.")
        return

    trouvee = False

    print("\n--- Résultats de la recherche ---")

    for i, tache in enumerate(taches, start=1):
        if mot_cle.lower() in tache.lower():
            print(f"{i}. {tache}")
            trouvee = True

    if not trouvee:
        print("Aucune tâche trouvée.")


while True:
    afficher_menu()

    choix = input("Votre choix : ").strip()

    if choix == "1":
        ajouter_tache()

    elif choix == "2":
        afficher_taches()

    elif choix == "3":
        rechercher_tache()

    elif choix == "0":
        print("Programme terminé.")
        break

    else:
        print("Erreur : option invalide.")
# Fonction de recherche ajoutée
# Version finale du projet