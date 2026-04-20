from supabase import create_client
from datetime import datetime

# 🔑 Replace with your Supabase credentials
SUPABASE_URL = "https://nbisgligcpjvwdsndmfp.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5iaXNnbGlnY3Bqdndkc25kbWZwIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzY2MDQwOTYsImV4cCI6MjA5MjE4MDA5Nn0.pFptiVEl9224J_Vk9RKm1byLyotB4FCkWbBtMZetSr4"

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)


def log(question, answer, confidence):
    try:
        data = {
            "question": question,
            "answer": answer,
            "confidence": float(confidence),
            "created_at": datetime.utcnow().isoformat()
        }

        supabase.table("chat_logs").insert(data).execute()

    except Exception as e:
        print("Logging error:", e)
