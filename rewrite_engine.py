#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Motore principale di riscrittura delle recensioni.
1. Carica i 815 body dal JSON
2. Per ogni body, individua i pattern presenti
3. Sostituisce ogni pattern con un'alternativa unica (mai riutilizzata)
4. Salva confronto vecchio vs nuovo e SQL di aggiornamento
"""

import json
import random
import copy
import sys

# Assicura output UTF-8
sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

# Import dei dizionari di pattern (part6 importa ricorsivamente part5→4→3→2→1)
from rewrite_reviews_part9 import PATTERNS

random.seed(42)

# ──────────────────────────────────────────────────────────────
# 1. Caricamento dati
# ──────────────────────────────────────────────────────────────
with open("reviews_with_patterns.json", "r", encoding="utf-8") as f:
    reviews = json.load(f)

print(f"Caricate {len(reviews)} recensioni")

# ──────────────────────────────────────────────────────────────
# 2. Preparazione pool alternativi
#    Per ogni chiave, mescoliamo e teniamo un indice di consumo
# ──────────────────────────────────────────────────────────────

# De-duplica le chiavi: alcune puntano allo stesso array (apostrofo dritto / tipografico)
unique_patterns = {}     # chiave canonica → lista alternative (shuffled copy)
key_to_canon = {}       # ogni chiave → chiave canonica
seen_ids = set()

for key, alts in PATTERNS.items():
    alt_id = id(alts)
    if alt_id in seen_ids:
        # È un alias (stessa lista), trova la canonica
        for canon, calt in unique_patterns.items():
            if id(PATTERNS[canon]) == alt_id or calt is alts:
                key_to_canon[key] = canon
                break
    else:
        seen_ids.add(alt_id)
        shuffled = list(alts)
        random.shuffle(shuffled)
        unique_patterns[key] = shuffled
        key_to_canon[key] = key

# Indice consumo: quanti alternative sono già state usate per ogni pattern canonico
consume_idx = {k: 0 for k in unique_patterns}

def get_replacement(pattern_key):
    """Restituisce la prossima alternativa unica per il pattern dato."""
    canon = key_to_canon[pattern_key]
    pool = unique_patterns[canon]
    idx = consume_idx[canon]
    if idx >= len(pool):
        # Pool esaurito: ricicla mescolando di nuovo (non dovrebbe accadere)
        random.shuffle(pool)
        consume_idx[canon] = 0
        idx = 0
        print(f"  ⚠ Pool esaurito e riciclato per: {canon[:50]}", file=sys.stderr)
    consume_idx[canon] = idx + 1
    return pool[idx]

# ──────────────────────────────────────────────────────────────
# 3. Ordinamento delle chiavi pattern dal più lungo al più corto
#    (per evitare sostituzioni parziali su sotto-stringhe)
# ──────────────────────────────────────────────────────────────
sorted_keys = sorted(PATTERNS.keys(), key=len, reverse=True)

# ──────────────────────────────────────────────────────────────
# 4. Riscrittura di ogni recensione
# ──────────────────────────────────────────────────────────────
results = []  # lista di {id, stars, product_name, old_body, new_body, patterns_found}
unchanged = 0
changed = 0

for rev in reviews:
    body = rev["body"]
    new_body = body
    patterns_found = []

    for pat_key in sorted_keys:
        if pat_key in new_body:
            replacement = get_replacement(pat_key)
            new_body = new_body.replace(pat_key, replacement, 1)
            patterns_found.append(pat_key[:50])

    if new_body != body:
        changed += 1
    else:
        unchanged += 1

    results.append({
        "id": rev["id"],
        "stars": rev["stars"],
        "product_name": rev["product_name"],
        "old_body": body,
        "new_body": new_body,
        "patterns_found": patterns_found,
    })

print(f"Modificate: {changed}, Invariate: {unchanged}")

# ──────────────────────────────────────────────────────────────
# 5. Salvataggio confronto TXT
# ──────────────────────────────────────────────────────────────
with open("confronto_recensioni.txt", "w", encoding="utf-8") as f:
    for r in results:
        f.write(f"═══ ID {r['id']} | {r['stars']}★ | {r['product_name']} ═══\n")
        f.write(f"VECCHIA:\n{r['old_body']}\n\n")
        f.write(f"NUOVA:\n{r['new_body']}\n\n")
        if r['patterns_found']:
            f.write(f"Pattern sostituiti: {', '.join(r['patterns_found'])}\n")
        f.write("─" * 70 + "\n\n")

print("Salvato: confronto_recensioni.txt")

# ──────────────────────────────────────────────────────────────
# 6. Salvataggio JSON delle nuove recensioni
# ──────────────────────────────────────────────────────────────
output_json = [
    {"id": r["id"], "new_body": r["new_body"]}
    for r in results
    if r["new_body"] != r["old_body"]
]
with open("new_reviews.json", "w", encoding="utf-8") as f:
    json.dump(output_json, f, ensure_ascii=False, indent=2)

print(f"Salvato: new_reviews.json ({len(output_json)} recensioni)")

# ──────────────────────────────────────────────────────────────
# 7. Generazione SQL (batch da 50) con encoding UTF-8 corretto
# ──────────────────────────────────────────────────────────────
def sql_escape(text):
    """Escape per stringhe PostgreSQL: raddoppia gli apostrofi."""
    return text.replace("'", "''")

batch_size = 50
sql_batches = []
current_batch = []
for i, item in enumerate(output_json):
    escaped = sql_escape(item["new_body"])
    current_batch.append(
        f"UPDATE reviews SET body = '{escaped}' WHERE id = {item['id']};"
    )
    if len(current_batch) >= batch_size or i == len(output_json) - 1:
        sql_batches.append("\n".join(current_batch))
        current_batch = []

for idx, batch in enumerate(sql_batches):
    fname = f"update_batch_{idx+1:02d}.sql"
    with open(fname, "w", encoding="utf-8") as f:
        f.write(batch + "\n")
    print(f"Salvato: {fname} ({batch.count('UPDATE')} query)")

print(f"\nTotale batch SQL: {len(sql_batches)}")
print("Fatto ✓")
