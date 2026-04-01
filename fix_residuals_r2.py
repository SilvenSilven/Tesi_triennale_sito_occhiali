#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fix round 2 — pattern residui dopo il primo fix."""

import psycopg2

DATABASE_URL = (
    "postgresql://neondb_owner:npg_uFxVSRoTj95w"
    "@ep-damp-sea-anvn4fw4.c-6.us-east-1.aws.neon.tech"
    "/neondb?sslmode=require"
)

PATTERNS = {

    # 46x — chiusura negativa
    "ma non basta per salvarlo nel mio uso.": [
        "ma non è abbastanza da farmi cambiare idea completamente.",
        "ma non compensa il difetto principale.",
        "ma la bilancia non pende abbastanza dalla sua parte.",
        "ma non è sufficiente a capovolgere il giudizio.",
        "ma rimane un punto debole che non riesco a ignorare.",
        "ma non riesce a colmare la lacuna di fondo.",
        "ma non è sufficiente da spostare il mio parere.",
        "ma nel complesso il conto non torna.",
        "ma il punto critico resta lì, inamovibile.",
        "ma non supera il problema che ho con lui.",
        "ma nel lungo periodo pesa di più il difetto.",
        "ma non è un vantaggio abbastanza solido.",
        "ma il saldo finale rimane in negativo.",
        "ma il difetto principale sopravanza questo pregio.",
        "ma non costituisce un argomento risolutivo.",
        "ma il punto debole rimane visibile e pesa.",
        "ma è un vantaggio troppo parziale per ribaltare la valutazione.",
        "ma la lacuna strutturale rimane irrisolta.",
        "ma il punto critico non si elimina con questo.",
        "ma non è una giustificazione sufficiente.",
        "ma il lato negativo pesa di più nella pratica quotidiana.",
        "ma non cambia il giudizio complessivo.",
        "ma non è abbastanza da fare la differenza.",
        "ma non riesce a coprire la debolezza principale.",
        "ma il margine è troppo stretto per essere decisivo.",
        "ma non compensa la mancanza che sento.",
        "ma il punto spinoso rimane al suo posto.",
        "ma non risolve il problema di fondo.",
        "ma è un merito che si esaurisce rapidamente.",
        "ma non ribalta la mia posizione.",
        "ma la criticità principale rimane intatta.",
        "ma non sposta l'ago della bilancia dalla mia parte.",
        "ma il difetto strutturale è più ingombrante.",
        "ma non è un plus abbastanza grande da incidere.",
        "ma la zavorra di fondo non sparisce.",
        "ma non è un motivo sufficiente per tenerli.",
        "ma il punto che mi frena resta solido.",
        "ma è troppo poco rispetto a quello che manca.",
        "ma non supera le aspettative che avevo.",
        "ma non è abbastanza da far pendere la bilancia.",
        "ma non basta a farmi innamorare.",
        "ma non elimina la debolezza principale.",
        "ma il range rimane troppo stretto per l'uso che faccio io.",
        "ma il peso del difetto maggiore rimane.",
        "ma il lato critico è troppo ingombrante.",
        "ma non riesco comunque a dimenticare il problema principale.",
        "ma il punto debole che ho con lui non scompare.",
    ],

    # 45x
    "hanno iniziato a lavorare davvero insieme.": [
        "hanno trovato la loro dimensione comune.",
        "hanno smesso di sembrare elementi separati.",
        "hanno cominciato a dialogare in modo convincente.",
        "hanno preso a funzionare come un sistema coerente.",
        "hanno raggiunto una sintonia che prima non c'era.",
        "hanno trovato il modo di completarsi a vicenda.",
        "hanno iniziato a parlarsi come avrebbero dovuto.",
        "hanno smesso di combattersi e hanno trovato un accordo.",
        "hanno cominciato a formare una narrazione unica.",
        "hanno iniziato a sostenersi reciprocamente.",
        "hanno trovato la chiave per integrarsi.",
        "hanno iniziato a funzionare come un tutt'uno.",
        "hanno smesso di sembrare una somma di elementi distinti.",
        "hanno iniziato a costruire un'identità condivisa.",
        "hanno preso a lavorare in armonia.",
        "hanno smesso di stare separati e si sono uniti.",
        "hanno cominciato a creare un senso compiuto.",
        "hanno trovato la loro coerenza interna.",
        "hanno smesso di fare a gara e hanno trovato equilibrio.",
        "hanno cominciato a rispondersi nel modo giusto.",
        "hanno trovato la via per essere un sistema.",
        "hanno iniziato a esprimere qualcosa di unico insieme.",
        "hanno smesso di essere contraddittori e si sono armonizzati.",
        "hanno cominciato a costruire qualcosa che funziona.",
        "hanno trovato la loro sinergia naturale.",
        "hanno smesso di dividersi e hanno creato un discorso unico.",
        "hanno iniziato a formare un tutto coerente.",
        "hanno trovato il ritmo per stare insieme.",
        "hanno cominciato a dare senso all'insieme.",
        "hanno smesso di tirarsi in direzioni opposte.",
        "hanno trovato la via dell'equilibrio componente per componente.",
        "hanno iniziato a esprimere qualcosa di più grande.",
        "hanno smesso di essere frammentati e si sono unificati.",
        "hanno trovato il tono condiviso.",
        "hanno iniziato a costruire un dialogo stilistico autentico.",
        "hanno trovato il modo di sostenersi senza sopraffarsi.",
        "hanno smesso di essere una lista di caratteristiche e sono diventati uno.",
        "hanno cominciato a formare una proposta coerente.",
        "hanno trovato il loro punto di incontro.",
        "hanno iniziato a respirare insieme.",
        "hanno acquistato una coerenza che prima mancava.",
        "hanno cominciato a parlare con una voce sola.",
        "hanno trovato il modo di essere complementari.",
        "hanno smesso di contendersi lo spazio e sono diventati armonici.",
        "hanno iniziato a raccontare la stessa storia.",
        "hanno trovato la loro forma di convivenza stilistica.",
        "hanno iniziato a esprimere un progetto unitario.",
    ],

    # 40x
    "si è comportato meglio del previsto.": [
        "ha superato le mie attese iniziali.",
        "ha reso più di quanto mi aspettassi.",
        "ha dimostrato più di quanto pensassi.",
        "ha sorpreso in modo concreto.",
        "ha avuto un rendimento superiore alle mie previsioni.",
        "ha convinto più di quanto pronosticassi.",
        "ha risposto meglio di quanto temessi.",
        "ha offerto più di quanto sperassi.",
        "ha performato al di sopra delle aspettative.",
        "ha convinto dove non me lo aspettavo.",
        "ha reso più del previsto nella pratica.",
        "ha mostrato un rendimento che avevo sottostimato.",
        "ha fatto meglio di quanto la scheda tecnica facesse sperare.",
        "ha retto meglio di quanto immaginassi.",
        "ha sorpreso positivamente nel lungo periodo.",
        "ha dato risultati che non avevo anticipato.",
        "ha dimostrato risorse che non avevo valutato.",
        "ha convinto con l'uso, nonostante i dubbi iniziali.",
        "ha risposto meglio di quanto pensassi all'inizio.",
        "ha offerto una qualità superiore alle previsioni.",
        "ha sorpreso per la tenuta nel tempo.",
        "ha fatto meglio del previsto in condizioni reali.",
        "ha dimostrato una solidità che non mi aspettavo.",
        "ha superato facilmente i dubbi iniziali.",
        "ha dimostrato più carattere di quanto pensassi.",
        "ha convinto sul campo in modo netto.",
        "ha mostrato un'affidabilità superiore alle attese.",
        "ha reso meglio in condizioni di uso reale.",
        "ha confermato con i fatti ciò che le descrizioni suggerivano.",
        "ha offerto nel tempo più di quanto promesso.",
        "ha tenuto molto meglio di quanto mi aspettassi.",
        "ha sorpreso in positivo su quasi tutti i fronti.",
        "ha dimostrato di valere più del prezzo che ci ho messo.",
        "ha convinto in modo che non avevo previsto.",
        "ha risposto all'uso con più solidità del previsto.",
        "ha reso molto meglio di quanto prevedessero le prime impressioni.",
        "ha fatto molto più di quanto la prima lettura lasciasse intendere.",
        "ha superato senza problemi il test dell'uso quotidiano.",
        "ha risposto positivamente alla prova dei fatti.",
        "ha tenuto bene su una linea temporale più lunga del previsto.",
    ],

    # 39x
    "mi ha preso subito, ma è usando": [
        "ha catturato la mia attenzione al primo sguardo, ma solo usandolo",
        "mi ha convinto a prima vista, anche se è nell'uso che",
        "mi ha colpito subito, però è nella pratica che",
        "mi ha attirato al primo impatto, ma è nell'uso quotidiano che",
        "ha suscitato interesse immediato, ma è usando il prodotto che",
        "mi ha preso di sorpresa, ma è nel tempo che",
        "mi ha convinto visivamente da subito, ma è con l'uso che",
        "ho avuto un'impressione positiva immediata, ma è dandogli quotidianità che",
        "ha fatto un'ottima prima impressione, ma è nella pratica che",
        "mi ha sedotto al primo sguardo, ma è nell'utilizzo continuato che",
        "mi ha convinto al volo, ma è portandolo ogni giorno che",
        "ho sentito subito qualcosa, ma è nell'uso a lungo termine che",
        "ha fatto colpo al primo contatto, ma è usandolo costantemente che",
        "mi ha piacevolmente sorpreso fin dall'inizio, ma è col tempo che",
        "ha destato curiosità sin da subito, ma è con l'impiego che",
        "mi ha conquistato visivamente, ma è nell'esperienza d'uso che",
        "ha fatto breccia al primo sguardo, ma è nella vita reale che",
        "mi ha catturato immediatamente, ma è portandolo fuori che",
        "ha generato entusiasmo presto, ma è con la pratica che",
        "mi ha impressionato a prima vista, ma è nell'uso prolungato che",
        "mi ha colpito d'impatto, ma è portandolo davvero che",
        "ha fatto colpo a prima lettura, ma è nella realtà quotidiana che",
        "mi ha convinto al decollo, ma è nell'atterraggio che",
        "mi ha attratto con forza fin dall'inizio, però è usandolo che",
        "ha generato subito aspettative, ma è nell'esperienza che",
        "mi ha convinto all'istante, ma è dandogli tempo che",
        "ha fatto una prima impressione forte, ma è nell'uso reale che",
        "mi ha preso di slancio, ma è nel rodaggio che",
        "mi ha sedotto senza difficoltà, ma è nell'utilizzo reale che",
        "ho sentito un'attrazione immediata, ma è con l'uso che",
        "mi ha conquistato in fretta, ma è nella pratica che",
        "ha fatto una buona partenza, ma è nell'uso continuato che",
        "mi ha colpito all'inizio, ma è nel lungo periodo che",
        "ha aperto bene le danze, ma è continuando a indossarlo che",
        "mi ha convinto al primo round, ma è con il tempo che",
        "ha creato subito un'aspettativa, ma è col rodaggio che",
        "mi ha impressionato a primo impatto, ma è in condizioni reali che",
        "mi ha catturato al lancio, ma è nell'uso concreto che",
        "ha convinto all'apertura, ma è indossandolo davvero che",
    ],

    # 39x
    "Il passaggio decisivo è stato vederlo": [
        "Il momento che ha spostato la bilancia è stato indossarlo",
        "La svolta è arrivata quando l'ho visto",
        "Quello che ha cambiato la percezione è stato vederlo",
        "Il punto di non ritorno è arrivato guardandolo",
        "La prova decisiva è stata portarlo",
        "Il momento che ha risolto ogni dubbio è stato vederlo",
        "La virata è arrivata nel momento in cui l'ho visto",
        "Ciò che ha spostato il mio giudizio è stato vederlo",
        "L'ago della bilancia si è spostato vedendolo",
        "Il momento cruciale è stato quando l'ho indossato",
        "Il punto di svolta è arrivato quando l'ho portato",
        "La decisione si è chiarita vedendolo",
        "La transizione verso il sì è avvenuta quando l'ho provato",
        "Il nodo si è sciolto nel momento in cui l'ho indossato",
        "Quello che ha fatto la differenza è stato portarlo",
        "Il momento che ha inclinato la bilancia è stato vedendolo",
        "Il giudizio definitivo è arrivato portandolo fuori",
        "Ciò che ha tolto ogni dubbio è stato indossarlo",
        "Il fattore che ha smosso tutto è stato vederlo",
        "La svolta concreta è arrivata quando l'ho portato",
        "Il verdetto si è formato vedendolo",
        "Il momento che ha fatto chiarezza è stato indossandolo",
        "Quello che ha inclinato la bilancia è stato portandolo",
        "Il punto di cambiamento è arrivato quando l'ho indossato",
        "Il passaggio che ha risolto la questione è stato vederlo",
        "Il colpo di grazia del dubbio è arrivato vedendolo",
        "La pietra angolare della valutazione è stata indossarlo",
        "Il salto di qualità nella comprensione è avvenuto vedendolo",
        "Il momento che ha fatto pendere la bilancia è stato vederlo",
        "La verifica finale è arrivata portandolo fuori",
        "Il punto che ha sciolto l'incertezza è stato vedendolo",
        "Il salto definitivo è avvenuto quando l'ho portato",
        "Il decisore è stato vedendolo nella realtà",
        "L'elemento conclusivo è stato indossandolo davvero",
        "La chiusura del ragionamento è arrivata portandolo",
        "Il test finale si è risolto vedendolo",
        "Il tassello mancante si è aggiunto indossandolo",
        "Il chiarimento è arrivato nel momento in cui l'ho portato",
        "L'ultimo argomento è stato vedendolo in contesto reale",
        "Il giudizio si è solidificato nel momento in cui l'ho indossato",
    ],

    # 38x
    "mi ha dato subito la misura di un progetto pensato": [
        "mi ha comunicato fin da subito di essere un oggetto progettato",
        "mi ha trasmesso immediatamente l'idea di un progetto consapevole",
        "mi ha fatto capire sin dall'inizio che si tratta di un disegno intenzionale",
        "ha mostrato da principio di essere frutto di un lavoro deliberato",
        "mi ha segnalato subito che siamo di fronte a una scelta progettuale precisa",
        "ha dimostrato fin da subito di non essere nato per caso",
        "mi ha dato l'immediata impressione di un lavoro di testa",
        "ha comunicato da subito di essere il risultato di un progetto ragionato",
        "mi ha fatto capire velocemente che c'è una regia dietro",
        "ha trasmesso fin da subito la sensazione di un lavoro calibrato",
        "mi ha dato l'impressione immediata di un oggetto costruito con intenzione",
        "ha mostrato subito di essere il frutto di scelte precise",
        "mi ha convinto sin da principio di trovarmi davanti a qualcosa di progettato",
        "ha segnalato subito di essere un lavoro definito",
        "mi ha dato da subito la sensazione di un progetto con una direzione chiara",
        "ha rivelato immediatamente di essere il risultato di un'idea coerente",
        "mi ha trasmesso sin dall'inizio la solidità di un lavoro pensato",
        "ha mostrato subito di provenire da una riflessione stilistica vera",
        "mi ha fatto capire subito che non è un prodotto improvvisato",
        "ha comunicato da subito la coerenza di un progetto consapevole",
        "mi ha dato l'impressione immediata di qualcosa di studiato",
        "ha dimostrato fin dal primo momento di essere un lavoro calibrato",
        "mi ha trasmesso da subito la sensazione di un oggetto con una logica interna",
        "ha segnalato immediatamente di essere il frutto di una visione",
        "mi ha dato subito la percezione di essere davanti a qualcosa di costruito",
        "ha mostrato da principio di avere una tesi stilistica",
        "mi ha fatto capire fin dall'inizio che c'è un'architettura dietro",
        "ha comunicato subito di essere il risultato di un lavoro intenzionale",
        "mi ha trasmesso da subito la chiarezza di un progetto con identità",
        "ha rivelato sin dal primo istante di essere il frutto di scelte consapevoli",
        "mi ha dato immediata percezione di un lavoro serio e calibrato",
        "ha dimostrato da principio di non essere casuale nel design",
        "mi ha segnalato subito la coerenza interna di un progetto ragionato",
        "ha mostrato fin da subito di avere un'intenzione stilistica precisa",
        "mi ha comunicato sin dall'inizio l'intenzione di un progetto maturo",
        "ha trasmesso da subito la solidità di un lavoro strutturato",
        "mi ha fatto capire al volo che si tratta di design pensato",
        "ha rivelato immediatamente di essere il prodotto di una riflessione vera",
        "mi ha dato l'impressione fin dal primo sguardo di un progetto con radici",
        "ha segnalato sin dal primo contatto di avere una propria filosofia costruttiva",
    ],

    # 37x
    "Ci sono cose che mi piacciono:": [
        "Ci sono aspetti che apprezzo:",
        "Ha dei pregi concreti:",
        "Alcune cose funzionano davvero:",
        "Ci sono punti positivi da segnalare:",
        "Alcune componenti mi convincono:",
        "Ci sono lati che mi piacciono:",
        "Ha delle qualità che val la pena riconoscere:",
        "Alcune caratteristiche mi soddisfano:",
        "Ci sono elementi che apprezzo:",
        "Ha dei punti di forza reali:",
        "Alcuni aspetti sono indubitabilmente riusciti:",
        "Alcune note positive ci sono:",
        "Ci sono cose che risaltano in positivo:",
        "Ha dei meriti che non posso ignorare:",
        "Alcune scelte mi convincono del tutto:",
        "Ha tratti che funzionano:",
        "Ci sono aspetti che reggono bene:",
        "Ha qualcosa che apprezzo concretamente:",
        "Alcune parti mi soddisfano:",
        "Ci sono elementi che mi convincono:",
        "Ha alcuni dei prodotti che apprezzo davvero:",
        "Alcune cose riescono bene:",
        "Ci sono aspetti positivi da tenere presente:",
        "Ha dei lati che colpiscono favorevolmente:",
        "Alcune componenti sono ben riuscite:",
        "Ci sono pregi che emergono nell'uso:",
        "Ha caratteristiche che mi hanno convinto:",
        "Alcune note positive si fanno notare:",
        "Ci sono punti dove eccelle:",
        "Ha dei tratti che funzionano perfettamente:",
        "Alcune scelte estetiche mi convincono:",
        "Ci sono aspetti che mi colpiscono in modo positivo:",
        "Ha dei meriti su cui non ho nulla da ridire:",
        "Alcune parti lavorano benissimo:",
        "Ci sono punti forti da segnalare:",
        "Ha elementi che apprezzo in modo sincero:",
        "Alcune cose sono fatte bene:",
        "Ci sono pregi che saltano all'occhio:",
        "Ha caratteristiche apprezzabili:",
        "Alcune note riuscite ci sono sicuramente:",
    ],

    # 37x
    "mi ha fatto rivedere le mie aspettative": [
        "mi ha spinto a rivedere le mie previsioni",
        "ha cambiato la mia prospettiva iniziale",
        "ha spostato il mio punto di vista",
        "ha ribaltato le mie previsioni",
        "ha modificato la mia lettura iniziale",
        "ha aggiornato il mio punto di vista",
        "ha riposizionato le mie previsioni",
        "ha ri-calibrato la mia valutazione",
        "ha fatto saltare le mie previsioni",
        "mi ha convinto a rivedere il primo giudizio",
        "ha spostato i parametri di riferimento",
        "mi ha fatto riconsiderare il giudizio iniziale",
        "ha ribaltato le aspettative con cui ho iniziato",
        "ha messo in discussione il mio punto di partenza",
        "mi ha portato a cambiare prospettiva",
        "ha aggiornato in modo netto la mia visione iniziale",
        "mi ha costretto a rielaborare la valutazione",
        "ha reso necessario un aggiornamento del giudizio",
        "mi ha condotto a riconsiderare la stima iniziale",
        "ha rimescolato le carte con cui avevo iniziato",
        "ha spostato la valutazione in una direzione inattesa",
        "mi ha imposto di ricalibrare il giudizio di partenza",
        "ha smantellato le previsioni con cui ho iniziato",
        "mi ha spinto a riformulare il punto di partenza",
        "ha resettato il mio schema di valutazione iniziale",
        "mi ha portato a un aggiornamento sostanziale del giudizio",
        "ha cambiato le coordinate della mia lettura iniziale",
        "mi ha fatto rivedere la proiezione con cui mi ero avvicinato",
        "ha messo in crisi le previsioni iniziali",
        "mi ha spinto a un ripensamento radicate",
        "ha fatto saltare le premesse su cui mi basavo",
        "mi ha costretto a un reset del giudizio iniziale",
        "ha spostato l'asse della mia valutazione",
        "mi ha portato a riconsiderare il quadro di partenza",
        "ha ridisegnato le mie premesse valutative",
        "mi ha convinto a rivedere la posizione con cui ho iniziato",
        "ha smentito le previsioni che avevo formulato",
        "ha eroso la certezza del giudizio di partenza",
        "mi ha imposto di rivedere il framework di valutazione",
        "ha spostato in modo netto il mio punto di riferimento",
    ],

    # 32x
    "Il punto non è che sia sbagliato, è che non mi scatta l'istinto.": [
        "Non è che abbia torto, è che non mi accende.",
        "Non è un errore di progetto, è che non scatta qualcosa in me.",
        "Il problema non è la qualità, è che non mi parla.",
        "Non è sbagliato in sé, è che non mi appartiene.",
        "Non è che fallisce, è che non mi prende.",
        "Non è un difetto, è un'indifferenza che non supero.",
        "Non è che sia brutto, è che non mi convince fino in fondo.",
        "Non è una questione di qualità, è che non creo connessione.",
        "Non è un problema oggettivo, è che non mi sento a mio agio.",
        "Non è che faccia male il suo lavoro, è che non mi emoziona.",
        "Non è che sia incoerente, è che non mi appartiene stilisticamente.",
        "Non è un difetto di progettazione, è un'incompatibilità personale.",
        "Non è sbagliato, è che non si adatta al mio viso.",
        "Non è che sia poco curato, è che non mi scatta il feeling.",
        "Non è un errore, è un'incompatibilità di fondo.",
        "Non è che manchi di qualità, è che non mi convince affettivamente.",
        "Non è che sia mal costruito, è che non mi ci vedo.",
        "Non è che sia un fallimento, è che non mi appartiene.",
        "Non è una questione tecnica, è che non mi parla.",
        "Non è che sia fuori posto, è che non mi dà quella spinta.",
        "Non è che sia mediocre, è che non mi prende l'entusiasmo.",
        "Non è che manchino le qualità, è che non creo feeling.",
        "Non si tratta di una critica, ma di un'incompatibilità personale.",
        "Non è un giudizio negativo assoluto, è che non mi fa innamorare.",
        "Non è una questione di pregio, è che non mi appartiene visivamente.",
        "Non manca di carattere, è che il suo carattere non è il mio.",
        "Non è un cattivo prodotto, è che non mi scalda.",
        "Non è che ci sia qualcosa che non va, è che non mi prende.",
        "Non è una delusione tecnica, è solo una distanza emotiva.",
        "Non è un problema del prodotto, è una difficoltà mia di connettermi.",
        "Non è che sia un prodotto sbagliato, è che non è il mio.",
        "Non è una critca alla lavorazione, è che non mi appartiene.",
    ],

    # 32x
    "Quindi lo tengo in una terra di mezzo.": [
        "Quindi rimango in una zona grigia.",
        "La mia valutazione resta sospesa.",
        "Il giudizio è quindi interlocutorio.",
        "Finisco per relegarlo in una zona di incertezza.",
        "Il verdetto rimane in sospeso.",
        "Resto quindi con un giudizio aperto.",
        "La mia posizione resta ambigua.",
        "Mi fermo quindi su una valutazione provvisoria.",
        "Resto in una zona di penombra valutativa.",
        "Il mio giudizio rimane incerto e aperto.",
        "Resto con un'opinione non definitiva.",
        "Il verdetto è quindi ancora da scrivere.",
        "Mi fermo a un giudizio incompiuto.",
        "Finisco in una zona di ambivalenza.",
        "Rimango in uno stato di incertezza valutativa.",
        "La valutazione si arena in una zona neutra.",
        "Il giudizio si colloca in un limbo.",
        "Resto fermo in una posizione ambiguamente sospesa.",
        "Mi fermo a una valutazione non risolta.",
        "Il giudizio rimane tra due acque.",
        "Finisco per tenere aperta la partita.",
        "La valutazione si ferma a metà strada.",
        "Non riesco a chiudere la partita in nessun senso.",
        "Il mio parere resta incompiuto.",
        "Rimango con un giudizio che non si stabilizza.",
        "Il verdetto è sospeso tra il sì e il no.",
        "Resto su una linea di confine valutativa.",
        "La mia posizione resta a cavallo tra due letture.",
        "Mi fermo in una zona di dubbio persistente.",
        "Non riesco ad arrivare a un giudizio definitivo.",
        "Il mio parere si solidifica su una soglia ambivalente.",
        "Finisco con un giudizio che non si risolve.",
        "La valutazione rimane aperta, senza verdetto netto.",
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
print("✅ Round 2 completato!" if errors == 0 else f"⚠️ {errors} errori.")
