import pymongo
import geojson
import json

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["telkomsat"]
collection = db["desas"]
collection.create_index([("geometry.coordinates", "2dsphere")])


# Load GeoJSON data
with open("data-penduduk.json") as f:
    data = json.load(f)

# Insert GeoJSON data into MongoDB
features = data["features"]
# data = json.dumps(features)
result = collection.insert_many(features)


print(f"Imported {len(result.inserted_ids)} documents")

# import requests
# import geojson
# import json


# url = "http://localhost:3030/desa"
# headers = {"Content-Type": "application/json"}

# with open('data-penduduk.geojson')as  f:
#     data = geojson.load(f)
# j = 0
# print('Success open data')
# for i in data["features"]:
#     j = j+1
#     response = requests.post(url, data=json.dumps(data), headers=headers)
#     if (response.status_code == 200):
#         print('Success:', j+1)
