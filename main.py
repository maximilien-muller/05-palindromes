import string
from unidecode import unidecode
#### Fonction secondaire
#fonction palindrome
def ispalindrome(p):
    """
    Vérifie si une chaîne est un palindrome.

    Args:
        p (str): La chaîne à tester.

    Returns:
        bool: True si la chaîne est un palindrome, sinon False.
    """

    # Nettoyage de la chaîne
    p = unidecode(p).lower().replace(" ", "").translate(str.maketrans('', '', string.punctuation))

    # votre code ici

    # Cas de base : chaîne vide ou un seul caractère
    if len(p) <= 1 : return True #impair et pair

    # Vérifie les extrémités et appelle récursivement
    if p[0] == p[-1] :
        return ispalindrome(p[1 : -1])

    return False

#### Fonction principale
def main():
    """
    Fonction principale pour tester les palindromes.
    """
    # vos appels à la fonction secondaire ici
    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))

#blaaa
if __name__ == "__main__":
    #appel main
    main()