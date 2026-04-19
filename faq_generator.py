import pandas as pd
from sklearn.cluster import KMeans
from embeddings import encode


def generate_faq(log_file="logs/chatbot_logs.csv", num_clusters=5):
    df = pd.read_csv(log_file)

    questions = df["question"].dropna().tolist()

    if len(questions) < num_clusters:
        return ["Not enough data to generate FAQs yet."]

    embeddings = encode(questions)

    kmeans = KMeans(n_clusters=num_clusters, random_state=42)
    labels = kmeans.fit_predict(embeddings)

    faq = []

    for i in range(num_clusters):
        cluster_questions = [q for q, l in zip(questions, labels) if l == i]

        if not cluster_questions:
            continue

        representative = cluster_questions[0]

        faq.append({
            "question": representative,
            "examples": cluster_questions[:3]
        })

    return faq


if __name__ == "__main__":
    faqs = generate_faq()

    for i, f in enumerate(faqs, 1):
        print(f"\nFAQ {i}: {f['question']}")
        print("Examples:")
        for ex in f["examples"]:
            print("-", ex)