import json
from mastodon import Mastodon
from datetime import datetime
from hdfs import InsecureClient

# Fonction pour encoder les objets datetime en format JSON
def custom_json_encoder(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()
    raise TypeError(f"Object of type {obj.__class__.__name__} is not JSON serializable")

# Fonction pour récupérer des toots depuis Mastodon
def fetch_toots():
    # Créer une instance Mastodon
    mastodon = Mastodon(
        client_id="p2OI-lFK4icN8uj34DIiZ08UrTvVj-M1H0iqzF_Hakc",
        client_secret="ShWKKwOFkIozzYBDti2ayXpFKzocHKm2-r6y0EQThb4",
        access_token="vMSJLofANgNb7uVjgILg9S0ErCKeucF8S0pDjuaDOa4",
        api_base_url="https://mastodon.social"
    )

    # Définir le nombre total de toots à récupérer
    toots_to_fetch = 1000

    # Liste pour stocker les toots
    all_toots = []

    while len(all_toots) < toots_to_fetch:
        # Récupérer les toots dans la limite par itération
        toots = mastodon.timeline_public(limit=toots_to_fetch - len(all_toots))
        all_toots.extend(toots)

    return all_toots

# Fonction pour enregistrer les toots dans un fichier JSON et les télécharger vers HDFS
def save_toots_to_hdfs(toots):
    # Récupérer la date et l'heure actuelles au format "yyyy-MM-dd-HH-mm-ss"
    current_datetime = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    json_file_name = f"data/{current_datetime}.json"

    # Écrire les données dans un fichier JSON en utilisant l'encodeur JSON personnalisé
    
    with open(json_file_name, 'w', encoding='utf-8') as json_file:
        json_str = json.dumps(toots, default=custom_json_encoder)
        json_file.write(json_str)
                #   ensure_ascii=False, default=custom_json_encoder)

    # Utiliser la bibliothèque HDFS pour stocker le fichier JSON sur HDFS
    hdfs_client = InsecureClient("http://localhost:9870", user="hadoop")
    hdfs_directory = "/Mastadon/datalake/"
    hdfs_client.upload(hdfs_directory, json_file_name, overwrite=True, n_threads=1)

    print(f"Les toots ont été enregistrés dans le fichier '{json_file_name}' et sur HDFS : {hdfs_directory}/{json_file_name}")

# Fonction principale pour exécuter le processus
def main():
    toots = fetch_toots()
    save_toots_to_hdfs(toots)

if __name__ == "__main__":
    main()
