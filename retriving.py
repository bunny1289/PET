# Replace "your_database_name" with the actual database name
from mongoConnection import db
photo_collection = db['photos']
retrieved_document = photo_collection.find_one()
retrieved_photo_data = retrieved_document["photo"]

with open("retrieved_photo.jpg", "wb") as retrieved_photo_file:
    retrieved_photo_file.write(retrieved_photo_data)

print("Retrieved photo saved.")
