#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Estrae frasi complete ripetute dalle nuove recensioni per identificare pattern residui.
Usa n-gram più lunghi e cerca le frasi intere.
"""
import json
import sys
from collections import Counter

sys.stdout.reconfigure(encoding='utf-8')

with open("new_reviews.json", "r", encoding="utf-8") as f:
    reviews = json.load(f)

# Raccogli tutte le frasi (split per '. ' o simile) e conta
sentence_counter = Counter()
for rev in reviews:
    body = rev["new_body"]
    # Split per frasi: '. ', '! ', '? ', e anche ', '
    import re
    # Estrai frasi complete (tra punti)
    sentences = re.split(r'(?<=[.!?])\s+', body)
    for s in sentences:
        s = s.strip()
        if len(s) > 30:  # Solo frasi abbastanza lunghe
            sentence_counter[s] += 1

print("FRASI COMPLETE RIPETUTE (≥ 5 volte):")
print("=" * 70)
repeated = [(s, c) for s, c in sentence_counter.items() if c >= 5]
repeated.sort(key=lambda x: -x[1])
for s, c in repeated:
    print(f"[{c:3d}x] {s}")

print(f"\nTotale frasi ripetute ≥5: {len(repeated)}")

# Anche sotto-frasi (tra virgole) lunghe
print("\n\nSEGMENTI TRA VIRGOLE RIPETUTI (≥ 8 volte):")
print("=" * 70)
segment_counter = Counter()
for rev in reviews:
    body = rev["new_body"]
    segments = re.split(r'[.!?,;:]\s*', body)
    for s in segments:
        s = s.strip()
        if len(s) > 25:
            segment_counter[s] += 1

repeated2 = [(s, c) for s, c in segment_counter.items() if c >= 8]
repeated2.sort(key=lambda x: -x[1])
for s, c in repeated2[:80]:
    print(f"[{c:3d}x] {s}")
