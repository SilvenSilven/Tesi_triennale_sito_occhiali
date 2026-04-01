# -*- coding: utf-8 -*-
import psycopg2, sys, re
from collections import defaultdict
sys.stdout.reconfigure(encoding='utf-8')

DATABASE_URL = "postgresql://neondb_owner:npg_uFxVSRoTj95w@ep-damp-sea-anvn4fw4.c-6.us-east-1.aws.neon.tech/neondb?sslmode=require"

# Cerca le frasi complete per i pattern noti dal verify
SEARCH_TERMS = [
    "verde salvia non va d'accordo",
    "viso stretto possono sembrare",
    "viso molto lungo l'ottagono",
    "nello specchio di casa",
    "scontrato con un fatto semplice",
    "presi quasi d'impulso",
    "intelligenza formale che si nota",
    "struttura sottile pu",
    "Non lo bocci",
    "ponte non",
    "best friend universale",
    "viaggio tra aeroporto",
    "pulizia che mi convince",
    "danno carattere senza essere rumorosi",
    "dubbio iniziale, temevo che",
    "Equilibrio tra vintage e attuale",
    "restano eleganti senza irrigidire",
]

conn = psycopg2.connect(DATABASE_URL)
cur = conn.cursor()
cur.execute("SELECT id, body FROM reviews ORDER BY id")
rows = cur.fetchall()

print(f"Recensioni totali: {len(rows)}")
print()

for term in SEARCH_TERMS:
    matches = []
    for rid, body in rows:
        if body and term in body:
            # Trova la frase contenente il termine
            sentences = re.split(r'(?<=[.!?])\s+', body)
            for s in sentences:
                if term in s:
                    matches.append(s.strip())
    
    if matches:
        # Conta le frasi uniche
        counts = defaultdict(int)
        for m in matches:
            counts[m] += 1
        sorted_counts = sorted(counts.items(), key=lambda x: -x[1])
        print(f"=== '{term}' ===")
        for frase, cnt in sorted_counts[:5]:
            print(f"  {cnt}x -> {frase}")
        print()

cur.close()
conn.close()
