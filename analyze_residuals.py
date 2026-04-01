#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Analisi approfondita pattern residui nel DB e generazione fix."""

import psycopg2
from collections import Counter, defaultdict
import json

DATABASE_URL = (
    "postgresql://neondb_owner:npg_uFxVSRoTj95w"
    "@ep-damp-sea-anvn4fw4.c-6.us-east-1.aws.neon.tech"
    "/neondb?sslmode=require"
)

conn = psycopg2.connect(DATABASE_URL)
cur = conn.cursor()
cur.execute("SELECT id, body, stars, is_published FROM reviews ORDER BY id")
rows = cur.fetchall()
cur.close()
conn.close()

print(f"Totale recensioni: {len(rows)}")
published = [(r[0], r[1], r[2]) for r in rows if r[3]]
unpublished = [(r[0], r[1], r[2]) for r in rows if not r[3]]
print(f"  Pubblicate: {len(published)}")
print(f"  Non pubblicate: {len(unpublished)}")

# Campione delle 5 recensioni con il pattern top
pattern_check = "La cosa più onesta che posso dire è che"
print(f"\nCampione recensioni con '{pattern_check[:40]}...':")
count = 0
for r in rows:
    if pattern_check in r[1]:
        count += 1
        if count <= 3:
            print(f"  ID:{r[0]} published:{r[3]} | {r[1][:150]}")
            print()
print(f"  TOTALE: {count}")

# Top pattern in ALL reviews
all_bodies = [r[1] for r in rows]

def get_ngrams(text, n):
    words = text.split()
    return [" ".join(words[i:i+n]) for i in range(len(words)-n+1)]

all_ngrams = Counter()
for body in all_bodies:
    seen = set()
    for n in range(7, 12):
        for ng in get_ngrams(body, n):
            if ng not in seen:
                seen.add(ng)
                all_ngrams[ng] += 1

# Top 20 frasi complete (7+ parole, >=10x)
top = [(ng, c) for ng, c in all_ngrams.items() if c >= 10]
top.sort(key=lambda x: -x[1])

print(f"\n=== TOP 30 FRASI RIPETUTE (7+ parole, >=10x) ===")
for ng, c in top[:30]:
    print(f"  {c:3d}x | {ng}")

# Salva le top 100 per lavorarci
with open("residual_patterns_final.json", "w", encoding="utf-8") as f:
    json.dump([{"phrase": ng, "count": c} for ng, c in top[:100]], f, ensure_ascii=False, indent=2)

print(f"\nSalvati {len(top[:100])} pattern in residual_patterns_final.json")
print(f"Totale frasi ripetute >=10x: {len([x for x in top if x[1]>=10])}")
