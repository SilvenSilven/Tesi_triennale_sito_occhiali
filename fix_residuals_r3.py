#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fix round 3 — pattern residui da 29-39 occorrenze."""

import psycopg2

DATABASE_URL = (
    "postgresql://neondb_owner:npg_uFxVSRoTj95w"
    "@ep-damp-sea-anvn4fw4.c-6.us-east-1.aws.neon.tech"
    "/neondb?sslmode=require"
)

PATTERNS = {

    # 39x — connettore mid-sentence introdotto dai fix precedenti
    "e adesso posso dire che ha": [
        "e posso affermare con certezza che ha",
        "e il tempo mi ha dimostrato che ha",
        "e ora posso confermare che ha",
        "e il bilancio finale dice che ha",
        "e con le settimane ho capito che ha",
        "e alla fine dei conti ha",
        "e la pratica ha confermato che ha",
        "e l'uso quotidiano ha rivelato che ha",
        "e col senno di poi ha",
        "e l'esperienza reale dice che ha",
        "e ripensandoci a mente fredda ha",
        "e nel resoconto finale ha",
        "e la realtà di tutti i giorni conferma che ha",
        "e guardando il quadro completo ha",
        "e a distanza di settimane ha",
        "e facendo la somma di tutto ha",
        "e nel complesso ha",
        "e stando ai fatti ha",
        "e il verdetto pratico è che ha",
        "e l'analisi a posteriori dice che ha",
        "e nel tempo si è visto che ha",
        "e alla prova dei fatti ha",
        "e il risultato concreto mostra che ha",
        "e in retrospettiva ha",
        "e dopo un uso prolungato ha",
        "e togliendo l'entusiasmo iniziale ha",
        "e valutando con distacco ha",
        "e il giudizio definitivo è che ha",
        "e con l'uso costante si è visto che ha",
        "e passata la fase di adattamento ha",
        "e col passare del tempo ha",
        "e nella quotidianità ha",
        "e portandolo ogni giorno ho visto che ha",
        "e con il rodaggio necessario ha",
        "e nella valutazione complessiva ha",
        "e levandomi il cappello iniziale ha",
        "e al netto dell'entusiasmo del primo momento ha",
        "e in condizioni d'uso reale ha",
        "e con occhi più critici ha",
        "e nella pratica effettiva ha",
    ],

    # 34x — apertura di frase
    "La parte migliore è che la": [
        "Il punto forte è che la",
        "Il pregio principale è che la",
        "Il meglio viene quando la",
        "La cosa che convince di più è che la",
        "Il vantaggio chiave è che la",
        "La qualità più alta emerge quando la",
        "Il punto vincente è che la",
        "Ciò che funziona meglio è che la",
        "L'aspetto più riuscito risiede nel fatto che la",
        "Il colpo da maestro è che la",
        "Quello che più sorprende è che la",
        "La nota più alta è che la",
        "Il valore aggiunto è che la",
        "L'elemento forte è che la",
        "Il momento di eccellenza è quando la",
        "Il punto di picco è che la",
        "Il fattore decisivo è che la",
        "La scelta più felice è che la",
        "Il tratto che brilla di più è che la",
        "La qualità dominante sta nel fatto che la",
        "L'aspetto che prevale su tutto è che la",
        "Il plus principale è che la",
        "La nota migliore è che la",
        "Il punto di punta è che la",
        "Il dettaglio più riuscito è che la",
        "L'elemento che spicca è che la",
        "Il cuore del progetto è che la",
        "La caratteristica più esaltante è che la",
        "Il pregio tecnico maggiore è che la",
        "La scelta che alza il livello è che la",
        "Il tratto più felice è che la",
        "Il punto che sorprende di più è che la",
        "Il valore che emerge con chiarezza è che la",
        "L'aspetto che emerge sopra gli altri è che la",
        "Il dato più positivo è che la",
    ],

    # 33x
    "Su di me funzionano bene in": [
        "Nel mio uso quotidiano si comportano al meglio in",
        "Per come indosso gli occhiali, rendono di più in",
        "Con la mia faccia e il mio stile funzionano in particolare in",
        "Sul mio viso danno il massimo in",
        "Per come li porto io vanno molto bene in",
        "Con la mia conformazione facciale si trovano a proprio agio in",
        "Nel contesto in cui li uso più spesso, rendono tantissimo in",
        "Indossandoli come faccio io, performano al meglio in",
        "Nel mio caso funzionano particolarmente bene in",
        "Con il mio stile di vita si adattano perfettamente in",
        "Per la mia routine quotidiana sono ideali in",
        "Con il mio fisico li sento meglio in",
        "Sul mio viso si esprimono al massimo in",
        "Con il mio approccio all'outfit rendono di più in",
        "Nel mio contesto di utilizzo brillano soprattutto in",
        "Con il mio tipo di viso sono al loro meglio in",
        "Li sento più miei quando li uso in",
        "Con le mie abitudini funzionano soprattutto in",
        "Con il mio guardaroba si abbinano meglio in",
        "Con la mia routine li trovo perfetti in",
        "Nella mia quotidianità rendono soprattutto in",
        "Con il mio stile personale li sento più a loro agio in",
        "Per il modo in cui vivo li uso meglio in",
        "Nel mio caso il rendimento migliore è in",
        "Con la mia tipologia di viso si adattano meglio in",
        "Per come mi muovo e mi vesto rendono di più in",
        "Con le mie abitudini vestimentarie li trovo a loro agio soprattutto in",
        "Considerato il mio stile, li sento più adatti in",
        "Per come li porto io si esprimono soprattutto in",
        "Nel mio utilizzo personale il picco di resa è in",
        "Per la mia struttura facciale il momento migliore è in",
        "Con il mio approccio stilistico danno il meglio in",
        "Nella mia esperienza di utilizzo rendono di più in",
        "Con il mio guardaroba tipico li trovo al meglio in",
    ],

    # 32x
    "Sono sincero: non siamo mai entrati in sintonia.": [
        "Non devo nasconderlo: tra noi non ha mai funzionato.",
        "Devo essere franco: non siamo mai andati d'accordo.",
        "La verità è che non abbiamo mai trovato la nostra frequenza.",
        "Senza girarci intorno: non c'è mai stato il click.",
        "Lo dico apertamente: non siamo mai stati in sintonia.",
        "Non è ipocrita dirlo: non siamo mai entrati in connessione.",
        "Per essere diretto: non ci siamo mai trovati.",
        "Devo ammetterlo: non abbiamo mai trovato il ritmo giusto insieme.",
        "Parlo chiaro: tra noi la chemistry non è mai scattata.",
        "Senza filtri: non è mai scattato qualcosa tra noi.",
        "La mia onestà vuole che dica: non siamo mai andati.",
        "Non me lo nascondo: non c'è mai stata vera sintonia.",
        "Lo riconosco apertamente: non siamo mai entrati in risonanza.",
        "Nessun giro di parole: non abbiamo mai trovato l'intesa.",
        "Devo riconoscerlo: non c'è mai stato il giusto feeling.",
        "Senza ipocrisie: non siamo mai stati davvero in sintonia.",
        "È onesto dirlo: non abbiamo mai trovato l'accordo.",
        "Lo ammetto senza riserve: tra noi non c'è mai stata intesa.",
        "Parlando senza veli: non si è mai creata la connessione.",
        "Non voglio mentire: non siamo mai stati allineati.",
        "Va detto: non siamo mai stati sulla stessa lunghezza d'onda.",
        "Senza edulcorare: non abbiamo mai costruito un rapporto.",
        "Non c'è modo carino per dirlo: tra noi non ha mai funzionato.",
        "Lo dico con rispetto ma con chiarezza: non ci siamo mai capiti.",
        "La sintesi è questa: non c'è mai scattato nulla.",
        "Per rispetto della verità: non abbiamo mai trovato la nostra frequenza.",
        "Non mi illudo: tra noi non c'è mai stata vera sintonia.",
        "Parlo liberamente: la connessione non è mai nata.",
        "Non giro intorno alla cosa: tra noi non è mai funzionato.",
        "Devo dirlo com'è: non siamo mai andati d'accordo.",
        "La mia valutazione è netta: non c'è mai stata sintonia.",
        "Non posso far finta di niente: tra noi non ha funzionato.",
        "Lo dico chiaramente: la nostra sintonia non è mai decollata.",
    ],

    # 31x
    "Nel complesso restano un acquisto molto riuscito.": [
        "Nel complesso, è stato un acquisto soddisfacente.",
        "Complessivamente, la valutazione è positiva.",
        "Il bilancio finale è ampiamente positivo.",
        "In sintesi, l'acquisto si è rivelato valido.",
        "Tutto sommato, è stato un buon investimento.",
        "Il giudizio complessivo rimane favorevole.",
        "Alla fine, l'acquisto ha ripagato l'aspettativa.",
        "Nel totale, l'impressione è molto positiva.",
        "Facendo il punto, è un acquisto che rifarei.",
        "Il resoconto finale è largamente positivo.",
        "Sommando tutto, l'acquisto vale quello che ho pagato.",
        "Il bilancio è chiaramente favorevole.",
        "Alla resa dei conti, è uno degli acquisti migliori.",
        "Mettendo sulla bilancia i pro e i contro, si vince.",
        "In ultima analisi, l'acquisto è stato centrato.",
        "Nel quadro generale, l'esperienza è stata buona.",
        "Il verdetto finale è nettamente positivo.",
        "Nel complesso, è un prodotto che consigliei.",
        "Guardando il tutto, è stato un acquisto azzeccato.",
        "Facendo la somma, l'esperienza è positiva.",
        "Il computo finale porta a un giudizio positivo.",
        "Nell'insieme, è stata una scelta centrata.",
        "Alla fine dei conti, soddisfa pienamente.",
        "Il saldo finale è positivo senza dubbi.",
        "Mettendo tutto sul tavolo, è stato un buon acquisto.",
        "Nel complesso, è un prodotto che si difende bene.",
        "A conti fatti, l'acquisto è andato bene.",
        "Il giudizio d'insieme è chiaramente favorevole.",
        "Sommando pro e contro, la valutazione è positiva.",
        "Il totale è un giudizio che propende verso l'alto.",
        "Guardando dall'alto, è stato un acquisto riuscito.",
        "Alla somma di tutto, l'esperienza è soddisfacente.",
    ],

    # 30x
    "Mi sembrano occhiali da scegliere con intenzione, non per automatismo.": [
        "Mi sembrano occhiali che richiedono una scelta consapevole, non casuale.",
        "Non sono un acquisto da fare di fretta: richiedono riflessione.",
        "Sono un paio da acquistare sapendo cosa si vuole.",
        "Non si acquistano per abitudine, ma con una precisa visione in testa.",
        "Richiedono una scelta deliberata, non impulsiva.",
        "Non sono un ripiego: vanno cercati con cognizione.",
        "Si comprano con un'idea chiara, non per comodità.",
        "Non sono occhiali da acquistare per esclusione: vanno voluti.",
        "Li consiglio a chi sa già cosa cerca.",
        "Non si scelgono come default, ma come opzione voluta.",
        "Sono un paio che richiede un acquirente con le idee chiare.",
        "Non sono adatti a chi compra senza pensarci.",
        "Richiedono un acquirente consapevole, non distratto.",
        "Si comprano perché si vogliono davvero, non per caso.",
        "Non sono occhiali da primo impulso: vanno cercati attivamente.",
        "Sono un'opzione per chi compra con cognizione di causa.",
        "Non si prendono senza sapere cosa fare con loro.",
        "Sono adatti a chi ha un'identità stilistica precisa.",
        "Non si scelgono per riempire un vuoto: si cercano on purpose.",
        "Sono pensati per un utente che sa quello che vuole.",
        "Non si acquistano di default, ma con un progetto in testa.",
        "Li consiglio a chi non li sceglie per esclusione.",
        "Non sono un acquisto di convenienza, ma di visione.",
        "Richiedono la giusta testa per essere valorizzati appieno.",
        "Non sono un paio per tutte le stagioni: vanno cercati.",
        "Si acquistano con un senso, non per mancanza di alternative.",
        "Non sono adatti a un acquisto impulsivo.",
        "Sono occhiali per chi ha chiari i propri confini stilistici.",
        "Non si prendono al volo: si cercano con pazienza.",
        "Si scelgono sapendo dove si va, non alla cieca.",
        "Richiedono un acquirente che abbia già trovato il suo stile.",
    ],

    # 30x
    "Restano molto riusciti, solo non universali.": [
        "Restano un prodotto riuscito, ma non adatto a tutti.",
        "Sono molto ben fatti, solo non per tutti i gusti.",
        "Ottima esecuzione, ma con un profilo selettivo.",
        "Prodotto riuscito, ma non per ogni tipo di viso o stile.",
        "Ben costruiti, ma con un target preciso.",
        "Il prodotto funziona bene, solo non è universale.",
        "Molto curati, ma non per tutti.",
        "Qualità alta, pubblico selezionato.",
        "Sono validi, solo non si adattano a ogni contesto.",
        "Ottimo prodotto, ma con un appeal specifico.",
        "Fortemente riusciti, ma destinati a un segmento preciso.",
        "Prodotto di livello, ma non per tutte le silhouette.",
        "Ben progettati, ma non indossabili da chiunque.",
        "Fanno il loro lavoro bene, ma non per ogni situazione.",
        "Di qualità elevata, ma con una nicchia di destinazione precisa.",
        "Molto ben eseguiti, ma destinati a chi si sa come si vuole.",
        "Prodotto solido, ma non per il grande pubblico.",
        "Curatissimi, ma non universali nell'appeal.",
        "Riusciti nell'esecuzione, selettivi nell'adattabilità.",
        "Di fascia alta ma con un target ben definito.",
        "Molto soddisfacenti, ma non per ogni tipo di utenza.",
        "Pregevoli, ma non per ogni morfologia.",
        "Ben concepiti, ma non adatti a ogni stile personale.",
        "Ottimi, ma con una vocazione stilistica precisa.",
        "Di alto profilo, con una selettività implicita.",
        "Prodotto eccellente per chi ci si ritrova.",
        "Molto riusciti, ma non per chi cerca qualcosa di più neutro.",
        "Qualità indiscussa, ma con un pubblico di riferimento specifico.",
        "Molto validi, ma si rivolgono a un'utenza ben precisa.",
        "Realizzati benissimo, ma pensati per una tipologia specifica.",
        "Prodotto di valore, ma non universalmente adattabile.",
    ],

    # 29x
    "C'è dentro molta più questione di proporzioni che di semplice tendenza.": [
        "C'è più riflessione geometrica che inseguimento della moda.",
        "È più una questione di architettura del viso che di trend.",
        "La sostanza è più di progetto strutturale che di moda.",
        "È più una faccenda di proporzioni che di correnti stilistiche.",
        "Il ragionamento che c'è sotto è geometrico, non modaiolo.",
        "C'è più costruzione spaziale che tendenza vuota.",
        "È più un gioco di volumi che di mode passeggere.",
        "La chiave di lettura è strutturale, non modaiola.",
        "C'è più architettura visiva che adeguamento al trend.",
        "Il contenuto è più geometrico che effimero.",
        "È più questione di rapporti spaziali che di stagioni.",
        "C'è più pensiero costruttivo che omaggio al momento.",
        "La sostanza è nel rapporto tra le forme, non nella moda.",
        "È più un discorso di proporzioni che un omaggio al trend.",
        "C'è più ragionamento strutturale che adesione alle tendenze.",
        "È più una faccenda di misure e rapporti che di mode.",
        "C'è più intenzione progettuale che inseguimento del mercato.",
        "La lettura corretta è geometrica, non modaiola.",
        "C'è più metodo architettonico che superficialità stilistica.",
        "È più un'elaborazione di volumi che una risposta al trend.",
        "C'è più solidità progettuale che effimero modaiolo.",
        "Il cuore è una questione di rapporti spaziali, non di moda.",
        "È più un discorso di architettura facciale che di tendenze.",
        "C'è più densità concettuale che semplice attualità stilistica.",
        "La sua logica è proporzionale, non modaiola.",
        "C'è più senso delle misure che inseguimento delle tendenze.",
        "È fondamentalmente una questione di geometria, non di mode.",
        "C'è più progetto silenzioso che adesione al trend dominante.",
        "La sua radice è proporzionale, non effimera.",
        "C'è più struttura solida che tendenza passeggera.",
    ],

    # 29x
    "Con il contesto giusto rende molto più che bene.": [
        "Nel contesto adatto, rende sorprendentemente bene.",
        "Quando l'abbinamento è giusto, dà il meglio di sé.",
        "Con la situazione di utilizzo corretta, funziona magnificamente.",
        "Nel setting ideale, il risultato è eccellente.",
        "Usato nel contesto che gli appartiene, rende al massimo.",
        "Nel momento e nel posto giusto, è difficile fare di meglio.",
        "Quando si trova in condizioni ottimali, eccelle.",
        "Con l'outfit giusto, diventa straordinario.",
        "Nel contesto per cui è pensato, funziona benissimo.",
        "Abbinato correttamente, il rendimento è alto.",
        "In condizioni di utilizzo ideali, esprime tutta la sua qualità.",
        "Con il giusto abbinamento, si eleva notevolmente.",
        "Quando l'ambiente è quello adatto, il risultato è notevole.",
        "Nel suo elemento naturale, rende senza sforzo.",
        "Con l'abbinamento che gli si addice, fa la differenza.",
        "Nel contesto che lo valorizza, non ha competitor.",
        "Calato nel setting corretto, è difficile trovare di meglio.",
        "Abbinato come si deve, il potenziale emerge in pieno.",
        "Con la situazione stilistica giusta, esprime il suo picco.",
        "Nel momento in cui è più a suo agio, è davvero difficile fare di meglio.",
        "Con il giusto contesto attorno, si trasforma.",
        "Posizionato bene, il suo rendimento è eccellente.",
        "Nel setting che gli compete, eccelle senza fatica.",
        "Con l'abbinamento più naturale, diventa difficile da battere.",
        "Quando l'insieme funziona, il risultato è formidabile.",
        "Con il contesto che gli appartiene, non delude mai.",
        "Nel suo ambiente ideale, il rendimento è ottimo.",
        "Abbinato nel modo corretto, supera le attese.",
        "Con l'ambiente stilistico giusto, mostra il suo valore.",
        "Nel contesto progettato per lui, è al suo meglio.",
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
print("✅ Round 3 completato!" if errors == 0 else f"⚠️ {errors} errori.")
