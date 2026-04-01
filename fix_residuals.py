#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fix finale dei pattern residui.
Scarica dal DB, identifica frasi ripetute, le sostituisce con
alternative indicizzate (occurrence n → alternativa n), applica al DB.
"""

import psycopg2
from collections import defaultdict
import re

DATABASE_URL = (
    "postgresql://neondb_owner:npg_uFxVSRoTj95w"
    "@ep-damp-sea-anvn4fw4.c-6.us-east-1.aws.neon.tech"
    "/neondb?sslmode=require"
)

# ════════════════════════════════════════════════════════════════════
# DIZIONARIO PATTERN → POOL DI ALTERNATIVE (>=60 per pattern ad alta freq)
# ════════════════════════════════════════════════════════════════════

FINAL_FIXES = {

    # 51x — apertura con "è che ..."
    "La cosa più onesta che posso dire è che": [
        "La verità è che",
        "Il risultato concreto è che",
        "Con tutta onestà, devo ammettere che",
        "Senza filtri:",
        "Non giro intorno alle parole:",
        "Il bilancio reale porta a dire che",
        "Per rimanere sui fatti:",
        "Parlando senza fronzoli,",
        "La valutazione più diretta che posso dare è che",
        "In tutta franchezza,",
        "Non mi nascondo:",
        "Il dato di fatto è che",
        "Stando ai fatti nudi e crudi,",
        "Devo essere franco:",
        "La conclusione onesta è che",
        "Senza inutili giri di parole,",
        "Non esagero né sminuisco:",
        "La lettura più lucida del prodotto mi porta a dire che",
        "Per dirla in modo diretto,",
        "Il succo della questione è che",
        "Guardando le cose come stanno,",
        "La sintesi più fedele è che",
        "Il riscontro reale è che",
        "Con tutta sincerità,",
        "Per andare dritto al punto,",
        "Senza abbellire il racconto,",
        "Togliendo l'entusiasmo del primo momento,",
        "A mente fredda, quello che rimane è che",
        "Passato il rodaggio sentimentale,",
        "Togliendo ogni esagerazione,",
        "La risposta concreta è che",
        "Restando con i piedi per terra,",
        "Senza esaltazioni né critiche pretestuose,",
        "Il ragionamento più sobrio porta a dire che",
        "Alla luce dell'esperienza effettiva,",
        "Per essere preciso,",
        "Senza nascondersi dietro paroloni,",
        "Mettendo da parte i bias personali,",
        "Il resoconto onesto dice che",
        "Restando fedeli all'esperienza vissuta,",
        "Senza costruire aspettative artificiali,",
        "Il giudizio più equilibrato è che",
        "Al netto dell'entusiasmo iniziale,",
        "Per chi vuole sapere com'è andata davvero,",
        "Nella sostanza,",
        "Il quadro reale dice che",
        "Togliendo l'alone romantico dell'acquisto,",
        "Per dirla tutta,",
        "Senza voler impressionare nessuno,",
        "La voce più critica dentro di me dice che",
        "Riducendo tutto all'essenziale,",
        "Con i piedi ben saldi,",
        "Senza romanticherie,",
        "Il verdetto pratico è che",
        "Fuori dall'emozione del primo utilizzo,",
    ],

    # 49x — apertura con ":" seguito da "ha ..."
    "Qui la cosa che funziona è l'equilibrio:": [
        "Il punto di forza è l'armonia complessiva:",
        "L'aspetto che convince davvero è il bilanciamento:",
        "Ciò che regge tutto è la proporzione:",
        "Il segreto di questo pezzo è l'equilibrio tra le parti:",
        "La chiave è la coerenza visiva:",
        "Il valore aggiunto sta nell'armonia generale:",
        "Ciò che fa la differenza è il bilanciamento formale:",
        "Il motivo per cui funziona è la proporzione:",
        "Il punto centrale è l'armonia tra i dettagli:",
        "Quello che tiene insieme tutto è l'equilibrio:",
        "La forza sta nella coerenza del disegno:",
        "Il nucleo del progetto è la proporzione:",
        "La ragione del successo è l'armonia delle parti:",
        "Il cardine del design è il bilanciamento:",
        "Ciò che sorprende è la coerenza d'insieme:",
        "Il trait d'union tra le scelte è l'equilibrio:",
        "Il cuore del progetto è la proporzione studiata:",
        "Il fattore decisivo è l'armonia generale:",
        "La qualità più evidente è il bilanciamento dei pesi:",
        "Il valore di questo frame è la sua coerenza:",
        "Il principio costruttivo che emerge è l'equilibrio:",
        "Il fulcro visivo è la proporzione:",
        "Il colpo d'occhio è governato dall'armonia:",
        "Il dettaglio che più colpisce è la coerenza:",
        "Il punto su cui il designer ha puntato è l'armonia:",
        "Il filo conduttore è l'equilibrio formale:",
        "Ciò che rende il tutto convincente è la proporzione:",
        "L'aspetto più riuscito è la coerenza stilistica:",
        "La nota vincente è il bilanciamento dei volumi:",
        "Il progetto regge grazie all'armonia tra le parti:",
        "Il pregio principale è la proporzione d'insieme:",
        "Quello che più sorprende è la coerenza globale:",
        "Il trait d'union è l'equilibrio visivo:",
        "L'elemento che fa girare la testa è la proporzione:",
        "Il fattore che lega tutto è l'armonia:",
        "La vera riuscita sta nel bilanciamento dei componenti:",
        "Il principio guida è chiaramente la proporzione:",
        "Il valore percepito nasce dall'armonia generale:",
        "La base di tutto è la coerenza costruttiva:",
        "Il punto di forza che emerge è l'armonia formale:",
        "La chiave di lettura è il bilanciamento dei volumi:",
        "Il trait d'union tra le scelte visive è la proporzione:",
        "Il meccanismo che funziona è l'armonia d'insieme:",
        "L'elemento unificante è il bilanciamento studiato:",
        "La forza del progetto è la coerenza delle forme:",
        "Il dato più evidente è il bilanciamento visivo:",
        "Ciò che convince senza riserve è la proporzione:",
        "L'elemento portante è l'armonia delle linee:",
        "Il punto di attrazione è la coerenza del tutto:",
        "La nota dominante è il bilanciamento coerente:",
        "Il segreto è nell'armonia silenziosa tra le parti:",
    ],

    # 49x
    "ha tirato fuori una personalità più matura di quanto": [
        "ha rivelato una profondità caratteriale superiore a quanto",
        "ha mostrato una dimensione più adulta di quanto",
        "ha fatto emergere una maturità inaspettata rispetto a quanto",
        "ha espresso un carattere più definito di quanto",
        "ha portato in superficie una personalità più ricca di quanto",
        "ha sviluppato una presenza più sofisticata di quanto",
        "ha dimostrato una solidità caratteriale maggiore di quanto",
        "ha lasciato intravedere uno spessore più marcato di quanto",
        "ha prodotto un'impressione più raffinata di quanto",
        "ha costruito un'identità più complessa di quanto",
        "ha manifestato una presenza più decisa di quanto",
        "ha espresso una personalità più articolata di quanto",
        "ha rivelato sfaccettature caratteriali più profonde di quanto",
        "ha fatto trasparire una dimensione adulta superiore a quanto",
        "ha generato un'aura più definita di quanto",
        "ha sviluppato una personalità più stratificata di quanto",
        "ha mostrato una faccia più seria e consapevole di quanto",
        "ha trasmesso una maturità visiva superiore a quanto",
        "ha portato con sé una personalità più forte di quanto",
        "ha disvelato una complessità di fondo superiore a quanto",
        "ha rivelato un carattere più solido di quanto",
        "ha fatto capire uno spessore espressivo maggiore di quanto",
        "ha comunicato una presenza più decisa e strutturata di quanto",
        "ha lasciato emergere un lato più consapevole di quanto",
        "ha mostrato una stabilità identitaria superiore a quanto",
        "ha prodotto un carattere più sfaccettato di quanto",
        "ha trasmesso una profondità di linguaggio maggiore di quanto",
        "ha costruito un'immagine più adulta e definita di quanto",
        "ha espresso uno stile più costruito di quanto",
        "ha rivelato una voce stilistica più forte di quanto",
        "ha lasciato trasparire una personalità più piena di quanto",
        "ha comunicato uno spessore identitario superiore a quanto",
        "ha fatto emergere una maturità formale maggiore di quanto",
        "ha portato in luce una complessità stilistica superiore a quanto",
        "ha manifestato una personalità più ricca e articolata di quanto",
        "ha tradotto in immagine un carattere più profondo di quanto",
        "ha espresso una dimensione più matura di quanto",
        "ha fatto capire una complessità stilistica superiore a quanto",
        "ha trasmesso uno spessore caratteriale maggiore di quanto",
        "ha rivelato una presenza più solida di quanto",
        "ha mostrato un carattere più complesso e stratificato di quanto",
        "ha sviluppato una personalità visiva più piena di quanto",
        "ha portato con sé uno stile più elaborato di quanto",
        "ha lasciato intravedere una ricchezza espressiva superiore a quanto",
        "ha costruito un'identità più profonda e sfaccettata di quanto",
        "ha rivelato una maturità stilistica superiore a quanto",
        "ha trasmesso una caratterizzazione più forte di quanto",
        "ha fatto emergere un profilo espressivo più definito di quanto",
        "ha generato un'impressione di maggior spessore rispetto a quanto",
        "ha comunicato una personalità più complessa e radicata di quanto",
        "ha mostrato una profondità d'identità superiore a quanto",
    ],

    # 47x
    "ha confermato il suo carattere senza diventare": [
        "ha ribadito la sua identità senza trasformarsi in",
        "ha difeso la sua personalità senza scivolare in",
        "ha mantenuto la sua essenza senza cadere in",
        "ha conservato il suo tono senza virare verso",
        "ha preservato il suo stile senza degenerare in",
        "ha tenuto il punto senza cedere a",
        "ha rafforzato la sua voce senza esagerare fino a",
        "ha confermato la sua direzione senza eccedere in",
        "ha ribadito la sua cifra stilistica senza perdere equilibrio e diventare",
        "ha riaffermato la sua impronta senza scivolare in",
        "ha tenuto fede al suo carattere senza diventare assurdamente",
        "ha salvaguardato la sua unicità senza spingersi verso",
        "ha rispettato la sua anima stilistica senza imboccare la strada di",
        "ha sostenuto la sua identità senza cedere alla tentazione di diventare",
        "ha nutrito la propria personalità senza trasformarla in",
        "ha affermato sé stesso senza degenerare in",
        "ha difeso il proprio territorio senza invadere quello del",
        "ha tenuto la rotta senza finire nel",
        "ha riconfermato la sua natura senza slittare verso",
        "ha custodito la sua cifra senza esasperarla fino a diventare",
        "ha mantenuto la sua direzione senza virare bruscamente verso",
        "ha preservato la sua coerenza senza irrigidirsi in",
        "ha confermato il percorso senza tradirsi diventando",
        "ha ribadito la propria voce senza mutarsi in",
        "ha serbato la sua identità senza tracimare nel",
        "ha sostenuto il suo carattere senza eccedere fino a",
        "ha consolidato la propria impostazione senza irrigidirsi diventando",
        "ha rispettato la propria natura senza spingersi nel territorio del",
        "ha mantenuto la propria rotta senza diventare eccessivamente",
        "ha confermato la sua personalità senza cedere alla tentazione del",
        "ha difeso la sua posizione senza trasformare la forza in",
        "ha consolidato il suo tono senza virare nel",
        "ha ribadito la propria cifra senza tradire sé stesso diventando",
        "ha salvaguardato il proprio stile senza cadere nel compromesso del",
        "ha riaffermato la propria anima senza eccedere nel",
        "ha tenuto saldo il proprio carattere senza esasperarlo in",
        "ha riconfermato il proprio profilo senza degenerare in",
        "ha mantenuto la propria unicità senza slittare in",
        "ha preservato la propria identità visiva senza diventare banalmente",
        "ha difeso la propria impronta senza spingerla al punto da diventare",
        "ha conservato la propria direzione stilistica senza trasformarla in",
        "ha riaffermato la propria posizione senza cadere in",
        "ha consolidato il proprio profilo senza sbandare verso",
        "ha tenuto fede alla propria visione senza degenerare in",
        "ha mantenuto la propria prospettiva senza eccedere fino a diventare",
        "ha ribadito la propria impostazione senza cedere al",
        "ha preservato la propria essenza senza trasformarla in qualcosa di",
    ],

    # 47x
    "ha funzionato soprattutto nel passaggio dal tavolo al": [
        "ha brillato soprattutto nella transizione dalla scrivania al",
        "ha reso il meglio di sé nel cambio di contesto dalla riunione al",
        "ha trovato il suo momento migliore nel salto dal lavoro al",
        "ha dimostrato la sua versatilità nel passare dall'ufficio al",
        "si è distinto soprattutto nel bridge tra l'ambiente formale e il",
        "ha convinto nel momento del cambio tra la riunione e il",
        "ha espresso il massimo nel transito dall'ambiente professionale al",
        "ha reso al meglio nel cambio dalla scrivania verso il",
        "ha sorpreso nella fase di transizione dal contesto lavorativo al",
        "ha mostrato il suo valore nel passaggio dal formale al",
        "ha eccelluto nel momento critico della transizione professione-",
        "ha guadagnato punti nel salto tra il vestito da lavoro e il",
        "ha funzionato al meglio nel bridge tra l'ambiente controllato e il",
        "ha trovato la sua dimensione nel cambio di registro dall'ufficio al",
        "ha reso nella transizione dall'ambiente professionale a quello del",
        "ha sorpreso nella versatilità mostrata nel passaggio dall'ufficiale al",
        "ha brillato nel salto di registro tra il contesto lavorativo e il",
        "ha convinto nel bridge tra l'uso formale e il mondo del",
        "ha mostrato carattere nel passaggio dall'abito formale al look del",
        "ha guadagnato credibilità nel cambio dal contesto business al",
        "ha risposto bene nel salto tra la scrivania e il",
        "ha retto ottimamente la transizione dall'ufficio al",
        "si è adattato senza sbavature nel passaggio formale-",
        "ha conservato coerenza nel cambio dal professionale al",
        "ha mantenuto la sua identità nel salto tra il lavoro e il",
        "ha dimostrato flessibilità nel cambio di registro verso il",
        "ha passato senza problemi il test della transizione professione-",
        "ha convinto nel passare dall'ambiente strutturato al",
        "ha espresso il meglio di sé nel bridge tra l'ufficio e il",
        "ha funzionato egregiamente nel salto tra il formale e il",
        "ha risposto con coerenza nel transito dalla scrivania al",
        "ha brillato nel cambio di contesto dal professionale al",
        "ha retto bene il range dall'ambiente lavorativo al",
        "ha dimostrato di essere all'altezza nel passaggio ufficiale-",
        "ha mostrato versatilità concreta nel salto dal lavoro al",
        "ha conquistato sul campo nella transizione dal lavoro al",
        "ha reso al meglio del suo potenziale nel bridge lavoro-",
        "ha confermato la sua utilità nel cambio di contesto verso il",
        "ha tenuto bene nel passaggio dall'abito da lavoro al look del",
        "ha mantenuto la sua energia nel transito dall'ufficio al",
        "ha dimostrato carattere nel bridge tra professione e",
        "ha convinto in pienezza nel cambio dell'ambiente lavorativo verso il",
        "ha retto la prova nel passaggio tra il vestito da lavoro e il",
        "ha trovato la sua misura nel salto dal contesto professionale al",
        "ha reso nel cambio di registro tra il formale quotidiano e il",
        "ha risposto alla grande nel transito dall'ufficio alla",
        "ha brillato nell'uso duale tra il professionele e il",
    ],

    # 47x
    "ha mostrato un equilibrio che in foto non avevo capito fino in fondo": [
        "ha rivelato un'armonia che le immagini non riuscivano a trasmettere del tutto",
        "ha mostrato una coerenza che dagli scatti non era ancora percepibile a pieno",
        "ha espresso un bilanciamento che la fotografia non rende fino in fondo",
        "ha svelato una proporzione che le foto non comunicavano in modo completo",
        "ha trasmesso un equilibrio di forme che gli scatti non catturavano appieno",
        "ha rivelato un'armonia visiva che solo dal vivo diventa leggibile",
        "ha dimostrato una coerenza che guardando le immagini non avevo compreso",
        "ha fatto capire un bilanciamento che dalla scheda prodotto non emerge",
        "ha manifestato una proporzione che la foto piana non riesce a mostrare",
        "ha mostrato un'armonia che le immagini statiche non possono comunicare",
        "ha rivelato uno spessore che gli scatti frontali non restituiscono",
        "ha dimostrato un bilanciamento che le foto non trasmettono fedelmente",
        "ha espresso una proporzione che il rendering non cattura interamente",
        "ha fatto emergere un equilibrio che guardando le immagini avevo sottostimato",
        "ha svelato una coerenza che la fotografia ufficiale non riesce a rendere",
        "ha mostrato un'armonia che sulla carta sembrava impossibile da capire",
        "ha rivelato una proporzione che gli scatti promo non comunicavano",
        "ha dimostrato un equilibrio visivo che dagli screenshot non si intuiva",
        "ha fatto vedere un bilanciamento che le immagini di catalogo nascondono",
        "ha espresso una coerenza formale che le foto non trasmettevano",
        "ha svelato un'armonia che il monitor non riesce a rendere completamente",
        "ha mostrato una proporzione che online non si percepisce a fondo",
        "ha rivelato un equilibrio che le foto pubblicitarie non catturano",
        "ha dimostrato una coerenza che gli scatti promo appiattiscono",
        "ha fatto capire un bilanciamento che le immagini digitali penalizzano",
        "ha trasmesso un equilibrio che le foto da catalogo non sanno rendere",
        "ha rivelato un'armonia delle parti che andava toccata per essere capita",
        "ha fatto emergere una proporzione che solo dal vivo risalta",
        "ha mostrato un bilanciamento che sullo schermo non si vedeva",
        "ha svelato un equilibrio che le immagini promozionali sacrificavano",
        "ha espresso una coerenza formale che la fotografia flat nascondeva",
        "ha rivelato un'armonia che nelle foto sembrava quasi banale",
        "ha dimostrato una proporzione che le immagini di prodotto non comunicano",
        "ha fatto capire un equilibrio che dal preview online era invisibile",
        "ha mostrato una coerenza che guardando gli scatti non avrei detto",
        "ha svelato un'armonia che solo l'uso reale poteva mostrare",
        "ha rivelato una proporzione che le foto a uso commerciale non colgono",
        "ha espresso un bilanciamento che dalle immagini era difficile intuire",
        "ha dimostrato un equilibrio che le foto di sistema non trasmettono",
        "ha fatto emergere una coerenza che gli scatti professionali non catturano",
        "ha mostrato un'armonia che il monitor tendeva a svilire",
        "ha svelato un bilanciamento che guardando il sito non avevo valutato",
        "ha rivelato una proporzione che le foto ufficiali non restituiscono",
        "ha espresso una coerenza che andava vista dal vivo per essere apprezzata",
        "ha dimostrato un equilibrio che era nascosto nelle foto di presentazione",
        "ha fatto capire un bilanciamento che le immagini di anteprima schiacciavano",
        "ha mostrato un'armonia che solo indossandolo si riesce a cogliere appieno",
        "ha svelato una coerenza visiva che le foto bidimensionali non possono replicare",
        "ha rivelato un equilibrio che dal catalogo digitale non si percepiva",
        "ha espresso una proporzione che il display non rende com'è nella realtà",
        "ha dimostrato una coerenza che le foto da studio nascondevano parzialmente",
    ],

}

# ════════════════════════════════════════════════════════════════════
# CARICA E AGGIORNA IL DB
# ════════════════════════════════════════════════════════════════════

print("Connessione al DB...")
conn = psycopg2.connect(DATABASE_URL)
cur = conn.cursor()

print("Download tutte le recensioni...")
cur.execute("SELECT id, body, stars FROM reviews ORDER BY id")
rows = cur.fetchall()
print(f"Recensioni caricate: {len(rows)}")

# Per ogni pattern, traccia l'indice di occorrenza globale
pattern_occurrence = {p: 0 for p in FINAL_FIXES}

changes = []

for row_id, body, stars in rows:
    new_body = body
    changed = False

    for pattern, alternatives in FINAL_FIXES.items():
        if pattern not in new_body:
            continue

        # Conta quante volte appare nel testo
        count = new_body.count(pattern)
        for _ in range(count):
            if pattern not in new_body:
                break
            idx = pattern_occurrence[pattern] % len(alternatives)
            replacement = alternatives[idx]
            pattern_occurrence[pattern] += 1
            new_body = new_body.replace(pattern, replacement, 1)
            changed = True

    if changed and new_body != body:
        changes.append((new_body, row_id))

print(f"\nRecensioni da aggiornare: {len(changes)}")

# Applica in batch da 50
BATCH_SIZE = 50
applied = 0
errors = 0
batch_num = 0

print("Applicazione al DB...")
for i in range(0, len(changes), BATCH_SIZE):
    batch = changes[i:i+BATCH_SIZE]
    batch_num += 1
    try:
        for new_body, row_id in batch:
            cur.execute("UPDATE reviews SET body = %s WHERE id = %s", (new_body, row_id))
        conn.commit()
        applied += len(batch)
        print(f"  Batch {batch_num:2d}: {applied}/{len(changes)} aggiornate")
    except Exception as e:
        conn.rollback()
        errors += len(batch)
        print(f"  ERRORE batch {batch_num}: {e}")

cur.close()
conn.close()

print(f"\n{'='*50}")
print(f"Aggiornate: {applied} | Errori: {errors}")
for p, cnt in pattern_occurrence.items():
    print(f"  '{p[:50]}...' → {cnt} sostituzioni")
print("✅ Fix finale completato!" if errors == 0 else f"⚠️ {errors} errori.")
