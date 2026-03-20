# ============================================================
# eda.py — Analyse Exploratoire des Données
# Marchés et commerces du Sénégal
# ============================================================

import matplotlib.pyplot as plt
import seaborn as sns
import os
from config import FEATURES

# On crée le dossier de sortie s'il n'existe pas encore
os.makedirs("graphiques", exist_ok=True)


def afficher_distributions(df):
    """
    Trace un histogramme pour chaque variable numérique du dataset.
    Permet de visualiser comment les valeurs se répartissent
    sur l'ensemble des 500 commerces.
    """
    fig, axes = plt.subplots(3, 3, figsize=(15, 10))
    axes = axes.flatten()

    for i, col in enumerate(FEATURES):
        axes[i].hist(df[col], bins=30, color='steelblue', edgecolor='white')

        # On rend le titre lisible en remplaçant les underscores
        axes[i].set_title(col.replace("_", " ").title())
        axes[i].set_xlabel("Valeur")
        axes[i].set_ylabel("Fréquence")

    # On cache les cases vides si on a moins de 9 variables
    for j in range(len(FEATURES), len(axes)):
        axes[j].set_visible(False)

    plt.suptitle("Distribution des variables — Marchés Sénégal", fontsize=14)
    plt.tight_layout()

    # Sauvegarde + affichage
    plt.savefig("graphiques/distributions.png", dpi=150)
    plt.show()
    print("Graphique sauvegardé : graphiques/distributions.png")


def afficher_correlation(df):
    """
    Affiche une heatmap de corrélation entre toutes les variables.
    Utile pour repérer les liens forts entre revenus, surface,
    nombre d'employés, etc.
    """
    plt.figure(figsize=(9, 7))

    # Calcul de la matrice de corrélation
    matrice_corr = df[FEATURES].corr()

    sns.heatmap(
        matrice_corr,
        annot=True,        # Affiche les valeurs dans chaque case
        fmt=".2f",         # Arrondi à 2 décimales
        cmap="coolwarm",   # Rouge = corrélation positive, bleu = négative
        linewidths=0.5,
        square=True
    )

    plt.title("Matrice de Corrélation — Variables Commerces")
    plt.tight_layout()

    plt.savefig("graphiques/correlation.png", dpi=150)
    plt.show()
    print("Graphique sauvegardé : graphiques/correlation.png")


def afficher_boxplots(df):
    """
    Trace des boxplots pour comparer les commerces selon leur type.
    On regarde 4 variables clés : chiffre d'affaires, surface,
    clients par jour et nombre d'employés.
    """
    variables_cles = [
        "chiffre_affaires_mensuel",
        "surface_m2",
        "nb_clients_par_jour",
        "nombre_employes"
    ]

    fig, axes = plt.subplots(2, 2, figsize=(12, 8))
    axes = axes.flatten()

    for i, col in enumerate(variables_cles):
        # Boxplot horizontal pour mieux lire les étiquettes de type
        df.boxplot(
            column=col,
            by="type_commerce",
            ax=axes[i],
            vert=False,
            patch_artist=True   # Remplit les boîtes de couleur
        )
        axes[i].set_title(col.replace("_", " ").title())
        axes[i].set_xlabel("Valeur")

    plt.suptitle("Boxplots par Type de Commerce", fontsize=14)
    plt.tight_layout()

    plt.savefig("graphiques/boxplots.png", dpi=150)
    plt.show()
    print("Graphique sauvegardé : graphiques/boxplots.png")
