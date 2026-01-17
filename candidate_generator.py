from gpt_utils import gpt_call

def generate_candidates(text, n=5):
    prompt = f"""
You are a professional translator.
Generate {n} distinct English translations of the following sentence.
Preserve intent and tone.

Return ONLY a numbered list.

Sentence:
{text}
"""

    raw = gpt_call(prompt, temperature=0.7)

    print("\n[DEBUG] GPT Candidate Response:\n", raw)

    candidates = []
    for line in raw.split("\n"):
        line = line.strip()
        if line and line[0].isdigit() and ". " in line:
            candidates.append(line.split(". ", 1)[1])

    return candidates if candidates else ["Translation not available"]
