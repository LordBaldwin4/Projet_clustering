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

# on s'assure que le dossier existe avant de commencer, pour ne pas avoir d'erreur au moment de sauvegarder les graphiques
os.makedirs("graphiques", exist_ok=True)

print("=" * 60)
print("  CLUSTERING — MARCHÉS ET COMMERCES DU SÉNÉGAL")
print("=" * 60)

# ----------------------------------------------------------
# ÉTAPE 1 : Génération des données
# ----------------------------------------------------------
print("\n[1/5] Génération des données synthétiques...")
# on fabrique 500 commerces fictifs mais réalistes, inspirés des vrais marchés sénégalais
df = generer_donnees()
# on sauvegarde une copie brute avant tout traitement, utile si on veut revenir en arrière
df.to_csv("data_marches_senegal.csv", index=False)
print(f"      {df.shape[0]} commerces générés, {df.shape[1]} variables")

# ----------------------------------------------------------
# ÉTAPE 2 : Analyse Exploratoire (EDA)
# ----------------------------------------------------------
print("\n[2/5] Analyse exploratoire des données (EDA)...")
# un premier coup d'œil sur les chiffres : moyenne, min, max, écart-type...
# ça permet de repérer tout de suite si quelque chose cloche
print("\n--- Aperçu du dataset ---")
print(df.describe().round(0).to_string())

# on trace les distributions pour voir comment chaque variable se répartit
afficher_distributions(df)
# on regarde si certaines variables sont fortement liées entre elles
afficher_correlation(df)
# on compare les types de commerces sur les variables clés
afficher_boxplots(df)

# ----------------------------------------------------------
# ÉTAPE 3 : Prétraitement
# ----------------------------------------------------------
print("\n[3/5] Prétraitement et standardisation...")
# on met toutes les variables à la même échelle pour que K-Means ne soit pas biaisé
# par exemple, le chiffre d'affaires en FCFA est bien plus grand que la surface en m²
X_scaled, scaler = preparer_donnees(df)

# ----------------------------------------------------------
# ÉTAPE 4 : Clustering K-Means
# ----------------------------------------------------------
print("\n[4/5] Entraînement du modèle K-Means...")
print("      → Affichage de la méthode du coude...")
# on teste plusieurs valeurs de K et on cherche le "coude" dans la courbe d'inertie
# c'est là où ajouter un groupe de plus n'apporte plus grand chose
methode_coude(X_scaled)

print("      → Entraînement avec K=4 clusters...")
# on a choisi K=4 d'après la méthode du coude : c'est le nombre de groupes qui fait le plus sens
modele, labels = entrainer_kmeans(X_scaled)

# on colle les numéros de clusters directement dans le dataset pour les analyses suivantes
df["cluster"] = labels

# on sauvegarde cette version enrichie avec les clusters pour pouvoir la réutiliser plus tard
df.to_csv("data_marches_clusters.csv", index=False)
print("      Dataset avec clusters sauvegardé : data_marches_clusters.csv")

# ----------------------------------------------------------
# ÉTAPE 5 : Visualisation des résultats
# ----------------------------------------------------------
print("\n[5/5] Visualisation des clusters...")
# nuage de points pour voir comment les groupes se séparent dans l'espace
scatter_clusters(df)
# radar ou barres pour comprendre le profil économique de chaque cluster
profils_clusters(df)
# camembert ou barres pour voir la taille de chaque groupe
repartition_clusters(df)
# boxplots pour comparer la dispersion des variables entre les clusters
boxplot_par_cluster(df)

# ----------------------------------------------------------
# RÉSUMÉ FINAL
# ----------------------------------------------------------
print("\n" + "=" * 60)
print("  RÉSULTATS — SEGMENTATION DES COMMERCES")
print("=" * 60)

# on donne des noms parlants à chaque cluster pour que le résumé soit lisible
# ces noms correspondent aux 4 profils qu'on retrouve vraiment dans les marchés sénégalais
noms = {0: "Petits vendeurs", 1: "Boutiques quartier",
        2: "Commerces moyens", 3: "Grands commerçants"}

# on calcule les moyennes clés par cluster pour avoir une vue d'ensemble claire
resume = df.groupby("cluster").agg(
    nb_commerces    = ("id_commerce", "count"),
    ca_moyen_fcfa   = ("chiffre_affaires_mensuel", "mean"),
    surface_moy_m2  = ("surface_m2", "mean"),
    employes_moy    = ("nombre_employes", "mean"),
    clients_par_jour= ("nb_clients_par_jour", "mean"),
).round(0)

# on remplace les numéros de clusters par leurs vrais noms pour que le tableau soit compréhensible
resume.index = [noms.get(i, f"Cluster {i}") for i in resume.index]
print(resume.to_string())

print("\nGraphiques sauvegardés dans le dossier : graphiques/")
print("Projet terminé avec succès.")
