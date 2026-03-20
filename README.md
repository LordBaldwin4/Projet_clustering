# Clustering des Marchés et Commerces du Sénégal

Projet personnel réalisé en parallèle de ma formation GLSI à l'ESP de Dakar

L'idée de départ était simple : est-ce qu'on peut regrouper automatiquement des commerces sénégalais selon leurs caractéristiques, sans étiquettes préalables ? C'est ce qu'on appelle le **clustering non supervisé**, et j'ai choisi l'algorithme **K-Means** pour le mettre en pratique.

---

## Pourquoi ce sujet ?

Je voulais travailler sur quelque chose d'ancré dans la réalité locale. Les marchés comme Sandaga, Tilène, HLM ou Colobane regroupent des centaines de commerces très différents — du petit vendeur ambulant à l'importateur en gros. L'idée était de voir si un algorithme pouvait retrouver ces différences de façon autonome, à partir de quelques variables économiques.

Les données sont synthétiques (générées par script), mais elles essaient de coller aux réalités du commerce informel sénégalais : revenus en FCFA, marchés réels, types de boutiques courants, etc.

---

## Ce que le projet fait concrètement

En lançant `main.py`, le programme fait:

1. Génère un dataset de 500 commerces fictifs mais réalistes
2. Fait une exploration rapide des données (distributions, corrélations)
3. Standardise les variables avant d'appliquer K-Means
4. Cherche le bon nombre de clusters via la méthode du coude
5. Entraîne le modèle et affecte chaque commerce à un groupe
6. Produit plusieurs graphiques pour visualiser les résultats

Les graphiques s'ouvrent les uns après les autres — il faut fermer chaque fenêtre pour passer au suivant. Ils sont aussi sauvegardés dans le dossier `graphiques/`.

---

## Les 4 groupes trouvés

Après analyse, K=4 s'est révélé être le meilleur choix :

| Groupe | Nombre de commerces | CA moyen (FCFA) | Surface | Employés | Clients/jour |
|--------|---------------------|-----------------|---------|----------|--------------|
| Petits vendeurs | ~150 | 150 000 | 5 m² | 1 | 20 |
| Boutiques de quartier | ~175 | 400 000 | 15 m² | 2 | 50 |
| Commerces moyens | ~100 | 900 000 | 40 m² | 5 | 100 |
| Grands commerçants | ~75 | 2 500 000 | 90 m² | 12 | 200 |

Ces segments correspondent bien à ce qu'on observe dans la réalité, ce qui m'a semblé être un bon signe de cohérence.

---

## Organisation des fichiers
```
clustering-marches-senegal/
│
├── config.py           # Paramètres du projet (K, seed, variables)
├── generate_data.py    # Génération du dataset
├── preprocessing.py    # Standardisation avec StandardScaler
├── model_kmeans.py     # Méthode du coude + K-Means
├── eda.py              # Analyse exploratoire
├── visualisation.py    # Graphiques des clusters
├── main.py             # Point d'entrée — tout se lance depuis là
├── requirements.txt    # Bibliothèques nécessaires
└── README.md
```

---

## Installation

### 1. Cloner le dépôt
```bash
git clone https://github.com/bassirou-ousmane-ba/clustering-marches-senegal.git
cd clustering-marches-senegal
```

### 2. Créer un environnement virtuel
```bash
python -m venv venv

# Windows :
venv\Scripts\activate

# Mac/Linux :
source venv/bin/activate
```

### 3. Installer les dépendances
```bash
pip install -r requirements.txt
```

### 4. Lancer
```bash
python main.py
```

---

## Quelques notes sur l'algorithme

K-Means fonctionne en plaçant des centres au hasard, en assignant chaque point au centre le plus proche, puis en recalculant ces centres — et ainsi de suite jusqu'à stabilisation. C'est un algorithme simple mais efficace pour ce type de segmentation.

Pour choisir K, j'ai utilisé la **méthode du coude** : on trace l'inertie en fonction de K, et on cherche le point où la courbe "s'aplatit". Ici, le coude apparaît clairement à K=4.

Pour évaluer la qualité du clustering, j'ai aussi calculé le **score silhouette**. Plus il est proche de 1, mieux les clusters sont séparés.

---

## Graphiques générés

| Fichier | Contenu |
|---------|---------|
| `coude.png` | Courbe d'inertie — choix de K |
| `distributions.png` | Histogrammes des variables |
| `correlation.png` | Carte de corrélation |
| `boxplots.png` | Boxplots par type de commerce |
| `scatter_clusters.png` | Nuage de points coloré par cluster |
| `profils_clusters.png` | Profil moyen de chaque segment |
| `repartition.png` | Répartition en camembert |
| `boxplot_clusters.png` | Comparaison des clusters sur les variables clés |

---

## Bibliothèques utilisées

- `pandas` / `numpy` — manipulation des données
- `scikit-learn` — K-Means, StandardScaler, silhouette score
- `matplotlib` / `seaborn` — visualisations

---

## Désactiver l'environnement virtuel
```bash
deactivate
```

---

## Licence

MIT

---
Bassirou ousmane ba etudiant en licence 2 genie logiciel et Systeme d information a l'esp

## Auteur

**Bassirou Ousmane Ba** — Licence 2 Data Science / Machine Learning
