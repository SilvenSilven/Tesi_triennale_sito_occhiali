#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fix round 13b — pattern n-gram 10x con caratteri accentati corretti."""
import psycopg2

DATABASE_URL = (
    "postgresql://neondb_owner:npg_uFxVSRoTj95w"
    "@ep-damp-sea-anvn4fw4.c-6.us-east-1.aws.neon.tech"
    "/neondb?sslmode=require"
)

PATTERNS = {

    # 10x — fine frase (tono dissuasivo)
    "non è il paio che prendi quando vuoi sparire": [
        "non sono gli occhiali da scegliere per passare inosservato",
        "non è il modello per chi vuole restare nell'ombra",
        "non è il paio da mettere quando si vuole essere invisibili",
        "non sono il tipo di accessori da portare in incognito",
        "non è il modello giusto per chi cerca discrezione totale",
        "non è adatto a chi vuole evitare l'attenzione",
        "non è il paio per chi preferisce non essere notato",
        "non sono gli occhiali di chi non vuole farsi vedere",
        "non è il modello per chi vuole scomparire nella folla",
        "non si adatta a chi vuole passare inosservato",
        "non è il tipo di accessorio per chi cerca il basso profilo",
        "non sono adatti a chi vuole non attirare sguardi",
    ],

    # 10x — interno (acetato)
    "dal vivo avrei voluto un acetato ancora più strutturato": [
        "in persona avrei preferito un acetato con più corpo",
        "dal vero avrei gradito un acetato più consistente",
        "di persona mi sarebbe piaciuto un acetato più robusto",
        "vedendolo dal vivo avrei preferito più spessore nell'acetato",
        "in realtà avrei voluto una struttura in acetato più decisa",
        "de visu mi sarebbe piaciuto un acetato con più massa",
        "guardandolo di persona avrei apprezzato un acetato più spesso",
        "in mano avrei preferito un acetato ancora più presente",
        "dal vivo mi aspettavo un acetato di maggiore consistenza",
        "vedendolo in mano avrei voluto un acetato più pieno",
        "in persona avrei voluto sentire più peso nell'acetato",
        "dal vivo mi ero aspettato un acetato più solido",
    ],

    # 10x — fine frase (cat-eye)
    "chi vuole un cat-eye più aggressivo potrebbe trovarle troppo educate": [
        "per chi cerca un cat-eye più deciso potrebbero sembrare troppo contenute",
        "chi preferisce un cat-eye più estremo potrebbe trovarlo troppo morbido",
        "per i gusti più audaci il cat-eye potrebbe risultare troppo sobrio",
        "chi vuole un cat-eye più pronunciato potrebbe trovarlo troppo discreto",
        "per chi cerca più radicalità nel cat-eye il modello potrebbe sembrare tenue",
        "chi cerca un cat-eye più spinto potrebbe percepirlo come timido",
        "chi preferisce un cat-eye di carattere più forte potrebbe trovarlo soft",
        "per un cat-eye più incisivo il modello potrebbe risultare troppo disciplinato",
        "chi vuole una curvatura più netta potrebbe trovarlo troppo tranquillo",
        "per chi ama il cat-eye deciso questo potrebbe sembrare troppo classico",
        "chi cerca più angolazione nel cat-eye potrebbe trovarlo un po' addomesticato",
        "per i palati più estremi il cat-eye potrebbe essere troppo misurato",
    ],

    # 10x — fine frase (versatilità)
    "non sono il paio più versatile della rotazione": [
        "non sono il modello più adattabile nella selezione",
        "non sono il paio più flessibile dell'insieme",
        "non risultano i più versatili tra quelli che porto",
        "non sono il modello con più combinazioni nella rotazione",
        "non sono il paio da tutto e per tutto",
        "non sono il modello con la massima flessibilità d'uso",
        "non sono il paio più polifunzionale nella mia selezione",
        "non sono tra i modelli più versatili che possiedo",
        "non sono il paio con il più alto tasso di abbinabilità",
        "non sono la scelta più neutra della collezione",
        "non sono il modello più adattabile a ogni contesto",
        "non sono il paio con la massima versabilità di abbinamento",
    ],

    # 10x — interno (colore blu)
    "il blu dal vivo è più acceso di quanto lasci intuire la": [
        "il blu visto di persona risulta più intenso di quanto suggerisca la",
        "il colore blu in realtà è più luminoso di quanto sembri dalla",
        "il blu dal vivo si rivela più saturo rispetto a quanto indicasse la",
        "il tono blu è più vivace di quanto facesse pensare la",
        "il blu reale supera il tono suggerito dalla",
        "il blu de visu è più deciso di quanto mostri la",
        "guardando dal vivo il blu è più brillante rispetto alla",
        "in mano il blu si rivela più intenso di quanto indicasse la",
        "vedendolo di persona il blu appare più vivace rispetto alla",
        "il colore dal vivo è più saturo di quello percepibile dalla",
        "di persona il blu si mostra più acceso rispetto alla",
    ],

}

print("Connessione al DB...")
conn = psycopg2.connect(DATABASE_URL)
cur = conn.cursor()
cur.execute("SELECT id, body FROM reviews ORDER BY id")
rows = cur.fetchall()
print(f"Caricate: {len(rows)}")

pattern_occurrence = {p: 0 for p in PATTERNS}
changes = []

for row_id, body in rows:
    new_body = body
    changed = False
    for pattern, alternatives in PATTERNS.items():
        if pattern not in new_body:
            continue
        count = new_body.count(pattern)
        for _ in range(count):
            if pattern not in new_body:
                break
            idx = pattern_occurrence[pattern] % len(alternatives)
            new_body = new_body.replace(pattern, alternatives[idx], 1)
            pattern_occurrence[pattern] += 1
            changed = True
    if changed and new_body != body:
        changes.append((new_body, row_id))

print(f"Recensioni da aggiornare: {len(changes)}")

BATCH_SIZE = 50
applied = 0; errors = 0; bn = 0
for i in range(0, len(changes), BATCH_SIZE):
    batch = changes[i:i+BATCH_SIZE]
    bn += 1
    try:
        for nb, rid in batch:
            cur.execute("UPDATE reviews SET body = %s WHERE id = %s", (nb, rid))
        conn.commit()
        applied += len(batch)
        print(f"  Batch {bn}: {applied}/{len(changes)}")
    except Exception as e:
        conn.rollback(); errors += len(batch)
        print(f"  ERRORE batch {bn}: {e}")

cur.close(); conn.close()
print(f"Aggiornate: {applied} | Errori: {errors}")
print("Round 13b OK" if errors == 0 else f"ERRORI: {errors}")
