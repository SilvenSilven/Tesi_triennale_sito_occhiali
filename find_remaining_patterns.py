# -*- coding: utf-8 -*-
import psycopg2, sys, re
from collections import Counter, defaultdict

sys.stdout.reconfigure(encoding='utf-8')

DATABASE_URL = "postgresql://neondb_owner:npg_uFxVSRoTj95w@ep-damp-sea-anvn4fw4.c-6.us-east-1.aws.neon.tech/neondb?sslmode=require"
conn = psycopg2.connect(DATABASE_URL)
cur = conn.cursor()
cur.execute("SELECT id, body FROM reviews ORDER BY id")
rows = cur.fetchall()
cur.close()
conn.close()
print(f"Caricate: {len(rows)}")

# Target: find sentences containing these n-gram fragments (>= 9x)
target_fragments = [
    "non è il modello per chi",
    "dal vivo il blu è più",
    "costruiscono qualcosa di molto riuscito",
    "non c'è modo di farli passare per neutri",
    "la leggerezza del metallo mi fa temere",
    "con una giacca destrutturata e sneakers",
    "le lenti marroni sfumate e la",
    "richiedono un gusto un minimo definito",
    "funzionano bene su chi ama il",
    "è che montatura oversize ambra traslucida",
    "che ho capito il resto",
]

for frag in target_fragments:
    matches = []
    for rid, body in rows:
        if frag in body:
            # find the surrounding sentence
            idx = body.find(frag)
            start = body.rfind('.', 0, idx)
            start = start + 1 if start >= 0 else 0
            end = body.find('.', idx + len(frag))
            end = end + 1 if end >= 0 else len(body)
            sentence = body[start:end].strip()
            matches.append((rid, sentence[:120]))
    print(f"\n=== [{len(matches)}x] '{frag}' ===")
    seen = Counter(s for _, s in matches)
    for s, cnt in seen.most_common(5):
        print(f"  {cnt}x: {s}")
