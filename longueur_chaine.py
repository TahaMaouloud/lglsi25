def string_length(s):
    """Retourne la longueur d'une chaîne de caractères."""
    if not isinstance(s, str):
        raise TypeError("L'entrée doit être une chaîne de caractères.")
    
    return len(s)
#execution
if __name__ == "__main__":
    user_input = input("Entrez une chaîne de caractères : ")
    print(f"La longueur de la chaîne est : {string_length(user_input)}")
