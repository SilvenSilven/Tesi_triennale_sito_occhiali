#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Verifica pattern residui nelle recensioni riscritte.
Controlla se le nuove recensioni contengono ancora frasi ripetute (n-gram).
"""
import json
import sys
from collections import Counter

sys.stdout.reconfigure(encoding='utf-8')

with open("new_reviews.json", "r", encoding="utf-8") as f:
    reviews = json.load(f)

print(f"Analisi di {len(reviews)} recensioni riscritte\n")

# Raccogli n-gram da 6 a 12 parole
def get_ngrams(text, n):
    words = text.split()
    return [" ".join(words[i:i+n]) for i in range(len(words) - n + 1)]

for n in [8, 10, 12]:
    counter = Counter()
    for rev in reviews:
        ngrams = get_ngrams(rev["new_body"], n)
        for ng in set(ngrams):  # set per non contare duplicati nella stessa recensione
            counter[ng] += 1

    repeated = [(ng, c) for ng, c in counter.items() if c >= 5]
    repeated.sort(key=lambda x: -x[1])

    print(f"\n{'='*60}")
    print(f"N-GRAM DI {n} PAROLE - Frasi ripetute ≥ 5 volte:")
    print(f"{'='*60}")
    if not repeated:
        print("  ✓ Nessun n-gram ripetuto ≥ 5 volte!")
    else:
        for ng, c in repeated[:30]:
            print(f"  [{c:3d}x] {ng}")
        if len(repeated) > 30:
            print(f"  ... e altre {len(repeated)-30} frasi ripetute")

print("\n" + "="*60)
print("ANALISI COMPLETATA")
