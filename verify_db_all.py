#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Verifica stato pubblicazione e pattern su TUTTE le recensioni."""

import psycopg2
from collections import Counter

DATABASE_URL = (
    "postgresql://neondb_owner:npg_uFxVSRoTj95w"
    "@ep-damp-sea-anvn4fw4.c-6.us-east-1.aws.neon.tech"
    "/neondb?sslmode=require"
)

conn = psycopg2.connect(DATABASE_URL)
cur = conn.cursor()

# Distribuzione is_published
cur.execute("SELECT is_published, COUNT(*) FROM reviews GROUP BY is_published")
dist = cur.fetchall()
print("Distribuzione is_published:")
for row in dist:
    print(f"  {row[0]}: {row[1]}")

# Tutte le recensioni
cur.execute("SELECT id, body FROM reviews ORDER BY id")
rows = cur.fetchall()
cur.close()
conn.close()

print(f"\nTotale recensioni: {len(rows)}")

bodies = [r[1] for r in rows]

def get_ngrams(text, n):
    words = text.split()
    return [" ".join(words[i:i+n]) for i in range(len(words)-n+1)]

print("Analisi n-gram (6-10 parole)...")
all_ngrams = Counter()

for body in bodies:
    seen = set()
    for n in range(6, 11):
        for ng in get_ngrams(body, n):
            if ng not in seen:
                seen.add(ng)
                all_ngrams[ng] += 1

repeated = {ng: c for ng, c in all_ngrams.items() if c >= 5}
print(f"N-gram ripetuti (>=5x): {len(repeated)}")

top50 = sorted(repeated.items(), key=lambda x: -x[1])[:50]
print("\n=== TOP 50 FRASI RIPETUTE ===")
for i, (ng, c) in enumerate(top50, 1):
    print(f"  {c:4d}x | {ng[:80]}")

if repeated:
    pattern_set = set(repeated.keys())
    affected = sum(1 for b in bodies if any(p in b for p in pattern_set))
    print(f"\nRecensioni con almeno 1 frase ripetuta (>=5x): {affected}/{len(bodies)}")
else:
    print("\n✅ Nessun pattern con frequenza >=5 su tutte le recensioni!")

freq_10 = sum(1 for c in repeated.values() if c >= 10)
print(f"Pattern >=10x: {freq_10}")
