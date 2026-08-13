\#  Regroupement des marchés et commerces au Sénégal

> **Projet de Machine Learning non supervisé basé sur l'algorithme K-Means**

Ce projet a pour objectif d'étudier et de **regrouper automatiquement différents types de commerces sénégalais** en fonction de leurs caractéristiques économiques et commerciales.

L'idée est d'utiliser le **clustering non supervisé** pour identifier des profils de commerces sans avoir besoin de définir les catégories à l'avance.

Le projet a été réalisé dans le cadre d'une formation en **GLSI à l'ESP de Dakar**.

---

## Objectif du projet

Les marchés et commerces constituent une partie importante de l'activité économique au Sénégal.

Des marchés comme :

*  Sandaga
* Tilène
*  HLM
*  Colobane

regroupent des commerces très différents, allant du petit vendeur indépendant aux commerces de grande taille.

L'objectif de ce projet est donc de répondre à la question suivante :

> **Peut-on utiliser le Machine Learning pour identifier automatiquement différents profils de commerces sénégalais à partir de leurs caractéristiques économiques ?**

Pour répondre à cette question, nous utilisons une approche de **Machine Learning non supervisé**, plus précisément l'algorithme **K-Means**.

---

#  Méthode utilisée

Le projet suit plusieurs étapes :

```text
Génération des données
        ↓
Exploration des données
        ↓
Prétraitement
        ↓
Standardisation
        ↓
Recherche du nombre optimal de clusters
        ↓
K-Means
        ↓
Analyse des groupes
        ↓
Visualisation
```

---

##  Données

Les données utilisées dans ce projet sont **générées artificiellement** afin de reproduire des situations plausibles dans le contexte du commerce sénégalais.

Le programme génère **500 commerces simulés**.

Les variables représentent notamment :

| Variable           | Description                            |
| ------------------ | -------------------------------------- |
| `chiffre_affaires` | Chiffre d'affaires du commerce en FCFA |
| `surface`          | Surface du commerce en m²              |
| `employes`         | Nombre d'employés                      |
| `clients_jour`     | Nombre moyen de clients par jour       |

Les valeurs sont conçues pour représenter différents niveaux d'activité commerciale.

>  **Important :** les données sont synthétiques et ne constituent pas une base de données officielle sur les commerces sénégalais.

---

# 🔬 Analyse exploratoire

Avant d'appliquer le modèle, une analyse exploratoire des données (**EDA — Exploratory Data Analysis**) est réalisée.

Cette étape permet notamment de :

* comprendre la distribution des variables ;
* détecter les éventuelles anomalies ;
* observer les relations entre les variables ;
* mieux comprendre la structure du dataset.

Le fichier responsable de cette étape est :

```text
eda.py
```

---

#  Prétraitement

Les variables utilisées pour le clustering possèdent des échelles différentes.

Par exemple :

```text
Chiffre d'affaires → plusieurs centaines de milliers de FCFA
Surface           → quelques dizaines de m²
Employés          → quelques unités
Clients/jour      → plusieurs dizaines ou centaines
```

Pour éviter qu'une variable domine les autres, les données sont standardisées avec :

```python
StandardScaler
```

Cette étape est réalisée dans :

```text
preprocessing.py
```

---

#  K-Means

Le modèle principal utilisé est **K-Means**.

K-Means cherche à répartir les observations en `K` groupes de manière à minimiser la distance entre les observations et le centre de leur cluster.

De manière simplifiée :

```text
Données
   │
   ▼
Choix de K centroïdes
   │
   ▼
Attribution des commerces au centroïde le plus proche
   │
   ▼
Recalcul des centroïdes
   │
   ▼
Répétition
   │
   ▼
Clusters finaux
```

---

#  Choix du nombre de clusters

Pour déterminer le nombre approprié de groupes, le projet utilise la **méthode du coude (Elbow Method)**.

L'inertie est calculée pour différentes valeurs de `K`.

L'objectif est d'identifier le point où l'ajout de clusters supplémentaires apporte un gain de moins en moins important.

Dans ce projet, l'analyse conduit à retenir :

```text
K = 4
```

---

#  Résultats

L'application permet d'identifier **quatre grands profils de commerces**.

| Cluster | Profil                      |        CA moyen | Surface | Employés | Clients/jour |
| ------- | --------------------------- | --------------: | ------: | -------: | -----------: |
|  1    | Petits vendeurs             |   ~150 000 FCFA |   ~5 m² |       ~1 |          ~20 |
|  2    | Commerces de quartier       |   ~400 000 FCFA |  ~15 m² |       ~2 |          ~50 |
|  3    | Commerces de taille moyenne |   ~900 000 FCFA |  ~40 m² |       ~5 |         ~100 |
|  4    | Grands commerçants          | ~2 500 000 FCFA |  ~90 m² |      ~12 |         ~200 |

Ces groupes permettent de mettre en évidence une progression entre les petits commerces et les commerces de plus grande taille.

---

#  Visualisation

Le projet génère plusieurs graphiques permettant d'analyser les clusters.

Les visualisations permettent notamment de :

* comparer les différents groupes ;
* observer les relations entre les variables ;
* visualiser la répartition des commerces ;
* analyser les résultats du K-Means.

Les graphiques sont enregistrés dans le dossier :

```text
graphiques/
```

Les visualisations sont gérées par :

```text
visualisation.py
```

---

# 📁 Structure du projet

```text
Projet_clustering/
│
├── config.py
│   └── Configuration générale du projet
│
├── generate_data.py
│   └── Génération des données synthétiques
│
├── eda.py
│   └── Analyse exploratoire des données
│
├── preprocessing.py
│   └── Prétraitement et standardisation
│
├── model_kmeans.py
│   └── Méthode du coude et modèle K-Means
│
├── visualisation.py
│   └── Création des graphiques
│
├── main.py
│   └── Point d'entrée principal
│
├── requirements.txt
│   └── Dépendances Python
│
└── README.md
```

Cette structure correspond aux principaux fichiers actuellement présents dans le dépôt.

---

#  Technologies utilisées

*  **Python**
*  **NumPy**
*  **Pandas**
*  **Scikit-learn**
*  **Matplotlib**
*  **Seaborn**
*  **Machine Learning non supervisé**
*  **K-Means Clustering**
*  **StandardScaler**

---

#  Installation

## 1. Cloner le dépôt

```bash
git clone https://github.com/LordBaldwin4/Projet_clustering.git
cd Projet_clustering
```

## 2. Créer un environnement virtuel

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

## 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

---

# ▶️ Exécution

Le projet peut être lancé avec :

```bash
python main.py
```

Le programme enchaîne automatiquement les principales étapes du projet :

```text
1. Génération des données
2. Exploration
3. Prétraitement
4. Standardisation
5. Recherche du K optimal
6. Entraînement du K-Means
7. Attribution des clusters
8. Génération des visualisations
```

---

# 🔎 Exemple de fonctionnement

Un commerce peut être représenté par :

```text
Chiffre d'affaires : 450 000 FCFA
Surface            : 18 m²
Employés           : 2
Clients/jour       : 55
```

Après standardisation, ces caractéristiques sont fournies au modèle K-Means.

Le modèle peut alors attribuer automatiquement le commerce à un cluster correspondant à un profil similaire.

Par exemple :

```text
Commerce
   │
   ├── CA : 450 000 FCFA
   ├── Surface : 18 m²
   ├── Employés : 2
   └── Clients : 55
           │
           ▼
       K-Means
           │
           ▼
   Cluster 2
           │
           ▼
Commerces de quartier
```

---

#  Pourquoi utiliser le clustering ?

Le clustering est particulièrement intéressant lorsqu'on ne dispose pas de catégories prédéfinies.

Contrairement à une classification supervisée :

```text
Classification
Données → Catégorie connue
```

le clustering fonctionne plutôt comme ceci :

```text
Données → Algorithme → Groupes découverts
```

Cela permet d'explorer une population et de découvrir des structures qui n'étaient pas nécessairement connues à l'avance.

---

#  Intérêt pour le contexte sénégalais

Ce projet cherche surtout à montrer comment les techniques de **Data Science et de Machine Learning** peuvent être appliquées à des problématiques locales.

L'utilisation de caractéristiques exprimées en **FCFA**, de profils commerciaux et de références aux marchés sénégalais permet de construire un cas d'étude proche du contexte économique local.

À terme, une approche similaire pourrait être appliquée à des données réelles pour :

* segmenter les commerces ;
* identifier différents profils économiques ;
* aider à analyser les activités commerciales ;
* étudier les différences entre marchés ;
* faciliter certaines études économiques.

---

#  Limites

Ce projet présente plusieurs limites importantes.

### Données synthétiques

Les 500 commerces utilisés sont générés artificiellement.

Les résultats ne doivent donc pas être interprétés comme une étude statistique réelle du commerce sénégalais.

### Nombre de variables limité

Le clustering repose principalement sur quelques variables économiques et commerciales.

D'autres facteurs pourraient être intégrés :

* localisation GPS ;
* type de produits ;
* ancienneté ;
* charges ;
* nombre de fournisseurs ;
* saisonnalité ;
* prix moyens ;
* fréquentation ;
* présence en ligne.

### Choix de K

Le nombre de clusters a été fixé à **4** à partir de la méthode du coude et de l'interprétation des résultats. D'autres méthodes pourraient être utilisées pour confirmer ce choix.

---

#  Améliorations possibles

Plusieurs évolutions pourraient rendre le projet plus complet.

###  Ajouter la géolocalisation

Intégrer les coordonnées GPS permettrait d'étudier la répartition géographique des commerces.

###  Utiliser des données réelles

Remplacer les données synthétiques par des données réelles permettrait d'obtenir des résultats plus représentatifs.

###  Tester d'autres algorithmes

Comparer K-Means avec :

* DBSCAN ;
* Agglomerative Clustering ;
* Gaussian Mixture Models ;
* HDBSCAN.

permettrait d'étudier différentes structures de clusters.

###  Ajouter des métriques

Il serait intéressant d'ajouter :

* Silhouette Score ;
* Davies-Bouldin Index ;
* Calinski-Harabasz Score.

###  Ajouter une carte interactive

Une carte basée sur les clusters permettrait de visualiser les différents profils de commerces directement sur une carte du Sénégal.

---

#  Auteur

**LordBaldwin4**

Projet personnel réalisé dans le cadre d'une formation **GLSI à l'ESP de Dakar**.

---

#  Licence

Aucune licence open source spécifique n'est actuellement indiquée dans le dépôt.

Si le projet doit être distribué ou réutilisé, il est recommandé d'ajouter une licence explicite.

---

#  Conclusion

Ce projet montre une application concrète du **Machine Learning non supervisé** à une problématique inspirée du contexte commercial sénégalais.

À travers la génération de données, l'analyse exploratoire, le prétraitement, la méthode du coude et K-Means, il est possible d'identifier automatiquement différents profils de commerces.

> **L'objectif n'est pas seulement d'appliquer un algorithme, mais de montrer comment la Data Science peut être utilisée pour comprendre des problématiques locales.**
