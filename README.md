# Regroupement des marchés et des commerces au Sénégal

J'ai réalisé ce projet de mon côté pendant que je faisais ma formation GLSI à l'ESP de Dakar.

Au début, on s'est juste demandé si on pouvait rassembler des commerces sénégalais automatiquement d'après ce qu'ils sont, sans les avoir classés avant. C'est ce qu'on appelle du clustering non supervisé, et j'ai choisi l'algorithme K-Means pour le faire.

## Pourquoi parler de ça ?

> « Je voulais bosser sur un truc bien concret, qui se passe ici, chez nous. »

Les marchés comme Sandaga, Tilène, HLM ou Colobane, c'est vraiment un gros mélange. On y trouve de tout. Il y a le petit vendeur qui se balade avec ses choses et puis les gros gars qui importent des tonnes de marchandises. C'est ça qui est intéressant.

L'idée, c'était de vérifier si un algorithme pouvait, tout seul, repérer ces différences en se basant juste sur quelques données économiques.

Les données qu'on utilise sont créées par des programmes, mais elles sont faites pour ressembler le plus possible à ce qui se passe vraiment dans le commerce informel au Sénégal. Par exemple, les revenus sont en FCFA, on parle de vrais marchés et des types de boutiques qu'on trouve souvent là-bas.

## Ce que fait ce projet

En lançant `main.py`, le programme fait :

1. Crée un ensemble de données avec 500 commerces inventés, mais qui semblent réels.
2. Jette un coup d'œil rapide aux données pour voir comment elles se répartissent et si elles sont liées entre elles.
3. Avant d'utiliser K-Means, il faut harmoniser les variables.
4. On cherche le bon nombre de groupes en utilisant la méthode du coude.

Ensuite, on fait passer le modèle sur les données pour attribuer chaque magasin à un groupe.

Il fait plusieurs graphiques pour voir les résultats. Les graphiques s'affichent un par un, il faut fermer chaque fenêtre avant de pouvoir voir le suivant. Ils sont aussi enregistrés dans le dossier `graphiques`.

## Les 4 groupes qu'on a trouvés

Après réflexion, K=4 nous a semblé être l'option la plus judicieuse.

| Groupe | Nombre de magasins | Chiffre d'affaires moyen (FCFA) | Surface | Employés | Clients par jour |
|---|---|---|---|---|---|
| Petits vendeurs | ~150 | 150 000 | 5 m² | 1 | 20 |
| Commerces de quartier | ~175 | 400 000 | 15 m² | 2 | 50 |
| Commerces de taille moyenne | ~100 | 900 000 | 40 m² | 5 | 100 |
| Grands commerçants | ~75 | 2 500 000 | 90 m² | 12 | 200 |

Ces parties collent bien à ce qu'on voit en vrai, et pour moi, c'est un bon signe que tout tient la route.

## Comment bien organiser ses fichiers
```
clustering-marches-senegal/
├── config.py              # Voici les paramètres de notre projet : K, la valeur de départ, et les variables.
├── générer_données.py     # Génération du dataset
├── traitement_données.py  # Standardisation avec StandardScaler
├── modèle_kmeans.py       # Méthode du coude + K-Means
├── exploration_données.py # Découverte de données
├── visualisation.py       # Graphiques de clusters
├── main.py                # C'est le point de départ de tout, c'est de là que tout commence
├── requirements.txt       # Bibliothèques essentielles
└── README.md
```

## Installation

### 1. Copier le dépôt
```bash
git clone https://github.com/bassirou-ousmane-ba/clustering-marches-senegal.git
cd clustering-marches-senegal
```

### 2. Fabriquer un espace virtuel
```bash
python -m venv venv
```

Windows :
```bash
venv\Scripts\activate
```

Mac ou Linux :
```bash
source venv/bin/activate
```

### 3. Installer les éléments nécessaires
```bash
pip install -r requirements.txt
```

### 4. Mettre en marche
```bash
python main.py
```

---

## Quelques mots sur comment l'algorithme fonctionne

En gros, le K-Means commence par mettre des points un peu n'importe où. Après, il regarde chaque donnée et l'attribue au point le plus près. Ensuite, il recalcule la position de ces points, et ça continue comme ça jusqu'à ce que tout soit stable.

C'est un algorithme simple mais qui marche bien pour ce genre de découpage.

Pour choisir K, j'ai pris la méthode du coude : j'ai tracé l'inertie par rapport à K, et j'ai repéré l'endroit où la courbe devient plus plate.

Ici, tu peux bien voir le coude quand K est à 4.
