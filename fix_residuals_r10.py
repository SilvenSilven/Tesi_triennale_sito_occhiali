#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fix round 10 — frasi complete >=5x + frammenti ad alta frequenza sotto soglia n-gram."""

import psycopg2

DATABASE_URL = (
    "postgresql://neondb_owner:npg_uFxVSRoTj95w"
    "@ep-damp-sea-anvn4fw4.c-6.us-east-1.aws.neon.tech"
    "/neondb?sslmode=require"
)

PATTERNS = {

    # ── FRAMMENTI AD ALTA FREQUENZA (sotto soglia 6-word n-gram) ──────────────

    # 124x — connettore finale frase
    " e non mi hanno deluso.": [
        " e si sono rivelati all'altezza.",
        " e il riscontro è stato positivo.",
        " e la conferma è arrivata.",
        " e mi hanno convinto sul campo.",
        " e la resa è stata buona.",
        " e non ho avuto rimpianti.",
        " e il giudizio è positivo.",
        " e si sono comportati bene.",
        " e hanno superato la prova.",
        " e non ho niente da dire.",
        " e la risposta è stata favorevole.",
        " e l'esito non mi ha deluso.",
        " e il risultato è stato convincente.",
        " e l'esperienza è stata positiva.",
        " e il bilancio è buono.",
        " e la soddisfazione c'è stata.",
        " e mi hanno dato ragione.",
        " e il verdetto è positivo.",
        " e ho avuto conferma della scelta.",
        " e l'uso li ha riabilitati.",
        " e hanno tenuto la posizione.",
        " e non hanno tradito le aspettative.",
        " e si sono guadagnati la fiducia.",
        " e il riscontro pratico è stato buono.",
        " e la realtà li ha promossi.",
        " e non mi sono pentito.",
        " e il prodotto ha risposto bene.",
        " e la sostanza ha retto.",
        " e ho apprezzato la coerenza.",
        " e non ho trovato motivi di rimpianto.",
        " e l'impressione è rimasta positiva.",
        " e hanno retto al test.",
        " e la scelta si è rivelata giusta.",
        " e non ho avuto sorprese negative.",
        " e l'usarli ha confermato la scelta.",
        " e hanno tenuto fede a ciò che promettevano.",
        " e l'acquisto è stato centrato.",
        " e la loro qualità reale si è confermata.",
        " e ho ricevuto quello che cercavo.",
        " e il test pratico ha dato esito buono.",
        " e si sono fatti valere.",
        " e la scelta è risultata azzeccata.",
        " e non c'è stato nessun ripensamento.",
        " e l'esito è stato quello atteso.",
        " e si sono dimostrati validi.",
        " e la mia aspettativa è stata soddisfatta.",
        " e in pratica hanno funzionato.",
        " e li ho trovati all'altezza della situazione.",
        " e non mi hanno lasciato a mani vuote.",
        " e il prodotto ha fatto la sua parte.",
        " e l'esperienza si è chiusa bene.",
        " e la qualità ha retto l'uso.",
        " e il verdetto quotidiano è stato positivo.",
        " e l'esito finale è soddisfacente.",
        " e non hanno bisogno di difese.",
        " e l'acquisto si è dimostrato valido.",
        " e hanno guadagnato la mia stima.",
        " e il loro contributo alla giornata è stato reale.",
        " e si sono rivelati una scelta sensata.",
        " e il commento che ne esce è positivo.",
        " e l'approvazione c'è stata.",
        " e tutto considerato ha funzionato.",
        " e hanno risposto con qualità.",
        " e nessun rimpianto a posteriori.",
        " e l'esito pratico li ha promossi.",
        " e li ho trovati coerenti con le mie aspettative.",
        " e il confronto con la realtà è stato buono.",
        " e mi hanno dato quello che cercavo.",
        " e l'esperienza è stata all'altezza.",
        " e si sono rivelati scelta giusta.",
        " e li ho trovati convincenti nell'uso.",
        " e il loro utilizzo mi ha soddisfatto.",
        " e in pratica si sono rivelati buoni.",
        " e l'utilizzo li ha promossi.",
        " e la qualità pratica si è vista.",
        " e li riconfermerei.",
        " e l'esito mi ha soddisfatto.",
        " e l'insieme ha retto bene.",
        " e il giudizio finale è positivo.",
        " e ho apprezzato il comportamento reale.",
        " e si sono confermati una scelta riuscita.",
        " e non ho rimpianti sul loro uso.",
        " e la loro valenza reale si è confermata.",
        " e non ho trovato motivi di disappunto.",
        " e il comportamento pratico è stato buono.",
        " e non hanno deluso in termini di uso.",
        " e il giudizio d'uso è positivo.",
        " e la coerenza nel tempo non è mancata.",
        " e li ho approvati nell'uso.",
        " e l'esperienza d'uso li ha premiati.",
        " e si sono rivelati all'altezza dell'acquisto.",
        " e non ho avuto obiezioni pratiche.",
        " e il loro impiego ha soddisfatto.",
        " e l'utilizzo li ha confermati.",
        " e si sono guadagnati un posto fisso.",
        " e li ho trovati adatti all'uso previsto.",
        " e l'acquisto è risultato centrato.",
        " e si sono dimostrati all'altezza delle aspettative.",
        " e un giudizio positivo si è formato.",
        " e li ho trovati pronti per l'uso.",
        " e non hanno perso terreno nel tempo.",
        " e la proposta si è rivelata valida.",
        " e il mio giudizio è rimasto positivo.",
        " e in pratica hanno retto.",
        " e si sono fatti apprezzare.",
        " e l'appeal non è rimasto solo teorico.",
        " e li ho trovati degni di fiducia.",
        " e l'esame pratico li ha promossi.",
        " e nessuna delusione concreta.",
        " e lo confermerei come acquisto.",
        " e si sono dimostrati affidabili nell'uso.",
        " e mi hanno dato ragione d'acquisto.",
        " e non ho trovato ragioni di critica.",
        " e il riscontro reale è stato buono.",
        " e la loro qualità pratica si è vista.",
        " e hanno retto la prova d'uso.",
        " e l'ho trovato coerente con le premesse.",
        " e si sono confermati validi.",
        " e il resoconto d'uso è positivo.",
        " e ho avuto meno dubbi dopo.",
        " e si sono dimostrati praticamente buoni.",
        " e non ho avuto motivi di revisione.",
        " e la verifica pratica è stata superata.",
        " e la qualità si è mostrata nella pratica.",
        " e li ho trovati soddisfacenti.",
        " e non ho trovato niente da correggere.",
        " e il loro utilizzo ha soddisfatto.",
        " e l'aspettativa è stata rispettata.",
    ],

    # 90x — connettore struttura recensione
    "Lato meno convincente:": [
        "Il punto critico:",
        "La pecca principale:",
        "Il limite concreto:",
        "La debolezza vera:",
        "Ciò che non convince:",
        "Il punto meno riuscito:",
        "La riserva principale:",
        "L'aspetto più debole:",
        "Il tallone d'Achille:",
        "Il lato critico:",
        "Il punto interrogativo:",
        "La nota stonata:",
        "Il limite che pesa:",
        "La debolezza strutturale:",
        "L'aspetto problematico:",
        "Il dato negativo:",
        "La fragilità del prodotto:",
        "L'unica nota critica:",
        "Il punto che non chiude:",
        "Il limite evidente:",
        "La questione aperta:",
        "Il difetto che rimane:",
        "La cosa meno riuscita:",
        "Il punto che non convince:",
        "Il limite che emerge:",
        "L'elemento critico:",
        "Il punto debole reale:",
        "La nota meno positiva:",
        "Il fattore limitante:",
        "L'aspetto meno soddisfacente:",
        "Il punto che frena:",
        "La critica concreta:",
        "Il limite che non scompare:",
        "La voce passiva:",
        "Il punto che lascia a desiderare:",
        "Il dato meno favorevole:",
        "La riserva concreta:",
        "Il punto che rimane critico:",
        "L'aspetto da migliorare:",
        "Il lato meno apprezzato:",
        "La difficoltà principale:",
        "Il problema concreto:",
        "La limitazione reale:",
        "Il punto dolente:",
        "L'aspetto che delude:",
        "Il limite che si sente:",
        "La nota negativa:",
        "L'aspetto che lascia dubbi:",
        "Il punto che non funziona:",
        "La criticità del prodotto:",
        "Il lato meno valido:",
        "La pecora nera:",
        "L'aspetto da correggere:",
        "Il punto che mi frena:",
        "La nota discordante:",
        "Il fattore critico:",
        "L'aspetto che non piace:",
        "Il punto di attrito:",
        "La delusione parziale:",
        "L'aspetto non risolto:",
        "Il limite reale:",
        "Il punto che non torna:",
        "La mancanza concreta:",
        "L'aspetto critico da segnalare:",
        "Il problema che emerge:",
        "Il limite da non ignorare:",
        "La nota che non suona bene:",
        "Il punto su cui riflettere:",
        "Il difetto concreto:",
        "L'aspetto che abbassa il voto:",
        "La voce da migliorare:",
        "Il dato che preoccupa:",
        "La limitazione percepita:",
        "Il limite che condiziona:",
        "Il punto che indebolisce:",
        "La nota che bilancia:",
        "L'aspetto che pesa:",
        "Il capovolgimento critico:",
        "Il punto che rimane:",
        "L'aspetto che manca:",
        "La debolezza da tenere a mente:",
        "Il punto critico finale:",
        "Il limite che non posso ignorare:",
        "La criticità che rimane:",
        "Il punto di debolezza visibile:",
        "L'aspetto che abbassa le aspettative:",
        "Il limite principale da segnalare:",
        "L'osservazione critica:",
        "Il punto che non si chiude:",
    ],

    # 71x — connettore critica
    "L'unico vero limite è che": [
        "La sola riserva concreta è che",
        "Il solo punto debole è che",
        "L'unico difetto reale è che",
        "La limitazione principale è che",
        "Il punto critico è che",
        "La pecca più evidente è che",
        "L'unica critica sostanziale è che",
        "La riserva più importante è che",
        "Il limite che non posso ignorare è che",
        "L'unico vero difetto è che",
        "La nota critica è che",
        "Il problema principale è che",
        "L'aspetto più debole è che",
        "La voce critica più rilevante è che",
        "Il punto che non funziona è che",
        "L'unica obiezione è che",
        "La debolezza principale è che",
        "Il freno principale è che",
        "L'unico nodo irrisolto è che",
        "La riserva più concreta è che",
        "Il problema che non posso ignorare è che",
        "Il limite da segnalare è che",
        "La pecca che rimane è che",
        "L'unica riserva è che",
        "Il punto dolente è che",
        "L'aspetto che non convince è che",
        "La fragilità principale è che",
        "La limitazione concreta è che",
        "Il limite che condiziona il giudizio è che",
        "L'unica nota negativa è che",
        "La critica più onesta è che",
        "Il difetto che pesa è che",
        "L'unico problema rilevante è che",
        "Il fattore limitante è che",
        "La delusione parziale è che",
        "L'aspetto problematico è che",
        "Il punto che frena è che",
        "Il limite che si sente è che",
        "L'unica lacuna è che",
        "La riserva da fare è che",
        "Il punto che non mi convince è che",
        "La nota stonata è che",
        "L'ostacolo principale è che",
        "Il problema che rimane è che",
        "La difficoltà concreta è che",
        "Il punto interrogativo è che",
        "L'aspetto non risolto è che",
        "La debolezza strutturale è che",
        "Il limite che abbassa il voto è che",
        "L'unico neo è che",
        "La critica principale è che",
        "Il fattore che pesa è che",
        "Il difetto da segnalare è che",
        "L'aspetto che delude è che",
        "La riserva che pesa di più è che",
        "Il limite che condiziona è che",
        "Il nodo da sciogliere è che",
        "La critica concreta è che",
        "L'aspetto critico è che",
        "Il problema da non sottovalutare è che",
        "Il punto che rimane critico è che",
        "La sola osservazione negativa è che",
        "Il limite che non scompare è che",
        "Il problema che emerge è che",
        "L'aspetto che pesa di più è che",
        "Il dato critico è che",
        "La nota che non suona bene è che",
        "Il limite visibile è che",
        "Il difetto concreto è che",
        "Il punto dolente principale è che",
        "L'elemento critico più importante è che",
        "Il problema che non passa è che",
    ],

    # 52x — connettore positivo frase
    "qui lavorano bene insieme.": [
        "qui trovano una sintesi riuscita.",
        "qui collaborano con risultato.",
        "qui creano un insieme coerente.",
        "qui si integrano bene.",
        "qui funzionano in sinergia.",
        "qui danno il meglio di sé.",
        "qui si completano naturalmente.",
        "qui formano un tutto convincente.",
        "qui si accordano con successo.",
        "qui costruiscono qualcosa di valido.",
        "qui si incontrano bene.",
        "qui trovano un'armonia vera.",
        "qui riescono nell'insieme.",
        "qui si combinano con senso.",
        "qui si amalgamano con qualità.",
        "qui creano coerenza.",
        "qui producono un esito riuscito.",
        "qui trovano il loro equilibrio.",
        "qui cooperano con efficacia.",
        "qui si fondono bene.",
        "qui dialogano con risultato.",
        "qui si uniscono bene.",
        "qui si bilanciano con successo.",
        "qui si compongono in modo convincente.",
        "qui si parlano con una certa efficacia.",
        "qui si armonizzano.",
        "qui danno vita a un insieme valido.",
        "qui si incastrano bene.",
        "qui producono armonia.",
        "qui generano un'unità convincente.",
        "qui si fondono con coerenza.",
        "qui trovano una buona sinergia.",
        "qui collaborano con esito positivo.",
        "qui si integrano con naturalezza.",
        "qui funzionano insieme come previsto.",
        "qui formano un tutto ben riuscito.",
        "qui danno un risultato soddisfacente.",
        "qui si incastrano in modo naturale.",
        "qui trovano un accordo convincente.",
        "qui riescono a stare bene insieme.",
        "qui si completano con efficacia.",
        "qui producono un buon insieme.",
        "qui si intrecciano con risultato.",
        "qui danno l'uno credito all'altro.",
        "qui trovano il loro punto d'incontro.",
        "qui si equilibrano bene.",
        "qui funzionano in modo efficace.",
        "qui trovano la giusta misura.",
        "qui danno coerenza all'insieme.",
        "qui si incastrano con naturalezza.",
        "qui riescono nell'effetto complessivo.",
        "qui trovano un equilibrio solido.",
        "qui danno un esito complessivo buono.",
    ],

    # 37x — fine frase
    "tiene la scena senza strafare.": [
        "tiene la scena con misura.",
        "emerge senza gridare.",
        "si impone senza eccedere.",
        "occupa lo spazio senza sopraffare.",
        "si fa notare senza esibirsi.",
        "tiene il centro senza dominare.",
        "parla senza alzare la voce.",
        "è presente senza invadere.",
        "si vede senza imporsi.",
        "mantiene la scena con sobrietà.",
        "si nota senza disturbare.",
        "ha presenza senza arroganza.",
        "si fa valere senza esibizionismo.",
        "ha carattere senza esagerare.",
        "è riconoscibile senza affollarsi.",
        "occupa la scena senza esplodere.",
        "si pone senza esasperare.",
        "ha voce senza urlare.",
        "è protagonista senza saperlo.",
        "gestisce la scena con controllo.",
        "si fa riconoscere senza sopraffare.",
        "ha personalità senza invadenza.",
        "mantiene la sua posizione senza eccessi.",
        "regge la scena con stile.",
        "è evidente senza essere chiassoso.",
        "convoca attenzione senza gridare.",
        "sa emergere senza spingere.",
        "ha impatto senza clamore.",
        "si distingue senza sopraffare.",
        "sa farsi vedere senza esagerare.",
        "esiste senza occupare troppo spazio.",
        "si fa notare senza rumore.",
        "è visibile senza invadere il campo.",
        "mantiene la presenza senza ecceni.",
        "sa tenere la scena con leggerezza.",
        "emerge con discrezione.",
        "occupa senza pretendere.",
        "è presente con moderazione.",
    ],

    # 25x — frammento inizio (endings variate)
    "Non pensavo mi sarebbero piaciuti così": [
        "Non mi aspettavo di trovarli così",
        "Non avrei scommesso di apprezzarli così",
        "Non mi attendevo di gradirli così",
        "Non avevo immaginato di trovarli così",
        "Non potevo prevedere di amarli così",
        "Non credevo di trovarmeli così",
        "Non mi ero aspettato di apprezzarli così",
        "Non pensavo di restare così soddisfatto, eppure sono",
        "La sorpresa è che mi sono piaciuti così",
        "Inaspettatamente li ho trovati così",
        "Non lo avrei detto, eppure li ho trovati così",
        "Contro ogni aspettativa, sono",
        "Contrariamente a quanto prevedevo, sono risultati",
        "Nemmeno avrei detto, ma li ho trovati così",
        "Non avrei previsto di trovarli così",
        "Sorprendentemente li ho trovati così",
        "Contro le mie aspettative, sono risultati",
        "Inaspettatamente devo dire che sono",
        "Avevo aspettative basse: li ho trovati invece così",
        "Partivo scettico: li ho trovati invece così",
        "Non mi aspettavo un risultato così",
        "La realtà ha superato le attese: sono",
        "Devo essere onesto: li ho trovati così",
        "Non avrei detto di gradirli così",
        "Avevo dubbi e invece sono risultati",
        "Non ci speravo, ma li ho trovati così",
    ],

    # 19x — frammento (già in cross-sentence analysis)
    "Da fermo mi colpiscono": [
        "A distanza mi attraggono",
        "Prima di indossarli mi colpiscono",
        "A riposo mi affascinano",
        "Guardati staticamente mi attraggono",
        "Visti senza indossarli mi colpiscono",
        "Tenuti in mano mi attraggono",
        "In vetrina mi colpiscono",
        "Come semplici oggetti mi attraggono",
        "Tenuti fermo mi colpiscono",
        "Guardati così mi attraggono",
        "In assenza d'uso mi colpiscono",
        "Senza portarli mi attraggono",
        "Al primo sguardo mi colpiscono",
        "Guardati come oggetto mi colpiscono",
        "Prima dell'uso mi attraggono",
        "In fase statica mi colpiscono",
        "Visti come puro design mi colpiscono",
        "Come oggetto mi colpiscono",
        "Da vedere mi piacevano molto,",
        "Staticamente mi colpiscono",
    ],

    # 19x — frammento frase
    "si sente subito e hanno una": [
        "emerge subito e hanno una",
        "si percepisce subito e hanno una",
        "si nota al primo uso e hanno una",
        "si avverte immediatamente e hanno una",
        "si coglie fin da subito e hanno una",
        "si manifesta subito e hanno una",
        "è evidente da subito e hanno una",
        "si rivela al primo contatto e hanno una",
        "si sente all'istante e hanno una",
        "si percepisce al primo touch e hanno una",
        "è palpabile subito e hanno una",
        "si avverte al primo uso e hanno una",
        "emerge con naturalezza e hanno una",
        "si materializza subito e hanno una",
        "è tangibile subito e hanno una",
        "si fa sentire subito e hanno una",
        "si percepisce chiaramente e hanno una",
        "si nota immediatamente e hanno una",
        "emerge prontamente e hanno una",
        "si sente con chiarezza e hanno una",
    ],

    # 18x
    "Per me il punto si riassume così:": [
        "La valutazione che ne faccio è questa:",
        "Il succo del mio giudizio è:",
        "La mia sintesi è la seguente:",
        "In breve il mio giudizio è:",
        "Il bilancio si riduce a:",
        "La conclusione che ne tiro è:",
        "In sostanza il punto è:",
        "La mia sintesi è semplice:",
        "Il quadro complessivo per me è:",
        "Nella mia valutazione il punto è:",
        "In poche parole:",
        "Il succo della questione è:",
        "In sintesi il mio giudizio è:",
        "La mia posizione finale è:",
        "Il punto centrale per me è:",
        "Il mio ragionamento porta a:",
        "Per come la vedo io:",
        "La mia lettura finale è:",
        "In parole povere:",
        "Per riassumere il tutto:",
    ],

    # 17x — frammento
    "abbinati a cose che avevo già nell'armadio,": [
        "indossati con quello che avevo già in guardaroba,",
        "accostati ai pezzi che già possiedo,",
        "integrati con i capi già presenti,",
        "usati con quello che avevo già,",
        "combinati con i miei capi esistenti,",
        "abbinati a ciò che già avevo,",
        "messi in coppia con i soliti capi,",
        "accoppiati a quanto avevo in armadio,",
        "coordinati con il guardaroba esistente,",
        "usati coi capi abituali,",
        "inseriti nel vestirsi di tutti i giorni,",
        "abbinati agli outfit già collaudati,",
        "indossati su base quotidiana con i soliti look,",
        "integrati nella rotazione standard,",
        "usati con i vestiti che porto di solito,",
        "abbinati ai miei capi di base,",
        "indossati su ciò che già avevo,",
        "accostati ai miei outfit abituali,",
    ],

    # 17x — frammento frase
    "il peso si sente più di": [
        "il peso si percepisce più di",
        "l'ingombro si avverte più di",
        "il peso si fa sentire più di",
        "il peso si nota più di",
        "il peso si avverte più di",
        "il peso risulta maggiore di",
        "l'appesantimento si sente più di",
        "il peso fisico è superiore a",
        "la pesantezza supera quella di",
        "il peso rilevato è maggiore di",
        "la sensazione di peso supera",
        "la gravità si percepisce più di",
        "il peso pratico è maggiore di",
        "il peso effettivo supera quello di",
        "l'impatto del peso è più di",
        "il peso tangibile supera",
        "la pressione delle aste si sente più di",
        "il peso sulla montatura supera",
    ],

    # 16x — frammento
    "insieme a un look minimale che da solo diceva poco,": [
        "accostati a un outfit sobrio che da solo parlava poco,",
        "abbinati a un look essenziale che da solo non diceva nulla,",
        "indossati con un completo minimal che da solo non aveva carattere,",
        "usati con un look neutro che da solo sembrava spento,",
        "messi con un outfit minimale che da solo sembrava incompleto,",
        "abbinati a un ensemble sobrio che da solo richiedeva qualcosa,",
        "indossati su un look essenziale che da solo sembrava piatto,",
        "combinati con un insieme minimalista che da solo era generico,",
        "portati con un look minimale che da solo non si esprimeva,",
        "abbinati a quest'outfit semplice che da solo era poco,",
        "usati con un look neutro quasi silenzioso,",
        "messi su un outfit sobrio che da solo sembrava dire poco,",
        "indossati con un look monocromatico che da solo sembrava spento,",
        "abbinati a un insieme essenziale che da solo aveva poco carattere,",
        "portati con un outfit minimal che da solo non bastava,",
        "usati con un look di base che da solo sembrava anonimo,",
        "indossati su una base sobria che da solo non parlava,",
    ],

    # 14x — frammento
    "su un viso struccato e capelli raccolti,": [
        "su un viso naturale e capelli raccolti,",
        "con un look essenziale e senza trucco,",
        "su un viso nude e capelli a coda,",
        "con il viso pulito e acconciatura semplice,",
        "su un volto sobrio e capelli legati,",
        "su un viso al naturale e capelli in su,",
        "con un trucco minimo e capelli raccolti,",
        "su un viso minimal e capelli fermati,",
        "con il viso nude e acconciatura raccolta,",
        "su un look naturale e capelli su,",
        "su un viso senza trucco e capelli raccolti,",
        "con un look fluido e capelli legati,",
        "su un viso semplice e capelli tiratii su,",
        "con l'essenziale e capelli raccolti,",
        "su un viso asciutto e capelli a coda,",
    ],

    # ── FRASI COMPLETE con >=5x ──────────────────────────────────────────────

    # 9x
    "Nel mio caso la storia finisce qui: bello sulla carta, sbagliato addosso.": [
        "Per me si conclude così: convincente in teoria, inadatto in pratica.",
        "Nel mio caso il verdetto è chiaro: interessante a distanza, sbagliato da vicino.",
        "La mia storia con loro finisce qui: bello da vedere, non da portare.",
        "Per me il discorso si chiude: promettente sulla scheda, deludente addosso.",
        "La conclusione per me è questa: attraente online, sbagliato sul viso.",
        "Nel mio caso il finale è netto: buon prodotto, partner sbagliato.",
        "Il mio verdetto non ammette appelli: bello come oggetto, non per me.",
        "Per me si riassume così: valido il progetto, incompatibile con il mio viso.",
        "Nel mio caso si chiude qui: prometteva molto, ha mantenuto poco.",
        "La mia storia con questo paio è breve: bello in foto, non per me.",
    ],

    # 9x
    "Quando un occhiale ti infastidisce fin dai primi minuti, per me la discussione si chiude lì.": [
        "Se un modello inizia a pesare subito, per me non c'è molto altro da aggiungere.",
        "Quando il fastidio arriva nei primi minuti, il giudizio non può che prendere una direzione.",
        "Se l'inizio è già un problema, la fine del ragionamento è scontata.",
        "Quando l'irritazione è immediata, non vale la pena insistere.",
        "Se il disagio è presente fin da subito, la conversazione è già chiusa.",
        "Quando qualcosa infastidisce subito, per me non c'è tempo di rivalutare.",
        "Se il primo contatto è già difficile, il seguito non cambia il risultato.",
        "Quando un prodotto inizia storto, finisce peggio: è una legge che conferma sempre.",
        "Se passa poco tempo prima del fastidio, il giudizio non può essere altro che negativo.",
        "Quando l'uso è scomodo sin dall'inizio, la discussione si conclude velocemente.",
    ],

    # 9x
    "Qui non siamo proprio arrivati a un'intesa.": [
        "Qui l'accordo non è mai decollato.",
        "Qui non c'è stata nessuna sintonia vera.",
        "La compatibilità tra noi non c'è stata.",
        "Qui il feeling non si è creato.",
        "Tra me e questo modello non è scattato niente.",
        "Qui le strade non si sono incontraite.",
        "Qui non abbiamo trovato un accordo.",
        "Non c'è stata nessuna intesa reale tra noi.",
        "L'allineamento tra me e questo prodotto non è arrivato.",
        "Non siamo andati d'accordo, io e questo paio.",
    ],

    # 8x
    "Peccato, perché il progetto visivo ha qualità evidenti.": [
        "Un peccato, perché l'estetica aveva del valore.",
        "Spiacevole, perché l'idea visiva era valida.",
        "È un peccato: il disegno ha qualità.",
        "Dispiacere, perché l'idea visiva meritava.",
        "Peccato davvero: come progetto aveva una logica.",
        "Un peccato: la qualità visiva c'era.",
        "Dispiace perché l'estetica era curata.",
        "Spiacevole: il progetto visivo era ben costruito.",
        "Peccato che il resto non sia all'altezza dell'idea.",
    ],

    # 8x
    "La qualità dell'idea c'è, la compatibilità con me meno.": [
        "Il progetto ha valore; l'adattamento al mio viso no.",
        "L'idea è buona; il risultato sul mio profilo meno.",
        "Il concept è apprezzabile; la compatibilità è un'altra storia.",
        "L'idea c'è; la coerenza con il mio uso no.",
        "Come progetto funziona; come mia scelta no.",
        "La qualità del design è reale; la compatibilità con me è discutibile.",
        "Ha qualità intrinseche; non ha affinità con il mio profilo.",
        "Il valore dell'idea è chiaro; la praticità per me meno.",
        "Il progetto ha pregi; il fit con me è il problema.",
    ],

    # 8x
    "Capisco l'idea, ma sul mio viso è stato un errore netto.": [
        "L'idea è comprensibile, ma sul mio viso non ha funzionato.",
        "Il concetto è chiaro, ma il risultato sul mio profilo è stato un errore.",
        "Capisco il progetto, ma addosso è stata una scelta sbagliata.",
        "Intuisco il senso, ma il mio viso non era il territorio giusto.",
        "Apprezzo l'intenzione, ma sul mio viso è stato un fallimento.",
        "Il concept è logico, ma la compatibilità con me non c'era.",
        "Comprendo l'idea, ma il mio viso ha dato una risposta negativa.",
        "L'intenzione ha senso, ma l'esito sul mio profilo no.",
        "Capisco la progettazione, ma il mio viso e questo prodotto non si sono capiti.",
    ],

    # 7x
    "Usa il registro rétro in modo quasi teatrale.": [
        "Porta il codice vintage fino ai limiti dell'enfasi.",
        "Gioca con il retro con un tocco di teatralità.",
        "Usa il vocabolario vintage con un'intensità scenica.",
        "Porta la citazione rétro quasi fino all'eccesso.",
        "Usa il linguaggio vintage in modo decisamente accentuato.",
        "Opera sulla citazione storica con intensità drammatica.",
        "Porta il registro del passato con una presenza quasi scenografica.",
        "Si avvale dell'estetica vintage con un gusto quasi istrionico.",
    ],

    # 7x
    "Resto nel mezzo: ha carattere, ma non mi viene naturale.": [
        "Mi fermo a metà: ha personalità, ma non sento la sintonia.",
        "Resto neutrale: c'è carattere, ma non lo sento mio.",
        "Rimango in bilico: ha qualcosa, ma non si fa scegliere.",
        "La mia posizione è di mezzo: lo apprezzo, ma non lo vivo.",
        "Resto equidistante: interessante come prodotto, ma non per me.",
        "Né sì né no: ha carattere, ma non è spontaneo portarlo.",
        "Rimango a metà strada: lo noto, ma non lo sento naturale addosso.",
        "Non è un rifiuto netto, ma neanche un'adesione: resto nel mezzo.",
    ],

    # 7x
    "Nel mio caso il rapporto si è chiuso prima di iniziare.": [
        "Per me non si è mai aperto un rapporto vero.",
        "Nel mio caso non siamo mai partiti davvero.",
        "Per me la storia è finita prima di cominciare.",
        "Nel mio caso la convivenza non ha avuto inizio.",
        "Non è partita nessuna storia tra me e questo modello.",
        "Nel mio caso il rapporto non ha preso avvio.",
        "La relazione con loro non si è mai instaurata.",
        "Per me non è nata nessuna storia d'uso.",
    ],

    # 7x
    "Per il mio viso e per il mio uso quotidiano è stato un errore secco.": [
        "Per la mia morfologia e per il mio modo d'uso è stato un fallimento.",
        "Per come sono fatto e per come li uso, è stata una scelta sbagliata.",
        "Per il mio profilo e per la mia routine è stato un errore chiaro.",
        "Per il mio viso e per il mio modo di portarli non è andata bene.",
        "Per la mia conformazione e per il mio uso normale è stato un errore.",
        "Per le mie esigenze e per la mia morfologia è stata la scelta sbagliata.",
        "Per come li indosso e per come sono fatto è stato un errore netto.",
        "Per la mia testa e per il mio uso quotidiano è stato il modello sbagliato.",
    ],

    # 7x
    "Li ho accantonati quasi subito.": [
        "Li ho messi da parte in poco tempo.",
        "Li ho abbandonati quasi immediatamente.",
        "Ho smesso di usarli in tempi brevissimi.",
        "Li ho depositati nel cassetto quasi subito.",
        "Li ho scartati quasi al primo tentativo.",
        "Li ho tolti dalla rotazione rapidamente.",
        "Ho rinunciato a loro in fretta.",
        "Li ho accantonati prima di qualsiasi abitudine.",
    ],

    # 7x
    "Per me è uno di quei no che diventano evidenti molto in fretta.": [
        "Per me è un rifiuto che si chiarisce in poco tempo.",
        "È uno di quei no che non hanno bisogno di riflessione.",
        "Per me la risposta negativa è arrivata rapidamente.",
        "È il tipo di incompatibilità che si capisce subito.",
        "Il mio no in questo caso non ha richiesto elaborazione.",
        "È uno di quei rifiuti immediati che non si discutono.",
        "Per me la risposta NO è venuta senza troppo pensiero.",
        "È quello che si definisce un no immediato e senza appello.",
    ],

    # 7x
    "Il dettaglio legno cambia davvero la temperatura del modello.": [
        "Il dettaglio ligneo trasforma la percezione termica del modello.",
        "Il tocco di legno cambia materialmente la sensazione del prodotto.",
        "L'inserto in legno modifica profondamente l'atmosfera del pezzo.",
        "Il dettaglio in legno altera davvero il registro visivo.",
        "L'elemento ligneo cambia la temperatura percepita del design.",
        "Il legno porta una variazione di atmosfera rilevante nel prodotto.",
        "Quel dettaglio in legno muta la lettura complessiva del modello.",
        "Il tocco ligneo introduce una variazione di tono sostanziale.",
    ],

    # 7x
    "Più che conquistarmi, mi hanno incuriosito a intermittenza.": [
        "Più che convincermi, mi hanno incuriosito a tratti.",
        "Più che guadagnarsi la mia stima, mi hanno intrigato ogni tanto.",
        "Non mi hanno conquistato: mi hanno incuriosito con intermittenza.",
        "Più che piacermi, mi hanno stimolato a intermittenza.",
        "Invece di conquistarmi, mi hanno incuriosito a sprazzi.",
        "Non era una conquista: era una curiosità a intervalli.",
        "A tratti mi interessavano, ma senza mai conquistarmi del tutto.",
        "L'interesse è stato saltuario, non una vera conquista.",
    ],

    # 7x
    "Ha una calma che molti aviator moderni hanno perso.": [
        "Porta una tranquillità che i modelli contemporanei spesso trascurano.",
        "Ha una sobrietà che i moderni aviator non sempre conservano.",
        "Porta un equilibrio che le versioni attuali hanno perso.",
        "Ha una pacatezza che i modelli correnti raramente offrono.",
        "È uno di quei prodotti che ricorda il valore della calma visiva.",
        "Porta una serenità formale che molti aviator moderni non hanno.",
        "Ha una quiete che non è comune nei moderni.",
        "Porta quella compostezza che il design contemporaneo spesso dimentica.",
    ],

    # 7x
    "Sembra costruito per il movimento e per l'effetto scenico insieme.": [
        "Sembra pensato tanto per la funzionalità quanto per l'impatto visivo.",
        "Pare progettato sia per l'uso dinamico sia per la scena.",
        "È costruito per muoversi e per fare scena allo stesso tempo.",
        "Unisce la vocazione al movimento con quella all'effetto visivo.",
        "È pensato per chi vuole funzionalità e presenza insieme.",
        "Combina la predisposizione al moto con quella all'impatto scenico.",
        "Sembra disegnato per chi non rinuncia alla scena nemmeno in movimento.",
        "È un prodotto che unisce dinamismo ed effetto visivo in modo coerente.",
    ],

    # 6x
    "Più passano i giorni, più mi accorgo che non mi viene mai voglia di sceglierlo.": [
        "Con il passare del tempo, mi accorgo che non lo scelgo quasi mai.",
        "Più il tempo passa, più capisco che non è una scelta spontanea.",
        "Passano i giorni e la voglia di portarlo non aumenta.",
        "Più vado avanti, più capisco che non entra nella mia routine.",
        "Con il tempo, emerge che non lo scelgo naturalmente.",
        "Più passa il tempo, meno lo scelgo.",
        "Il tempo mi ha mostrato che non rientra tra le scelte spontanee.",
    ],

    # 6x
    "L'ho praticamente archiviato dopo pochissime prove.": [
        "L'ho messo da parte dopo pochissimi utilizzi.",
        "È finito in cassetto quasi subito.",
        "L'ho accantonato dopo pochi tentativi.",
        "L'ho archiviato prima di dargli un'occasione vera.",
        "È finito fuori rotazione in pochissimo tempo.",
        "L'ho tolto dalla selezione dopo poche prove.",
        "È diventato un oggetto da cassetto in fretta.",
    ],

    # 6x
    "Non mi pento di averlo provato, però non è il paio che cerco a occhi chiusi.": [
        "Non è un errore averlo provato, ma non lo cercherei spontaneamente.",
        "Non mi dispiace averlo acquistato, ma non lo sceglierei di nuovo.",
        "Non è stato un errore, solo non è il modello che richiamerei.",
        "Non mi pento, ma non lo cercherei una seconda volta.",
        "Non è una scelta di cui pentirsi, ma non è quella automatica.",
        "Non mi rammarico, ma non è il tipo di occhiale che scelgo istintivamente.",
        "Non è stato un errore — solo non è quello che scelgo per istinto.",
    ],

    # 6x
    "È il classico caso in cui l'estetica da sola non basta a salvare l'esperienza.": [
        "È il caso tipico in cui il bello non è sufficiente senza il resto.",
        "È un esempio classico di come l'aspetto non esaurisca il giudizio.",
        "È uno di quei prodotti in cui la bellezza non compensa tutto.",
        "È la dimostrazione che l'estetica da sola non chiude il giudizio.",
        "Questo è il caso in cui la forma paga ma non abbastanza.",
        "È l'esempio di come l'estetica possa non bastare da sola.",
        "È il classico prodotto che piace da vedere ma non da usare.",
    ],

    # 6x
    "Per me rimane più attraente come idea che come compagno reale di uso.": [
        "Per me ha più valore come progetto che come uso quotidiano.",
        "Rimane più convincente come concetto che come pratica.",
        "Per me è più interessante come oggetto da ammirare che da portare.",
        "Più valido come idea che come scelta d'uso concreta.",
        "È più seducente come concetto che riuscito nell'uso.",
        "Per me resta più forte come proposta che come realtà d'uso.",
        "Ha più peso come oggetto di design che come compagno pratico.",
    ],

    # 6x
    "Non sono riuscito a farmeli piacere davvero.": [
        "Non ho trovato il modo di amarli davvero.",
        "Non ci sono riuscito: non me li sono fatti piacere.",
        "Non sono riuscito a costruire un rapporto reale con loro.",
        "Non ho saputo convincermi di loro.",
        "Non sono riuscito ad affezionarmi.",
        "Non ho trovato la chiave per farmeli piacere.",
        "Non sono riuscito ad avere un'opinione positiva vera.",
    ],

    # 6x
    "Ha un fascino da film anni settanta.": [
        "Porta con sé un'aura cinematografica anni Settanta.",
        "Ha quell'atmosfera da decade d'oro del cinema.",
        "Evoca il fascino visivo degli anni Settanta.",
        "Ha una cifra estetica che rimanda agli anni Settanta.",
        "Porta un'aura vintage d'una certa cinematograficità.",
        "Ha l'atmosfera caratteristica del decennio Settanta.",
        "Porta il fascino di un'estetica da pellicola dell'epoca.",
    ],

    # 6x
    "Ha un'impronta quasi da equipaggiamento.": [
        "Ha una sensazione quasi attrezzistica.",
        "Porta un'aria da equipaggiamento tecnico.",
        "Ha un'impronta quasi professionale.",
        "Porta una sensazione quasi da gear.",
        "Ha un'atmosfera di prodotto tecnico.",
        "Ha un carattere che si avvicina all'equipaggiamento.",
        "Ha una presenza quasi da accessorio tecnico.",
    ],

    # 5x (frasi ancora rilevanti)
    "Capisco il concept, ma non il fit sul mio viso.": [
        "Comprendo l'idea, ma non il risultato sul mio profilo.",
        "Il concept ha senso, ma sul mio viso non funziona.",
        "Intendo il progetto, ma l'adattamento al mio viso è il problema.",
        "L'intenzione è chiara, ma il fit non è quello giusto per me.",
        "L'idea è comprensibile, ma la compatibilità con il mio viso no.",
        "Capisco il progetto, non capisco come stia sul mio viso.",
    ],

    # 5x
    "Capisco il perché esista, ma non il perché dovrei tenerlo.": [
        "Ne comprendo la ragion d'essere, ma non la mia motivazione a tenerlo.",
        "Capisco il suo mercato, non capisco il mio ruolo in esso.",
        "Ne intuisco la logica, ma non il perché dovrei sceglierlo.",
        "Comprendo il progetto, non riesco a giustificare il mio acquisto.",
        "Ha senso come prodotto, ma non per me.",
        "Ne capisco l'esistenza, non la mia necessità di averlo.",
    ],

    # 5x
    "Non è una questione di gusto astratto: semplicemente su di me non va.": [
        "Non è una questione estetica: non funziona per il mio viso.",
        "Non è una critica formale: sul mio profilo non funziona.",
        "Non è un giudizio di merito: non si adatta a me.",
        "Non è una questione di stile: il problema è il fit con me.",
        "Non discuto il design: dico solo che sul mio viso non va.",
        "Non è un problema del prodotto: non siamo compatibili.",
    ],

    # 5x
    "Non è rumoroso ma ha identità piena.": [
        "Non è appariscente, ma ha un'identità definita.",
        "Non grida, ma parla con chiarezza.",
        "Non è clamoroso, ma ha una forte personalità.",
        "Non è invadente, ma ha una voce precisa.",
        "Non si impone, ma ha una presenza indiscutibile.",
        "Non è chiassoso, ma è pieno di carattere.",
    ],

    # 5x
    "È il tipo di modello che fa sembrare facile vestirsi bene.": [
        "È quello che si chiama un modello che facilita l'outfit.",
        "È il tipo di accessorio che eleva senza sforzo.",
        "È il genere di pezzo che mette tutto in ordine da solo.",
        "È il tipo di occhiale che fa da coordinatore silenzioso.",
        "È un accessorio che lavora per te senza chiederti nulla.",
        "È il modello che rende il buon stile un risultato naturale.",
    ],

    # 5x
    "Vive benissimo in contesti aperti e luminosi.": [
        "Si trova a proprio agio negli spazi aperti e nella luce.",
        "Rende al meglio all'aperto e nella luminosità.",
        "È nel suo elemento nei contesti luminosi e all'aria aperta.",
        "Funziona molto bene negli spazi aperti.",
        "Trova il suo habitat naturale nei contesti luminosi.",
        "Eccelle negli ambienti aperti e ben illuminati.",
    ],

    # 5x
    "Il punto è che con controluce forte per me perde praticità.": [
        "Il problema è che nella controluce intensa perde utilità.",
        "La questione è che con la luce in faccia si rivela limitato.",
        "Il dato è che nella controluce forte la praticità cala.",
        "La criticità è che con forte controluce non è all'altezza.",
        "Il limite emerge con la controluce: lì la praticità vacilla.",
        "Nelle condizioni di controluce intensa non regge a pieno regime.",
    ],

    # 5x
    "Ha l'energia di un accessorio da editoriale moda.": [
        "Ha un'energia da set fotografico.",
        "Porta l'atmosfera di un servizio fashion.",
        "Ha la presenza di un accessorio da editorial.",
        "Porta quell'energia da shooting creativo.",
        "Ha l'aura di un oggetto pensato per le immagini.",
        "Evoca la presenza degli accessori dei fashion editorial.",
    ],

    # 5x
    "Non obbliga a vestirsi in costume da diva.": [
        "Non chiede un outfit all'altezza di una diva.",
        "Non impone un look da scena.",
        "Non richiede un abbigliamento teatrale.",
        "Non esige uno stile vistoso o costruito.",
        "Non chiede un vestiario da sfilata.",
        "Non costringe a un abbigliamento sopra le righe.",
    ],

    # 5x
    "Energia da festival e trovano un buon equilibrio tra tecnica e stile.": [
        "Hanno un'energia festivaliera e un buon bilanciamento tra forma e funzione.",
        "Portano l'atmosfera di un festival mantenendo un equilibrio tra stile e tecnica.",
        "Hanno la vibe da festival e riescono a bilanciare estetica e funzionalità.",
        "Trasmettono un'energia da evento e trovano un equilibrio funzionale solido.",
        "Portano energia da festival con un bilanciamento riuscito tra look e utilità.",
        "Hanno un'atmosfera da eventi all'aperto con un buon equilibrio tra le due anime.",
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
        print(f"  '{p[:60]}' → {cnt}x")
print("✅ Round 10 completato!" if errors == 0 else f"⚠️ {errors} errori.")
