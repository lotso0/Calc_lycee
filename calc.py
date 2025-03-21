def calculatrice(nb1, nb2, opp):
    if opp == "+":  # Vérifie si l'opérateur est "+"
        return nb1 + nb2
    elif opp == "-":  # Vérifie si l'opérateur est "-"
        return nb1 - nb2
    elif opp == "*":  # Vérifie si l'opérateur est "*"
        return nb1 * nb2
    elif opp == "/":  # Vérifie si l'opérateur est "/"
        if nb2 != 0:  # Évite la division par zéro
            return nb1 / nb2
        else:
            return "Erreur: Division par zéro"
    else:
        return "Erreur: Opérateur invalide"  # Message d'erreur si l'opérateur n'est pas reconnu

nb1 = int(input("Entrez votre premier nombre: "))  # Choisir le premier nombre
nb2 = int(input("Entrez votre deuxième nombre: "))  # Choisir le deuxième nombre
opp = input("Entrez votre opérateur (+, -, *, /): ")  # Choisir l'opérateur

result = calculatrice(nb1, nb2, opp)
print(f"Le résultat est: {result}")  # Affiche le résultat
print("Merci de choisir une opération")
