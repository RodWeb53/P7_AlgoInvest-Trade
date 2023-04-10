# Résolvez des problèmes en utilisant des algorithmes en Python

**Fonctionnalités** 

- Lire les données d'un fichier csv et les traiter

-   Un budget de 500 € est donné
-   Chaque action ne peut acheter qu'une seule fois
-   On ne peut pas acheter de partiel d'action

-   Trouver le meilleur résultat de rentablité

    -   Sur le fichier de 20 actions :
        -   Calcul Brute force pour analyser tous les résultats possible
    -   Sur les fichiers de 1000 lignes :
        -   Calcul avec un algorithme optimisé
    

## Mise en place du programme

`Pré-requis : python 3 doit être installé sur votre machine`

- Télécharger ce code dans ''code'' > ''Download ZIP''
- Décompresser le dossier

### 1. Création de l'environnement virtuel

Ouvrez le terminal, allez dans le dossier que vous avez téléchargé

Tapez la commande suivante pour créer l'environnement virtuel

    python -m venv env

### 2. Lancement de l'environnement virtuel

Sous Windows tapez la commande suivante :

    env\Scripts\activate.bat

Sous MAC ou Linux tapez la commande suivante :

    source env/bin/activate



## Lancement des programmes

Pour le lancement de Brute force sur les 20 actions :

    python bruteforce.py

Pour le lancement de la version optimisé et du fichier datas set1 :

    python optimized.py
