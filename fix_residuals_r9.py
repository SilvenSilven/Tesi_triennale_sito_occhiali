#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fix round 9 — tutte le 17 frasi complete con >=10x."""

import psycopg2

DATABASE_URL = (
    "postgresql://neondb_owner:npg_uFxVSRoTj95w"
    "@ep-damp-sea-anvn4fw4.c-6.us-east-1.aws.neon.tech"
    "/neondb?sslmode=require"
)

PATTERNS = {

    # 27x
    "Lo promuovo, pur senza idealizzarlo.": [
        "Lo apprezzo, senza esagerarne i pregi.",
        "Lo tengo in buona considerazione, con qualche riserva.",
        "Lo promuovo con una menzione di merito parziale.",
        "Lo valuto positivamente, senza esaltarlo.",
        "Gli riconosco i meriti, senza eccedere.",
        "Lo promuovo a titolo meritato, non entusiastico.",
        "Lo considero buono, non eccezionale.",
        "Lo apprezzo con senso della misura.",
        "Mi piace senza che mi faccia perdere la testa.",
        "Lo promuovo con una stima pacata.",
        "Lo giudico positivo, pur mantenendo una posizione critica.",
        "Lo apprezzo razionalmente, senza infatuarmi.",
        "Lo confermo come acquisto valido, con un asterisco.",
        "Lo valuto bene, tenendo i piedi per terra.",
        "Lo promuovo, con la lucidità di chi resta distaccato.",
        "Lo giudico positivo, non definitivo.",
        "Lo apprezzo per quello che è, senza attribuirgli di più.",
        "Lo promuovo, restando consapevole dei suoi limiti.",
        "Lo considero una scelta solida, non un capolavoro.",
        "Lo approvo con una certa compostezza.",
        "Gli do una valutazione soddisfacente, non esaltata.",
        "Lo promuovo, mantenendo le aspettative calibrate.",
        "Lo giudico positivamente, con la dovuta sobrietà.",
        "Lo considero degno di acquisto, senza incenso.",
        "Lo valuto bene, ma con criterio.",
        "Lo promuovo a piena coscienza dei suoi limiti.",
        "Lo apprezzo, rimanendo ancorato alla realtà.",
        "Lo considero un buon acquisto, non un'esperienza memorabile.",
        "Lo promuovo — senza farne un elogio eccessivo.",
    ],

    # 19x
    "Hanno una presenza che non dipende dal logo o dall'effetto moda del momento.": [
        "Comunicano qualcosa di concreto senza appoggiarsi al brand o alla tendenza.",
        "La loro personalità non richiede etichette per farsi sentire.",
        "Non hanno bisogno della firma o del momento per essere riconoscibili.",
        "La loro identità è autonoma dalla moda e dal marchio visibile.",
        "Parlano per sé senza contare sul logo o sull'onda del momento.",
        "Il loro carattere non dipende dall'effetto stagione.",
        "Non si appoggiano al brand: la forma parla da sola.",
        "Sono riconoscibili per quello che sono, non per dove viene scritto il nome.",
        "Non si avvalgono della tendenza: il progetto è sufficiente.",
        "La loro forza non viene da un marchio in evidenza o da una moda passeggera.",
        "Non richiedono una griffe per avere senso: si reggono da soli.",
        "Fanno a meno della tendenza per risultare interessanti.",
        "Il loro peso estetico non è delegato al logo o al momento culturale.",
        "Portano la loro presenza senza bisogno di una tendenza a supportarli.",
        "Hanno una voce che non chiede amplificazione esterna.",
        "La loro identità non dipende da validazioni esterne come la moda o la firma.",
        "Non chiedono aiuto a nessuna tendenza: la forma è già tutto.",
        "Non vivono di moda: hanno fondamenta proprie.",
        "Il design è sufficiente: non serve il momento per capirli.",
        "Hanno dignità propria, senza appoggiarsi al codice di stagione.",
    ],

    # 18x
    "Mi lascia con più rispetto che entusiasmo.": [
        "Mi lascia con più stima che emozione.",
        "Ne esco con più considerazione che calore.",
        "Mi lascia più ammirato che coinvolto.",
        "Il bilancio è intellettuale più che emotivo.",
        "Mi lascia con più apprezzamento che passione.",
        "Ne esco con più rispetto che affetto.",
        "Mi lascia con più riconoscimento che slancio.",
        "Mi lascia più lucido che entusiasta.",
        "Il risultato è una stima fredda, non un'adesione calda.",
        "Ne esco con un giudizio positivo ma distante.",
        "Mi lascia con più distinzione che trasporto.",
        "Ne esco con più cognizione che calore.",
        "Mi lascia più capace di apprezzarlo che di amarlo.",
        "Il giudizio è positivo, ma non è entusiasmo.",
        "Mi lascia con stima razionale, non passione.",
        "Ne esco più informato che conquistato.",
        "Mi lascia con un rispetto intellettuale, non un'adesione istintiva.",
        "Il mio giudizio è positivo: la mia emozione è limitata.",
        "Mi lascia capace di valutarlo, incapace di innamorarmene.",
    ],

    # 17x
    "Mi ha dato subito fiducia anche senza bisogno di abituarmi.": [
        "Mi ha conquistato senza bisogno di un periodo di adattamento.",
        "Ha costruito fiducia istantaneamente, senza rodaggio.",
        "Si è imposto naturalmente senza richiedere abitudine.",
        "Ha guadagnato la mia fiducia al primo uso, senza mediazione.",
        "Non ho avuto bisogno di un periodo di adattamento: si è imposto subito.",
        "La fiducia è arrivata immediatamente, senza richiedere tempo.",
        "Ha detto la sua al primo tentativo senza bisogno di supporto.",
        "Si è conquistato la mia stima senza rodaggio preliminare.",
        "Non ha richiesto nessuna fase di adattamento: ha funzionato al primo colpo.",
        "Ha risposto bene fin dal primo momento, senza bisogno di aspettare.",
        "Ha guadagnato la fiducia in modo naturale, senza richiedere alcun test.",
        "Ha ottenuto il mio consenso immediatamente, senza dover essere 'imparato'.",
        "Non ho dovuto aspettare: si è fatto valere al primo utilizzo.",
        "Ha convinto senza traversie iniziali.",
        "La sintonia è arrivata subito, senza adattamenti.",
        "Non ha rinchiuso la sua qualità in una curva di apprendimento.",
        "Ha preso forza immediata, senza dover essere indossato a lungo per convincere.",
        "Ha trovato la sua collocazione nel primo uso senza incertezze.",
    ],

    # 16x
    "Il risultato finale è buono, purché gli si conceda il terreno adatto.": [
        "Il bilancio è soddisfacente, a condizione di usarlo nel contesto giusto.",
        "Il risultato è positivo, a patto di sceglierlo con consapevolezza.",
        "Il prodotto funziona bene, se si rispetta la sua vocazione.",
        "Il giudizio finale è buono, con un 'se' importante: il contesto giusto.",
        "La valutazione è positiva, purché si conosca il suo ambito d'uso.",
        "La conclusione è buona, con la condizione di non impiegarlo fuori contesto.",
        "Il risultato è convincente, se lo si mette in mano alla situazione giusta.",
        "Il prodotto regge bene, purché non si chieda più di quello che sa dare.",
        "La riuscita è piena, a patto di rispettarne le condizioni naturali.",
        "Il risultato è buono, con la condizione implicita di un utilizzo adatto.",
        "Il giudizio è positivo, ma con una clausola: il contesto corretto.",
        "Il bilancio complessivo è ottimo, se si rispetta la sua destinazione.",
        "Il prodotto è riuscito, purché inserito nel suo ambiente ideale.",
        "Il risultato parla bene di sé, se si rispetta il terreno d'uso.",
        "La valutazione è solida, con la clausola del contesto opportuno.",
        "Il bilancio è favorevole, a patto di non forzarne l'utilizzo.",
        "La riuscita è alta, purché si conosca quando e come indossarlo.",
    ],

    # 16x
    "Non è perfetto, ma ha abbastanza qualità da farsi scegliere spesso.": [
        "Non è impeccabile, ma vale la pena tenerlo nella rotazione.",
        "Non è senza difetti, ma ha abbastanza da giustificarne l'uso.",
        "Non è irreprensibile, ma si fa scegliere con regolarità.",
        "Non è il migliore in assoluto, ma tra i più usati che ho.",
        "Non è privo di limiti, ma li sopporta bene grazie ai suoi punti forti.",
        "Non è il top, ma le qualità bastano a renderlo frequente.",
        "Non è perfetto: ha però abbastanza per finire sopra gli altri.",
        "Non è senza riserve, ma le sue qualità superano i difetti.",
        "Non è il modello dei sogni, ma vive bene nella mia rotazione.",
        "Non brilla per perfezione, ma è abbastanza buono da sceglierlo spesso.",
        "Non è inappuntabile, ma è abbastanza solido da essere usato regolarmente.",
        "Non è esente da difetti, ma non abbastanza da farlo scalare nella lista.",
        "Non eccelso, ma con abbastanza pregi per restare sul tavolo.",
        "Non è il numero uno, ma si difende bene e finisce addosso spesso.",
        "Non è senza sbavature, ma ha abbastanza sostanza da risultare frequente.",
        "Non è un prodotto perfetto, ma è un prodotto che funziona.",
        "Non è eccezionale, ma ha qualità sufficienti per essere una scelta regolare.",
    ],

    # 15x
    "La delusione non è totale, ma è abbastanza da fermarmi.": [
        "Non è una delusione completa, ma è sufficiente a fermare l'entusiasmo.",
        "Non è un flop totale, ma la delusione è abbastanza per rimanere cauta.",
        "Non è un disastro, ma la delusione è reale e concreta.",
        "Non è tutto sbagliato, ma quanto basta per non andare avanti con convinzione.",
        "Non mi ha deluso del tutto, ma abbastanza da fermare l'intenzione di tenerli.",
        "Non è un insuccesso completo, ma la delusione supera la tolleranza.",
        "Non è totalmente negativo, ma la delusione è abbastanza significativa.",
        "Non è totale il fallimento, ma la delusione è abbastanza concreta.",
        "Non mi ha deluso completamente, ma abbastanza da riesaminare la scelta.",
        "Non è un acquisto da buttar via, ma la delusione supera il recuperabile.",
        "Non è tutto perduto, ma la delusione ha già preso troppo spazio.",
        "Non è un rifiuto netto, ma la delusione è abbastanza per rallentare.",
        "Non mi ha convinto fino in fondo, e la delusione è reale.",
        "Non è una bocciatura totale, ma la delusione pesa abbastanza.",
        "Non è un disastro irreparabile, ma la delusione è tangibile.",
        "Non è priva di meriti, ma la delusione prevale.",
    ],

    # 14x
    "Rimane una promessa che sul mio viso non si compie.": [
        "Resta un'idea interessante che sul mio profilo non si realizza.",
        "Rimane un progetto promettente che non riesce a compiersi con me.",
        "È una proposta convincente che sul mio viso perde forza.",
        "Rimane un design che ha del potenziale ma non si completa con il mio viso.",
        "È un prodotto che promette ma non mantiene, almeno per me.",
        "Rimane qualcosa di intrigante che sul mio profilo non si chiude bene.",
        "È una bella idea che non trova esecuzione sul mio viso.",
        "Rimane un progetto aperto che con me non raggiunge la conclusione.",
        "È una promessa di stile che con il mio viso rimane irrisolta.",
        "Rimane un acquisto che avrebbe potuto essere molto più di quello che è stato.",
        "È un prodotto che poteva essere il mio: non ci è riuscito.",
        "Rimane un design che sul mio viso si arresta prima del traguardo.",
        "È una proposta che non trova compimento sul mio profilo.",
        "Rimane una possibilità non realizzata, almeno per la mia morfologia.",
        "È un prodotto che allude a qualcosa che non arriva a fare.",
    ],

    # 14x
    "Peccato, perché il progetto aveva elementi interessanti.": [
        "Un peccato, perché l'idea di fondo era promettente.",
        "È un dispiacere, dato che la base di partenza era interessante.",
        "Spiacevole, considerando che il disegno di base aveva del potenziale.",
        "Un peccato, perché il proposito stilistico era attraente.",
        "Nella scheda c'era qualcosa di intrigante: peccato che non sia arrivato.",
        "La premessa era valida: il risultato non è stato all'altezza.",
        "Peccato, il punto di partenza era promettente.",
        "Un dispiacere, perché la concezione mostrava idee interessanti.",
        "È un peccato: il progetto iniziale aveva radici solide.",
        "L'idea di partenza era buona: la realizzazione ha mancato il segno.",
        "Peccato davvero: il progetto partiva da premesse interessanti.",
        "La base aveva qualità: peccato per l'esito.",
        "Spiacevole: l'impostazione aveva del merito.",
        "Il concept aveva valore: l'esecuzione lo ha limitato.",
        "C'era del potenziale: non è stato sfruttato pienamente.",
    ],

    # 13x
    "Finisce tra i paia che guardo più di quanto indossi.": [
        "Finisce nella categoria 'belle da vedere, difficili da portare'.",
        "Finisce nella pila degli occhiali che guardo ma non indosso.",
        "Entra a far parte dei pezzi che ammiro più che utilizzare.",
        "Va a unirsi ai modelli che restano in cassetto più che sul viso.",
        "Diventa uno di quei pezzi che ho ma che non uso.",
        "Finisce nell'elenco degli acquisti che tengo senza portare.",
        "Si aggiunge ai pezzi che appartengono alla mia raccolta ma non alla mia faccia.",
        "Prende posto tra i modelli che esistono per il mio sguardo, non per il mio viso.",
        "Finisce nel gruppo 'ci sono ma non li uso'.",
        "Diventa un oggetto da guardare più che da indossare.",
        "Passa nella lista degli acquisti che non trovano spazio nella rotazione attiva.",
        "Si unisce ai pezzi che ho smesso di considerare opzioni reali.",
        "Finisce ai margini della rotazione, più ammirato che portato.",
        "Entra nel limbo degli acquisti che restano senza utilizzo.",
    ],

    # 13x
    "Per me è stato un acquisto sbagliato.": [
        "Con il senno di poi, non avrei dovuto prenderli.",
        "Guardandolo a distanza, è stato un errore di valutazione.",
        "Devo ammetterlo: non era l'acquisto giusto per me.",
        "A posteriori, è stato un acquisto che avrei evitato.",
        "Non è andata bene: è stato un acquisto fuori target.",
        "L'onestà vuole che io ammetta che non era il prodotto giusto.",
        "Se potessi tornare indietro, avrei scelto diversamente.",
        "Non era quello che serviva: l'acquisto è stato sbagliato.",
        "Rivedendo la scelta, è stato un errore.",
        "Non ha funzionato per me: l'acquisto non era allineato ai miei bisogni.",
        "Con il trascorrere del tempo, è diventato chiaro che era un acquisto errato.",
        "L'esperienza mi ha dimostrato che non era la scelta giusta.",
        "Non era adatto a me: l'acquisto va classificato come sbagliato.",
        "Ammetto l'errore: non era il modello giusto per me.",
    ],

    # 13x
    "La distanza tra come li immaginavo e come mi stanno è stata ampia.": [
        "Il divario tra le aspettative e la realtà sul viso è stato notevole.",
        "L'aspettativa e il risultato erano molto distanti.",
        "Tra come li immaginavo e come mi stanno c'è stato un gap significativo.",
        "La differenza tra l'atteso e il reale è stata grande.",
        "L'immaginato e il vissuto non si sono incontrati bene.",
        "Aspettativa e realtà si sono trovate su binari diversi.",
        "Il contrasto tra l'immagine che avevo in testa e il risultato è stato forte.",
        "Le aspettative erano alte; la realtà sul viso ha ridimensionato tutto.",
        "Tra come pensavo stessero e come mi stanno davvero c'è stata una bella distanza.",
        "Ho trovato un disallineamento tra le mie aspettative e il risultato concreto.",
        "Quello che mi aspettavo e quello che ho ottenuto erano molto diversi.",
        "La proporzione tra attesa e realtà non era quella che speravo.",
        "Le mie aspettative e il risultato finale si sono scontrati.",
        "Aspettative e realtà hanno viaggiato su strade separate.",
    ],

    # 12x
    "Per il mio uso quotidiano i compromessi sono troppi.": [
        "Nei contesti che frequento ogni giorno, i limiti pesano troppo.",
        "Per come li uso ogni giorno, i punti deboli finiscono per dominare.",
        "Nella mia routine, le rinunce richieste superano il valore del prodotto.",
        "Per il mio stile di vita, i compromessi da accettare sono eccessivi.",
        "Nell'uso quotidiano che faccio, i margini di criticità sono troppo alti.",
        "Per la mia tipologia di utilizzo, le limitazioni si sommano fino a pesare.",
        "Per il mio ritmo quotidiano, i problemi che portano sono troppi.",
        "Nell'uso che ho bisogno di farne ogni giorno, le riserve si moltiplicano.",
        "Per come li vivo ogni giorno, i difetti occupano troppo spazio.",
        "Nella mia giornata tipo, i compromessi che impongono sono insostenibili.",
        "Per come li uso io, gli aspetti negativi finiscono per prevalere.",
        "Nell'uso real-life, le concessioni richieste sono davvero troppe.",
        "Per il mio modo di indossarli, le limitazioni superano il beneficio.",
    ],

    # 11x
    "Io con questo paio ho chiuso presto.": [
        "Ho smesso di usarli prima del previsto.",
        "Con questo modello la storia è finita in fretta.",
        "Li ho accantonati prima di averli davvero conosciuti.",
        "L'avventura con questo paio si è conclusa rapidamente.",
        "Ho rinunciato a loro in tempi piuttosto brevi.",
        "Li ho abbandonati senza cercare di convincermi.",
        "Non ho insistito: ho deciso di lasciar perdere presto.",
        "La convivenza con loro è durata poco.",
        "Ho smesso di portarli prima di qualsiasi forma di abitudine.",
        "Ne ho preso congedo rapidamente.",
        "Li ho messi da parte senza rimpianti e in poco tempo.",
        "Non ho aspettato a lungo prima di passare oltre.",
    ],

    # 11x
    "Quando la calzata non gira, tutto il resto perde peso in fretta.": [
        "Se il comfort non c'è, ogni altra qualità vale meno.",
        "Quando la vestibilità è sbagliata, il design perde rilevanza.",
        "Una calzata scorretta mette fuori gioco anche i migliori pregi.",
        "Se la vestibilità non va, tutto il resto conta poco.",
        "Quando la calzata è un problema, nessun'altra qualità compensa.",
        "Se non calzano bene, anche la bellezza smette di importare.",
        "Quando la portabilità è compromessa, il giudizio cambia in fretta.",
        "Una calzata sbagliata pesa più di qualsiasi valore estetico.",
        "Quando il fitting non funziona, niente altro riesce a salvare il prodotto.",
        "Se non stanno bene, i punti di forza diventano irrilevanti.",
        "Una vestibilità precaria annulla i pregi con rapidità.",
        "Quando la calzata non è giusta, è difficile apprezzare il resto.",
    ],

    # 10x
    "L'estetica da sola, qui, non mi basta a salvarli.": [
        "La bellezza visiva, da sola, non è sufficiente per tenerli.",
        "L'aspetto non riesce, qui, a compensare i punti deboli.",
        "L'estetica non salva da sola: ha bisogno di altri argomenti.",
        "Solo la forma non basta: qui non c'è abbastanza sostanza.",
        "L'attrattiva visiva non supera le riserve pratiche.",
        "La bellezza del disegno non è argomento sufficiente in questo caso.",
        "Qui l'estetica non riesce a fare da traino sufficiente.",
        "Il design non può sostenere da solo tutta la valutazione.",
        "L'aspetto bello non vale abbastanza da sopravanzare i difetti.",
        "La forma piacevole non compensa le debolezze in questo caso.",
        "Solo il disegno non è abbastanza: serve qualcosa di più.",
    ],

    # 10x
    "Non gli trovo un posto vero nella mia rotazione.": [
        "Non riesco a inserirli stabilmente nella mia rotazione.",
        "Non trovano una collocazione fissa tra quello che uso.",
        "Non riescono a guadagnarsi un posto stabile nel mio uso.",
        "Non li riesco a collocare davvero tra i miei occhiali attivi.",
        "Non hanno un ruolo preciso nella mia selezione quotidiana.",
        "Non rientrano mai nella scelta naturale del mattino.",
        "Non trovano spazio né nel quotidiano né nelle occasioni speciali.",
        "Non riesco a costruire un contesto in cui usarli davvero.",
        "Non hanno trovato il loro posto nella mia rotazione.",
        "Non ci sono finiti: restano al margine della rotazione.",
        "Non hanno guadagnato una collocazione stabile tra i pezzi che uso.",
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
        print(f"  '{p[:65]}' → {cnt}x")
print("✅ Round 9 completato!" if errors == 0 else f"⚠️ {errors} errori.")
