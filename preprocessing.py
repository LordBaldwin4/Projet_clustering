# ============================================================
#  preprocessing.py — Préparation des données pour le clustering
# ============================================================

import pandas as pd
from sklearn.preprocessing import StandardScaler
from config import FEATURES

def preparer_donnees(df):
    """
    Extrait les features et applique la standardisation.
    Le clustering est sensible aux échelles → StandardScaler obligatoire.
    """
    X = df[FEATURES].copy()

    # Vérification des valeurs manquantes
    if X.isnull().sum().sum() > 0:
        print("Attention : valeurs manquantes détectées, remplacement par la moyenne.")
        X = X.fillna(X.mean())

    # Standardisation : moyenne=0, écart-type=1
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    X_scaled_df = pd.DataFrame(X_scaled, columns=FEATURES)

    print("Prétraitement terminé.")
    print(f"  Dimensions : {X_scaled_df.shape}")
    print(f"  Variables  : {list(FEATURES)}")

    return X_scaled_df, scaler
