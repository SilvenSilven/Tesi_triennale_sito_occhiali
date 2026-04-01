#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fix round 7 — pattern residui 21x + cleanup testo spazzatura."""

import psycopg2

DATABASE_URL = (
    "postgresql://neondb_owner:npg_uFxVSRoTj95w"
    "@ep-damp-sea-anvn4fw4.c-6.us-east-1.aws.neon.tech"
    "/neondb?sslmode=require"
)

PATTERNS = {

    # 21x — frase completa
    "e devo dire che il lavoro sulle proporzioni si capisce.": [
        "e devo ammettere che il bilanciamento delle forme è evidente.",
        "e sono costretto a riconoscere che la geometria funziona bene.",
        "e non posso negare che la costruzione formale regge.",
        "e in effetti la ricerca sulle proporzioni si sente.",
        "e la cura nella struttura si vede chiaramente.",
        "e si percepisce quanto lavoro ci sia dietro alla forma.",
        "e la progettazione degli equilibri formali è visibile.",
        "e il pensiero dietro alle proporzioni emerge con chiarezza.",
        "e l'attenzione alla forma è innegabile.",
        "e l'armonia delle dimensioni parla da sola.",
        "e la coerenza costruttiva si sente ad ogni uso.",
        "e il rigore nella forma è palpabile.",
        "e si capisce immediatamente quanto si sia lavorato sul volume.",
        "e la precisione delle proporzioni si traduce in un solido risultato.",
        "e il lavoro di cesello sulla struttura è sotto gli occhi.",
        "e si sente che nessuna proporzione è stata lasciata al caso.",
        "e la qualità della modellazione è riconoscibile.",
        "e il bilanciamento strutturale emerge anche nell'uso quotidiano.",
        "e la scelta delle misure si rivela azzeccata.",
        "e l'equilibrio dei volumi è stato studiato con attenzione.",
        "e la progettazione rivela un'attenzione alla proporzione non comune.",
        "e l'architettura formale è credibile.",
        "e si sente quanto siano stati pensati anche i dettagli più piccoli.",
    ],

    # 21x — frase completa
    "Quando un occhiale chiede troppe attenzioni smette di essere un piacere.": [
        "Un accessorio che pretende troppa cura finisce per diventare un peso.",
        "Quando un oggetto occupa più tempo del dovuto perde il suo valore d'uso.",
        "Un prodotto che richiede attenzione continua si trasforma in un onere.",
        "Quando qualcosa chiede troppe cure perde il carattere di piacere.",
        "Un oggetto che si fa notare per le sue esigenze non è liberatorio.",
        "Quando un accessorio esige troppo in termini di gestione, distrae.",
        "Un pezzo che richiede continua supervisione smette di essere spontaneo.",
        "Quando l'uso diventa gestione, il piacere si perde per strada.",
        "Un occhiale che è anche un problema logistico non può essere un compagno ideale.",
        "Quando qualcosa richiede troppe risorse di attenzione, diventa ostacolo.",
        "Un accessorio che vuole essere coccolato troppo non è pratico.",
        "Quando la cura supera il godimento, il valore diminuisce.",
        "Un oggetto eccessivamente esigente smette di essere spontaneo da indossare.",
        "Quando si ha bisogno di pensarci troppo, l'oggetto diventa un impegno.",
        "Un occhiale che si porta dietro troppe condizioni non è davvero pratico.",
        "Quando un prodotto vuole troppo da te, il rapporto si capovolge.",
        "Un occhiale eccessivamente fragile o delicato cambia il suo ruolo.",
        "Quando l'oggetto governa te più di quanto tu governi lui, c'è qualcosa che non va.",
        "Un accessorio che esige troppe attenzioni perde il carattere di compagno.",
        "Quando si devono pianificare troppe cose per indossarlo, il piacere svanisce.",
        "Un oggetto che ti occupa la testa è già a metà della strada per annoiarti.",
        "Quando il prodotto ti chiede più di quanto ti dia, è tempo di rivalutarlo.",
        "Un occhiale che vuole troppo cede il suo spazio come piacere quotidiano.",
    ],

    # 21x — frase completa
    "e lì si vede se un modello regge davvero o no.": [
        "e quel momento rivela il vero carattere di un modello.",
        "e proprio lì emerge la differenza tra l'oggetto promesso e quello reale.",
        "e in quel frangente il modello si svela per quello che è.",
        "e quello è il banco di prova che conta davvero.",
        "e in quel contesto si capisce se vale la pena o meno.",
        "e lì si misura l'onestà del prodotto.",
        "e il quadro reale emerge solo in quel momento.",
        "e lì il modello non può più nascondersi dietro le aspettative.",
        "e in quel passaggio si materializza il verdetto.",
        "e quello è il punto in cui il giudizio si forma.",
        "e quel contesto parla più chiaro di qualsiasi foto.",
        "e in quella fase si distingue un prodotto solido da uno fragile.",
        "e solo allora si capisce se l'acquisto reggeva davvero.",
        "e in quel preciso momento il modello dà il suo responso.",
        "e in quella tappa si esclude tutto il rumore e rimane solo la sostanza.",
        "e quel test è il più autentico che un occhiale possa superare.",
        "e in quel momento la qualità o si palesa o si dissolve.",
        "e lì si decide se il prodotto ha senso nella vita reale.",
        "e quella è la prova che non am mette scuse.",
        "e in quel contesto si chiarisce tutto ciò che sembrava ambiguo.",
        "e quella verifica non lascia zone grigie.",
        "e in quel frangente ogni dubbio riceve risposta.",
        "e lì si chiude la partita tra attesa e realtà.",
    ],

    # ~11-15x — frase completa (in coppia con "molto meno del previsto")
    "Sulla carta interessante, nella pratica molto meno.": [
        "In teoria convincente, in pratica deludente.",
        "Sulla scheda sembrava giusto, nella realtà meno.",
        "A distanza pareva valido, da vicino perdeva attrattiva.",
        "Le aspettative erano alte; il prodotto reale le scalava.",
        "Nelle immagini tutto bene, indossato meno.",
        "Il concept prometteva, il risultato ha tradito.",
        "La proposta teorica era interessante; la pratica meno.",
        "Guardato online sembrava solido; portato, mostra le crepe.",
        "L'idea era buona; l'esecuzione tradiva aspettative.",
        "La descrizione faceva pensare ad altro; il reale è più sobrio.",
        "Da catalogo sembrava perfetto; dalla realtà meno.",
        "In vetrina funzionava; addosso deludeva.",
        "Come progetto aveva senso; come oggetto d'uso meno.",
        "La premessa era credibile; il prodotto finale non all'altezza.",
        "L'appeal teorico non si traduceva in soddisfazione reale.",
        "Tutto bene in teoria, nella pratica è altra storia.",
        "Prometteva molto, manteneva poco.",
        "Il divario tra idea e realtà era qui molto evidente.",
        "Sembrava bello da acquistare, meno da portare.",
        "Il promesso e il ricevuto divergevano sensibilmente.",
        "Da scheda prodotto era convincente; dal vivo, meno.",
    ],

    # 21x — frammento iniziale frase (endings variate)
    "La prima cosa che ho notato,": [
        "La prima osservazione che ho fatto,",
        "Ciò che ho colto subito,",
        "Il primo dettaglio che ho registrato,",
        "Quello che mi ha colpito sin dall'inizio,",
        "La prima cosa che mi sono accorto,",
        "Il primo elemento che ho percepito,",
        "Il dato iniziale più evidente,",
        "Quello che ho notato per primo,",
        "La prima impressione che mi sono fatto,",
        "La prima cosa che ho registrato,",
        "Ciò che mi ha raggiunto subito,",
        "Il primo aspetto che ho colto,",
        "La prima nota che ho preso,",
        "La prima cosa che ha catturato la mia attenzione,",
        "Il primo elemento che ha parlato,",
        "La cosa iniziale più evidente,",
        "La prima percezione che ho avuto,",
        "Quello che ho catturato subito,",
        "Il primo punto che ho registrato,",
        "La prima reazione che ho avuto,",
        "La cosa che ho visto subito,",
        "Il primo dato che ho raccolto,",
    ],

    # Pulizia testo spazzatura — "molto meno del previsto." finale di frase garbled
    # Sostituisco il frammento sporco con la fine corretta (solo il punto)
    " molto meno del previsto.": [
        ".",
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
print("✅ Round 7 completato!" if errors == 0 else f"⚠️ {errors} errori.")
