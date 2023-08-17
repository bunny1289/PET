from pymongo import MongoClient

client = MongoClient("mongodb+srv://karthikm20:12345677@cluster0.qrb6qry.mongodb.net/?retryWrites=true&w=majority")
db = client.your_database_name  # Replace "your_database_name" with the actual database name

photo_collection = db.photos
retrieved_document = photo_collection.find_one()
retrieved_photo_data = retrieved_document["photo"]

with open("retrieved_photo.jpg", "wb") as retrieved_photo_file:
    retrieved_photo_file.write(retrieved_photo_data)

print("Retrieved photo saved.")
