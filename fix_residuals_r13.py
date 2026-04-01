#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fix round 13 - pattern n-gram 10x residui post round 12."""
import psycopg2

DATABASE_URL = (
    "postgresql://neondb_owner:npg_uFxVSRoTj95w"
    "@ep-damp-sea-anvn4fw4.c-6.us-east-1.aws.neon.tech"
    "/neondb?sslmode=require"
)

PATTERNS = {

    # 10x - fine frase
    "visivamente resta vicino a molti altri classici del mercato": [
        "visivamente si avvicina a molti altri classici del settore",
        "formalmente rimane vicino a diversi modelli classici del mercato",
        "visivamente si accosta a molti classici esistenti",
        "come forma non si discosta molto da altri modelli storici",
        "visivamente si inserisce nel panorama di altri classici affermati",
        "nella silhouette ricorda molti altri modelli icona del mercato",
        "dal punto di vista formale si avvicina ad altri classici noti",
        "nell'aspetto rimane vicino a molti modelli classici del settore",
        "visivamente dialoga con molti altri classici del mercato",
        "esteticamente si affianca a molti classici del panorama",
        "nella forma si accosta a diversi modelli classici",
        "come disegno non si allontana troppo dai classici del mercato",
    ],

    # 10x - inizio frase
    "Impostazione iconica si sente subito e": [
        "La struttura iconografica emerge subito e",
        "Il carattere iconico si avverte immediatamente e",
        "L'impostazione classica appare evidente subito e",
        "Il carattere distintivo si nota subito e",
        "La cifra iconica si percepisce subito e",
        "L'impronta storica si sente all'istante e",
        "La struttura di riferimento emerge subito e",
        "Il profilo iconico si riconosce subito e",
        "L'identita classica si avverte da subito e",
        "Il registro iconico si fa sentire subito e",
        "L'impostazione da classico emerge subito e",
        "Il tono iconico si coglie subito e",
    ],

    # 10x - interno frase (colore blu)
    "il blu dal vivo e piu acceso di quanto lasci intuire la": [
        "il blu visto di persona risulta piu intenso di quanto suggerisca la",
        "il colore blu in realta e piu luminoso di quanto sembri dalla",
        "il blu dal vivo si rivela piu saturo rispetto a quanto indicasse la",
        "il tono blu e piu vivace di quanto facesse pensare la",
        "il blu reale supera il tono suggerito dalla",
        "il blu de visu e piu deciso di quanto mostri la",
        "guardando dal vivo il blu e piu brillante rispetto alla",
        "in mano il blu si rivela piu intenso di quanto indicasse la",
        "vedendolo di persona il blu appare piu vivace rispetto alla",
        "il colore dal vivo e piu saturo di quello percepibile dalla",
        "di persona il blu si mostra piu acceso rispetto alla",
    ],

    # 10x - interno frase (descrizione prodotto)
    "base nera che frena la lente": [
        "bordo scuro che bilancia la lente",
        "struttura nera che contiene la lente",
        "cornice nera che delimita la lente",
        "montatura nera che inquadra la lente",
        "elemento nero che ne bilancia la lente",
        "profilo scuro che stabilizza la lente",
        "fascia nera che bilancia il vetro",
        "telaio nero che incornicia la lente",
        "parte nera che trattiene la lente",
        "bordo scuro che incornicia la lente",
        "base scura che incornicia la lente",
        "elemento nero che delimita la lente",
    ],

    # 10x - fine frase (tono dissuasivo)
    "non e il paio che prendi quando vuoi sparire": [
        "non sono gli occhiali da scegliere per passare inosservato",
        "non e il modello per chi vuole restare nell'ombra",
        "non e il paio da mettere quando si vuole essere invisibili",
        "non sono il tipo di accessori da portare in incognito",
        "non e il modello giusto per chi cerca discrezione totale",
        "non e adatto a chi vuole evitare l'attenzione",
        "non e il paio per chi preferisce non essere notato",
        "non sono gli occhiali di chi non vuole farsi vedere",
        "non e il modello per chi vuole scomparire nella folla",
        "non si adatta a chi vuole passare inosservato",
        "non e il tipo di accessorio per chi cerca il basso profilo",
        "non sono adatti a chi vuole non attirare sguardi",
    ],

    # 10x - interno frase (acetato)
    "dal vivo avrei voluto un acetato ancora piu strutturato": [
        "in persona avrei preferito un acetato con piu corpo",
        "dal vero avrei gradito un acetato piu consistente",
        "di persona mi sarebbe piaciuto un acetato piu robusto",
        "vedendolo dal vivo avrei preferito piu spessore nell'acetato",
        "in realta avrei voluto una struttura in acetato piu decisa",
        "de visu mi sarebbe piaciuto un acetato con piu massa",
        "guardandolo di persona avrei apprezzato un acetato piu spesso",
        "in mano avrei preferito un acetato ancora piu presente",
        "dal vivo mi aspettavo un acetato di maggiore consistenza",
        "vedendolo in mano avrei voluto un acetato piu pieno",
        "in persona avrei voluto sentire piu peso nell'acetato",
        "dal vivo mi ero aspettato un acetato piu solido",
    ],

    # 10x - fine frase (cat-eye)
    "chi vuole un cat-eye piu aggressivo potrebbe trovarle troppo educate": [
        "per chi cerca un cat-eye piu deciso potrebbero sembrare troppo contenute",
        "chi preferisce un cat-eye piu estremo potrebbe trovarlo troppo morbido",
        "per i gusti piu audaci il cat-eye potrebbe risultare troppo sobrio",
        "chi vuole un cat-eye piu pronunciato potrebbe trovarlo troppo discreto",
        "per chi cerca piu radicalita nel cat-eye il modello potrebbe sembrare tenue",
        "chi cerca un cat-eye piu spinto potrebbe percepirlo come timido",
        "chi preferisce un cat-eye di carattere piu forte potrebbe trovarlo soft",
        "per un cat-eye piu incisivo il modello potrebbe risultare troppo disciplinato",
        "chi vuole una curvatura piu netta potrebbe trovarlo troppo tranquillo",
        "per chi ama il cat-eye deciso questo potrebbe sembrare troppo classico",
        "chi cerca piu angolazione nel cat-eye potrebbe trovarlo un po' addomesticato",
        "per i palati piu estremi il cat-eye potrebbe essere troppo misurato",
    ],

    # 10x - fine frase (versatilita)
    "non sono il paio piu versatile della rotazione": [
        "non sono il modello piu adattabile nella selezione",
        "non sono il paio piu flessibile dell'insieme",
        "non risultano i piu versatili tra quelli che porto",
        "non sono il modello con piu combinazioni nella rotazione",
        "non sono il paio da tutto e per tutto",
        "non sono il modello con la massima flessibilita d'uso",
        "non sono il paio piu polifunzionale nella mia selezione",
        "non sono tra i modelli piu versatili che possiedo",
        "non sono il paio con il piu alto tasso di abbinabilita",
        "non sono la scelta piu neutra della collezione",
        "non sono il modello piu adattabile a ogni contesto",
        "non sono il paio con la massima versatilita di abbinamento",
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
print("Round 13 OK" if errors == 0 else f"ERRORI: {errors}")
