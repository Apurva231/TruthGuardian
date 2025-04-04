# analyze_image.py
from reverse_image import reverse_search
from metadata_check import check_metadata
from deepfake_check import detect_blur_and_edges

def analyze_image(image_path):
    reverse_result = reverse_search(image_path)
    meta_result = check_metadata(image_path)
    tamper_result = detect_blur_and_edges(image_path)

    result = {
        "reverse_match_found": reverse_result["reverse_match"],
        "match_details": reverse_result["matches"],
        "metadata": meta_result,
        "tampering_detected": tamper_result["manipulated"],
        "blurriness_score": tamper_result["blurriness_score"],
        "edge_score": tamper_result["edge_score"],
    }

    # Final flag
    result["final_verdict"] = "Possibly Fake" if result["tampering_detected"] or result["reverse_match_found"] else "Likely Real"

    return result
