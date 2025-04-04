# metadata_check.py
from PIL import Image
import exifread

def check_metadata(image_path):
    image = Image.open(image_path)
    tags = {}
    with open(image_path, 'rb') as f:
        exif = exifread.process_file(f)
        for tag in exif.keys():
            if tag not in ('JPEGThumbnail', 'TIFFThumbnail'):
                tags[tag] = str(exif[tag])

    return tags
