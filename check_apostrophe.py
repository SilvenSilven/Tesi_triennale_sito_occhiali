# -*- coding: utf-8 -*-
import psycopg2, sys
sys.stdout.reconfigure(encoding='utf-8')
DB = "postgresql://neondb_owner:npg_uFxVSRoTj95w@ep-damp-sea-anvn4fw4.c-6.us-east-1.aws.neon.tech/neondb?sslmode=require"
conn = psycopg2.connect(DB)
cur = conn.cursor()

# Check which apostrophe char is in the DB for these patterns
cur.execute("SELECT id, body FROM reviews WHERE body LIKE '%salita dell%angolo va misurata%' LIMIT 3")
rows = cur.fetchall()
print(f"Rows con 'salita dell...angolo': {len(rows)}")
for rid, body in rows:
    idx = body.find("salita dell")
    if idx >= 0:
        snippet = body[max(0, idx-20):idx+70]
        print(f"  ID {rid}: ...{snippet}...")
        for i, ch in enumerate(snippet):
            if ord(ch) > 127:
                print(f"    pos {i}: U+{ord(ch):04X} = {ch!r}")

# Check curly apostrophe
pat_curly = "su un viso molto tondo la salita dell\u2019angolo va misurata bene."
cur.execute("SELECT count(*) FROM reviews WHERE body LIKE %s", [f"%{pat_curly}%"])
print(f"\nCurly apostrophe \\u2019 match: {cur.fetchone()[0]}")

# Check straight apostrophe
pat_straight = "su un viso molto tondo la salita dell'angolo va misurata bene."
cur.execute("SELECT count(*) FROM reviews WHERE body LIKE %s", [f"%{pat_straight}%"])
print(f"Straight apostrophe match: {cur.fetchone()[0]}")

# Also check verde salvia
pat2_curly = "il verde salvia non va d\u2019accordo con ogni guardaroba."
cur.execute("SELECT count(*) FROM reviews WHERE body LIKE %s", [f"%{pat2_curly}%"])
print(f"\nVerde salvia curly: {cur.fetchone()[0]}")

pat2_straight = "il verde salvia non va d'accordo con ogni guardaroba."
cur.execute("SELECT count(*) FROM reviews WHERE body LIKE %s", [f"%{pat2_straight}%"])
print(f"Verde salvia straight: {cur.fetchone()[0]}")

# Check sul mio viso rotondo
pat3_curly = "sul mio viso rotondo l\u2019angolo sale un po\u2019 troppo."
cur.execute("SELECT count(*) FROM reviews WHERE body LIKE %s", [f"%{pat3_curly}%"])
print(f"\nViso rotondo curly: {cur.fetchone()[0]}")

pat3_straight = "sul mio viso rotondo l'angolo sale un po' troppo."
cur.execute("SELECT count(*) FROM reviews WHERE body LIKE %s", [f"%{pat3_straight}%"])
print(f"Viso rotondo straight: {cur.fetchone()[0]}")

cur.close()
conn.close()
