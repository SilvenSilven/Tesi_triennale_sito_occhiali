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
    "con lenti marroni sfumate crea un insieme davvero",
    "mi ha chiarito subito che non era il paio giusto",
    "verde salvia non ama tutti gli",
    "sembrano studiati e non casuali",
    "nel modo giusto, grazie anche a",
    "Col passare dei giorni, temevo che",
    "hanno un punto di vista chiarissimo",
    "Su di me funzionano bene nelle",
    "Li ho messi la prima volta per",
    "insieme hanno personalità. Va anche detto che,",
    "su visi molto allungati vanno testati",
    "non vive da sola: il telaio",
    "e il lato intellettuale del modello",
    "però la realtà per me è che",
    "Li ho usati per un fine",
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
    for s, cnt in seen.most_common(4):
        print(f"  {cnt}x: {s}")
