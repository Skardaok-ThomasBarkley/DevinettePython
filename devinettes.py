#!/usr/bin/env python3
"""

Jeu de devinettes.

Par Thomas Barkley
"""
import random

# Constantes
CHEAT_GAGNÉ = 'GGG'
CHEAT_PERDU = 'PPP'
MAX_ESSAIS = 10
MAX_RANDOM = 100
# Variables
nbEssaie = 1
nbEssaieTotal = 0
nbPartieTotal = 0


def gagner(séquence):
    """
    affiche le texte quand la partit est gagné
    :param séquence: la séquence d'essai
    """
    print("Bravo, vous avez deviné le nombre")
    print(f"Votre séquence gagnante est: {séquence}")


def perdre(nb, nbe):
    """
    affiche le texte quand la partit est perdu
    :param nb: le nombre qu'il faut trouver
    :param nbe: le nombre de tentative de l'utilisateur
    """
    print(f"Désolé,vous avez échoué après {nbe} tentatives")
    print(f"Le nombre choisi était: {nb}")


def rejouer():
    """
    permet de savoir si on lance une nouvelle partie ou non
    :return: vrai si l'utilisateur répond oui ou O
    """
    while True:
        rejoué = input("Voulez-vous rejouer? [O/N]")
        if rejoué == "oui" or rejoué == "O":
            return True
        elif rejoué == "non" or rejoué == "N":
            return False
        else:
            print("Choix invalide")


def main():
    """
    Fonction principale
    """
    global nbEssaie
    global nbEssaieTotal
    global nbPartieTotal
    print(f"""
Bonjour, je m'appel Thomax 2020
J'ai choisi un nombre entier entre 1 et {MAX_RANDOM}
Pouvez-vous le deviner ?
    """)

    while True:
        nombre = random.randrange(1, MAX_RANDOM + 1)
        séquencegagnante = []
        while nbEssaie <= MAX_ESSAIS:
            try:
                essaie = int(input(f"Essaie {nbEssaie}: "))
                nbEssaie += 1
                séquencegagnante.append(essaie)
                if nombre == essaie:
                    gagner(séquencegagnante)
                    break
                elif essaie < nombre:
                    print("Votre nombre est trop petit...")
                else:
                    print("Votre nombre est trop grand...")

            except ValueError as value:
                value = str(value)[-4:-1]
                if value == CHEAT_PERDU:
                    perdre(nombre, nbEssaie)
                    break
                elif value == CHEAT_GAGNÉ:
                    séquencegagnante.append(value)
                    gagner(séquencegagnante)
                    break
                else:
                    print("ERREUR: Entrez un nombre entier svp")
        if nbEssaie == MAX_ESSAIS + 1:
            perdre(nombre, nbEssaie - 1)

        nbPartieTotal += 1
        nbEssaieTotal += nbEssaie
        nbEssaie = 1
        if not rejouer():
            print(f"Nombre de parties jouées: {nbPartieTotal}")
            print(f"Nombre d'essais effectués: {nbEssaieTotal}")
            print(f"Moyenne d'essais par partie: {nbEssaieTotal / nbPartieTotal}")
            return print("Au revoir!")


if __name__ == '__main__':
    main()
