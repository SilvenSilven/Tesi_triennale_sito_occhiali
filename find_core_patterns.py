#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Identifica le FRASI TEMPLATE CORE (non n-gram sovrapposti).
Cerca frasi che iniziano e finiscono in modo naturale (inizio frase / fine frase o punteggiatura).
"""
import json, re, sys
from collections import Counter

sys.stdout.reconfigure(encoding='utf-8')

with open("all_reviews.json", "r", encoding="utf-8") as f:
    reviews = json.load(f)

# Estrai tutte le frasi (divise per punto, punto esclamativo, ecc.)
clause_counter = Counter()

for rev in reviews:
    body = rev["body"]
    # Dividi per punti, ma mantieni i segmenti
    # Prima splitta per ". " (frase intera)
    sentences = re.split(r'(?<=[.!?])\s+', body)
    for sent in sentences:
        sent = sent.strip()
        if len(sent) > 20:  # solo frasi significative
            clause_counter[sent] += 1

# Frasi complete ripetute >= 5 volte
repeated_sentences = {k: v for k, v in clause_counter.items() if v >= 5}
print(f"Frasi COMPLETE ripetute >= 5 volte: {len(repeated_sentences)}")

# Ora cerca anche sotto-frasi (clausole separate da virgola)
subclause_counter = Counter()
for rev in reviews:
    body = rev["body"]
    # Dividi anche per virgola + congiunzione, o per ; 
    clauses = re.split(r'(?<=[,;])\s+', body)
    for cl in clauses:
        cl = cl.strip()
        if 15 < len(cl) < 100:
            subclause_counter[cl] += 1

repeated_subclauses = {k: v for k, v in subclause_counter.items() if v >= 10}
print(f"Sotto-clausole ripetute >= 10 volte: {len(repeated_subclauses)}")

# Combina: frasi complete (>=5) e sotto-clausole (>=10)
# Ordina per frequenza
all_repeated = {}
all_repeated.update(repeated_sentences)
all_repeated.update(repeated_subclauses)

# Dedup: rimuovi frasi che sono sotto-stringhe di frasi più lunghe con stessa o maggiore frequenza
sorted_phrases = sorted(all_repeated.items(), key=lambda x: (-len(x[0]), -x[1]))
core_phrases = {}
for phrase, count in sorted_phrases:
    is_sub = False
    for existing in core_phrases:
        if phrase in existing and core_phrases[existing] >= count * 0.8:
            is_sub = True
            break
    if not is_sub:
        core_phrases[phrase] = count

# Ordina per frequenza
result = sorted(core_phrases.items(), key=lambda x: -x[1])

print(f"\nCORE PHRASES dopo dedup: {len(result)}")
print(f"\n{'='*90}")
print(f"{'FREQ':>5}  TIPO     FRASE")
print(f"{'='*90}")

for phrase, count in result[:150]:
    tipo = "INCIPIT" if any(rev["body"].startswith(phrase) for rev in reviews[:500]) else "INTERNA"
    print(f"{count:>5}  {tipo:8s} {phrase[:80]}")

# Salva risultato completo
with open("core_patterns.txt", "w", encoding="utf-8") as f:
    f.write(f"CORE PHRASES: {len(result)}\n\n")
    for phrase, count in result:
        f.write(f"{count:>5}x | {phrase}\n")

# Salva come JSON per uso programmatico
output = [{"phrase": p, "count": c} for p, c in result]
with open("core_patterns.json", "w", encoding="utf-8") as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print(f"\nSalvati: core_patterns.txt, core_patterns.json")
