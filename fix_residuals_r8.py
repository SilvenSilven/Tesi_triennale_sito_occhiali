#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fix round 8 — pattern residui 19-20x."""

import psycopg2

DATABASE_URL = (
    "postgresql://neondb_owner:npg_uFxVSRoTj95w"
    "@ep-damp-sea-anvn4fw4.c-6.us-east-1.aws.neon.tech"
    "/neondb?sslmode=require"
)

PATTERNS = {

    # 20x — frase completa
    "Il punto è sempre lo stesso: bello non vuol dire automaticamente giusto.": [
        "Il ragionamento non cambia: estetica gradevole non significa adatto a me.",
        "La domanda è sempre la stessa: bello non equivale a necessario.",
        "La logica di base non cambia: mi piace non è lo stesso di mi calza.",
        "La riflessione ricorrente è sempre quella: un bell'oggetto non è per forza quello giusto.",
        "La conclusione è sempre simile: attraente non vuol dire adeguato.",
        "La distinzione che faccio ogni volta: apprezzare un design non significa indossarlo.",
        "Il nodo è lì da sempre: bello da vedere non combacia automaticamente con bello da portare.",
        "Il pensiero ricorrente è questo: estetica e adattamento sono piani diversi.",
        "Il punto fermo che porto con me: l'ammirazione visiva non è adozione quotidiana.",
        "La domanda che mi ripeto: bella forma non implica forma per me.",
        "La riflessione che non passa: l'attrattiva visiva non risolve la compatibilità.",
        "La certezza che ho consolidato: un progetto interessante non è automaticamente il mio progetto.",
        "La convinzione che rimane: il fascino non garantisce la sintonia.",
        "Il pensiero che si ripete: la qualità estetica non dice nulla sull'adattabilità.",
        "L'insegnamento che torno a fare: bello sulla carta non è bello addosso per forza.",
        "La verità semplice è questa: gradire non basta, serve appartenere.",
        "La distinzione che mantengo: ammirare un prodotto è diverso dal volerlo ogni giorno.",
        "Il ragionamento che faccio sempre: trovarlo elegante non mi dice se funziona per il mio viso.",
        "La posizione che non abbandono: un design convincente non si trasforma in scelta automatica.",
        "Il punto che non supero: piacermi visivamente non è lo stesso di funzionare per me.",
        "La constatazione solita: la bellezza oggettiva non implica la giustezza soggettiva.",
    ],

    # 19x — frase completa
    "Per me restano più convincenti come oggetto che come compagni di giornata.": [
        "Li apprezzo come progetto, ma non come compagni d'uso.",
        "Li stimo come prodotto, ma non li sento adatti alla mia giornata.",
        "Li rispetto come oggetto di design, ma non me li vedo addosso ogni giorno.",
        "Hanno più valore da guardare che da portare, nel mio caso.",
        "Come oggetti li trovo eccellenti: come miei compagni meno.",
        "Li ammiro come realizzazione, ma non li sento estendibili al mio quotidiano.",
        "Come prodotti li valuto positivamente; come miei compagni è altra storia.",
        "Li apprezzo da fuori più che dall'interno.",
        "Hanno più senso come concept che come parte della mia routine.",
        "Li considero riusciti come oggetti, meno come occhiali per me.",
        "Sono da ammirare più che da indossare, nel mio caso.",
        "Li stimo come artefatti: non li vivo come compagni d'uso.",
        "Li rispetto come design, non li adotto come quotidianità.",
        "Più apprezzati come prodotto che come alternativa per me.",
        "Meglio come oggetti che come miei alleati di tutti i giorni.",
        "Li tengo in grande stima ma fuori dalla rotazione quotidiana.",
        "Per come li uso, restano più interessanti che praticabili.",
        "Meritano rispetto come oggetti: non meritano il mio uso regolare.",
        "Più ammirati che portati, per quanto mi riguarda.",
        "Li valuto bene come prodotti: li tengo fuori dalla mia selezione giornaliera.",
    ],

    # 20x — frammento inizio frase (endings variate)
    "Li ho messi alla prova in": [
        "Li ho testati in",
        "Li ho portati in",
        "Li ho indossati in",
        "Li ho usati in",
        "Li ho provati in",
        "Li ho sfidati in",
        "Li ho valutati in",
        "Li ho verificati in",
        "Li ho impiegati in",
        "Li ho sperimentati in",
        "Li ho adattati a",
        "Li ho misurati su",
        "Li ho osservati in",
        "Li ho esposti a",
        "Li ho calati in",
        "Li ho confrontati con",
        "Li ho verificati su",
        "Li ho inseriti in",
        "Li ho applicati a",
        "Li ho introdotti in",
        "Li ho lanciati in",
    ],

    # 20x — frammento inizio frase
    "Li ho presi quasi d'impulso, temevo che": [
        "Li ho acquistati di slancio, avevo paura che",
        "Li ho comprati quasi per istinto, con la preoccupazione che",
        "L'ho fatto senza pensarci troppo, con la paura che",
        "Li ho scelti d'istinto, preoccupandomi che",
        "Li ho presi di getto, dubitando che",
        "È stato un acquisto rapido, con il timore che",
        "Li ho ordinati di impulso, pensando che",
        "L'impulso ha prevalso, con la preoccupazione che",
        "Li ho cercati d'istinto, avevo dubbi sul fatto che",
        "Un acquisto d'impulso, tra la paura che",
        "Li ho presi senza riflettere troppo, non sicuro che",
        "Li ho puntati e presi subito, pur temendo che",
        "Li ho messi nel carrello di corsa, preoccupato che",
        "È stato un click quasi immediato, con qualche riserva sul fatto che",
        "Li ho puntati e comprati subito, nonostante dubitassi che",
        "Li ho voluti quasi in tempo reale, con il dubbio che",
        "Un acquisto veloce, nonostante la preoccupazione che",
        "Li ho presi senza indugio, pur essendo un po' scettico sul fatto che",
        "Ho ceduto all'impulso, sperando di sbagliare sul fatto che",
        "Li ho acquistati di corsa, con la riserva mentale che",
        "Ho comprato veloce, pur non essendo sicuro che",
    ],

    # 19x — frammento inizio frase (garbled endings)
    "Avevo qualche dubbio iniziale, è che": [
        "Avevo qualche perplessità iniziale, ma il dato concreto è che",
        "Nutrivo qualche riserva all'inizio, ma la realtà è che",
        "Non ero del tutto convinto, eppure la verità è che",
        "Avevo dei dubbi, ma quello che ho scoperto è che",
        "L'incertezza di partenza era reale, ma la conclusione è che",
        "Ero partito scettico, ma quello che emerge è che",
        "All'inizio avevo qualche riserva, poi ho visto che",
        "Non ero sicuro, ma la scoperta è stata che",
        "Partivo con perplessità, ma la realtà pratica mostra che",
        "Avevo dei dubbi legittimi, ma la risposta è che",
        "La mia incertezza iniziale era concreta, ma il fatto verificato è che",
        "Ero titubante, ma il risultato dimostra che",
        "Non sapevo bene cosa aspettarmi, e la risposta è stata che",
        "Avevo qualche interrogativo, ma la risposta è che",
        "Partivo con qualche preoccupazione, ma ho scoperto che",
        "Non ero pienamente convinto, ma la verità è che",
        "I dubbi c'erano, ma il risultato ha dimostrato che",
        "Avevo timori, ma quello che ho trovato è che",
        "Le riserve iniziali erano concrete, ma poi ho visto che",
        "Partivo cauto, ma la realtà ha dimostrato che",
        "Non mi aspettavo molto, ma il riscontro reale dice che",
    ],

    # 19x — conclusione di frase (sentence ending)
    ", e il suo carattere diventa leggibile.": [
        ", e lì il suo carattere si rivela.",
        ", e in quel momento il suo linguaggio emerge.",
        ", e in quel contesto la sua personalità si definisce.",
        ", e lì la sua identità si manifesta chiaramente.",
        ", e in quella condizione il suo senso si svela.",
        ", e in quel momento tutto diventa coerente.",
        ", e in quell'uso la sua natura prende forma.",
        ", e lì si capisce davvero che tipo di prodotto sia.",
        ", e solo allora il suo carattere viene fuori.",
        ", e lì si capisce la sua vera natura.",
        ", e in quella condizione si apprezza la coerenza del progetto.",
        ", e in quel contesto parla con una voce propria.",
        ", e nel momento giusto il progetto si svela davvero.",
        ", e quella è l'istanza in cui tutto ha senso.",
        ", e il suo vero registro emerge.",
        ", e lì si chiarisce tutto il pensiero formale.",
        ", e in quel momento la scelta stilistica si giustifica.",
        ", e in quella condizione il modello diventa eloquente.",
        ", e lì prende la parola nel modo più diretto.",
        ", e in quell'uso il disegno parla da solo.",
    ],

    # 19x — frammento inizio (endings variate)
    "in un modo che trovo molto": [
        "in maniera che considero molto",
        "con un risultato che apprezzo come molto",
        "in modo da risultare",
        "con un equilibrio che reputo",
        "con una sinergia che trovo",
        "in una formula che mi sembra molto",
        "in un rapporto che valuto come molto",
        "con una coerenza che ritengo",
        "con un'armonia che considero molto",
        "con un esito che definirei molto",
        "con una congiunzione che trovo",
        "in modo da creare qualcosa di",
        "costruendo qualcosa che giudico molto",
        "creando un insieme che valuto come",
        "con un'unità che trovo",
        "in maniera tale da essere",
        "in una sintesi che reputo molto",
        "con un incontro che trovo",
        "in un'integrazione che considero",
        "con un connubio che definirei",
    ],

}

# ════════════════════════════════════════════════════════════════════
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
        print(f"  Batch {bn:2d}: {applied}/{len(changes)}")
    except Exception as e:
        conn.rollback(); errors += len(batch)
        print(f"  ERRORE batch {bn}: {e}")

cur.close(); conn.close()
print(f"\nAggiornate: {applied} | Errori: {errors}")
for p, cnt in pattern_occurrence.items():
    if cnt > 0:
        print(f"  '{p[:62]}' → {cnt}x")
print("✅ Round 8 completato!" if errors == 0 else f"⚠️ {errors} errori.")
