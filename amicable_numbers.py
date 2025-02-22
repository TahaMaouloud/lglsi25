def sum_of_divisors(n):
    """Calcule la somme des diviseurs propres d'un nombre n (hors n lui-même)."""
    return sum([i for i in range(1, n // 2 + 1) if n % i == 0])

def are_amicable(a, b):
    """Vérifie si deux nombres sont amis."""
    return sum_of_divisors(a) == b and sum_of_divisors(b) == a
