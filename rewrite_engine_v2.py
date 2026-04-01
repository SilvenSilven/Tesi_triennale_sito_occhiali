#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Motore di riscrittura v2 – Recensioni occhiali
Carica tutti i dizionari di pattern, applica sostituzioni uniche,
genera confronto.txt e batch SQL.
"""

import json
import random
import re
import os
import copy

# ── Import dizionari ──
from patterns_part1_incipit import INCIPIT_PATTERNS
from patterns_part2_incipit import INCIPIT_PATTERNS_2
from patterns_part3_internal import INTERNAL_PATTERNS
from patterns_part4_connectors import CONNECTOR_PATTERNS
from patterns_part5_evaluations import EVALUATION_PATTERNS
from patterns_part6_style import STYLE_PATTERNS
from patterns_part7_midfreq import MIDFREQ_PATTERNS
from patterns_part8_medfreq import MEDFREQ_PATTERNS
from patterns_part9_residual import RESIDUAL_HIGH
from patterns_part10_residual import RESIDUAL_MID
from patterns_part11_residual import RESIDUAL_LOW
from patterns_part12_residual import RESIDUAL_FINAL
from patterns_part13_extra import RESIDUAL_EXTRA1
from patterns_part14_extra import RESIDUAL_EXTRA2
from patterns_part15_final import FINAL_HIGH
from patterns_part16_final import FINAL_LOW
from patterns_part17_cleanup import CLEANUP_PATTERNS

# ── Unifica tutti i dizionari ──
ALL_PATTERNS = {}
for d in [INCIPIT_PATTERNS, INCIPIT_PATTERNS_2, INTERNAL_PATTERNS,
          CONNECTOR_PATTERNS, EVALUATION_PATTERNS, STYLE_PATTERNS,
          MIDFREQ_PATTERNS, MEDFREQ_PATTERNS,
          RESIDUAL_HIGH, RESIDUAL_MID, RESIDUAL_LOW, RESIDUAL_FINAL,
          RESIDUAL_EXTRA1, RESIDUAL_EXTRA2, FINAL_HIGH, FINAL_LOW,
          CLEANUP_PATTERNS]:
    ALL_PATTERNS.update(d)

print(f"Pattern caricati: {len(ALL_PATTERNS)}")

# ── Carica recensioni ──
with open("all_reviews.json", "r", encoding="utf-8") as f:
    reviews = json.load(f)

print(f"Recensioni caricate: {len(reviews)}")

# ── Ordina pattern dal più lungo al più corto (longest first) ──
sorted_patterns = sorted(ALL_PATTERNS.keys(), key=len, reverse=True)

# ── Tracciamento alternative usate per ogni pattern ──
used_alternatives = {p: [] for p in ALL_PATTERNS}

def get_unique_alternative(pattern):
    """Restituisce un'alternativa mai usata per questo pattern."""
    alternatives = ALL_PATTERNS[pattern]
    available = [a for a in alternatives if a not in used_alternatives[pattern]]
    if not available:
        # Reset se tutte le alternative sono state usate
        used_alternatives[pattern] = []
        available = list(alternatives)
    choice = random.choice(available)
    used_alternatives[pattern].append(choice)
    return choice

# ── Applica sostituzioni ──
random.seed(42)  # Riproducibilità
changes = []
changed_count = 0
unchanged_count = 0

for review in reviews:
    original_body = review["body"]
    new_body = original_body

    review_changed = False
    for pattern in sorted_patterns:
        if pattern in new_body:
            replacement = get_unique_alternative(pattern)
            new_body = new_body.replace(pattern, replacement, 1)
            review_changed = True
            # Se il pattern appare più volte, sostituisci le altre occorrenze
            while pattern in new_body:
                replacement2 = get_unique_alternative(pattern)
                new_body = new_body.replace(pattern, replacement2, 1)

    if review_changed:
        changes.append({
            "id": review["id"],
            "product_name": review.get("product_name", ""),
            "stars": review.get("stars", 0),
            "old_body": original_body,
            "new_body": new_body
        })
        review["new_body"] = new_body
        changed_count += 1
    else:
        review["new_body"] = original_body
        unchanged_count += 1

print(f"\nRecensioni modificate: {changed_count}")
print(f"Recensioni invariate: {unchanged_count}")

# ── Verifica residui ──
print("\n=== VERIFICA PATTERN RESIDUI ===")
residual_counts = {}
for review in reviews:
    body = review.get("new_body", review["body"])
    for pattern in sorted_patterns:
        count = body.count(pattern)
        if count > 0:
            residual_counts[pattern] = residual_counts.get(pattern, 0) + count

if residual_counts:
    print(f"ATTENZIONE: {len(residual_counts)} pattern hanno ancora residui:")
    for p, c in sorted(residual_counts.items(), key=lambda x: -x[1])[:20]:
        print(f"  {c:4d}x | {p[:60]}")
else:
    print("PERFETTO: Nessun pattern residuo trovato!")

# ── Genera confronto.txt ──
print("\nGenerazione confronto_recensioni_v2.txt...")
with open("confronto_recensioni_v2.txt", "w", encoding="utf-8") as f:
    f.write("=" * 100 + "\n")
    f.write("CONFRONTO RECENSIONI - PRIMA E DOPO RISCRITTURA\n")
    f.write(f"Totale recensioni modificate: {changed_count}\n")
    f.write(f"Totale pattern coperti: {len(ALL_PATTERNS)}\n")
    f.write("=" * 100 + "\n\n")

    for i, ch in enumerate(changes, 1):
        f.write(f"--- Recensione #{i} (ID: {ch['id']}) | {ch['product_name']} | {ch['stars']}★ ---\n")
        f.write(f"\n📌 PRIMA:\n{ch['old_body']}\n")
        f.write(f"\n✅ DOPO:\n{ch['new_body']}\n")
        f.write("\n" + "-" * 80 + "\n\n")

print(f"  Scritte {len(changes)} modifiche in confronto_recensioni_v2.txt")

# ── Genera batch SQL ──
def sql_escape(text):
    """Escape per SQL PostgreSQL."""
    return text.replace("'", "''")

BATCH_SIZE = 50
batch_num = 0
sql_count = 0

# Elimina vecchi batch v2
for f_name in os.listdir("."):
    if f_name.startswith("update_v2_batch_") and f_name.endswith(".sql"):
        os.remove(f_name)

current_batch = []
for ch in changes:
    escaped_body = sql_escape(ch["new_body"])
    stmt = f"UPDATE reviews SET body = '{escaped_body}' WHERE id = {ch['id']};"
    current_batch.append(stmt)
    sql_count += 1

    if len(current_batch) >= BATCH_SIZE:
        batch_num += 1
        fname = f"update_v2_batch_{batch_num:02d}.sql"
        with open(fname, "w", encoding="utf-8") as f:
            f.write("BEGIN;\n")
            f.write("\n".join(current_batch))
            f.write("\nCOMMIT;\n")
        current_batch = []

# Ultimo batch
if current_batch:
    batch_num += 1
    fname = f"update_v2_batch_{batch_num:02d}.sql"
    with open(fname, "w", encoding="utf-8") as f:
        f.write("BEGIN;\n")
        f.write("\n".join(current_batch))
        f.write("\nCOMMIT;\n")

print(f"\nGenerati {batch_num} file SQL (update_v2_batch_01..{batch_num:02d}.sql)")
print(f"Totale UPDATE: {sql_count}")

# ── Salva anche JSON con tutti i cambiamenti ──
with open("changes_v2.json", "w", encoding="utf-8") as f:
    json.dump(changes, f, ensure_ascii=False, indent=2)

print(f"\nSalvati {len(changes)} cambiamenti in changes_v2.json")
print("\n✅ COMPLETATO. Controlla confronto_recensioni_v2.txt prima di applicare i batch SQL.")
