# ============================================================
#  visualisation.py — Visualisation des clusters
# ============================================================
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from config import FEATURES, N_CLUSTERS

# une couleur par segment pour que les graphiques soient cohérents d'un bout à l'autre du projet
COULEURS = ["#E74C3C", "#3498DB", "#2ECC71", "#F39C12"]

# on donne des vrais noms aux clusters pour que les graphiques soient lisibles par n'importe qui
# ces noms correspondent aux 4 profils qu'on retrouve dans les marchés sénégalais
NOMS_CLUSTERS = {
    0: "Petits vendeurs",
    1: "Boutiques quartier",
    2: "Commerces moyens",
    3: "Grands commerçants"
}

def scatter_clusters(df, label_col="cluster"):
    """
    Nuage de points : Chiffre d'affaires vs Nb clients/jour
    coloré par cluster.
    """
    plt.figure(figsize=(9, 6))

    # on trace chaque cluster séparément pour pouvoir les colorer différemment
    # mask permet de filtrer uniquement les commerces du groupe k
    for k in range(N_CLUSTERS):
        mask = df[label_col] == k
        plt.scatter(
            df.loc[mask, "chiffre_affaires_mensuel"],
            df.loc[mask, "nb_clients_par_jour"],
            c=COULEURS[k],
            label=NOMS_CLUSTERS.get(k, f"Cluster {k}"),
            alpha=0.6,          # un peu de transparence pour voir les points qui se chevauchent
            edgecolors='white',
            linewidths=0.4,
            s=60
        )

    plt.xlabel("Chiffre d'affaires mensuel (FCFA)")
    plt.ylabel("Nombre de clients par jour")
    plt.title("Segmentation des Commerces — Marchés du Sénégal")
    plt.legend(title="Segment")
    plt.grid(True, linestyle='--', alpha=0.3)
    plt.tight_layout()
    # on sauvegarde avant plt.show() sinon l'image exportée est vide
    plt.savefig("graphiques/scatter_clusters.png", dpi=150)
    plt.show()
    print("Graphique sauvegardé : graphiques/scatter_clusters.png")

def profils_clusters(df, label_col="cluster"):
    """
    Graphique en barres : moyenne de chaque variable par cluster.
    Permet d'interpréter le profil de chaque segment.
    """
    # on calcule la moyenne de chaque variable pour chaque groupe
    # c'est ce qui permet de dire "les grands commerçants ont en moyenne X employés"
    moyennes = df.groupby(label_col)[FEATURES].mean()

    # on remplace les numéros de clusters par leurs noms pour que l'axe soit compréhensible
    moyennes.index = [NOMS_CLUSTERS.get(i, f"Cluster {i}") for i in moyennes.index]

    # .T transpose le tableau : les variables passent en lignes et les segments en colonnes
    # comme ça chaque groupe de barres représente une variable
    ax = moyennes.T.plot(kind='bar', figsize=(12, 6),
                         color=COULEURS[:N_CLUSTERS], edgecolor='white')

    plt.title("Profil Moyen par Segment de Commerce")
    plt.xlabel("Variable")
    plt.ylabel("Valeur moyenne")
    plt.xticks(rotation=30, ha='right')  # on incline les labels pour éviter qu'ils se chevauchent
    plt.legend(title="Segment", bbox_to_anchor=(1.01, 1))  # légende placée hors du graphique
    plt.tight_layout()
    plt.savefig("graphiques/profils_clusters.png", dpi=150)
    plt.show()
    print("Graphique sauvegardé : graphiques/profils_clusters.png")

def repartition_clusters(df, label_col="cluster"):
    """Camembert de la répartition des commerces par cluster."""
    # on compte combien de commerces appartiennent à chaque groupe
    counts = df[label_col].value_counts().sort_index()
    labels = [NOMS_CLUSTERS.get(i, f"Cluster {i}") for i in counts.index]

    plt.figure(figsize=(7, 7))
    plt.pie(
        counts.values,
        labels=labels,
        colors=COULEURS[:N_CLUSTERS],
        autopct='%1.1f%%',      # affiche le pourcentage dans chaque part
        startangle=140,          # on commence à 140° pour un meilleur équilibre visuel
        wedgeprops=dict(edgecolor='white', linewidth=1.5)  # bordures blanches pour séparer les parts
    )
    plt.title("Répartition des Commerces par Segment")
    plt.tight_layout()
    plt.savefig("graphiques/repartition.png", dpi=150)
    plt.show()
    print("Graphique sauvegardé : graphiques/repartition.png")

def boxplot_par_cluster(df, label_col="cluster"):
    """Boxplots des variables clés par cluster."""
    # on choisit les 4 variables qui résument le mieux les différences entre les segments
    variables = ["chiffre_affaires_mensuel", "surface_m2",
                 "nb_clients_par_jour", "stock_moyen_fcfa"]

    fig, axes = plt.subplots(2, 2, figsize=(12, 8))
    axes = axes.flatten()

    # on crée une colonne avec les vrais noms pour que l'axe X soit lisible
    df_plot = df.copy()
    df_plot["segment"] = df_plot[label_col].map(NOMS_CLUSTERS)

    for i, col in enumerate(variables):
        sns.boxplot(data=df_plot, x="segment", y=col,
                    palette=COULEURS[:N_CLUSTERS], ax=axes[i])
        axes[i].set_title(col.replace("_", " ").title())
        axes[i].set_xlabel("")  # on enlève le label X car les noms de segments suffisent
        axes[i].tick_params(axis='x', rotation=15)  # légère rotation pour éviter les chevauchements

    plt.suptitle("Distribution des Variables par Segment", fontsize=14)
    plt.tight_layout()
    plt.savefig("graphiques/boxplot_clusters.png", dpi=150)
    plt.show()
    print("Graphique sauvegardé : graphiques/boxplot_clusters.png")
