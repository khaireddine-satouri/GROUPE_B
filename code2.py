#Code en Python qui permet de trouver tous les nombres premiers jusqu'à une limite donnée en utilisant le crible d'Ératosthène 

def eratosthenes_sieve(n):
    """Retourne une liste de tous les nombres premiers jusqu'à n"""
    prime_list = [True] * (n + 1)
    prime_list[0] = prime_list[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if prime_list[i]:
            for j in range(i * i, n + 1, i):
                prime_list[j] = False

    return [i for i in range(n + 1) if prime_list[i]]

# Demander à l'utilisateur d'entrer une limite supérieure pour la recherche de nombres premiers
limit = int(input("Entrez une limite supérieure pour la recherche de nombres premiers : "))

# Appeler la fonction eratosthenes_sieve pour trouver tous les nombres premiers jusqu'à la limite
prime_numbers = eratosthenes_sieve(limit)

# Afficher les nombres premiers trouvés
print("Les nombres premiers jusqu'à", limit, "sont : ")
for prime in prime_numbers:
    print(prime)
