# 🛒 Clustering des Marchés et Commerces du Sénégal

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-Clustering-orange?logo=scikit-learn&logoColor=white)
![Niveau](https://img.shields.io/badge/Niveau-Licence%202-purple)
![License](https://img.shields.io/badge/Licence-MIT-green)

> Segmentation non supervisée de commerces issus des marchés sénégalais (Sandaga, Tilène, HLM, Colobane…)
> à l'aide de l'algorithme **K-Means**, sur des données synthétiques réalistes.

---

## 🎯 Objectif du projet

Identifier des **groupes homogènes de commerces** à partir de leurs caractéristiques économiques
(chiffre d'affaires, surface, nombre d'employés, stock…) afin d'aider à :

- Mieux cibler les politiques de soutien aux commerçants
- Adapter les offres de microcrédit selon le profil
- Comprendre la structure économique des marchés locaux

---

## 📊 Résultats — 4 segments identifiés

| Segment | Nb commerces | CA moyen (FCFA) | Surface moy. | Employés moy. | Clients/jour |
|---|---|---|---|---|---|
| Petits vendeurs | ~150 | 150 000 | 5 m² | 1 | 20 |
| Boutiques de quartier | ~175 | 400 000 | 15 m² | 2 | 50 |
| Commerces moyens | ~100 | 900 000 | 40 m² | 5 | 100 |
| Grands commerçants | ~75 | 2 500 000 | 90 m² | 12 | 200 |

---

## ⚙️ Fonctionnement au lancement

Quand tu exécutes `main.py`, voici ce qui se passe dans l'ordre :

1. Génération des données synthétiques (500 commerces)
2. Analyse exploratoire : distributions, corrélations, boxplots
3. Prétraitement : standardisation des variables
4. Méthode du coude → choix de K=4
5. Entraînement K-Means → affectation des clusters
6. Visualisation : scatter, profils, camembert, boxplots

> Chaque graphique s'ouvre dans une fenêtre → **ferme-la** pour passer à la suivante.
> Tous les graphiques sont aussi **sauvegardés automatiquement** dans `graphiques/`.

---

## 📁 Structure du projet

```
clustering-marches-senegal/
│
├── config.py           # Paramètres globaux (K, seed, features)
├── generate_data.py    # Génération du dataset synthétique sénégalais
├── preprocessing.py    # Standardisation des données (StandardScaler)
├── model_kmeans.py     # Méthode du coude + entraînement K-Means
├── eda.py              # Analyse exploratoire (distributions, corrélation, boxplots)
├── visualisation.py    # Visualisation des clusters (scatter, profils, camembert)
├── main.py             # ← POINT D'ENTRÉE — pipeline complet
├── requirements.txt    # Dépendances Python
└── README.md
```

---

## 🚀 Installation et lancement

### Étape 1 — Cloner le projet

```bash
git clone https://github.com/bassirou-ousmane-ba/clustering-marches-senegal.git
cd clustering-marches-senegal
```

### Étape 2 — Créer un environnement virtuel

```bash
# Créer le venv
python -m venv venv

# Activer — Windows :
venv\Scripts\activate

# Activer — Mac/Linux :
source venv/bin/activate
```

### Étape 3 — Installer les dépendances

```bash
pip install -r requirements.txt
```

### Étape 4 — Lancer le projet

```bash
python main.py
```

---

## 🧠 Algorithme utilisé : K-Means

Le **K-Means** est un algorithme de clustering non supervisé qui :

1. Choisit K centres aléatoires
2. Affecte chaque point au centre le plus proche
3. Recalcule les centres (moyennes)
4. Répète jusqu'à convergence

### Choix du K — Méthode du Coude

On teste K de 2 à 10 et on observe la courbe d'inertie.
Le "coude" indique le K optimal (ici **K=4**).

### Évaluation — Score Silhouette

Le score silhouette mesure la qualité des clusters :
- Proche de **1** → clusters bien séparés
- Proche de **0** → clusters qui se chevauchent
- Négatif → mauvais clustering

---

## 📊 Graphiques générés

| Fichier | Description |
|---|---|
| `coude.png` | Méthode du coude — choix de K |
| `distributions.png` | Histogrammes des 7 variables |
| `correlation.png` | Heatmap de corrélation |
| `boxplots.png` | Boxplots par type de commerce |
| `scatter_clusters.png` | Nuage de points coloré par cluster |
| `profils_clusters.png` | Profil moyen de chaque segment |
| `repartition.png` | Camembert de la répartition |
| `boxplot_clusters.png` | Boxplots des variables clés par segment |

---

## 🌍 Contexte des données

Dataset **synthétique** simulé avec des caractéristiques réalistes du commerce informel sénégalais :

- Marchés : Sandaga, Tilène, HLM, Colobane, Thiaroye, Pikine, Rufisque, Touba, Thiès, Ziguinchor
- Types : épiceries, dibiteries, quincailleries, tissus, électronique, boulangeries…
- Revenus en **FCFA**
- Variables : chiffre d'affaires, surface, employés, ancienneté, stock, clients, distance

---

## 📦 Dépendances

| Librairie | Utilisation |
|---|---|
| `pandas` / `numpy` | Manipulation des données |
| `scikit-learn` | K-Means, StandardScaler, score silhouette |
| `matplotlib` / `seaborn` | Visualisations |

---

## 🔧 Désactiver le venv

```bash
deactivate
```

---

## 📄 Licence

Ce projet est sous licence [MIT](LICENSE).

---

## 👤 Auteur

**Bassirou Ousmane Ba**
> Projet réalisé dans le cadre d'une formation en **Data Science / Machine Learning** — Niveau Licence 2
