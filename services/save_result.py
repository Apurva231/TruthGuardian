from database.mongo import results_collection

def save_to_db(data):
    results_collection.insert_one(data)
