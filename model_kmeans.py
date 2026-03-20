# ============================================================
#  model_kmeans.py — Clustering K-Means
# ============================================================
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from config import SEED, N_CLUSTERS

def methode_coude(X_scaled):
    """
    Teste K de 2 à 10 et trace la courbe d'inertie (méthode du coude).
    Permet de choisir le bon nombre de clusters visuellement.
    """
    inerties = []
    K_range = range(2, 11)  # on teste de 2 à 10 groupes, en dessous de 2 ça n'a pas de sens

    for k in K_range:
        # on entraîne un K-Means pour chaque valeur de K et on récupère son inertie
        # l'inertie mesure à quel point les commerces sont proches de leur centre de groupe
        km = KMeans(n_clusters=k, random_state=SEED, n_init=10)
        km.fit(X_scaled)
        inerties.append(km.inertia_)

    plt.figure(figsize=(8, 5))
    plt.plot(K_range, inerties, marker='o', color='steelblue', linewidth=2)
    plt.title("Méthode du Coude — Choix du nombre de clusters")
    plt.xlabel("Nombre de clusters (K)")
    plt.ylabel("Inertie")
    plt.xticks(K_range)
    plt.grid(True, linestyle='--', alpha=0.5)  # grille discrète pour mieux lire la courbe
    plt.tight_layout()
    # on sauvegarde avant plt.show() sinon matplotlib génère une image vide
    plt.savefig("graphiques/coude.png", dpi=150)
    plt.show()
    print("Graphique sauvegardé : graphiques/coude.png")

def entrainer_kmeans(X_scaled):
    """
    Entraîne le modèle K-Means avec N_CLUSTERS clusters.
    Retourne le modèle et les labels de clusters.
    """
    # n_init=10 veut dire qu'on relance l'algorithme 10 fois avec des points de départ différents
    # on garde le meilleur résultat pour éviter de tomber sur un mauvais découpage par hasard
    km = KMeans(n_clusters=N_CLUSTERS, random_state=SEED, n_init=10)
    labels = km.fit_predict(X_scaled)  # on entraîne et on récupère le groupe de chaque commerce en une seule ligne

    # le score silhouette mesure si chaque commerce est bien dans son groupe
    # un score proche de 1 veut dire que les groupes sont bien séparés et cohérents
    # un score proche de 0 ou négatif veut dire que les frontières sont floues
    score = silhouette_score(X_scaled, labels)

    print(f"\nK-Means entraîné avec K={N_CLUSTERS}")
    print(f"  Score Silhouette : {score:.4f}  (plus proche de 1 = meilleur)")
    print(f"  Inertie          : {km.inertia_:.2f}")

    return km, labels
