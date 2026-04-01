#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Mostra frasi complete con >=5x e analizza pattern cross-sentence."""
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

sentence_counts = Counter()
for rid, body in rows:
    frasi = re.split(r'(?<=\.)\s+', body.strip())
    seen = set()
    for frase in frasi:
        frase = frase.strip()
        if len(frase) < 15 or len(frase) > 250:
            continue
        if frase not in seen:
            sentence_counts[frase] += 1
            seen.add(frase)

print("=== FRASI COMPLETE CON >=5x ===")
for frase, cnt in sentence_counts.most_common(200):
    if cnt < 5:
        break
    print(f"  {cnt:3d}x | {frase}")

print("\n=== ANALISI FRAMMENTI CROSS-SENTENCE ===")
# Cerca frammenti che attraversano il confine . (periodo)
cross_fragments = [
    "e non mi hanno deluso.",
    "L'unico vero limite è che",
    "Lato meno convincente:",
    "Per me il punto si riassume così:",
    "fosse troppo evidente. Invece hanno una",
    "tiene la scena senza strafare.",
    "qui lavorano bene insieme.",
    "su un viso struccato e capelli raccolti,",
    "solo a tratti.",
    "Da fermo mi colpiscono",
    "si sente subito e hanno una",
    "il peso si sente più di",
    "abbinati a cose che avevo già",
    "insieme a un look minimale che da solo diceva",
    "tra metro, marciapiedi e tavolini al sole,",
    "Non pensavo mi sarebbero piaciuti così",
]

for frag in cross_fragments:
    cnt = sum(1 for _, body in rows if frag in body)
    if cnt >= 5:
        # Mostra un esempio
        ex = next((body for _, body in rows if frag in body), "")
        idx = ex.find(frag)
        snippet = ex[max(0, idx-20):idx+len(frag)+50].replace('\n', ' ')
        print(f"  {cnt:3d}x | '{frag}' → ...{snippet}...")
