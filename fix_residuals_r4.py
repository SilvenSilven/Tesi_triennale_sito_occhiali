#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fix round 4 — pattern residui da 26-28 occorrenze."""

import psycopg2

DATABASE_URL = (
    "postgresql://neondb_owner:npg_uFxVSRoTj95w"
    "@ep-damp-sea-anvn4fw4.c-6.us-east-1.aws.neon.tech"
    "/neondb?sslmode=require"
)

PATTERNS = {

    # 28x
    "Li considero interessanti più che irresistibili.": [
        "Li trovo curiosi più che coinvolgenti.",
        "Li apprezzo senza sentirmi preso del tutto.",
        "Li stimo senza esserne innamorato.",
        "Li giudico belli senza sentire il bisogno compulsivo di tenerli.",
        "Li trovo piacevoli, ma non irresistibili.",
        "Li valorizzerei su altri, ma non mi fanno impazzire.",
        "Li vedo interessanti, senza sentire l'urgenza di indossarli.",
        "Li rispetto come progetto, senza esserne catturato.",
        "Li reputo validi senza farmi prendere dall'entusiasmo.",
        "Li considero buoni senza sentire il click emotivo.",
        "Li stimo come prodotto, senza sentire la necessità di tenerli.",
        "Li giudico meritevoli senza sentire la scintilla.",
        "Li trovo eleganti, ma non mi appartengono completamente.",
        "Li valuto con rispetto, senza esserne convinto fino in fondo.",
        "Li considero piacevoli, ma non imprescindibili.",
        "Li trovo curati senza sentire il bisogno urgente di averli.",
        "Li apprezzo come oggetto, senza innamorarmene.",
        "Li stimo per la qualità, pur non essendo il mio ideale.",
        "Li considero riusciti senza però esserne conquistato.",
        "Li trovo validi senza avvertire un'attrazione forte.",
        "Li rispetto senza sentire la necessità di possederli.",
        "Li vedo belli senza avere la sensazione di doverli avere.",
        "Li stimo in modo distaccato, senza il coinvolgimento che cercavo.",
        "Li giudico buoni, ma non sono il mio tipo.",
        "Li apprezzo senza sentirmi investito completamente.",
        "Li valuto positivamente, ma il feeling non è scattato.",
        "Li riconosco come prodotto valido, senza sentirli miei.",
        "Li stimo, pur senza sentirli necessari al mio guardaroba.",
        "Li trovo ben fatti, ma non si sono insinuati nella mia routine.",
    ],

    # 28x — fragment: keep ending, replace opening
    "Su di me funzionano bene con": [
        "Per me rendono di più con",
        "Sul mio viso si esprimono meglio con",
        "Nel mio caso l'abbinamento migliore è con",
        "Indossandoli come faccio io, vanno forte con",
        "Per come li porto io, il picco è con",
        "Con la mia morfologia facciale il match è perfetto con",
        "Per il mio stile il connubio migliore è con",
        "Nel mio contesto stilistico si trovano bene con",
        "Con il mio guardaroba rendono soprattutto con",
        "Considerato il mio abbigliamento, danno il meglio con",
        "Con il mio stile personale li sento al meglio con",
        "Per come mi vesto di solito, il massimo è con",
        "Sulla mia faccia l'abbinamento vincente è con",
        "Nel mio uso quotidiano ci siamo trovati principalmente con",
        "Con la mia routine vestimentaria brillano soprattutto con",
        "Per la mia tipologia di look rendono perfettamente con",
        "Con il mio approccio all'outfit il top è con",
        "Dato il mio stile abituale, li sento meglio con",
        "Per il modo in cui mi vesto, il rendimento è alto con",
        "Con i miei abiti tipici l'abbinamento riuscito è con",
        "Nel mio guardaroba abituale si integrano meglio con",
        "Tenendo conto del mio stile, rendono di più con",
        "Con la mia conformazione si adattano meglio con",
        "Per come li vivo nella quotidianità, brillano con",
        "Con le mie abitudini vestimentarie mi sono trovato bene con",
        "Per il mio tipo di look, il connubio è forte con",
        "Sulla mia testa danno il meglio con",
        "Con il mio guardaroba il picco di resa è con",
        "Per come uso il mio guardaroba rendono di più con",
    ],

    # 27x — fragment (ciascuna continuazione è diversa)
    "che ho capito il resto: la": [
        "che si è completato il quadro: la",
        "che ho visto il progetto nella sua interezza: la",
        "che tutto ha preso senso: la",
        "che la visione complessiva è diventata chiara: la",
        "che ho colto il disegno completo: la",
        "che mi sono reso conto di tutto: la",
        "che le tessere si sono unite: la",
        "che il ragionamento si è chiarito: la",
        "che la lettura è diventata completa: la",
        "che il puzzle si è composto: la",
        "che ho decifrato il progetto: la",
        "che ho capito fino in fondo: la",
        "che ho compreso l'intenzione di fondo: la",
        "che il quadro è diventato nitido: la",
        "che il contesto si è rivelato: la",
        "che ho afferrato l'idea centrale: la",
        "che ho letto il design nella sua interezza: la",
        "che tutto si è messo a fuoco: la",
        "che l'intenzione del progetto è emersa: la",
        "che la logica costruttiva si è rivelata: la",
        "che ho capito il filo che tiene insieme tutto: la",
        "che il disegno si è fatto chiaro: la",
        "che ho percepito la coerenza del progetto: la",
        "che ho realizzato il disegno generale: la",
        "che la struttura concettuale mi è apparsa chiara: la",
        "che il codice stilistico si è svelato: la",
        "che la visione del designer si è fatta leggibile: la",
        "che l'architettura del prodotto si è rivelata: la",
    ],

    # 27x — frase completa (seguita da continuazioni variabili)
    "dà proprio quel segno in più che cercavo.": [
        "offre quel dettaglio distintivo che stavo cercando.",
        "porta quella nota in più che volevo.",
        "aggiunge il carattere che mi mancava.",
        "porta quel tocco di identità che cercavo.",
        "introduce quell'elemento differenziante che desideravo.",
        "garantisce esattamente il segno personale che volevo.",
        "fornisce quella personalizzazione che mi serviva.",
        "porta quella riconoscibilità che volevo aggiungere.",
        "offre il contrasto stilistico che stavo cercando.",
        "aggiunge quella presenza che volevo avere.",
        "porta quel dettaglio di carattere che stavo inseguendo.",
        "conferisce quel peso visivo che cercavo.",
        "dona quella nota di carattere che mi mancava.",
        "introduce quell'accento che rendeva il look incompleto.",
        "aggiunge quella particolarità che fa la differenza.",
        "porta quel segno visivo che mi definisce.",
        "offre quella personalità extra che stavo cercando.",
        "introduce quel dettaglio che completa l'insieme.",
        "porta quella cifra stilistica che inseguivo.",
        "aggiunge il carattere distintivo che volevo incorporare.",
        "garantisce quel plus visivo che il look richiedeva.",
        "dona quella nota identitaria che stavo cercando.",
        "offre quella specificità che trasforma il look.",
        "porta quella penalizzazione zero che cercavo.",
        "introduce quel qualcosa che completava il quadro.",
        "aggiunge il tocco personale che volevo.",
        "porta quel marchio di stile che cercavo.",
        "dona quell'impronta personale che volevo dare.",
    ],

    # 26x — frase completa
    "ha una bella idea dietro.": [
        "ha un'idea progettuale interessante.",
        "ha una buona impostazione concettuale.",
        "ha un'intenzione stilistica valida.",
        "ha una visione di design chiara.",
        "ha un fondamento estetico solido.",
        "ha un'architettura concettuale riuscita.",
        "ha una tesi stilistica ben definita.",
        "è nato da un'idea che funziona.",
        "ha una direzione progettuale coerente.",
        "ha una visione formale apprezzabile.",
        "ha un disegno d'insieme valido.",
        "ha una base progettuale interessante.",
        "ha un'intuizione stilistica condivisibile.",
        "ha una logica costruttiva apprezzabile.",
        "ha un'ispirazione di partenza solida.",
        "ha un'idea generatrice valida.",
        "ha una personalità progettuale ben costruita.",
        "ha una proposta concettuale convincente.",
        "ha una direzione estetica precisa.",
        "ha un principio generativo interessante.",
        "ha una visione stilistica riconoscibile.",
        "ha una struttura ideativa apprezzabile.",
        "ha un'architettura visiva ragionata.",
        "ha un'intenzione di design ben sviluppata.",
        "ha una proposta estetica con una sua logica.",
        "ha un'ispirazione che funziona in astratto.",
        "ha un'identità progettuale ben definita.",
    ],

    # 26x — frase completa
    "Alla fine il bilancio per me è positivo, anche con qualche riserva concreta.": [
        "Alla fine il giudizio complessivo è positivo, con alcune riserve.",
        "Il saldo finale è favorevole, pur con qualche nota critica.",
        "Tirando le somme, la valutazione è buona, con qualche eccezione.",
        "Il bilancio totale è bilanciato ma in positivo.",
        "Alla fine dei conti, l'esperienza è soddisfacente nonostante qualche limite.",
        "Il verdetto finale è sostanzialmente positivo, con qualche caveat.",
        "Facendo la somma, il giudizio pende verso il bene, con un asterisco.",
        "Il computo complessivo è positivo, pur con alcune riserve da registrare.",
        "Alla resa dei conti, è un bilancio in attivo, con qualche passivo.",
        "Mettendo tutto sulla bilancia, il piatto positivo pesa di più.",
        "In ultima analisi il giudizio è positivo, anche se con qualche incertezza.",
        "Il quadro finale è largamente favorevole, nonostante le riserve.",
        "Facendo il punto, il segno è positivo, con qualche nota critica da ricordare.",
        "Il saldo complessivo è favorevole, pur con alcuni pesi dall'altra parte.",
        "Al netto di qualche critica, il bilancio rimane positivo.",
        "Sommando tutto, l'esperienza si chiude in positivo, non senza riserve.",
        "Il resoconto finale pende verso il sì, con qualche distinguo.",
        "Togliendo le riserve, rimane un giudizio positivo.",
        "Il bilancio finale è costruttivo, con qualche aspettativa non soddisfatta.",
        "Alla fine, il conto torna a favore, anche se non senza qualche eccezione.",
        "Guardando l'insieme, l'esperienza è positiva con qualche asterisco.",
        "Il giudizio complessivo rimane positivo, non esente da osservazioni.",
        "In definitiva, la valutazione è favorevole, con qualche limite da segnalare.",
        "Tirando le somme, la bilancia pende a favore, con qualche peso contrario.",
        "Il bilancio netto è positivo, anche se non privo di ombre.",
        "Alla fine il risultato è soddisfacente, con qualche zona grigia.",
        "Il verdetto complessivo è buono, pur con qualche riserva dichiarata.",
    ],

}

# ════════════════════════════════════════════════════════════════════
print("Connessione al DB...")
conn = psycopg2.connect(DATABASE_URL)
cur = conn.cursor()

print("Download recensioni...")
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
        conn.rollback()
        errors += len(batch)
        print(f"  ERRORE batch {bn}: {e}")

cur.close(); conn.close()

print(f"\n{'='*50}")
print(f"Aggiornate: {applied} | Errori: {errors}")
for p, cnt in pattern_occurrence.items():
    if cnt > 0:
        print(f"  '{p[:55]}' → {cnt}x")
print("✅ Round 4 completato!" if errors == 0 else f"⚠️ {errors} errori.")
