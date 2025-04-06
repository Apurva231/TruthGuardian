import cv2
import mediapipe as mp
import numpy as np

# Initialize mediapipe face mesh
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(static_image_mode=True, max_num_faces=1)

# Load image
image_path = "test_image6.png"
image = cv2.imread(image_path)

if image is None:
    print("Error: Image not found!")
    exit()

# Convert image to RGB for MediaPipe
rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
results = face_mesh.process(rgb_image)

# Exit if no face detected
if not results.multi_face_landmarks:
    print("No face detected!")
    exit()

# Get image dimensions
h, w, _ = image.shape

# Get landmark coordinates
landmarks = results.multi_face_landmarks[0].landmark
points = np.array([[int(lm.x * w), int(lm.y * h)] for lm in landmarks])

# Calculate horizontal midpoint of the face
x_coords = points[:, 0]
mid_x = (np.min(x_coords) + np.max(x_coords)) // 2

# Symmetric landmark pairs (left, right)
symmetric_pairs = [
    (33, 263),   # Outer eye corners
    (133, 362),  # Inner eye corners
    (61, 291),   # Mouth corners
    (234, 454),  # Jawline near ears
    (93, 323),   # Cheeks
]

# Calculate asymmetry for each pair
asymmetry_scores = []

for left_idx, right_idx in symmetric_pairs:
    left = points[left_idx]
    right = points[right_idx]
    
    # Mirror right point horizontally
    mirrored_right = np.array([2 * mid_x - right[0], right[1]])

    # Distance between left point and mirrored right
    distance = np.linalg.norm(left - mirrored_right)
    asymmetry_scores.append(distance)

# Compute average asymmetry score
symmetry_score = np.mean(asymmetry_scores)

# Classification using updated threshold
threshold = 8.0
if symmetry_score >= threshold:
    classification = "Fake"
    color = (0, 0, 255)  # Red
else:
    classification = "Real"
    color = (0, 255, 0)  # Green

# Draw facial landmarks
for pt in points:
    cv2.circle(image, tuple(pt), 1, (0, 255, 0), -1)

# Draw symmetry score and prediction
cv2.putText(image, f"Symmetry Score: {symmetry_score:.2f}", (30, 50),
            cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
cv2.putText(image, f"Prediction: {classification}", (30, 90),
            cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)

# Print results in terminal
print(f"Symmetry Score: {symmetry_score:.2f}")
print(f"Prediction: {classification}")

# Show image
cv2.imshow("Face Landmarks with Symmetry Score", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
