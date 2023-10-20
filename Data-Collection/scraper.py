import csv
from mastodon import Mastodon
import time
from datetime import datetime
import pandas as pd
from hdfs import InsecureClient
import os

# Créer une instance Mastodon
mastodon = Mastodon(
    client_id="p2OI-lFK4icN8uj34DIiZ08UrTvVj-M1H0iqzF_Hakc",
    client_secret="ShWKKwOFkIozzYBDti2ayXpFKzocHKm2-r6y0EQThb4",
    access_token="vMSJLofANgNb7uVjgILg9S0ErCKeucF8S0pDjuaDOa4",
    api_base_url="https://mastodon.social"
)

# Définir le nombre total de toots à récupérer
total_toots_to_fetch = 50

# Compteur de toots récupérés
toots_fetched = 0
max_results_per_iteration = 20  # Nombre de toots à récupérer à chaque itération
max_files_per_lot = 10  # Nombre de fichiers par lot

while toots_fetched < total_toots_to_fetch:
    # Créer une liste pour stocker les fichiers de ce lot
    lot_files = []

    for i in range(max_files_per_lot):
        # Générer un nom de fichier unique pour cette itération en utilisant le timestamp
        timestamp = int(time.time())
        csv_file = f"{timestamp}.csv"

        # Ouvrir le fichier CSV pour écriture
        with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)

            # Écrire la ligne d'en-tête
            writer.writerow(["Toot ID", "Account Name", "Account Username", "Followers Count", "Following Count",
                             "Statuses Count", "Account Acct", "Note", "Last Status At", "Account Locked", "Tags", "Media Attachments",
                             "Emojis", "Mentions", "Visibility", "Content", "Created At", "Edited At", "Language", "URL",
                             "Replies Count", "Reblogs Count", "Reblog", "Reblogged", "Favorite Counts", "Favourited",
                             "Bookmarked"])

            # Récupérer les toots dans la limite par itération
            toots = mastodon.timeline_public(limit=max_results_per_iteration)

            for toot in toots:
                toot_id = toot['id']
                account_name = toot['account']['display_name']
                account_username = toot['account']['username']
                followers_count = toot['account']['followers_count']
                following_count = toot['account']['following_count']
                statuses_count = toot['account']['statuses_count']
                acct = toot['account']['acct']
                note = toot['account']['note']
                last_status_at = toot['account']['last_status_at']
                last_status_at = toot['account']['last_status_at']
                locked = toot['account']['locked']
                tags = toot['tags']
                media = toot['media_attachments']
                emojis = toot['emojis']
                mentions = toot['mentions']
                visibility = toot['visibility']
                content = toot['content']
                created_at = toot['created_at']
                edited_at = toot['edited_at']
                language = toot['language']
                url = toot['url']
                replies_count = toot['replies_count']
                reblogs_count = toot['reblogs_count']
                reblog = toot['reblog']
                reblogged = toot['reblogged']
                favorite_counts = toot['favourites_count']
                favourited = toot['favourited']
                bookmarked = toot['bookmarked']

                # Écrire les informations du toot dans le fichier CSV
                writer.writerow([toot_id, account_name, account_username, followers_count, following_count, statuses_count, acct,
                                 note, last_status_at, locked, tags, media, emojis, mentions, visibility, content, created_at,
                                 edited_at, language, url, replies_count, reblogs_count, reblog, reblogged, favorite_counts,
                                 favourited, bookmarked])

            # Ajouter le nom du fichier à la liste des fichiers du lot
            lot_files.append(csv_file)
            
    # Obtenir la date et l'heure actuelles au format "yyyy-MM-dd-HH-mm-ss"
    current_datetime = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    # Concaténer les fichiers du lot en un seul fichier CSV
    concatenated_df = pd.concat([pd.read_csv(file) for file in lot_files], ignore_index=True)
    
    # Générer un nom de fichier pour le lot concaténé
    concatenated_file_name = f"{current_datetime}.csv"
    
    concatenated_df.to_csv(concatenated_file_name)


    # Utilisez la bibliothèque HDFS pour stocker le fichier concaténé sur HDFS
    hdfs_client = InsecureClient("http://localhost:9870", user="hadoop")
    print("Connexion etablie !")
    hdfs_directory = "/MastadonDataLake"
    hdfs_client.upload(hdfs_directory, concatenated_file_name, overwrite=True, n_threads=1)

    print(f"Les fichiers du lot ont été concaténés et stockés sur HDFS : {hdfs_directory}/{concatenated_file_name}")


    # Incrémenter le compteur de toots récupérés
    toots_fetched += max_results_per_iteration * max_files_per_lot

    # Faites une pause pour éviter de dépasser les limites de l'API
    time.sleep(60)  # Pause de 60 secondes
