#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Verifica pattern ripetitivi nelle recensioni del DB aggiornato.
Usa n-gram per trovare frasi ripetute (minimo 6 parole, minimo 5 occorrenze).
"""

import psycopg2
from collections import Counter

DATABASE_URL = (
    "postgresql://neondb_owner:npg_uFxVSRoTj95w"
    "@ep-damp-sea-anvn4fw4.c-6.us-east-1.aws.neon.tech"
    "/neondb?sslmode=require"
)

print("Connessione al DB...")
conn = psycopg2.connect(DATABASE_URL)
cur = conn.cursor()

print("Download recensioni...")
cur.execute("SELECT id, body FROM reviews WHERE is_published = true ORDER BY id")
rows = cur.fetchall()
cur.close()
conn.close()

print(f"Recensioni caricate: {len(rows)}\n")

bodies = [r[1] for r in rows]

# N-gram basato su parole (6-10 parole consecutive)
def get_ngrams(text, n):
    words = text.split()
    return [" ".join(words[i:i+n]) for i in range(len(words)-n+1)]

# Conta n-gram su tutti i testi
print("Analisi n-gram (6-10 parole)...")
all_ngrams = Counter()

for body in bodies:
    # Usa set per non contare lo stesso ngram due volte nella stessa recensione
    seen = set()
    for n in range(6, 11):
        for ng in get_ngrams(body, n):
            if ng not in seen:
                seen.add(ng)
                all_ngrams[ng] += 1

# Filtra n-gram che appaiono in >=5 recensioni
repeated = {ng: c for ng, c in all_ngrams.items() if c >= 5}

# Rimuovi n-gram che sono sotto-sequenze di n-gram più lunghi con stessa frequenza
print(f"N-gram ripetuti (>=5x): {len(repeated)}")

# Top 50
top50 = sorted(repeated.items(), key=lambda x: -x[1])[:50]

print("\n=== TOP 50 FRASI RIPETUTE ===")
for i, (ng, c) in enumerate(top50, 1):
    print(f"  {c:4d}x | {ng[:80]}")

# Conta recensioni con almeno 1 pattern (>=5x)
if repeated:
    pattern_set = set(repeated.keys())
    affected = sum(1 for b in bodies if any(p in b for p in pattern_set))
    print(f"\nRecensioni con almeno 1 frase ripetuta (>=5x): {affected}/{len(bodies)}")
else:
    print("\n✅ Nessun pattern con frequenza >=5 trovato!")

# Statistiche generali
freq_10 = sum(1 for c in repeated.values() if c >= 10)
freq_20 = sum(1 for c in repeated.values() if c >= 20)
print(f"\nPattern >=10x: {freq_10}")
print(f"Pattern >=20x: {freq_20}")
