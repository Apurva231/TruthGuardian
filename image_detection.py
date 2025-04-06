import cv2
import mediapipe as mp
import numpy as np
import tempfile

mp_face_mesh = mp.solutions.face_mesh

def analyze_face_image(file_bytes):
    # Write bytes to temp file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp:
        tmp.write(file_bytes)
        tmp_path = tmp.name

    # Load image
    image = cv2.imread(tmp_path)
    if image is None:
        return {
            "label": "Error",
            "score": 0,
            "notes": ["Image could not be read."]
        }

    face_mesh = mp_face_mesh.FaceMesh(static_image_mode=True, max_num_faces=1)
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb_image)

    if not results.multi_face_landmarks:
        return {
            "label": "Fake",
            "score": 100,
            "notes": ["No face detected in image."]
        }

    h, w, _ = image.shape
    landmarks = results.multi_face_landmarks[0].landmark
    points = np.array([[int(lm.x * w), int(lm.y * h)] for lm in landmarks])

    x_coords = points[:, 0]
    mid_x = (np.min(x_coords) + np.max(x_coords)) // 2

    symmetric_pairs = [
        (33, 263), (133, 362), (61, 291), (234, 454), (93, 323),
    ]

    asymmetry_scores = []
    for left_idx, right_idx in symmetric_pairs:
        left = points[left_idx]
        right = points[right_idx]
        mirrored_right = np.array([2 * mid_x - right[0], right[1]])
        distance = np.linalg.norm(left - mirrored_right)
        asymmetry_scores.append(distance)

    symmetry_score = np.mean(asymmetry_scores)
    threshold = 8.0
    label = "Fake" if symmetry_score >= threshold else "Real"
    confidence = min(100, round((symmetry_score / threshold) * 100)) if label == "Fake" else 100 - int(symmetry_score)

    return {
        "label": label,
        "score": confidence,
        "notes": [f"Symmetry score: {symmetry_score:.2f}"]
    }
