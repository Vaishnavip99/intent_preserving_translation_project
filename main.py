from intent_extractor import extract_intent
from candidate_generator import generate_candidates
from evaluator import select_best

def run_translation(text):
    src_intent = extract_intent(text)
    candidates = generate_candidates(text)
    final, confidence = select_best(candidates, src_intent)

    return {
        "input": text,
        "detected_intent": src_intent,
        "final_translation": final,
        "confidence": round(confidence, 2)
    }

if __name__ == "__main__":
    result = run_translation("ठीक है, देखेंगे")
    print(result)
