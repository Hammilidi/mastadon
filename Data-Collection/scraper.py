import csv
from mastodon import Mastodon
from datetime import datetime
from hdfs import InsecureClient
import pandas as pd

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

# Déterminez la liste complète de toutes les clés (noms de colonnes) présentes dans les toots
all_keys = set().union(*(d.keys() for d in all_toots))

# Écrire les données dans un fichier CSV
with open(csv_file_name, 'w', newline='', encoding='utf-8') as csv_file:
    fieldnames = list(all_keys)
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(all_toots)

# Utiliser la bibliothèque HDFS pour stocker le fichier CSV sur HDFS
hdfs_client = InsecureClient("http://localhost:9870", user="hadoop")
hdfs_directory = "/MastadonDataLake"
hdfs_client.upload(hdfs_directory, csv_file_name, overwrite=True, n_threads=1)

print(f"Les toots ont été stockés dans le fichier '{csv_file_name}' et sur HDFS : {hdfs_directory}/{csv_file_name}")

# Afficher les 5 premières lignes du fichier CSV
df = pd.read_csv(csv_file_name)
print(df.head())
