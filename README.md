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

## Base de données

Une nouvelle base de données est créee au premier lancement du programme.
la solution Tinydb est utilisée dans ce projet comme base de données, elle répond parfaitement aux besoins du projet.

Arborescence du ficher de la base de données:

```ssh
./database
└── db.json
```
## 1. Création d'un nouveau joueur

A partir de l'option 1 du menu principal, nous arrivons sur la procédure de création d'un nouveau joueur.

Exemple de saisie pour l'ajout d'un nouveau utilisateur après le choix de l'ption 1 du menu principal.
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
## 2. Afficher la liste des joueurs par ordre alphabétique
A partir de l'option 2 du menu principal, nous arrivons sur la procédure d'afficher la liste des joueurs par ordre alphabétique.

## 3. Modifier joueur

Grêce à l'option 3 du menu principal, nous pouvons modifier les données d'un joueur.
Voici un exemple:
```ssh
Choisissez ce que vous souhaitez faire :3
Veuillez saisir le prénom du joueur à modifier: ***
le prénom du joueur à modifier est : ***
Veuillez saisir le nom du joueur à modifier: ***
le nom du joueur à modifier est : ***
Le joueur est trouvé 
Veuillez saisir le nouveau prénom du joueur: ***
le nouveau prénom du joueur est : ***
Veuillez saisir le nouveau nom du joueur: ***
le nouveau nom du joueur est : ***
Veuillez saisir la nouvelle date de naissance du joueur: **/**/****
la nouvelle date de naissance du joueur est : **/**/****
Modification avec succés !
```


## 4. Création d'un nouveau tournois
A partir de l'option 4 du menu principal, nous arrivons sur la procédure de création d'un nouveau tournoi.

Exemple de saisie pour l'ajout d'un nouveau tournoi après le choix de l'ption 4 du menu principal.
```ssh
Choisissez ce que vous souhaitez faire :4
Veuillez saisir le nom du tournoi: ****
Veuillez saisir la localisation du tournoi: ****
Veuillez saisir la date du début du tournoi: au format dd/MM/yyyy : **/**/****
la date du début du tournoi est : **/**/****
Veuillez saisir la date de fin du tournoi: au format dd/MM/yyyy : **/**/****
la date de fin du tournoi est : **/**/****
Veuillez saisir la description du tournoi: ****
Veuillez saisir le nombre du tours ou laisser vide(4 par défaut): *
Veuillez saisir le nombre du joueurs (* nombre pair au moins égal à deux *): *
Le tournoi tournois a été crée avec succès
```
A noter aussi qu'à la fin de la création du tournoi, un sous menu vous propose d'ajouter des joueurs au tournoi et aussi d'afficher ses participants.
Dans notre cas, nous pouvons quitter le tournois et revenir lorsque nous le souhaitons pour rajouter des joueur à ce tournois qui est maintenant sauvegardé en base de données. 

## 5. Reprendre un tournois

Grâce à l'option 5 du menu principal, il est possible de charger un tournois existant en base de données.

Si ce n'est pas le cas, le programme vous indiquera qu'aucun tournoi n'existe en base de données.
Sinon il vous affichera la liste des tournois en vous demandant de faire sélectionner le tournois à importer.
Voici un exemple:

```ssh
Choisissez ce que vous souhaitez faire :5

============================================================================================================================================
 Id  |       Nom       |     Lieu     | Date de début |  Date de fin  |     Description      | Nbre de joueurs 
********************************************************************************************************************************************
 1   |    tournoi-1    |    paris     |    1/1/2001   |    2/2/2002   |     dddddddd fff     |       8       
--------------------------------------------------------------------------------------------------------------------------------------------

 2   |    tournoi_2    |    paris     |    7/7/2009   |    7/9/2009   |     finale desp      |       4       
--------------------------------------------------------------------------------------------------------------------------------------------

Veuillez saisir l id tournoi choisi : 1
Tournoi trouvé : tournoi-1
=======================================================================================================================
                                                    * MENU TOURNOIS*                                                   
###### TOURNOI :  tournoi-1 | JOUEURS :  8/8 | TOURS :  4 / 4
1. Ajouter des joueurs.
*. Le Tournoi est terminé ! 
3. Afficher la liste des participants par classement.
4. Afficher la liste des participants par ordre alphabétique.
5. Afficher la liste de tours et tous les matchs du tour.
0. Quitter le tournoi.
=======================================================================================================================
Choisissez ce que vous souhaitez faire :
```
Nous choisisons celui que nous venons de créer gâce à son Id (1).

Il nous affiche les infos du tournoi et nous propose un sous menu comme après sa création.

A noter, tant que les joeurs requis ne sont pas rajouter, le tournoi ne peut pas commencer.

Dès que l'ajout de tous les joueurs terminé, le menu va changer en nous proposant de commencer le tournois.

## 6. Afficher la liste de tous les tournois

Grâce à l'option 6 du menu principal, il est possible d'afficher la liste de tous les tournois existant en base de données.

## 7. Rechercher un tournois
Grâce à l'option 7 du menu principal, il est possible de chercher un tournois existant en base de données grâce à son nom et elle affiche la date de début et la date de fin de tournoi.
voici un exemple:

```ssh
Choisissez ce que vous souhaitez faire :7
Veuillez saisir Le nom du  Tournoi à chercher : tournoi-1
===========================================================================
Tournoi : tournoi-1 Début : 1/1/2001 Fin le : 2/2/2002
===========================================================================
```

## Utilisation de flake8

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