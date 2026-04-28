from knowledge_base import KNOWLEDGE_BASE
from embeddings import encode, cosine_sim

SEM_WEIGHT = 0.4
KEY_WEIGHT = 0.6
MULTI_INTENT_THRESHOLD = 0.75  # second intent must be close


# Precompute KB embeddings
KB = []

for entry in KNOWLEDGE_BASE:
    if entry["patterns"]:
        vec = encode(entry["patterns"]).mean(axis=0)
    else:
        vec = None

    KB.append({
        "entry": entry,
        "vector": vec,
        "patterns": entry["patterns"]
    })


def keyword_score(query, patterns):
    query_words = set(query.lower().split())
    scores = []

    for pattern in patterns:
        pattern_words = set(pattern.lower().split())
        overlap = query_words.intersection(pattern_words)

        if pattern_words:
            scores.append(len(overlap) / len(pattern_words))

    return max(scores) if scores else 0


def compute_scores(question):
    q_vec = encode([question])[0]

    scored = []

    for item in KB:
        entry = item["entry"]
        vec = item["vector"]
        patterns = item["patterns"]

        semantic = cosine_sim(q_vec, vec) if vec is not None else 0
        semantic = (semantic + 1) / 2

        keyword = keyword_score(question, patterns)

        final = (SEM_WEIGHT * semantic) + (KEY_WEIGHT * keyword)

        scored.append({
            "entry": entry,
            "score": final
        })

    return sorted(scored, key=lambda x: x["score"], reverse=True)


def get_response(question):
    ranked = compute_scores(question)

    top1 = ranked[0]
    top2 = ranked[1]

    # If low confidence → fallback
    if top1["score"] < 0.4:
        for entry in KNOWLEDGE_BASE:
            if entry["intent"] == "fallback":
                return entry["answer"], top1["score"], "fallback"

    # Multi-intent logic
    if top2["score"] > (top1["score"] * MULTI_INTENT_THRESHOLD):
        combined = (
            top1["entry"]["answer"] +
            "\n\nAdditionally:\n" +
            top2["entry"]["answer"]
        )
        return combined, top1["score"], top1["entry"]["intent"]

    return top1["entry"]["answer"], top1["score"], top1["entry"]["intent"]
