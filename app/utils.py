import re


def make_json(text : str) -> str:
    # Step 1: Extract JSON code block (inside triple backticks or the first {...})
    match = re.search(r'```(?:json)?\s*({.*?})\s*```', text, re.DOTALL)

    # Fallback: look for first top-level {...} block
    if not match:
        match = re.search(r'({[^{}]*?(?:{[^{}]*?}[^{}]*?)*})', text, re.DOTALL)

    json_str = match.group(1) if match else None

    return json_str