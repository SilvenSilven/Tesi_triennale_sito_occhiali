#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Trova le frasi complete che contengono i pattern ripetuti."""
import psycopg2, re

DATABASE_URL = (
    "postgresql://neondb_owner:npg_uFxVSRoTj95w"
    "@ep-damp-sea-anvn4fw4.c-6.us-east-1.aws.neon.tech"
    "/neondb?sslmode=require"
)

FRAGMENTS = [
    "Li sto usando più del previsto",
    "Avevo voglia di farmeli piacere, soprattutto per",
    "molto meno del previsto. Sulla carta",
    "ma non abbastanza da farmi sciogliere del tutto. Nel contesto",
]

conn = psycopg2.connect(DATABASE_URL)
cur = conn.cursor()
cur.execute("SELECT id, body FROM reviews ORDER BY id")
rows = cur.fetchall()
cur.close(); conn.close()

for frag in FRAGMENTS:
    print(f"\n{'='*60}")
    print(f"FRAMMENTO: '{frag}'")
    examples = []
    for rid, body in rows:
        if frag in body:
            # Trova la frase completa (fino al prossimo punto/fine riga)
            idx = body.index(frag)
            # Cerca inizio frase (cerca il punto precedente + spazio, o inizio stringa)
            start = body.rfind('. ', 0, idx)
            if start == -1:
                start = 0
            else:
                start += 2  # skip '. '
            # Cerca fine frase (prossimo punto)
            end = body.find('. ', idx)
            if end == -1:
                end = len(body)
            else:
                end += 1  # include il punto
            sentence = body[start:end].strip()
            examples.append(sentence)
            if len(examples) >= 3:
                break
    for i, ex in enumerate(examples, 1):
        print(f"  [{i}] {ex}")
