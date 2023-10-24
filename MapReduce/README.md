# Mapper

#### Description

Ce script Python est conçu pour traiter des données JSON à partir d'une source spécifique et émettre des paires clé-valeur pour une analyse ou un traitement ultérieur des données. Le script lit les données d'entrée à partir de l'entrée standard (stdin) et analyse les objets JSON de chaque ligne. Il extrait ensuite les informations pertinentes de ces objets et émet des paires clé-valeur vers la sortie standard (stdout). Les données émises peuvent être utilisées en tant qu'entrée pour un pipeline MapReduce ou une analyse de données.

#### Utilisation

Pour utiliser ce script, vous devez disposer de Python 3 installé sur votre système. Vous pouvez exécuter le script de la manière suivante :

```bash
python3 script.py < input_data.json
```

Où `script.py` est le nom du script Python et `input_data.json` est le fichier JSON que vous souhaitez traiter. Vous pouvez remplacer `input_data.json` par le nom de fichier réel ou fournir des données JSON via l'entrée standard.

#### Format d'Entrée

Les données d'entrée doivent être un flux JSON séparé par des sauts de ligne, où chaque ligne contient un objet JSON.

#### Sortie

Le script traite les données JSON et émet des paires clé-valeur vers la sortie standard. Ces paires clé-valeur peuvent être utilisées pour diverses tâches d'analyse ou de traitement ultérieur.

Les paires clé-valeur émises comprennent :

- Données liées à l'utilisateur :
  - ID de l'utilisateur, Date, Abonnés, Taux d'engagement
  - Exemple : `user:1234 {"date": "2023-10-23", "followers": 1000, "engagement_rate": 0.05}`

- Données de croissance (liées à l'année et au mois de création du compte utilisateur) :
  - ID de croissance, Valeur, ID de l'utilisateur
  - Exemple : `croissance:2023-10 {"value": 1, "user_id": "user:1234"}`

- Données de toot avec des médias :
  - ID de Toot avec des Médias, Valeur
  - Exemple : `toot_with_media {"value": 1}`

- Données de langue :
  - ID de langue, Valeur
  - Exemple : `language:Français {"value": 1}`

- Données d'emoji :
  - ID de l'emoji, Valeur
  - Exemple : `emoji:sourire {"value": 1}`

- Données de site web (extraites du contenu) :
  - ID du site Web, Valeur
  - Exemple : `website:exemple.com {"value": 1}`

#### Gestion des Erreurs

Le script tente de traiter chaque ligne en tant qu'objet JSON. Si l'analyse échoue ou si d'autres exceptions se produisent lors du traitement, il enregistre un message d'erreur dans la sortie d'erreur standard (stderr).

Assurez-vous que vos données d'entrée respectent le format attendu pour éviter les erreurs.

#### Remarque

Ce README fournit un aperçu de la fonctionnalité du script. Pour utiliser ce script efficacement, assurez-vous de bien comprendre le format des données d'entrée et le but prévu des paires clé-valeur émises.





# Reducer
Bien sûr, voici un fichier README.md à ajouter à votre projet Python existant, en supposant que ce nouveau script soit un complément ou une mise à jour du précédent. Vous pouvez ajouter ce nouveau contenu sous le README précédent :

```markdown


## Description

Ce projet Python est conçu pour traiter des données JSON à partir d'une source spécifique et émettre des paires clé-valeur pour une analyse ou un traitement ultérieur des données. Il se compose de deux scripts Python, le premier étant le script original (script.py) et le second étant un script de réduction (reducer.py).

## Script Original (mapper.py)

Le script original (mapper.py) lit les données d'entrée à partir de l'entrée standard (stdin) et analyse les objets JSON de chaque ligne. Il extrait ensuite les informations pertinentes de ces objets et émet des paires clé-valeur vers la sortie standard (stdout). Les données émises peuvent être utilisées en tant qu'entrée pour un pipeline MapReduce ou une analyse de données.

Pour plus d'informations sur l'utilisation et le fonctionnement du script original, consultez le README du script d'origine.

## Script de Réduction (reducer.py)

Le script de réduction (reducer.py) est conçu pour prendre les paires clé-valeur générées par le script original et effectuer des agrégations et des calculs supplémentaires. Il regroupe les données en fonction de clés spécifiques et calcule des statistiques telles que la moyenne du taux d'engagement des utilisateurs et le nombre d'occurrences de différents événements.

Le script de réduction prend en charge les catégories suivantes :

- Données liées à l'utilisateur
- Données de croissance
- Données de langue
- Données de Toot avec des médias
- Données d'emoji
- Données de site Web

Le script de réduction génère des résultats agrégés pour chaque catégorie et les émet vers la sortie standard.

## Utilisation

Pour utiliser le script de réduction, exécutez-le de la manière suivante :

```bash
python3 reducer.py < input_data.json
```

Assurez-vous que les données d'entrée proviennent du script original (script.py) pour obtenir des résultats significatifs.

## Format d'Entrée

Les données d'entrée pour le script de réduction doivent être les paires clé-valeur générées par le script original. Chaque ligne doit être au format "clé\tvaleur".

## Sortie du Script de Réduction

Le script de réduction émet des données agrégées sous forme de paires clé-valeur. Les résultats incluent des statistiques agrégées pour chaque catégorie de données.

Pour plus d'informations sur le format de sortie spécifique, consultez le README du script de réduction.

## Gestion des Erreurs

Le script de réduction est conçu pour traiter les données correctement et générer des résultats précis. Il effectue des calculs et des agrégations sur les données pour obtenir des statistiques significatives.

## Remarque

Ce README fournit un aperçu du fonctionnement du script de réduction, qui est un complément du script original. Pour utiliser efficacement ce projet Python, assurez-vous de bien comprendre le format des données d'entrée et du format de sortie généré par le script de réduction.

Pour toute question ou problème lié à ce projet Python, veuillez contacter l'auteur du projet.

