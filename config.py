# ============================================================
#  config.py — Paramètres globaux du projet
# ============================================================

SEED       = 42      # Reproductibilité des résultats
N_SAMPLES  = 500     # Nombre de commerces simulés
N_CLUSTERS = 4       # Nombre de clusters K-Means

# Variables utilisées pour le clustering
FEATURES = [
    "chiffre_affaires_mensuel",
    "surface_m2",
    "nombre_employes",
    "anciennete_annees",
    "stock_moyen_fcfa",
    "nb_clients_par_jour",
    "distance_marche_central_km",
]
