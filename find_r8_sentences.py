#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import psycopg2
from collections import Counter

DATABASE_URL = (
    "postgresql://neondb_owner:npg_uFxVSRoTj95w"
    "@ep-damp-sea-anvn4fw4.c-6.us-east-1.aws.neon.tech"
    "/neondb?sslmode=require"
)

FRAGMENTS = [
    "Li ho messi alla prova in",
    "su un viso struccato e capelli",
    "Li ho presi quasi d'impulso, temevo che",
    "in un modo che trovo molto",
    "solo a tratti. Da fermo mi colpiscono",
    "Per me restano più convincenti come oggetto",
    "Avevo qualche dubbio iniziale, è che",
    "e il suo carattere diventa leggibile",
]

conn = psycopg2.connect(DATABASE_URL)
cur = conn.cursor()
cur.execute("SELECT id, body FROM reviews ORDER BY id")
rows = cur.fetchall()
cur.close(); conn.close()

for frag in FRAGMENTS:
    print(f"\n{'='*60}")
    print(f"FRAMMENTO: '{frag}'")
    sentences = Counter()
    for rid, body in rows:
        if frag not in body:
            continue
        idx = body.index(frag)
        start = body.rfind('. ', 0, idx)
        start = 0 if start == -1 else start + 2
        end = body.find('.', idx + len(frag))
        end = len(body) if end == -1 else end + 1
        sentence = body[start:end].strip()
        sentences[sentence] += 1
    for sent, cnt in sentences.most_common(4):
        print(f"  {cnt:3d}x | {sent}")
