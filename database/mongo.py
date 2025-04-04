from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["rumor_detection"]
results_collection = db["analysis_results"]
