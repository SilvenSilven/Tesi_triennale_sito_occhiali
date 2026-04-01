#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Applica le recensioni riscritte direttamente al database Neon
usando psycopg2 con query parametrizzate (safe encoding, no SQL injection).
"""

import json
import psycopg2
import psycopg2.extras
import time

# ── Connessione diretta (unpooled per transazioni lunghe) ──
DATABASE_URL = (
    "postgresql://neondb_owner:npg_uFxVSRoTj95w"
    "@ep-damp-sea-anvn4fw4.c-6.us-east-1.aws.neon.tech"
    "/neondb?sslmode=require"
)

BATCH_SIZE = 50  # UPDATE per commit

# ── Carica le modifiche ──
print("Caricamento changes_v2.json...")
with open("changes_v2.json", "r", encoding="utf-8") as f:
    changes = json.load(f)

print(f"Trovate {len(changes)} recensioni da aggiornare.")

# ── Connessione ──
print("\nConnessione al database Neon...")
try:
    conn = psycopg2.connect(DATABASE_URL)
    conn.autocommit = False
    cur = conn.cursor()
    print("  Connessione stabilita.")
except Exception as e:
    print(f"  ERRORE connessione: {e}")
    raise

# ── Applica in batch ──
total = len(changes)
applied = 0
errors = 0
batch_count = 0

print(f"\nApplicazione in batch da {BATCH_SIZE} UPDATE...\n")

for i in range(0, total, BATCH_SIZE):
    batch = changes[i : i + BATCH_SIZE]
    batch_count += 1

    try:
        for ch in batch:
            cur.execute(
                "UPDATE reviews SET body = %s WHERE id = %s",
                (ch["new_body"], ch["id"])
            )

        conn.commit()
        applied += len(batch)
        end = min(i + BATCH_SIZE, total)
        print(f"  Batch {batch_count:3d}: righe {i+1:5d}-{end:5d} | aggiornate {applied:5d}/{total}")

    except Exception as e:
        conn.rollback()
        errors += len(batch)
        print(f"  ERRORE batch {batch_count}: {e}")
        # Ritenta una alla volta per isolare l'errore
        for ch in batch:
            try:
                cur.execute(
                    "UPDATE reviews SET body = %s WHERE id = %s",
                    (ch["new_body"], ch["id"])
                )
                conn.commit()
                applied += 1
            except Exception as e2:
                conn.rollback()
                errors += 1
                print(f"    ERRORE singolo ID {ch['id']}: {e2}")

    # Piccola pausa ogni 10 batch per non sovraccaricare
    if batch_count % 10 == 0:
        time.sleep(0.5)

# ── Chiusura ──
cur.close()
conn.close()

print(f"\n{'='*60}")
print(f"COMPLETATO")
print(f"  Aggiornate: {applied}")
print(f"  Errori:     {errors}")
print(f"  Totale:     {total}")
print(f"{'='*60}")

if errors == 0:
    print("\n✅ Tutte le recensioni sono state aggiornate correttamente!")
else:
    print(f"\n⚠️  {errors} recensioni non aggiornate - verifica i log sopra.")
