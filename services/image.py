async def analyze_image(file):
    return {
        "verdict": "Manipulated Image",
        "confidence": 92,
        "reasons": ["Reverse image search shows older unrelated event"],
        "source_links": ["https://fact-check.org/photo-origin"]
    }
