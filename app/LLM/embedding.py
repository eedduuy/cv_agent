import json


def extract_text_chunks(profile):
    chunks = []
    for section in ["summary", "experience", "education", "courses", "languages", "skills"]:
        items = profile.get(section, [])
        if isinstance(items, str):
            chunks.append(f"{section.capitalize()}: {items}")
        elif isinstance(items, list):
            for item in items:
                chunks.append(json.dumps(item))
    return chunks

