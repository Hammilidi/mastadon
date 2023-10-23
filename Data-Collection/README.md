## Data Collection

```markdown
# Collecte de Données depuis Mastodon

Ce script Python vous permet de collecter des données à partir de Mastodon et de les stocker dans un format de votre choix (CSV ou JSON). Le script récupère des toots publics et les enregistre dans un fichier local avant de téléverser les données vers HDFS.

## Prérequis

Avant d'utiliser ce script, vous devez avoir les éléments préalables suivants installés :

- Python 3.x
- Bibliothèque `mastodon.py` (pour interagir avec Mastodon)
- Bibliothèque `pandas` (pour la manipulation de données)
- Bibliothèque `hdfs` (pour l'interaction avec HDFS)

Vous avez également besoin d'un accès à une instance Mastodon et d'une application API pour l'authentification.

## Utilisation

1. Mettez à jour les informations d'authentification Mastodon et autres paramètres dans le script.

2. Exécutez le script avec la commande suivante :

   ```bash
   python script.py
   ```

3. Le script collectera un nombre spécifié de toots (1000 par défaut), les enregistrera dans un fichier CSV avec un horodatage dans le nom de fichier, puis téléversera le fichier vers HDFS.

## Configuration

Vous pouvez modifier les options de configuration suivantes dans le script :

- `total_toots_to_fetch` : Le nombre total de toots à collecter.
- `toots_to_fetch` : Le nombre de toots à récupérer à chaque exécution.
- `hdfs_directory` : Le répertoire HDFS où les données seront stockées.

## Format du Fichier

Par défaut, le script enregistre les données dans un fichier CSV avec les champs suivants :

- ID du Toot
- Nom du Compte
- Nom d'Utilisateur du Compte
- Nombre d'Abonnés
- Nombre d'Abonnements
- ...

## Licence

Ce code est sous licence [MIT License](LICENSE).

## Auteur

- [Votre Nom](https://github.com/votreutilisateur)

## Remerciements

- Un grand merci aux développeurs de Mastodon et des bibliothèques utilisées dans ce script.

```