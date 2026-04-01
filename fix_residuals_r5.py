#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fix round 5 — pattern residui 23-25x."""

import psycopg2

DATABASE_URL = (
    "postgresql://neondb_owner:npg_uFxVSRoTj95w"
    "@ep-damp-sea-anvn4fw4.c-6.us-east-1.aws.neon.tech"
    "/neondb?sslmode=require"
)

PATTERNS = {

    # 25x
    "Non si affidano al colpo facile ma a un disegno ragionato.": [
        "Non puntano sull'effetto immediato, ma su un progetto meditato.",
        "Non cercano l'impatto facile: puntano a una coerenza profonda.",
        "Non si basano sul colpo d'occhio, ma su una logica costruttiva.",
        "Non cercano il consenso immediato: preferiscono una visione strutturata.",
        "Non vivono di effetto superficiale, ma di un ragionamento formale.",
        "Non inseguono l'impatto di superficie: costruiscono qualcosa di più solido.",
        "Non si servono dell'effetto wow, ma di un disegno elaborato.",
        "Non cercano la scena: lavorano su una struttura pensata.",
        "Non puntano al facile consenso, ma a una tesi stilistica.",
        "Non si basano sull'emozione immediata: hanno un'architettura.",
        "Non si affidano al gesto drammatico, ma a un ragionamento preciso.",
        "Non cercano il riconoscimento rapido: costruiscono su fondamenta.",
        "Non inseguono l'applauso immediato: partono da un progetto.",
        "Non operano sull'effetto momentaneo, ma su una visione organica.",
        "Non giocano sull'impatto visivo primario: lavorano su una logica.",
        "Non si avvalgono del colore o del peso per fare effetto: preferiscono la forma.",
        "Non sono il tipo di prodotto che convince al volo: richiedono il tempo giusto.",
        "Non vivono dell'immediato: il loro linguaggio è costruttivo.",
        "Non cercano il plauso rapido: offrono una lettura più profonda.",
        "Non puntano all'effetto wow: preferiscono la costruzione lenta.",
        "Non si appoggiano al colore per fare breccia: il progetto parla da solo.",
        "Non cercano l'attenzione: la guadagnano con un disegno solido.",
        "Non operano sulla prima impressione: lavorano sul lungo periodo.",
        "Non inseguono il consenso facile: preferiscono una proposizione strutturata.",
        "Non vivono di effimero: hanno una base teorica riconoscibile.",
    ],

    # 24x
    "Gli manca poco per convincermi del tutto.": [
        "Ci vuole poco per farlo diventare perfetto per me.",
        "È a un passo dal convincermi pienamente.",
        "Manca ancora qualcosa per chiudere il cerchio.",
        "Un piccolo dettaglio separa questo prodotto dalla perfezione per me.",
        "È quasi dove voglio che sia.",
        "Ci manca un margine stretto per il pieno convincimento.",
        "Un po' meno di questo o un po' di più di quello e sarebbe perfetto.",
        "È molto vicino a quello che cerco, ma non del tutto.",
        "Il gap è piccolo, ma percepibile.",
        "Manca un'ultima spunta per la valutazione piena.",
        "È quasi lì, ma 'quasi' conta.",
        "La distanza dalla piena soddisfazione è minima ma presente.",
        "Ci separa poco dalla valutazione massima.",
        "Un dettaglio in più lo renderebbe definitivo.",
        "È al confine tra il buono e l'ottimo, ma non supera la soglia.",
        "Quasi, ma non abbastanza.",
        "Manca un passo per il giudizio pieno.",
        "Ci vuole un piccolo aggiustamento per il pieno convincimento.",
        "È a distanza ravvicinata dalla piena approvazione.",
        "Un ulteriore affinamento lo renderebbe irresistibile.",
        "È molto buono, ma non ancora definitivo per me.",
        "Ci manca quella piccola spinta finale.",
        "Ha quasi tutto: manca solo l'ultimo dettaglio.",
        "È al limite superiore del 'quasi convincente'.",
        "Quasi del tutto, ma non completamente.",
    ],

    # 23x
    "Resta un ottimo acquisto, semplicemente non totalmente universale.": [
        "Resta un buon acquisto, solo non adatto a ogni morfologia.",
        "È un prodotto valido, semplicemente non per tutti i profili.",
        "Rimane un acquisto solido, solo con un pubblico specifico.",
        "È un ottimo prodotto, non universalmente indossabile.",
        "Rimane un acquisto di qualità, con una destinazione selettiva.",
        "È molto ben fatto, semplicemente non su ogni viso.",
        "Rimane un ottimo pezzo, solo per chi si riconosce nel tipo.",
        "È un buon acquisto per chi ci si trova, non per tutti.",
        "Rimane valido come prodotto, meno come opzione universale.",
        "È di qualità, semplicemente con un appeal definito.",
        "Rimane un acquisto apprezzabile, ma con una nicchia di utilizzo.",
        "È ben riuscito, solo non si adatta a ogni stile.",
        "Rimane un prodotto eccellente, con un target preciso.",
        "È un buon pezzo, semplicemente non per ogni contesto.",
        "Rimane di alto profilo, solo non per ogni tipo di utente.",
        "È un acquisto riuscito, semplicemente non per ogni viso.",
        "Rimane molto valido, solo con un registro stilistico definito.",
        "È di ottima qualità, non però adattabile a ogni silhouette.",
        "Rimane un acquisto centrato, con una selettività insita.",
        "È valido e ben costruito, semplicemente non per tutti.",
        "Rimane molto buono, con un'applicabilità selettiva.",
        "È un ottimo pezzo per chi lo cerca davvero.",
        "Rimane di alto livello, ma non universale nell'adattabilità.",
        "È eccellente per il giusto utente, non per ogni tipo.",
    ],

    # 23x
    "Fanno molto meglio dal vivo che nelle foto.": [
        "In realtà superano di molto l'impressione data dagli scatti.",
        "Dal vivo guadagnano enormemente rispetto alle immagini online.",
        "La differenza tra le foto e il prodotto reale è notevole.",
        "Gli scatti non rendono la quota di qualità che emerge dal vivo.",
        "Indossati rendono molto più delle immagini promozionali.",
        "La fotografia non riesce a catturare il loro reale valore.",
        "Il live è tutta un'altra cosa rispetto alle immagini del catalogo.",
        "Da vicino si capisce tutto quello che le foto non trasmettevano.",
        "Dal vivo la percezione cambia completamente rispetto agli scatti.",
        "Le foto non rendono giustizia: dal vivo è un altro prodotto.",
        "Visti di persona, la qualità percepita sale notevolmente.",
        "Le immagini non comunicano la loro reale presenza fisica.",
        "Dal vivo l'impressione è molto più positiva di quella data dal monitor.",
        "Il divario tra foto e realtà è qui molto favorevole.",
        "Le immagini digitali non sanno replicare ciò che si vede dal vivo.",
        "Guardandoli di persona, si capisce perché valga la pena tenerli.",
        "Il contatto diretto li valorizza molto rispetto agli scatti.",
        "Visti di persona, guadagnano parecchio rispetto alla scheda online.",
        "Dal vivo emergono qualità che le foto schiacciavano.",
        "Le foto fanno da rete di sicurezza, ma il prodotto reale è superiore.",
        "Il reale e il digitale non si confrontano qui: vince il reale.",
        "Portarli cancella i dubbi alimentati dalle foto.",
        "In persona dimostrano quanto le immagini possano essere riduttive.",
        "Il salto di qualità tra la foto e il prodotto fisico è evidente.",
    ],

    # 23x
    "Il comfort per me resta l'argomento decisivo e qui non arrivo alla sufficienza emotiva.": [
        "Il comfort è il parametro che per me decide tutto, e qui non raggiunge la soglia.",
        "La questione del comfort è prioritaria per me e questo modello non soddisfa.",
        "Per me il comfort è il primo criterio e qui rimane un punto debole.",
        "Il benessere nell'uso è il mio parametro principale: qui non supera la soglia.",
        "Per come mi muovo, il comfort è fondamentale e qui non arriva dove vorrei.",
        "Il primo criterio che guarda la mia valutazione è il comfort: qui zoppica.",
        "Portabilità e comfort vengono prima di tutto per me e qui non convincono.",
        "Il comfort è il metro con cui valuto tutto: qui rimane una nota insufficiente.",
        "Per me l'uso prolungato è determinante e il comfort qui non convince.",
        "Il criterio del benessere è per me dirimente: e qui non supero l'incertezza.",
        "La mia priorità numero uno è il comfort: questa voce non si chiude in positivo.",
        "Per come li uso, il comfort è centrale e qui non arrivo alla piena soddisfazione.",
        "Il comfort ha la prima parola per me, e qui la risposta è insufficiente.",
        "Nel mio schema valutativo il comfort pesava più di tutto: e qui non convince.",
        "Per la mia tipologia di utente il comfort è decisivo: e qui manca qualcosa.",
        "Il criterio che guida il mio acquisto è il comfort: qui non si chiude bene.",
        "Il comfort per me è dirimente: questo modello non raggiunge il livello che cerco.",
        "Per me indossare bene è tutto: e qui la soddisfazione non arriva al pieno.",
        "Il benessere durante l'uso è la mia priorità: qui rimane insufficiente.",
        "Per come valuto gli occhiali, il comfort è il primo fattore: qui non basta.",
        "Il mio primo parametro è la portabilità: qui non supera il test.",
        "Il comfort parla prima di tutto: e il verdetto qui non è favorevole.",
        "Per me l'uso comodo è insostituibile: questo modello non convoca la certezza.",
        "La priorità assoluta è il comfort: e questa voce qui rimane in rosso.",
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
        print(f"  '{p[:55]}' → {cnt}x")
print("✅ Round 5 completato!" if errors == 0 else f"⚠️ {errors} errori.")
