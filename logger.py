import csv
import os
from datetime import datetime

LOG_FILE = "chatbot_logs.csv"


def log(question, answer, confidence):
    os.makedirs("logs", exist_ok=True)

    exists = os.path.isfile(LOG_FILE)

    with open(LOG_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)

        if not exists:
            writer.writerow(["time", "question", "answer", "confidence"])

        writer.writerow([
            datetime.now().isoformat(),
            question,
            answer,
            confidence
        ])
