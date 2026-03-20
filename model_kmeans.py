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
    K_range = range(2, 11)

    for k in K_range:
        km = KMeans(n_clusters=k, random_state=SEED, n_init=10)
        km.fit(X_scaled)
        inerties.append(km.inertia_)

    plt.figure(figsize=(8, 5))
    plt.plot(K_range, inerties, marker='o', color='steelblue', linewidth=2)
    plt.title("Méthode du Coude — Choix du nombre de clusters")
    plt.xlabel("Nombre de clusters (K)")
    plt.ylabel("Inertie")
    plt.xticks(K_range)
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.savefig("graphiques/coude.png", dpi=150)
    plt.show()
    print("Graphique sauvegardé : graphiques/coude.png")

def entrainer_kmeans(X_scaled):
    """
    Entraîne le modèle K-Means avec N_CLUSTERS clusters.
    Retourne le modèle et les labels de clusters.
    """
    km = KMeans(n_clusters=N_CLUSTERS, random_state=SEED, n_init=10)
    labels = km.fit_predict(X_scaled)

    score = silhouette_score(X_scaled, labels)
    print(f"\nK-Means entraîné avec K={N_CLUSTERS}")
    print(f"  Score Silhouette : {score:.4f}  (plus proche de 1 = meilleur)")
    print(f"  Inertie          : {km.inertia_:.2f}")

    return km, labels
