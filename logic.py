import math


class Cercle:
    """Classe simple pour calculer les valeurs d'un cercle."""

    def __init__(self, rayon):
        self.rayon = float(rayon)
        self.verifier_rayon()

    def verifier_rayon(self):
        """Verifie que le rayon est valide."""
        if self.rayon < 0:
            raise ValueError("Le rayon doit etre positif.")

    def aire(self):
        """Calcule l'aire du cercle."""
        return math.pi * self.rayon * self.rayon

    def perimetre(self):
        """Calcule le perimetre du cercle."""
        return 2 * math.pi * self.rayon
