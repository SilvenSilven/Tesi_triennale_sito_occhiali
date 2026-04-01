# -*- coding: utf-8 -*-
"""Round 21c - Ultimi 2 pattern residui."""
import psycopg2, sys
from collections import defaultdict
sys.stdout.reconfigure(encoding='utf-8')

DATABASE_URL = "postgresql://neondb_owner:npg_uFxVSRoTj95w@ep-damp-sea-anvn4fw4.c-6.us-east-1.aws.neon.tech/neondb?sslmode=require"

PATTERNS = {
    "chiede spazio sul viso e nello stile e": [
        "richiede presenza sul volto e nella scelta stilistica e",
        "pretende il suo spazio tanto sul viso quanto nel look e",
        "esige una certa ampiezza sul viso e nel guardaroba e",
        "domanda spazio sia sul viso sia nell'outfit e",
        "occupa il suo spazio tra lineamenti e stile e",
        "reclama attenzione sul volto e nell'abbinamento e",
    ],
    "non è il più stabile di sempre e": [
        "la stabilità non è il suo punto forte e",
        "non brilla per tenuta sul naso e",
        "non è campione di stabilità e",
        "la tenuta potrebbe essere migliore e",
        "non è il più saldo sulla faccia e",
    ],
}

conn = psycopg2.connect(DATABASE_URL)
cur = conn.cursor()
cur.execute("SELECT id, body FROM reviews ORDER BY id")
rows = cur.fetchall()

pattern_occurrence = defaultdict(int)
updates = []
for rid, body in rows:
    new_body = body
    modified = False
    for pattern, alternatives in PATTERNS.items():
        if pattern in new_body:
            idx = pattern_occurrence[pattern]
            pattern_occurrence[pattern] += 1
            alt = alternatives[idx % len(alternatives)]
            new_body = new_body.replace(pattern, alt, 1)
            modified = True
    if modified:
        updates.append((new_body, rid))

for p, c in sorted(pattern_occurrence.items(), key=lambda x: -x[1]):
    print(f"  {c}x | {p}")

print(f"Totale: {sum(pattern_occurrence.values())} occ, {len(updates)} recensioni")
errors = 0
for i in range(0, len(updates), 50):
    batch = updates[i:i+50]
    try:
        cur.executemany("UPDATE reviews SET body=%s WHERE id=%s", batch)
        conn.commit()
    except Exception as e:
        conn.rollback()
        errors += 1
        print(f"Errore: {e}")

cur.close()
conn.close()
print(f"Aggiornate: {len(updates)} | Errori: {errors}")
