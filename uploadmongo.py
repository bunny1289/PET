# from pymongo import MongoClient
import os
from mongoConnection import db
def trigger(ex):
    imagename = ""
    k = os.listdir()
    for x in k:
        try:
            if x.split('.')[1] == "png":
                imagename = x
        except:
            pass

    with open(imagename, "rb") as photo_file:
        photo_data = photo_file.read()

    photo_collection = db[ex] 
    photo_document = {"photo": photo_data}

    inserted_document = photo_collection.insert_one(photo_document)
    print("Photo inserted with ID:", inserted_document.inserted_id)
    # file_path = "path_to_your_file.txt"  # Replace with the actual path of the file you want to remove

    try:
        os.remove(imagename)
        # print(f"File {file_path} removed successfully.")
    except OSError as e:
        # print(f"Error removing file {file_path}: {e}")
        pass
    
    for x in k:
        try:
            if x.split('.')[1] == "png":
                trigger()
        except:
            pass

