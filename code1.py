#Voici un exemple de code en Python qui génère une liste de nombres aléatoires, calcule leur somme et leur moyenne, et affiche le résultat :

import random

# Génération de la liste de nombres aléatoires
random_list = [random.randint(0, 100) for _ in range(10)]

# Calcul de la somme des nombres
total_sum = sum(random_list)

# Calcul de la moyenne des nombres
average = total_sum / len(random_list)

# Affichage de la liste de nombres
print("Liste de nombres générés : ", random_list)

# Affichage de la somme des nombres
print("La somme des nombres est : ", total_sum)

# Affichage de la moyenne des nombres
print("La moyenne des nombres est : ", average)
