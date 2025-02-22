def main():
  """Fonction principale du programme."""
  print("Bienvenue dans le programme de nombres aléatoires !")

  min = int(input("Entrez la valeur minimale : "))
  max = int(input("Entrez la valeur maximale : "))

  nombre_aleatoire = generer_nombre_aleatoire(min, max)
  print("Le nombre aléatoire généré est :", nombre_aleatoire)

if __name__ == "__main__":
  main()