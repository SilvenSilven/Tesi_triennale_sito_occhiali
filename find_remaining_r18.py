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

targets = [
    "il rimless sul mio viso tende a muoversi",
    "su un viso piccolo diventano il centro di tutto",
    "Funziona meglio quando il resto del look resta",
    "con il caldo li devo sistemare spesso",
    "il verde bottiglia è molto caratterizzante",
    "il posizionamento premium mi rende più esigente",
    "il blu è più vivido dal vivo",
    "non perdona un viso troppo piccolo",
    "fosse troppo evidente. Invece sembrano più",
    "non vive da sola: la struttura",
    "se il naso non è compatibile",
    "la lente specchiata non è per",
    "Li ho usati durante un weekend",
    "La prima occasione è stata un",
    "e le punte con finitura legnosa",
    "e la costruzione a doppio ponte",
    "struttura aviator in metallo lucido e",
    "è che telaio leggero e pulito",
    "delle lenti crea un insieme davvero",
    "è che linea femminile ma misurata",
    "la lente in gradazione calda e",
    "chi cerca un cat-eye molto aggressivo potrebbe",
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
