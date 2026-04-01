#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Trova le frasi complete per i frammenti del round 4."""

import psycopg2
from collections import Counter

DATABASE_URL = (
    "postgresql://neondb_owner:npg_uFxVSRoTj95w"
    "@ep-damp-sea-anvn4fw4.c-6.us-east-1.aws.neon.tech"
    "/neondb?sslmode=require"
)

FRAGMENTS = [
    "Su di me funzionano bene con",
    "che ho capito il resto: la",
    "ha una bella idea dietro. Poi però",
    "dà proprio quel segno in più che cercavo.",
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
            snip = body[max(0, idx):idx+200]
            for ec in ['.', '!', '?', '\n']:
                ep = snip.find(ec, len(frag))
                if ep != -1:
                    snip = snip[:ep+1]
                    break
            contexts[snip.strip()] += 1
            idx = body.find(frag, idx+1)
    for s, c in contexts.most_common(8):
        print(f"  {c:3d}x | {s[:120]}")
