import json
from collections import Counter

with open('reviews_with_patterns.json', 'r', encoding='utf-8') as f:
    reviews = json.load(f)

# 1. Trova incipit ripetuti (prime 8 parole)
incipit_counter = Counter()
for r in reviews:
    words = r['body'].split()
    incipit = ' '.join(words[:8])
    incipit_counter[incipit] += 1

print("=== INCIPIT RIPETUTI (>= 3) ===")
for inc, cnt in sorted(incipit_counter.items(), key=lambda x: -x[1]):
    if cnt >= 3:
        print(f"  [{cnt}x] {inc}")

# 2. Trova frasi interne ripetute (n-gram di 6-10 parole)
from collections import defaultdict

phrase_counter = Counter()
for r in reviews:
    words = r['body'].split()
    for n in [7, 8, 9, 10]:
        for i in range(len(words) - n):
            phrase = ' '.join(words[i:i+n])
            phrase_counter[phrase] += 1

print("\n=== FRASI INTERNE RIPETUTE (>= 5, 7-10 parole) ===")
seen_phrases = set()
for phrase, cnt in sorted(phrase_counter.items(), key=lambda x: -x[1]):
    if cnt >= 5:
        # Skip if this phrase is a substring of an already-printed phrase
        skip = False
        for sp in seen_phrases:
            if phrase in sp:
                skip = True
                break
        if not skip:
            seen_phrases.add(phrase)
            print(f"  [{cnt}x] {phrase}")

# 3. Trova frasi di chiusura ripetute (ultime 8 parole)
closing_counter = Counter()
for r in reviews:
    words = r['body'].split()
    closing = ' '.join(words[-8:])
    closing_counter[closing] += 1

print("\n=== CHIUSURE RIPETUTE (>= 3) ===")
for cl, cnt in sorted(closing_counter.items(), key=lambda x: -x[1]):
    if cnt >= 3:
        print(f"  [{cnt}x] {cl}")
