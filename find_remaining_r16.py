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
    "sul mio viso quadrato la forma tonda non",
    "lo specchio richiede un po' di",
    "con specchio ghiaccio crea un insieme davvero",
    "su visi molto squadrati vanno provati",
    "non li trovo ideali per guidare",
    "il grigio scuro delle lenti e",
    "su visi rotondi vanno provati con",
    "parlano chiaramente il linguaggio dello sport",
    "fit a ponte alto non",
    "nel quotidiano classico per me",
    "è che impianto shield molto deciso",
    "Ha una forza visiva quasi da",
    "Sa essere protagonista in modo molto",
    "ma non è il paio che",
    "è il più universale nei mesi",
    "Non lo rifiuto, ma non è",
    "e la parte migliore è che",
    "non sono facili con tutti i",
    "in un modo che apprezzo molto",
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
