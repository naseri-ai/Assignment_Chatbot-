def estimate_confidence(score, answer):
    base = score
    length_bonus = min(len(answer) / 500, 0.15)

    return round(min(base + length_bonus, 1.0), 2)