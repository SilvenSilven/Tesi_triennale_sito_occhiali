#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Verifica pattern residui nelle recensioni riscritte."""
import json
from collections import Counter

with open("changes_v2.json", "r", encoding="utf-8") as f:
    changes = json.load(f)

with open("all_reviews.json", "r", encoding="utf-8") as f:
    all_reviews = json.load(f)

# Costruisci il corpo finale per ogni recensione
final_bodies = {}
for ch in changes:
    final_bodies[ch["id"]] = ch["new_body"]
for r in all_reviews:
    if r["id"] not in final_bodies:
        final_bodies[r["id"]] = r["body"]

# Cerca n-gram ripetuti (frasi di 8-15 parole)
from collections import defaultdict
ngram_locations = defaultdict(list)

for rid, body in final_bodies.items():
    words = body.split()
    for n in range(8, 16):
        for i in range(len(words) - n + 1):
            ngram = " ".join(words[i:i+n])
            ngram_locations[ngram].append(rid)

# Filtra solo quelli che appaiono >=5 volte
repeated = {k: len(v) for k, v in ngram_locations.items() if len(v) >= 5}

# Rimuovi sotto-frasi
sorted_by_len = sorted(repeated.keys(), key=len, reverse=True)
core = {}
for phrase in sorted_by_len:
    is_sub = False
    for existing in core:
        if phrase in existing:
            is_sub = True
            break
    if not is_sub:
        core[phrase] = repeated[phrase]

# Ordina per frequenza
sorted_core = sorted(core.items(), key=lambda x: -x[1])

print(f"Pattern residui (>=5x): {len(sorted_core)}")
print()

total_occurrences = 0
for phrase, count in sorted_core[:50]:
    print(f"  {count:4d}x | {phrase[:80]}")
    total_occurrences += count

print(f"\n... e altri {max(0, len(sorted_core)-50)} pattern")
print(f"Totale occorrenze nei top 50: {total_occurrences}")

# Conta quante recensioni hanno almeno un pattern residuo >=5x
affected = set()
for phrase, count in sorted_core:
    for rid in ngram_locations[phrase]:
        affected.add(rid)
print(f"\nRecensioni con almeno un pattern residuo (>=5x): {len(affected)}")
