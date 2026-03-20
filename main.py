# ============================================================
#  main.py — Point d'entrée du projet clustering
#  Segmentation des Marchés et Commerces du Sénégal
# ============================================================

import os
import pandas as pd

from generate_data   import generer_donnees
from preprocessing   import preparer_donnees
from model_kmeans    import methode_coude, entrainer_kmeans
from eda             import afficher_distributions, afficher_correlation, afficher_boxplots
from visualisation   import (scatter_clusters, profils_clusters,
                              repartition_clusters, boxplot_par_cluster)

# Création du dossier graphiques
os.makedirs("graphiques", exist_ok=True)

print("=" * 60)
print("  CLUSTERING — MARCHÉS ET COMMERCES DU SÉNÉGAL")
print("=" * 60)

# ----------------------------------------------------------
# ÉTAPE 1 : Génération des données
# ----------------------------------------------------------
print("\n[1/5] Génération des données synthétiques...")
df = generer_donnees()
df.to_csv("data_marches_senegal.csv", index=False)
print(f"      {df.shape[0]} commerces générés, {df.shape[1]} variables")

# ----------------------------------------------------------
# ÉTAPE 2 : Analyse Exploratoire (EDA)
# ----------------------------------------------------------
print("\n[2/5] Analyse exploratoire des données (EDA)...")
print("\n--- Aperçu du dataset ---")
print(df.describe().round(0).to_string())

afficher_distributions(df)
afficher_correlation(df)
afficher_boxplots(df)

# ----------------------------------------------------------
# ÉTAPE 3 : Prétraitement
# ----------------------------------------------------------
print("\n[3/5] Prétraitement et standardisation...")
X_scaled, scaler = preparer_donnees(df)

# ----------------------------------------------------------
# ÉTAPE 4 : Clustering K-Means
# ----------------------------------------------------------
print("\n[4/5] Entraînement du modèle K-Means...")
print("      → Affichage de la méthode du coude...")
methode_coude(X_scaled)

print("      → Entraînement avec K=4 clusters...")
modele, labels = entrainer_kmeans(X_scaled)

# Ajout des labels au dataset original
df["cluster"] = labels

# Sauvegarde du dataset avec clusters
df.to_csv("data_marches_clusters.csv", index=False)
print("      Dataset avec clusters sauvegardé : data_marches_clusters.csv")

# ----------------------------------------------------------
# ÉTAPE 5 : Visualisation des résultats
# ----------------------------------------------------------
print("\n[5/5] Visualisation des clusters...")
scatter_clusters(df)
profils_clusters(df)
repartition_clusters(df)
boxplot_par_cluster(df)

# ----------------------------------------------------------
# RÉSUMÉ FINAL
# ----------------------------------------------------------
print("\n" + "=" * 60)
print("  RÉSULTATS — SEGMENTATION DES COMMERCES")
print("=" * 60)

noms = {0: "Petits vendeurs", 1: "Boutiques quartier",
        2: "Commerces moyens", 3: "Grands commerçants"}

resume = df.groupby("cluster").agg(
    nb_commerces    = ("id_commerce", "count"),
    ca_moyen_fcfa   = ("chiffre_affaires_mensuel", "mean"),
    surface_moy_m2  = ("surface_m2", "mean"),
    employes_moy    = ("nombre_employes", "mean"),
    clients_par_jour= ("nb_clients_par_jour", "mean"),
).round(0)

resume.index = [noms.get(i, f"Cluster {i}") for i in resume.index]
print(resume.to_string())

print("\nGraphiques sauvegardés dans le dossier : graphiques/")
print("Projet terminé avec succès.")
