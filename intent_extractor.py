import json
from gpt_utils import gpt_call

def extract_intent(text):
    prompt = f"""
You are an intent analysis engine.

Analyze the following sentence and return ONLY valid JSON.

Sentence:
{text}

Return format:
{{
  "speech_act": "",
  "emotion": "",
  "confidence_level": ""
}}
"""

    response = gpt_call(prompt, force_json=True)

    print("\n[DEBUG] GPT Intent Response:\n", response)

    try:
        return json.loads(response)
    except json.JSONDecodeError:
        return {
            "speech_act": "unknown",
            "emotion": "unknown",
            "confidence_level": "unknown"
        }
