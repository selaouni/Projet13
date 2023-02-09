## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`


### Déploiement

Avant de passer au déploiement des étapes de test, linting et de dockerisation sont essentiel.
La pepline est composé de 3 job: 

    - build-test-lintting: qui lance les commandes Pytest et flake8 pour tester l'application et pour faire le linting.
    - dockerization: qui contruit l'image puis la push vers Docker hub.
    - deployment: qui lance les commandes necessaires pour deployer le site sous la plateforme heroku.

En plus des documents de base de l'application django, deux fichiers essentiels ont été ajoutés pour assurer le bon fonctionnement de la pepline:
    - Dockerfile: Définit la cofiguration nécessaire pour dockeriser l'application
    - Config.yml: Definit les jobs et le workflow da la pepeline ci/ci sous circle ci

Chaque modification poushée sous Github déclenche une pepline sous circle ci selon les regles de l'énoncé ci dessous:

- Configurez le déploiement de manière à ce que seules les modifications apportées à la branche master dans GitHub déclenchent la conteneurisation et le déploiement du site vers Heroku.
- Les modifications apportées aux autres branches doivent uniquement déclencher la compilation et les tests (sans déployer le site vers Heroku ou effectuer la conteneurisation)
- Le déploiement doit être répétable ; par exemple, vous devez pouvoir recréer facilement un déploiement supprimé dans Heroku.
- La tâche de conteneurisation ne doit être exécutée que si la compilation et de test sont réussies.
- Le travail de déploiement et de production ne doit s'exécuter que si le travail de conteneurisation est réussi.

les prerequis en terme d'outil et platforme: 
- Installation de Docker Desktop + création d'un compte Dockerhub qu'il faut relier à Docker Hub
- Un compte CircleCI lié au repo distant de votre repo Git
- Un compte Heroku + création d'une application qui est liée aussi au projet en question sous git
- Un compte Sentry lié à l'application django (voir commande et config sous sentry)

Variables d'environnement suivantes  (A définir dans circle ci :dans le setting du projet / menu Environment Variables):

DOCKERHUB_USERNAME : Correspond à votre login Docker hub,
DOCKERHUB_PAT: token défini au niveau des setting de Docker hub
DOCKERHUB_NAME_IMAGE: le nom donné à l'image Docker
HEROKU_TOKEN : vous pouvez trouver le Token de votre application dans le setting Heroku / heroku authorizations:create
HEROKU_APP_NAME : nom de l'appliaction sous Heroku


Au niveau de l'onglet "Settings" de l'application Heroku, Definir les Configs Vars suivants : 
- DEBUG : False
- SECRET_KEY : correspond à la clef secrète Django.

