# -*- coding: utf-8 -*-
import psycopg2, sys
from collections import Counter

sys.stdout.reconfigure(encoding='utf-8')

DATABASE_URL = "postgresql://neondb_owner:npg_uFxVSRoTj95w@ep-damp-sea-anvn4fw4.c-6.us-east-1.aws.neon.tech/neondb?sslmode=require"
conn = psycopg2.connect(DATABASE_URL)
cur = conn.cursor()
cur.execute("SELECT id, body FROM reviews ORDER BY id")
rows = cur.fetchall()
cur.close()
conn.close()
print(f"Caricate: {len(rows)}")

target_fragments = [
    "la montatura così fine mi trasmette una delicatezza che non adoro",
    "assomigliano a un archetipo che esiste già da tempo",
    "le lenti marroni sfumate e la",
    "che ho capito il resto:",
    "funzionano meglio dal vivo che in",
    "il doppio ponte sul mio naso non",
    "Sul viso appare più leggero del",
    "Non tradisce mai la promessa del",
    "la lente chiara in basso e più intensa sopra",
    "vorrei qualche segnale in più di unicità",
]

for frag in target_fragments:
    matches = []
    for rid, body in rows:
        if frag in body:
            idx = body.find(frag)
            start = body.rfind('.', 0, idx)
            start = start + 1 if start >= 0 else 0
            end = body.find('.', idx + len(frag))
            end = end + 1 if end >= 0 else len(body)
            sentence = body[start:end].strip()
            matches.append((rid, sentence[:150]))
    print(f"\n=== [{len(matches)}x] '{frag}' ===")
    seen = Counter(s for _, s in matches)
    for s, cnt in seen.most_common(5):
        print(f"  {cnt}x: {s}")
