# Projet gestion des tournoi hors ligne

Veuillez suivre ces étapes, afin de lancez le programme.

* Python 3.x
* Git
* pip (pour installer les dépendances)

## Installation

1. Exécuter la commande `git clone https://github.com/boulila-n/GestionTournois.git` sous windows ou linux.

2. Sous le dossier du projet cloné, exécutez la commande `python -m venv <nom de l'environnement virtuel>` pour créer votre environnement virtuel.

3. Exécutez la commande `pip install -r requirements.txt` pour installer les dépendances nécessaires.

## Exécution

1. Dans le terminal, tapez la commande `python ./main.py`.

## Comment utiliser le programme <a name="How_to_use"></a>

## Exemple d'affichage du menu principal <a name="Exemple_affichage_menu"></a>

```ssh
=======================================================================================================================
                                                   * MENU PRINCIPAL*                                                   
1. Ajouter un nouveau joueur
2. Afficher la liste des joueurs par ordre alphabétique
3. Modifier joueur
4. Créer un nouveau tournois
5. Reprendre un tournois
6. Afficher la liste de tous les tournois
7. Rechercher un tournois
0. Quitter le programme
=======================================================================================================================
Choisissez ce que vous souhaitez faire : 

```
Au lancement du programme, vous arrivez sur le menu principal, vous pouvez faire votre choix en tapant le numéro de l'option qui vous intéresse et ensuite taper sur "ENTRER".

## Base de données <a name="DB"></a>

Une nouvelle base de données est créee au premier lancement du programme.
la solution Tinydb est utilisée dans ce projet comme base de données, elle répond parfaitement aux besoins du projet.

Arborescence du ficher de la base de données:

```ssh
./database
└── db.json
```
## Création d'un nouveau joueur <a name="Create_player"></a>

A partir de l'option 1 du menu principal, nous arrivons sur la procédure de création d'un nouveau joueur.

Example de saisie pour l'ajout d'un nouveau utilisateur après le choix de l'ption 1 du menu principal.
```ssh
Choisissez ce que vous souhaitez faire :1
Veuillez saisir le prénom du joueur: ****
le prénom du joueur est : ****
Veuillez saisir le nom du joueur: ****
le nom du joueur est : ****
Veuillez saisir la date de naissance du joueur: au format dd/MM/yyyy : **/**/****
la date de naissance du joueur est : **/**/****
**** **** a bien été ajouté à la base de données
```
## Utilisation de flake8 <a name="Flake8"></a>

flake8 est un des outils mis à disposition par la communauté pour aider à valider son code Python au regard de la PEP 8.

Un fichier de configuration est présent dans l'arborescence du projet.

Fichier de configuration: .flake8

Contenu du fichier:

```ssh
[flake8]
exclude = .venv/
max-line-length = 119
format= html
htmldir= flake-report

```

### Inscructions pour générer un nouveau rapport flake8-html.

Exécution de flake8:

Se positionner dans le dossier du projet et s'assurer que l'environnement virtuel python est chargé.
Exécuter la commande suivante:

```ssh

$ flake8

```

Dossier du rapport flake8:

```ssh
flake-report/
├── back.svg
├── file.svg
├── index.html
└── styles.css
```
Exemple de rapport sans erreur:

![Rapport flake8](./rapport-html/img.png)