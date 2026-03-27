import tkinter as tk
from tkinter import messagebox

from logic import Cercle


class ApplicationCercle:
    """Interface graphique simple pour le calcul du cercle."""

    def __init__(self, fenetre):
        self.fenetre = fenetre
        self.fenetre.title("Calcul du cercle")
        self.fenetre.geometry("460x430")
        self.fenetre.minsize(460, 430)
        self.fenetre.resizable(False, False)
        self.fenetre.configure(bg="#eef2f7")

        self.creer_widgets()

    def creer_widgets(self):
        """Cree les elements de l'interface."""
        cadre = tk.Frame(
            self.fenetre,
            bg="white",
            bd=0,
            padx=24,
            pady=24
        )
        cadre.pack(padx=24, pady=24, fill="both", expand=True)

        titre = tk.Label(
            cadre,
            text="Cercle",
            font=("Arial", 18, "bold"),
            bg="white",
            fg="#1f2937"
        )
        titre.pack(pady=(0, 20))

        bloc_saisie = tk.Frame(cadre, bg="white")
        bloc_saisie.pack(fill="x", pady=(0, 18))

        label_rayon = tk.Label(
            bloc_saisie,
            text="Rayon (cm)",
            font=("Arial", 11),
            bg="white",
            fg="#374151"
        )
        label_rayon.pack(anchor="w")

        self.entree_rayon = tk.Entry(
            bloc_saisie,
            font=("Arial", 12),
            relief="solid",
            bd=1
        )
        self.entree_rayon.pack(fill="x", pady=(8, 0), ipady=5)

        bouton = tk.Button(
            cadre,
            text="Calculer",
            font=("Arial", 11, "bold"),
            bg="#2563eb",
            fg="white",
            activebackground="#1d4ed8",
            activeforeground="white",
            relief="flat",
            command=self.calculer
        )
        bouton.pack(fill="x", pady=(0, 18), ipady=6)

        zone_resultats = tk.LabelFrame(
            cadre,
            text="Resultats",
            font=("Arial", 11, "bold"),
            bg="white",
            fg="#1f2937",
            padx=14,
            pady=12
        )
        zone_resultats.pack(fill="x")

        ligne_aire = tk.Frame(zone_resultats, bg="white")
        ligne_aire.pack(fill="x", pady=(0, 8))

        label_aire = tk.Label(
            ligne_aire,
            text="Aire :",
            font=("Arial", 11),
            bg="white",
            fg="#374151"
        )
        label_aire.pack(side="left")

        self.resultat_aire = tk.Label(
            ligne_aire,
            text="--",
            font=("Arial", 11, "bold"),
            bg="white",
            fg="#111827"
        )
        self.resultat_aire.pack(side="right")

        ligne_perimetre = tk.Frame(zone_resultats, bg="white")
        ligne_perimetre.pack(fill="x")

        label_perimetre = tk.Label(
            ligne_perimetre,
            text="Perimetre :",
            font=("Arial", 11),
            bg="white",
            fg="#374151"
        )
        label_perimetre.pack(side="left")

        self.resultat_perimetre = tk.Label(
            ligne_perimetre,
            text="--",
            font=("Arial", 11, "bold"),
            bg="white",
            fg="#111827"
        )
        self.resultat_perimetre.pack(side="right")

        self.entree_rayon.focus()

    def calculer(self):
        """Recupere le rayon puis affiche le resultat."""
        valeur = self.entree_rayon.get().strip().replace(",", ".")

        try:
            cercle = Cercle(valeur)
            aire = cercle.aire()
            perimetre = cercle.perimetre()

            self.resultat_aire.config(text=f"{aire:.2f} cm2")
            self.resultat_perimetre.config(text=f"{perimetre:.2f} cm")
        except ValueError:
            messagebox.showerror(
                "Erreur",
                "Veuillez entrer un nombre valide et positif."
            )
            self.resultat_aire.config(text="--")
            self.resultat_perimetre.config(text="--")


def main():
    """Point d'entree du programme."""
    fenetre = tk.Tk()
    ApplicationCercle(fenetre)
    fenetre.mainloop()


if __name__ == "__main__":
    main()
