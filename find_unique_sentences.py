#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Trova le FRASI COMPLETE (non n-gram) più ripetute nel DB.
Divide il testo di ogni recensione in frasi usando il punto come separatore,
poi conta le frasi identiche che appaiono in più recensioni.
"""
import psycopg2, re
from collections import Counter

DATABASE_URL = (
    "postgresql://neondb_owner:npg_uFxVSRoTj95w"
    "@ep-damp-sea-anvn4fw4.c-6.us-east-1.aws.neon.tech"
    "/neondb?sslmode=require"
)

conn = psycopg2.connect(DATABASE_URL)
cur = conn.cursor()
cur.execute("SELECT id, body FROM reviews ORDER BY id")
rows = cur.fetchall()
cur.close(); conn.close()

sentence_counts = Counter()   # frase → numero di recensioni in cui appare
sentence_ids = {}             # frase → lista di ID che la contengono

for rid, body in rows:
    # Divide in frasi (split su punto + spazio o punto finale)
    frasi = re.split(r'(?<=\.)\s+', body.strip())
    seen_in_review = set()
    for frase in frasi:
        frase = frase.strip()
        # Scarta frasi troppo corte o troppo lunghe
        if len(frase) < 20 or len(frase) > 250:
            continue
        # Normalizza
        key = frase
        if key not in seen_in_review:
            sentence_counts[key] += 1
            if key not in sentence_ids:
                sentence_ids[key] = []
            sentence_ids[key].append(rid)
            seen_in_review.add(key)

print("=== FRASI COMPLETE PIÙ RIPETUTE (>=10x) ===")
count = 0
for frase, cnt in sentence_counts.most_common(150):
    if cnt < 10:
        break
    print(f"  {cnt:3d}x | {frase}")
    count += 1
print(f"\nTotale frasi uniche con >=10x: {count}")
print(f"Totale frasi uniche con >=5x: {sum(1 for c in sentence_counts.values() if c >= 5)}")
print(f"Totale frasi uniche con >=3x: {sum(1 for c in sentence_counts.values() if c >= 3)}")
