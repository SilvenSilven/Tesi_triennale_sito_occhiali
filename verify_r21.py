# -*- coding: utf-8 -*-
import psycopg2, sys
from collections import defaultdict
sys.stdout.reconfigure(encoding='utf-8')

DB = "postgresql://neondb_owner:npg_uFxVSRoTj95w@ep-damp-sea-anvn4fw4.c-6.us-east-1.aws.neon.tech/neondb?sslmode=require"
conn = psycopg2.connect(DB)
cur = conn.cursor()
cur.execute("SELECT body FROM reviews")
rows = cur.fetchall()
cur.close()
conn.close()

ngrams = defaultdict(int)
for (body,) in rows:
    words = body.lower().split()
    for n in range(8, 16):
        for i in range(len(words) - n + 1):
            ng = " ".join(words[i:i+n])
            ngrams[ng] += 1

repeated = [(c, ng) for ng, c in ngrams.items() if c >= 5]
repeated.sort(reverse=True)
print(f"Pattern >=5x: {len(repeated)}")
for c, ng in repeated[:50]:
    print(f"  {c}x | {ng[:90]}")
