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
    # on extrait uniquement les colonnes qui vont servir au clustering
    # on fait une copie pour ne pas modifier le dataset original par accident
    X = df[FEATURES].copy()

    # K-Means ne sait pas gérer les valeurs manquantes, il planterait directement
    # donc on vérifie avant de continuer, et si besoin on remplace par la moyenne de la colonne
    if X.isnull().sum().sum() > 0:
        print("Attention : valeurs manquantes détectées, remplacement par la moyenne.")
        X = X.fillna(X.mean())

    # le chiffre d'affaires est en millions de FCFA, la surface en m², les employés en unités...
    # sans standardisation, K-Means serait dominé par les grandes valeurs et ignorerait les petites
    # StandardScaler ramène tout à la même échelle : moyenne = 0, écart-type = 1
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # on remet les données dans un DataFrame pour garder les noms de colonnes
    # plus pratique pour déboguer et vérifier les résultats
    X_scaled_df = pd.DataFrame(X_scaled, columns=FEATURES)

    print("Prétraitement terminé.")
    print(f"  Dimensions : {X_scaled_df.shape}")
    print(f"  Variables  : {list(FEATURES)}")

    return X_scaled_df, scaler
