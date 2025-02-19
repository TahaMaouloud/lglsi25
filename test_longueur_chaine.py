import unittest
from longueur_chaine import string_length

class TestStringLength(unittest.TestCase):

    def test_normal_string(self):
        """Vérifie la longueur correcte d'une chaîne normale."""
        self.assertEqual(string_length("Hello"), 5)
        self.assertEqual(string_length("Python"), 6)

    def test_empty_string(self):
        """Vérifie que la longueur d'une chaîne vide est 0."""
        self.assertEqual(string_length(""), 0)

    def test_spaces(self):
        """Vérifie que les espaces sont comptés."""
        self.assertEqual(string_length(" "), 1)
        self.assertEqual(string_length("  "), 2)

    def test_special_characters(self):
        """Vérifie que les caractères spéciaux sont bien comptésS"""
        self.assertEqual(string_length("!@#$%^"), 6)

    def test_numeric_string(self):
        """Vérifie que les nombres sous forme de chaînes sont bien comptés."""
        self.assertEqual(string_length("12345"), 5)

    def test_non_string_input(self):
        """Vérifie qu'une erreur est levée pour une entrée qui n'est pas une chaîne."""
        with self.assertRaises(TypeError):
            string_length(123)

        with self.assertRaises(TypeError):
            string_length(None)

if __name__ == "__main__":
    unittest.main()
