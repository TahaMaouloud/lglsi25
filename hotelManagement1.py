from abc import ABC, abstractmethod

class Chambre(ABC):
    nb_chambres = 0

    def __init__(self, id, type, prix_nuit):
        self.id = id
        self.type = type
        self.prix_nuit = prix_nuit
        Chambre.nb_chambres += 1

    @abstractmethod
    def calculer_prix(self, nb_nuits):
        pass

    def afficher_details(self):
        return f"id: {self.id} type: {self.type} prixNuit: {self.prix_nuit}"


class ChambreStandard(Chambre):
    def __init__(self, id, type, prix_nuit, capacite):
        super().__init__(id, type, prix_nuit)
        self.capacite = capacite

    def calculer_prix(self, nb_nuits):
        return nb_nuits * self.prix_nuit


class Suite(Chambre):
    def __init__(self, id, type, prix_nuit, jacuzzi, vue_sur_mer):
        super().__init__(id, type, prix_nuit)
        self.jacuzzi = jacuzzi
        self.vue_sur_mer = vue_sur_mer

    def calculer_prix(self, nb_nuits):
        if self.jacuzzi or self.vue_sur_mer:
            return self.prix_nuit * nb_nuits * 1.10  # 10% extra for jacuzzi or sea view
        else:
            return nb_nuits * self.prix_nuit

