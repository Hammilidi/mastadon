import json
from mastodon import Mastodon
from datetime import datetime
from hdfs import InsecureClient
import pandas as pd

# Custom JSON encoder function to handle datetime objects
def custom_json_encoder(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()
    raise TypeError(f"Object of type {obj.__class__.__name__} is not JSON serializable")

# Create a Mastodon instance
mastodon = Mastodon(
    client_id="p2OI-lFK4icN8uj34DIiZ08UrTvVj-M1H0iqzF_Hakc",
    client_secret="ShWKKwOFkIozzYBDti2ayXpFKzocHKm2-r6y0EQThb4",
    access_token="vMSJLofANgNb7uVjgILg9S0ErCKeucF8S0pDjuaDOa4",
    api_base_url="https://mastodon.social"
)

# Define the total number of toots to fetch in each run
toots_to_fetch = 1000

# List to store the toots
all_toots = []

while len(all_toots) < toots_to_fetch:
    # Get toots within the limit per iteration
    toots = mastodon.timeline_public(limit=toots_to_fetch - len(all_toots))
    all_toots.extend(toots)

# Get the current date and time in the "yyyy-MM-dd-HH-mm-ss" format
current_datetime = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
json_file_name = f"data/{current_datetime}.json"

# Write the data into a JSON file using the custom JSON encoder
with open(json_file_name, 'w', encoding='utf-8') as json_file:
    json.dump(all_toots, json_file, ensure_ascii=False, default=custom_json_encoder)

# Use the HDFS library to store the JSON file on HDFS
hdfs_client = InsecureClient("http://localhost:9870", user="hadoop")
print("Success !")
hdfs_directory = "/Mastadon"
hdfs_client.upload(hdfs_directory, json_file_name, overwrite=True, n_threads=1)

print(f"The toots have been stored in the file '{json_file_name}' and on HDFS: {hdfs_directory}/{json_file_name}")

# # Display the 5 first rows of the JSON file
# with open(json_file_name, 'r', encoding='utf-8') as json_file:
#     data = json.load(json_file)

# # Display the first 5 entries
# for entry in data[:5]:
#     print(entry)
