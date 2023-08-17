# from pymongo import MongoClient
from mongoConnection import db
ex = 'coding'
photo_collection = db[ex]  # Replace "photos" with your collection name

# Find all documents in the collection
all_photo_documents = photo_collection.find()

# Iterate through the documents and retrieve the photo data
for document in all_photo_documents:
    photo_data = document["photo"]
    
    # Save the retrieved photo data to a file
    photo_id = document["_id"]
    photo_filename = f"E:\images\{ex}\photo_{photo_id}.jpg"
    with open(photo_filename, "wb") as photo_file:
        photo_file.write(photo_data)
    
    print(f"Photo with ID {photo_id} saved as {photo_filename}")

print("All photos retrieved.")
