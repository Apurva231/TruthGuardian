from pymongo import MongoClient
import gridfs

client = MongoClient("MONGO_URI")
db = client["rumor_detection"]
fs = gridfs.GridFS(db)
image_results_collection = db["image_results"]
text_results_collection = db["text_results"]
audio_results_collection = db["audio_results"]