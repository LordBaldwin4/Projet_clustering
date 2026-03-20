# ============================================================
#  generate_data.py — Génération du dataset synthétique
#  Contexte : marchés et commerces du Sénégal
# ============================================================

import numpy as np
import pandas as pd
from config import SEED, N_SAMPLES

def generer_donnees():
    np.random.seed(SEED)
    n = N_SAMPLES

    # --- Types de commerces simulés (4 profils réalistes) ---
    # Profil 0 : Petits vendeurs ambulants / étals simples
    # Profil 1 : Boutiques de quartier (dibiteries, épiceries)
    # Profil 2 : Commerces moyens (quincailleries, tissus)
    # Profil 3 : Grands commerçants (grossistes, supérettes)

    profils = np.random.choice([0, 1, 2, 3], size=n, p=[0.30, 0.35, 0.20, 0.15])

    chiffre_affaires = np.where(profils == 0, np.random.normal(150_000,  40_000, n),
                       np.where(profils == 1, np.random.normal(400_000,  80_000, n),
                       np.where(profils == 2, np.random.normal(900_000, 150_000, n),
                                              np.random.normal(2_500_000, 400_000, n))))

    surface = np.where(profils == 0, np.random.normal( 5,  2, n),
              np.where(profils == 1, np.random.normal(15,  5, n),
              np.where(profils == 2, np.random.normal(40, 10, n),
                                     np.random.normal(90, 20, n))))

    employes = np.where(profils == 0, np.random.randint(1, 2, n),
               np.where(profils == 1, np.random.randint(1, 4, n),
               np.where(profils == 2, np.random.randint(3, 8, n),
                                      np.random.randint(7, 20, n))))

    anciennete = np.where(profils == 0, np.random.randint(1,  5, n),
                 np.where(profils == 1, np.random.randint(2, 10, n),
                 np.where(profils == 2, np.random.randint(5, 20, n),
                                        np.random.randint(8, 30, n))))

    stock = np.where(profils == 0, np.random.normal( 50_000,  15_000, n),
            np.where(profils == 1, np.random.normal(200_000,  50_000, n),
            np.where(profils == 2, np.random.normal(600_000, 100_000, n),
                                   np.random.normal(2_000_000, 300_000, n))))

    clients_jour = np.where(profils == 0, np.random.randint(10,  40, n),
                   np.where(profils == 1, np.random.randint(30,  80, n),
                   np.where(profils == 2, np.random.randint(60, 150, n),
                                          np.random.randint(120, 300, n))))

    distance = np.where(profils == 0, np.random.uniform(0.1, 1.0, n),
               np.where(profils == 1, np.random.uniform(0.5, 3.0, n),
               np.where(profils == 2, np.random.uniform(1.0, 5.0, n),
                                      np.random.uniform(0.1, 2.0, n))))

    # Noms de marchés sénégalais
    marches = ["Sandaga", "Tilène", "HLM", "Colobane", "Thiaroye",
               "Pikine", "Rufisque", "Touba", "Thiès", "Ziguinchor"]
    types_commerce = ["Épicerie", "Dibiterie", "Quincaillerie", "Tissus",
                      "Électronique", "Alimentation générale", "Pharmacie",
                      "Boulangerie", "Téléphonie", "Vêtements"]

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
        "profil_reel"                : profils   # pour validation uniquement
    })

    return df

if __name__ == "__main__":
    df = generer_donnees()
    df.to_csv("data_marches_senegal.csv", index=False)
    print(f"Dataset généré : {df.shape[0]} commerces, {df.shape[1]} colonnes")
    print(df.head())
