# ============================================================
#  eda.py — Analyse Exploratoire des Données
# ============================================================

import matplotlib.pyplot as plt
import seaborn as sns
import os
from config import FEATURES

os.makedirs("graphiques", exist_ok=True)

def afficher_distributions(df):
    """Histogramme de chaque variable numérique."""
    fig, axes = plt.subplots(3, 3, figsize=(15, 10))
    axes = axes.flatten()

    for i, col in enumerate(FEATURES):
        axes[i].hist(df[col], bins=30, color='steelblue', edgecolor='white')
        axes[i].set_title(col.replace("_", " ").title())
        axes[i].set_xlabel("Valeur")
        axes[i].set_ylabel("Fréquence")

    # Masquer les axes inutilisés
    for j in range(len(FEATURES), len(axes)):
        axes[j].set_visible(False)

    plt.suptitle("Distribution des variables — Marchés Sénégal", fontsize=14)
    plt.tight_layout()
    plt.savefig("graphiques/distributions.png", dpi=150)
    plt.show()
    print("Graphique sauvegardé : graphiques/distributions.png")

def afficher_correlation(df):
    """Heatmap de corrélation entre les variables."""
    plt.figure(figsize=(9, 7))
    corr = df[FEATURES].corr()
    sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm",
                linewidths=0.5, square=True)
    plt.title("Matrice de Corrélation — Variables Commerces")
    plt.tight_layout()
    plt.savefig("graphiques/correlation.png", dpi=150)
    plt.show()
    print("Graphique sauvegardé : graphiques/correlation.png")

def afficher_boxplots(df):
    """Boxplots par type de commerce."""
    variables = ["chiffre_affaires_mensuel", "surface_m2",
                 "nb_clients_par_jour", "nombre_employes"]

    fig, axes = plt.subplots(2, 2, figsize=(12, 8))
    axes = axes.flatten()

    for i, col in enumerate(variables):
        df.boxplot(column=col, by="type_commerce", ax=axes[i],
                   vert=False, patch_artist=True)
        axes[i].set_title(col.replace("_", " ").title())
        axes[i].set_xlabel("Valeur")

    plt.suptitle("Boxplots par Type de Commerce", fontsize=14)
    plt.tight_layout()
    plt.savefig("graphiques/boxplots.png", dpi=150)
    plt.show()
    print("Graphique sauvegardé : graphiques/boxplots.png")
