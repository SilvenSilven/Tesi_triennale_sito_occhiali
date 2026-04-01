#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Trova frasi complete nel DB per i frammenti parziali rilevati."""

import psycopg2
from collections import Counter

DATABASE_URL = (
    "postgresql://neondb_owner:npg_uFxVSRoTj95w"
    "@ep-damp-sea-anvn4fw4.c-6.us-east-1.aws.neon.tech"
    "/neondb?sslmode=require"
)

FRAGMENTS = [
    "e adesso posso dire che ha",
    "La parte migliore è che la",
    "Su di me funzionano bene in",
    "Con il contesto giusto rende molto",
]

conn = psycopg2.connect(DATABASE_URL)
cur = conn.cursor()
cur.execute("SELECT id, body FROM reviews ORDER BY id")
rows = cur.fetchall()
cur.close(); conn.close()

for frag in FRAGMENTS:
    print(f"\n=== '{frag}' ===")
    contexts = Counter()
    for _, body in rows:
        idx = body.find(frag)
        while idx != -1:
            # Estrai 80 caratteri dal punto di inizio per vedere la frase completa
            snip = body[max(0, idx-5):idx+120]
            # Tronca alla prossima punteggiatura
            for end_char in ['.', '!', '?', '\n']:
                end_pos = snip.find(end_char, len(frag)+5)
                if end_pos != -1:
                    snip = snip[:end_pos+1]
                    break
            contexts[snip.strip()] += 1
            idx = body.find(frag, idx+1)

    for s, c in contexts.most_common(5):
        print(f"  {c:3d}x | {s[:100]}")
