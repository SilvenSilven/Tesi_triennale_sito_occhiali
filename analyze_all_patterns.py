#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Analizza TUTTE le 2388 recensioni per trovare ogni frase che appare >= 5 volte."""
import json, re, sys
from collections import Counter

sys.stdout.reconfigure(encoding='utf-8')

with open("all_reviews.json", "r", encoding="utf-8") as f:
    reviews = json.load(f)

print(f"Totale recensioni: {len(reviews)}")

# 1. Estrai tutti i segmenti di 6+ parole da ogni body
def extract_ngrams(text, min_words=6, max_words=15):
    words = text.split()
    ngrams = set()
    for n in range(min_words, min(max_words+1, len(words)+1)):
        for i in range(len(words) - n + 1):
            ngram = " ".join(words[i:i+n])
            ngrams.add(ngram)
    return ngrams

# 2. Conta frequenza di ogni n-gram su tutta la collezione
print("Analisi n-gram in corso (potrebbe richiedere qualche secondo)...")
ngram_counts = Counter()
for rev in reviews:
    body = rev["body"]
    ngrams = extract_ngrams(body, min_words=6, max_words=12)
    for ng in ngrams:
        ngram_counts[ng] += 1

# 3. Filtra: solo quelli che appaiono >= 5 volte
frequent = {k: v for k, v in ngram_counts.items() if v >= 5}
print(f"N-gram con freq >= 5: {len(frequent)}")

# 4. Rimuovi n-gram che sono sotto-stringhe di altri n-gram più lunghi con stessa frequenza
sorted_by_len = sorted(frequent.items(), key=lambda x: (-len(x[0]), -x[1]))
filtered = {}
for ngram, count in sorted_by_len:
    # Controlla se è già coperto da un n-gram più lungo
    is_substring = False
    for existing in filtered:
        if ngram in existing and filtered[existing] >= count:
            is_substring = True
            break
    if not is_substring:
        filtered[ngram] = count

# 5. Ordina per frequenza
result = sorted(filtered.items(), key=lambda x: -x[1])

print(f"\nPattern unici dopo dedup: {len(result)}")
print(f"\n{'='*80}")
print(f"{'FREQ':>5}  PATTERN")
print(f"{'='*80}")
for pattern, count in result[:100]:
    print(f"{count:>5}  {pattern}")

# 6. Salva in file
with open("all_patterns_analysis.txt", "w", encoding="utf-8") as f:
    f.write(f"Totale recensioni: {len(reviews)}\n")
    f.write(f"Pattern unici (freq >= 5): {len(result)}\n\n")
    for pattern, count in result:
        f.write(f"{count:>5}x  {pattern}\n")

print(f"\nSalvato: all_patterns_analysis.txt")

# 7. Conta quante recensioni hanno almeno un pattern freq >= 10
patterns_10 = {k for k, v in filtered.items() if v >= 10}
affected = sum(1 for rev in reviews if any(p in rev["body"] for p in patterns_10))
print(f"\nRecensioni con almeno un pattern >=10x: {affected}/{len(reviews)}")
