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

targets = [
    "non sembrano un travestimento se il resto del look",
    "la lente unica fa tutto il lavoro che deve",
    "non mi dimentico mai di averlo addosso",
    "e la costruzione da occhiale tecnico",
    "fuori dal contesto sportivo lo percepisco eccessivo",
    "e su di me si sente",
    "e hanno una presenza davvero forte",
    "con schermo iridescente crea un insieme davvero",
    "non passano inosservati in nessun modo",
    "il ponte alto resta una questione seria",
    "è che telaio leggero e pulito",
    "che profilo rimless molto arioso con",
    "temevo che accessorio protagonista fosse troppo",
    "è che profilo rimless molto arioso con",
]

for frag in targets:
    matches = []
    for rid, body in rows:
        if frag in body:
            idx = body.find(frag)
            start = body.rfind('.', 0, idx)
            start = start + 1 if start >= 0 else 0
            end = body.find('.', idx + len(frag))
            end = end + 1 if end >= 0 else len(body)
            sentence = body[start:end].strip()
            matches.append((rid, sentence[:140]))
    print(f"\n=== [{len(matches)}x] '{frag}' ===")
    seen = Counter(s for _, s in matches)
    for s, cnt in seen.most_common(4):
        print(f"  {cnt}x: {s}")
