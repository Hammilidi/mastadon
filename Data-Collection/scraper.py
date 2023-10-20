import csv
from mastodon import Mastodon
from datetime import datetime
from hdfs import InsecureClient

# Créer une instance Mastodon
mastodon = Mastodon(
    client_id="p2OI-lFK4icN8uj34DIiZ08UrTvVj-M1H0iqzF_Hakc",
    client_secret="ShWKKwOFkIozzYBDti2ayXpFKzocHKm2-r6y0EQThb4",
    access_token="vMSJLofANgNb7uVjgILg9S0ErCKeucF8S0pDjuaDOa4",
    api_base_url="https://mastodon.social"
)

# Définir le nombre total de toots à récupérer à chaque exécution
toots_to_fetch = 1000

# Liste pour stocker les toots
all_toots = []

while len(all_toots) < toots_to_fetch:
    # Récupérer les toots dans la limite par itération
    toots = mastodon.timeline_public(limit=toots_to_fetch - len(all_toots))
    all_toots.extend(toots)
    
# Obtenir la date et l'heure actuelles au format "yyyy-MM-dd-HH-mm-ss"
current_datetime = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
csv_file_name = f"{current_datetime}.csv"

# Écrire les données dans un fichier CSV
with open(csv_file_name, 'w', newline='', encoding='utf-8') as csv_file:
    fieldnames = all_toots[0].keys()
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(all_toots)

# Utiliser la bibliothèque HDFS pour stocker le fichier CSV sur HDFS
hdfs_client = InsecureClient("http://localhost:9870", user="hadoop")
print("Connexion etablie")
hdfs_directory = "/MastadonDataLake"
hdfs_client.upload(hdfs_directory, csv_file_name, overwrite=True, n_threads=1)

print(f"Les toots ont été stockés dans le fichier '{csv_file_name}' et sur HDFS : {hdfs_directory}/{csv_file_name}")
