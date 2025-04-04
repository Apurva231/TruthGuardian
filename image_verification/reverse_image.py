# reverse_image.py
from google.cloud import vision
import io

def reverse_search(image_path):
    client = vision.ImageAnnotatorClient.from_service_account_json('key.json')
    with io.open(image_path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)
    response = client.web_detection(image=image)
    web_detection = response.web_detection

    matches = []
    if web_detection.web_entities:
        for entity in web_detection.web_entities:
            matches.append((entity.description, entity.score))

    return {
        "reverse_match": bool(matches),
        "matches": matches
    }
