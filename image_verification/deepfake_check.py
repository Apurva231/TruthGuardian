# deepfake_check.py
import cv2
import numpy as np

def detect_blur_and_edges(image_path):
    image = cv2.imread(image_path, 0)  # grayscale
    laplacian = cv2.Laplacian(image, cv2.CV_64F).var()
    edges = cv2.Canny(image, 100, 200)
    edge_score = np.mean(edges)

    return {
        "blurriness_score": laplacian,
        "edge_score": edge_score,
        "manipulated": laplacian < 50 or edge_score < 20
    }
