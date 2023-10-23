# mastadon
Ce projet Vise à analyser les données des réseaux sociaux pour obtenir des informations sur l'engagement des utilisateurs, la popularité du contenu, etc. 
Nous utiliserons MapReduce pour le traitement des données, HBase pour le stcokage des resultats et orchestration le flux de travail sera realise avec Apache Airflow. 

# Collecte de données

Utilisation de l'API de la plateform avec un access tokens

Rassembler des données brutes sur du Plateform Mastadon.

Stockage des données brutes dans un système de fichiers distribué tel que HDFS pour plus d'évolutivité.

Définir la modélisation du Datalake HDFS .


# Traitement MapReduce 

Le rôle du mapper est de traiter les données d'entrée et de produire des paires clé-valeur. Pour ce projet, le mappeur traitera chaque ligne de l'ensemble de données et émettra des paires clé-valeur en fonction des métriques que vous souhaitez analyser (par exemple, les abonnés des utilisateurs, le taux d'engagement, les URL, les emojis, etc.).

Le rôle du reducer est d'agréger les paires clé-valeur produites par le mappeur. Pour ce projet, le réducteur regroupera des métriques telles que les abonnés des utilisateurs, les taux d'engagement et le nombre d'URL, d'emojis, etc.


# Exécution du travail MapReduce 

Utilisation de l'API de streaming Hadoop pour exécuter la tâche MapReduce. Fournissez les scripts du mappeur et du réducteur comme entrées dans le travail.

Surveillance de la progression de la tâche à l'aide de l'interface utilisateur Web Hadoop.


# Stockage des résultats dans HBase :

Conception du schéma HBase en fonction des informations que vous souhaitez en tirer.

Tenez compte des meilleures pratiques en matière de conception de clés de ligne (Row Key Design), de conception de familles de colonnes(Column Family Design), de compression, bloom filters , batch inserts etc.

Création d'une table requise dans HBase

Insérez la sortie du réducteur dans les tables HBase à l'aide d'un client HBase en Python ou d'une autre méthode préférée


 # Orchestration Apache Airflow 
 
 Définissez un DAG (Directed Acyclic Graph) pour orchestrer le workflow. Créez des tâches pour exécuter le travail MapReduce et stocker les résultats dans HBase. Surveillez les progrès et gérez les erreurs ou les échecs.


# Analyser les résultats : Interrogez les tables HBase pour récupérer les résultats stockés.

## Rédiger des requetes pour :


### Analyse des utilisateurs

### Identifiez les utilisateurs ayant le plus grand nombre d'abonnés.

### Analyser le taux d'engagement des utilisateurs.

### Analysez la croissance des utilisateurs au fil du temps à l'aide de la métrique `user_created_at`.

​

## Analyse du contenu

Identifiez les sites Web externes (URL) les plus partagés.

Analyse de la langue et de la région

Analyser la répartition des posts en fonction de leur langue.
​

## Analyse de l'engagement des médias

Déterminez le nombre de publications avec des pièces jointes multimédias. _


## Analyse des balises et des mentions

Identifiez les balises les plus fréquemment utilisées et les utilisateurs mentionnés.
​

# Exécution du flux de travail 
Dans l'interface utilisateur Web d'Airflow, activez le DAG. Surveillez la progression des exécutions du DAG. Vérifiez les journaux pour tout problème. Une fois le DAG terminé, vérifiez les résultats dans HBase.

# Optimisation et surveillance 
Optimisez les scripts MapReduce pour de meilleures performances. Surveillez HBase pour tout problème de stockage. Configurez des alertes dans Airflow pour les échecs de tâches.

Surveillez régulièrement Hadoop à l'aide de son interface Web respective.

Mise à jour du paramétrage des droits pour l’alimentation en données

API Mastodon: Assurez-vous que les tokens API que vous utilisez ont les permissions nécessaires pour récupérer les données. Si des rôles organisationnels changent, mettez à jour les tokens API en conséquence et que les tokens API ont les permissions de recherche nécessaires

​

Mise à jour de la documentation des accès et des règles de partage Incluez des détails sur les rôles ayant quelles permissions, comment demander l'accès, et le processus d'octroi ou de révocation d'accès.

Programmation des évolutions et des nouvelles procédures d’alimentation automatisées

Assurez-vous que les DAGs sont programmés pour s'exécuter à des intervalles appropriés pour le rafraîchissement des données.

Mise à jour du registre des traitements de données personnelles en vue de la mise en conformité du data lake avec le RGPD

Documentez toutes les données personnelles ingérées de Mastodon et comment elles sont traitées et stockées.

Assurez-vous que toutes les activités de traitement des données sont conformes aux réglementations du RGPD.



​

