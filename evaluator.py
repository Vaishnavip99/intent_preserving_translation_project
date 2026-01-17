from intent_extractor import extract_intent

def intent_fitness(src, tgt):
    score = 0
    if src["speech_act"] == tgt["speech_act"]:
        score += 0.5
    if src["emotion"] == tgt["emotion"]:
        score += 0.3
    if src["confidence_level"] == tgt["confidence_level"]:
        score += 0.2
    return score

def select_best(candidates, src_intent):
    scored = []
    for c in candidates:
        tgt_intent = extract_intent(c)
        scored.append((c, intent_fitness(src_intent, tgt_intent)))

    scored.sort(key=lambda x: x[1], reverse=True)
    best, score = scored[0]

    return best if score >= 0.5 else None, score
