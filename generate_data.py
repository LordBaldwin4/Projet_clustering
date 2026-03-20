# ============================================================
#  generate_data.py — Génération du dataset synthétique
#  Contexte : marchés et commerces du Sénégal
# ============================================================

import numpy as np
import pandas as pd
from config import SEED, N_SAMPLES

def generer_donnees():
    np.random.seed(SEED)  # on fixe la graine pour que les données soient les mêmes à chaque exécution
    n = N_SAMPLES

    # --- Types de commerces simulés (4 profils réalistes) ---
    # on a défini 4 types de vendeurs qu'on croise vraiment dans les marchés sénégalais :
    # Profil 0 : les petits vendeurs ambulants, ceux qui posent leur étal par terre
    # Profil 1 : les boutiques de quartier classiques, épiceries, dibiteries du coin
    # Profil 2 : les commerces un peu plus établis, quincailleries, vendeurs de tissus
    # Profil 3 : les grands commerçants, grossistes et supérettes bien installés

    # on tire au sort un profil pour chaque commerce en respectant leur proportion réelle
    # 30% de petits vendeurs, 35% de boutiques, 20% moyens, 15% grands
    profils = np.random.choice([0, 1, 2, 3], size=n, p=[0.30, 0.35, 0.20, 0.15])

    # le chiffre d'affaires mensuel varie beaucoup selon le profil
    # un petit vendeur tourne autour de 150 000 FCFA, un grand commerçant peut dépasser 2,5 millions
    chiffre_affaires = np.where(profils == 0, np.random.normal(150_000,  40_000, n),
                       np.where(profils == 1, np.random.normal(400_000,  80_000, n),
                       np.where(profils == 2, np.random.normal(900_000, 150_000, n),
                                              np.random.normal(2_500_000, 400_000, n))))

    # la surface suit la même logique : un étal fait à peine 5 m², un grand commerce peut dépasser 90 m²
    surface = np.where(profils == 0, np.random.normal( 5,  2, n),
              np.where(profils == 1, np.random.normal(15,  5, n),
              np.where(profils == 2, np.random.normal(40, 10, n),
                                     np.random.normal(90, 20, n))))

    # le nombre d'employés : souvent seul pour les petits, jusqu'à une vingtaine pour les grands
    employes = np.where(profils == 0, np.random.randint(1, 2, n),
               np.where(profils == 1, np.random.randint(1, 4, n),
               np.where(profils == 2, np.random.randint(3, 8, n),
                                      np.random.randint(7, 20, n))))

    # l'ancienneté reflète la stabilité du commerce : les grands sont souvent là depuis plus longtemps
    anciennete = np.where(profils == 0, np.random.randint(1,  5, n),
                 np.where(profils == 1, np.random.randint(2, 10, n),
                 np.where(profils == 2, np.random.randint(5, 20, n),
                                        np.random.randint(8, 30, n))))

    # le stock moyen en FCFA : un petit vendeur stocke peu, un grossiste peut avoir 2 millions de stock
    stock = np.where(profils == 0, np.random.normal( 50_000,  15_000, n),
            np.where(profils == 1, np.random.normal(200_000,  50_000, n),
            np.where(profils == 2, np.random.normal(600_000, 100_000, n),
                                   np.random.normal(2_000_000, 300_000, n))))

    # le nombre de clients par jour : de 10 pour un petit étal à plus de 200 pour un grand commerce
    clients_jour = np.where(profils == 0, np.random.randint(10,  40, n),
                   np.where(profils == 1, np.random.randint(30,  80, n),
                   np.where(profils == 2, np.random.randint(60, 150, n),
                                          np.random.randint(120, 300, n))))

    # la distance au marché central en km : les petits vendeurs restent souvent très proches
    distance = np.where(profils == 0, np.random.uniform(0.1, 1.0, n),
               np.where(profils == 1, np.random.uniform(0.5, 3.0, n),
               np.where(profils == 2, np.random.uniform(1.0, 5.0, n),
                                      np.random.uniform(0.1, 2.0, n))))

    # on liste les vrais noms de marchés sénégalais pour que les données semblent authentiques
    marches = ["Sandaga", "Tilène", "HLM", "Colobane", "Thiaroye",
               "Pikine", "Rufisque", "Touba", "Thiès", "Ziguinchor"]

    # et les types de commerces qu'on croise réellement dans ces marchés
    types_commerce = ["Épicerie", "Dibiterie", "Quincaillerie", "Tissus",
                      "Électronique", "Alimentation générale", "Pharmacie",
                      "Boulangerie", "Téléphonie", "Vêtements"]

    # on assemble toutes les colonnes dans un DataFrame propre
    # clip(min=...) sert à éviter les valeurs négatives ou absurdes dues au hasard
    df = pd.DataFrame({
        "id_commerce"                : range(1, n + 1),
        "marche"                     : np.random.choice(marches, n),
        "type_commerce"              : np.random.choice(types_commerce, n),
        "chiffre_affaires_mensuel"   : chiffre_affaires.astype(int).clip(min=50_000),
        "surface_m2"                 : surface.astype(int).clip(min=2),
        "nombre_employes"            : employes.clip(min=1),
        "anciennete_annees"          : anciennete.clip(min=1),
        "stock_moyen_fcfa"           : stock.astype(int).clip(min=10_000),
        "nb_clients_par_jour"        : clients_jour.clip(min=5),
        "distance_marche_central_km" : distance.round(2).clip(min=0.1),
        "profil_reel"                : profils   # on garde le vrai profil pour vérifier les résultats du clustering
    })

    return df

if __name__ == "__main__":
    df = generer_donnees()
    df.to_csv("data_marches_senegal.csv", index=False)  # on exporte tout dans un fichier CSV
    print(f"Dataset généré : {df.shape[0]} commerces, {df.shape[1]} colonnes")
    print(df.head())  # petit aperçu des premières lignes pour vérifier que tout est bon
