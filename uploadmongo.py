from pymongo import MongoClient
import os
client = MongoClient("mongodb+srv://karthikm20:12345677@cluster0.qrb6qry.mongodb.net/?retryWrites=true&w=majority")
db = client.your_database_name  # Replace "your_database_name" with the actual database name
imagename = ""
k = os.listdir()
for x in k:
    if x.split('.')[1] == "png":
        imagename = x
with open(imagename, "rb") as photo_file:
    photo_data = photo_file.read()

photo_collection = db.photos  # Replace "photos" with your desired collection name
photo_document = {"photo": photo_data}

inserted_document = photo_collection.insert_one(photo_document)
print("Photo inserted with ID:", inserted_document.inserted_id)
