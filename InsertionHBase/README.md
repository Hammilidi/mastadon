
Ce README.md fournit une documentation de base pour le script d'insertion de données dans HBase. Vous pouvez l'ajouter à votre projet pour expliquer son fonctionnement aux autres utilisateurs.

# Insertion de données dans HBase

Ce script Python vous permet de vous connecter à une base de données HBase locale et d'insérer des données à partir d'un fichier texte. Le script utilise la bibliothèque HappyBase pour effectuer la communication avec HBase.

## Prérequis

Assurez-vous d'avoir les éléments suivants installés sur votre système :

- Python
- HappyBase
- HBase (en cours d'exécution sur le serveur local)
- Un fichier texte contenant les données à insérer (dans cet exemple, nommé "reduced.txt")

## Utilisation

1. Assurez-vous que HBase est en cours d'exécution sur votre serveur local.

2. Installez la bibliothèque HappyBase en utilisant pip :

   ```bash
   pip install happybase
