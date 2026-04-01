#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Parte 7: Pattern residui terzo passaggio (≥10x dopo secondo passaggio)
"""
from rewrite_reviews_part6 import PATTERNS

# ═══════════════════════════════════════════════════════════
# FRASI COMPLETE ≥ 10x
# ═══════════════════════════════════════════════════════════

# "Mi lascia con più rispetto che entusiasmo." (18x)
PATTERNS["Mi lascia con pi\u00f9 rispetto che entusiasmo."] = [
    "Il risultato è più stima che trasporto.",
    "Prevale il rispetto sull'entusiasmo nel mio giudizio.",
    "Lo considero più di quanto mi emozioni.",
    "La mia reazione è più di stima che di slancio.",
    "L'apprezzamento c'è, l'entusiasmo meno.",
    "Resto con un voto di testa, non di cuore.",
    "Lo riconosco, ma non mi scalda.",
    "Il giudizio è più razionale che emotivo.",
    "Lo stimo senza provare entusiasmo vero.",
    "Il rispetto supera l'emozione nel mio parere.",
    "Lo valuto bene senza provare quel trasporto in più.",
    "Finisco con più ammirazione che passione.",
    "Lo colloco nel reparto stima senza che arrivi al cuore.",
    "La stima è alta, l'entusiasmo resta contenuto.",
    "Lo giudico bene, ma il battito resta calmo.",
    "La testa dice sì, lo stomaco non esulta.",
    "Lo promuovo razionalmente senza provare slancio emotivo.",
    "Resta un modello che apprezzo a freddo, non a caldo.",
]

# "Il punto è sempre lo stesso: bello non vuol dire automaticamente giusto." (17x)
PATTERNS["Il punto \u00e8 sempre lo stesso: bello non vuol dire automaticamente giusto."] = [
    "La lezione è la solita: estetica e vestibilità non coincidono per forza.",
    "Riconferma la regola: bello non significa adatto.",
    "Il concetto è noto: il bello e il giusto raramente sono la stessa cosa.",
    "L'evidenza si ripete: la bellezza non garantisce la vestibilità.",
    "Bello sì, giusto per me no: la distinzione è sempre la stessa.",
    "La verità resta quella: l'estetica da sola non basta.",
    "Il dilemma è il solito: può essere bello senza essere adatto.",
    "Torno sempre allo stesso punto: bello e adatto sono concetti diversi.",
    "Resta la constatazione di sempre: piacere alla vista non equivale a funzionare.",
    "La lezione si ripete: il fascino estetico non si traduce in vestibilità automatica.",
    "Il tema è ricorrente: bellezza e compatibilità non vanno di pari passo.",
    "Mi ritrovo al punto di partenza: bello non equivale a giusto.",
    "La morale è sempre la solita: non tutto ciò che è bello è anche per me.",
    "La distinzione fondamentale resta: bello non implica adatto.",
    "Il nodo è quello di sempre: l'estetica non garantisce la resa.",
    "La costante è che bello e giusto per me non sono sinonimi.",
    "Ecco il punto: la bellezza non equivale alla compatibilità.",
]

# "Il risultato finale è buono, purché gli si conceda il terreno adatto." (16x)
PATTERNS["Il risultato finale \u00e8 buono, purch\u00e9 gli si conceda il terreno adatto."] = [
    "La resa finale è positiva, a patto di trovare il contesto giusto.",
    "Il bilancio è buono se gli si dà l'ambientazione corretta.",
    "Il risultato c'è, purché si scelga la situazione adatta.",
    "A conti fatti va bene, ma richiede il setting giusto.",
    "La resa finale convince nel contesto adeguato.",
    "Il bilancio è positivo se lo si colloca nella situazione giusta.",
    "Il risultato soddisfa, a patto di usarlo nel terreno adatto.",
    "Funziona bene, ma chiede le circostanze giuste.",
    "Il verdetto è buono, con la premessa del contesto appropriato.",
    "La resa è positiva quando il terreno è quello giusto.",
    "Il risultato tiene, purché si rispetti il suo ambito naturale.",
    "Il bilancio finale è favorevole nel setting corretto.",
    "Il risultato convince, a condizione di inquadrarlo bene.",
    "La resa è buona, sempre che il contesto collabori.",
    "Il bilancio è buono se lo si usa nel suo territorio.",
    "Il risultato finale è valido, nel contesto che gli compete.",
]

# "Non è perfetto, ma ha abbastanza qualità da farsi scegliere spesso." (16x)
PATTERNS["Non \u00e8 perfetto, ma ha abbastanza qualit\u00e0 da farsi scegliere spesso."] = [
    "Non è impeccabile, ma la sostanza lo rende una scelta ricorrente.",
    "Ha i suoi limiti, eppure lo scelgo spesso.",
    "Non brilla in ogni aspetto, ma lo prendo regolarmente.",
    "Qualche difetto c'è, ma torna in mano con frequenza.",
    "Non è il massimo, ma ha quel che serve per essere scelto spesso.",
    "Ha margini di miglioramento, ma la frequenza d'uso parla per lui.",
    "Non è senza pecche, eppure lo preferisco più spesso del previsto.",
    "Non raggiunge la perfezione, ma si fa scegliere con costanza.",
    "Ho da ridire su qualcosa, ma lo prendo spesso comunque.",
    "I difetti non mancano, ma neanche le occasioni per sceglierlo.",
    "Non è senza difetti, ma lo uso con una frequenza che dice tutto.",
    "Qualche limite c'è, ma non abbastanza da farmelo ignorare.",
    "Ha delle imperfezioni, eppure lo scelgo regolarmente.",
    "Non è inattaccabile, ma la frequenza con cui lo prendo lo promuove.",
    "Ha i suoi nei, ma è uno di quelli che afferro con regolarità.",
    "Le imperfezioni ci sono, eppure finisce spesso nella mia selezione.",
]

# "E lo dico da persona che di solito cambia idea solo a fatica." (15x)
PATTERNS["E lo dico da persona che di solito cambia idea solo a fatica."] = [
    "E lo dico io che sono lento a cambiare opinione.",
    "Che non è poco, visto che di solito non mi ricredo facilmente.",
    "E parlo da uno che di solito non si fa impressionare facilmente.",
    "È significativo, dato che le mie opinioni cambiano raramente.",
    "E lo dico come persona notoriamente testarda nei giudizi.",
    "E per me non è scontato: di solito sono piuttosto rigido nei pareri.",
    "Non è poca cosa, dato il mio carattere poco incline al ripensamento.",
    "È un risultato notevole per uno che cambia idea molto raramente.",
    "E lo sottolineo perché di norma sono molto fermo nei miei pareri.",
    "Non capita spesso che cambi giudizio, e questo dice qualcosa.",
    "Parlo da persona che non si ricrede facilmente.",
    "E per me è un segnale forte, dato che cambio idea con difficoltà.",
    "Il fatto che io lo ammetta dice molto, visto quanto sono ostinato.",
    "È un elemento rilevante per uno come me, che raramente si ricrede.",
    "E parlo da persona che tende a confermare le prime impressioni.",
]

# "La delusione non è totale, ma è abbastanza da fermarmi." (15x)
PATTERNS["La delusione non \u00e8 totale, ma \u00e8 abbastanza da fermarmi."] = [
    "Non è una delusione completa, ma sufficiente a farmi esitare.",
    "La delusione non è piena, però basta a bloccarmi.",
    "Non mi ha deluso del tutto, ma abbastanza da non convincermi.",
    "La delusione è parziale, ma sufficiente a non farmi procedere.",
    "Non è un fiasco totale, ma il disappunto basta a frenarmi.",
    "La delusione non è assoluta, ma abbastanza da tenermi lontano.",
    "Non mi ha deluso completamente, ma quanto basta per non sceglierlo.",
    "Il disappunto non è totale, ma è sufficiente a fermarmi.",
    "Non è una catastrofe, ma la delusione è abbastanza per non andare avanti.",
    "La delusione è contenuta ma basta a non convincermi.",
    "Non è una stroncatura, ma il disappunto è sufficiente per non sceglierlo.",
    "La delusione è parziale, eppure basta a non promuoverlo nel mio bilancio.",
    "Non è tutto negativo, ma il disappunto è abbastanza per non consigliarlo.",
    "La delusione non è drammatica, ma è sufficiente per non farmi tornare.",
    "Non è stata una rottura totale, però basta a non volerci riprovare.",
]

# "Rimane una promessa che sul mio viso non si compie." (14x)
PATTERNS["Rimane una promessa che sul mio viso non si compie."] = [
    "Resta un potenziale che sul mio volto non si concretizza.",
    "La promessa c'è, ma il mio viso non la mantiene.",
    "Il potenziale rimane astratto: sul mio volto non si realizza.",
    "È una promessa non mantenuta dalla compatibilità col mio viso.",
    "Resta un buon proposito che il mio volto non traduce in realtà.",
    "La promessa del design non trova conferma sul mio viso.",
    "In teoria funziona, nella pratica del mio viso no.",
    "Il potenziale non si attiva sul mio volto.",
    "Resta un'idea che non si compie sulla geometria del mio viso.",
    "La promessa non arriva a compiersi nel confronto col mio volto.",
    "È come un film con una bella trama che sul mio viso non funziona.",
    "Il progetto c'è, ma non si realizza sui miei lineamenti.",
    "La resa teorica non si conferma sul mio tipo di viso.",
    "Il potenziale rimane sulla carta: il mio volto non lo sblocca.",
]

# "Peccato, perché il progetto aveva elementi interessanti." (14x)
PATTERNS["Peccato, perch\u00e9 il progetto aveva elementi interessanti."] = [
    "Un peccato, visto che le premesse progettuali erano buone.",
    "Il rammarico nasce dal fatto che il progetto partiva bene.",
    "Dispiace perché gli ingredienti c'erano.",
    "Peccato davvero, le basi erano promettenti.",
    "Il progetto meritava di più di come si è concretizzato.",
    "Spiace, perché l'idea di partenza era interessante.",
    "Peccato, perché le premesse di design erano valide.",
    "Il rammarico è proporzionale al potenziale visto.",
    "Dispiace, perché il concetto di base aveva valore.",
    "Un vero peccato, considerato il livello delle premesse.",
    "La delusione è amplificata dal progetto che faceva ben sperare.",
    "Peccato, perché le premesse erano fra le più promettenti.",
    "Spiace, perché il punto di partenza prometteva bene.",
    "Peccato: le basi per qualcosa di ben riuscito c'erano tutte.",
]

# "Ogni volta che li indosso cambiano il tono dell'outfit in meglio." (13x)
PATTERNS["Ogni volta che li indosso cambiano il tono dell\u2019outfit in meglio."] = [
    "Li metto e l'intero outfit ne beneficia.",
    "Ogni volta che li indosso alzano il livello del look.",
    "Hanno il potere di migliorare qualsiasi outfit.",
    "Ogni indossata conferma che elevano il look.",
    "Aggiungono qualcosa a qualsiasi combinazione di abbigliamento.",
    "Il look migliora ogni volta che li aggiungo.",
    "Funzionano come un upgrade automatico per qualsiasi outfit.",
    "Ogni volta che li scelgo il risultato finale del look migliora.",
    "Hanno quell'effetto di alzare il tono di qualsiasi abbinamento.",
    "Riescono a valorizzare ogni outfit a cui li aggiungo.",
    "L'outfit esce vincente ogni volta che li includo.",
    "Portano il livello del look un gradino più su.",
    "Migliorano qualsiasi combinazione con la loro sola presenza.",
]
PATTERNS["Ogni volta che li indosso cambiano il tono dell'outfit in meglio."] = PATTERNS["Ogni volta che li indosso cambiano il tono dell\u2019outfit in meglio."]

# "Li promuovo con convinzione, anche se non sono perfetti." (13x)
PATTERNS["Li promuovo con convinzione, anche se non sono perfetti."] = [
    "Li approvo senza riserve, pur riconoscendo qualche limite.",
    "Li consiglio con decisione, imperfezioni comprese.",
    "Li promuovo volentieri nonostante qualche piccola mancanza.",
    "Il mio giudizio è positivo e convinto, difetti inclusi.",
    "Li consiglio con sicurezza, anche con i loro piccoli nei.",
    "Li approvo con fermezza, pur non essendo impeccabili.",
    "Li promuovo senza troppi se, anche se qualcosa manca.",
    "Il verdetto è positivo e chiaro, limiti compresi.",
    "Li consiglio con convinzione pur riconoscendone i difetti minori.",
    "Li promuovo sapendo che non sono perfetti, ma abbastanza validi.",
    "Il mio sì è convinto, anche se non sono esenti da pecche.",
    "Li approvo con slancio, accettando le piccole imperfezioni.",
    "Li consiglio a chi cerca qualcosa di buono, non di perfetto.",
]

# "Finisce tra i paia che guardo più di quanto indossi." (13x)
PATTERNS["Finisce tra i paia che guardo pi\u00f9 di quanto indossi."] = [
    "Finisce nella categoria di quelli che ammiro più che portare.",
    "Va a finire fra i paia che apprezzo più che utilizzo.",
    "Si colloca tra gli occhiali che stimo più di quanto scelga.",
    "Rientra fra quelli che guardo nel cassetto più di quanto indossi.",
    "Finisce tra quelli che appoggio ma non prendo spesso.",
    "Entra nel gruppo di quelli che ammiro a distanza.",
    "Resta fra i paia che contemplo senza portarli davvero.",
    "Si piazza fra quelli che noto più di quanto selezioni.",
    "Va a finire nella fascia di quelli che stimo più di quanto usi.",
    "Rientra tra quelli che guardo con piacere ma scelgo con meno frequenza.",
    "Finisce fra i paia che rispetto più di quanto indossi.",
    "Va nella categoria dei modelli che noto nel cassetto senza prenderli.",
    "Si colloca tra gli occhiali che il giudizio promuove più dell'uso.",
]

# "Sono più intelligenti che appariscenti, che per me vale doppio." (13x)
PATTERNS["Sono pi\u00f9 intelligenti che appariscenti, che per me vale doppio."] = [
    "Sono più arguti che vistosi, e per me questo conta tantissimo.",
    "La sottigliezza prevale sull'appariscenza, e io apprezzo.",
    "L'intelligenza del design batte la vistosità, che è ciò che cerco.",
    "Preferisco sempre l'acume al clamore, e questi lo esprimono bene.",
    "La raffinatezza supera la vistosità, il che nel mio metro è un gran pregio.",
    "Puntano sulla sostanza più che sullo spettacolo, e per me è un valore.",
    "Sono più sottili che rumorosi, e questo per me è un pregio doppio.",
    "L'intelligenza del design è il loro punto di forza più grande.",
    "Colpiscono per la raffinatezza, non per la vistosità: esattamente ciò che cerco.",
    "Sono più pensati che appariscenti, e per me è il massimo complimento.",
    "Preferiscono l'acume alla scenografia, e io lo considero un merito.",
    "Sono più profondi che clamorosi, il che per me vale più di tutto.",
    "La loro forza è nella sottigliezza, non nel volume: esattamente il mio linguaggio.",
]

# "Li ricomprerei senza pensarci troppo." (13x)
PATTERNS["Li ricomprerei senza pensarci troppo."] = [
    "Se dovessi riacquistarli, non esiterei.",
    "Li rifarei senza troppe riflessioni.",
    "Un riacquisto che farei senza indugio.",
    "Non ci penserei due volte a ricomprarli.",
    "Li ricomprerei al volo.",
    "Se li perdessi, li riprenderei immediatamente.",
    "Se tornassi indietro, il riacquisto sarebbe automatico.",
    "La riconferma sarebbe immediata se dovessi riacquistarli.",
    "Non avrei esitazioni a rifarne l'acquisto.",
    "Li ricomprerei senza il minimo dubbio.",
    "Il riacquisto non richiederebbe alcuna riflessione.",
    "Se dovessi scegliere di nuovo, li riprenderei subito.",
    "La decisione di riacquistarli sarebbe istantanea.",
]

# "E infatti la differenza, come spesso accade, la fa il modo in cui si appoggia sul viso." (13x)
PATTERNS["E infatti la differenza, come spesso accade, la fa il modo in cui si appoggia sul viso."] = [
    "Come al solito, è la calzata sul viso a decidere l'esito.",
    "E come capita spesso, tutto si decide nell'appoggio sul volto.",
    "Ancora una volta, ciò che fa la differenza è come cade sul viso.",
    "La resa dipende, come sempre, da come si posa sul volto.",
    "Il discrimine è, come spesso succede, la calzata.",
    "Come prevedibile, è la resa sul viso a determinare tutto.",
    "E come spesso accade, il segreto è nell'appoggio sul volto.",
    "La differenza cruciale, come al solito, la fa la vestibilità sul viso.",
    "Ancora una volta il modo in cui sta sul volto è il fattore chiave.",
    "Come succede di frequente, il giudizio lo decide la calzata.",
    "Al solito, è il modo in cui si appoggia ai tratti del viso a fare la differenza.",
    "Come spesso nella mia esperienza, la calzata sul viso è il giudice finale.",
    "La variabile chiave è, come spesso capita, la resa sulla faccia.",
]

# "C'è un'aria quasi cinematografica nel modo in cui incorniciano lo sguardo." (12x)
PATTERNS["C\u2019\u00e8 un\u2019aria quasi cinematografica nel modo in cui incorniciano lo sguardo."] = [
    "Incorniciano lo sguardo con un effetto quasi da cinema.",
    "C'è un che di cinematografico nel modo in cui esaltano lo sguardo.",
    "L'effetto sullo sguardo ha una qualità quasi filmica.",
    "Danno allo sguardo una cornice che sembra uscita da un film.",
    "L'incorniciatura dello sguardo ha un fascino quasi cinematografico.",
    "L'effetto visivo sullo sguardo richiama atmosfere da cinema.",
    "Danno un taglio quasi filmico allo sguardo.",
    "L'impatto sullo sguardo ha una teatralità quasi da pellicola.",
    "Valorizzano lo sguardo con un effetto che ricorda il grande schermo.",
    "Lo sguardo acquista una dimensione quasi cinematografica.",
    "L'effetto che danno agli occhi è quasi da pellicola d'autore.",
    "Regalano allo sguardo una cornice con un sapore da cinema.",
]
PATTERNS["C'\u00e8 un'aria quasi cinematografica nel modo in cui incorniciano lo sguardo."] = PATTERNS["C\u2019\u00e8 un\u2019aria quasi cinematografica nel modo in cui incorniciano lo sguardo."]

# "Per me resta sospeso tra idea riuscita e uso intermittente." (11x)
PATTERNS["Per me resta sospeso tra idea riuscita e uso intermittente."] = [
    "Resto in un limbo fra il progetto che ammiro e l'uso che ne faccio.",
    "Il giudizio oscilla fra idea ben riuscita e utilizzo saltuario.",
    "Sto in bilico fra il concetto che apprezzo e l'uso che non diventa costante.",
    "Resta sospeso: lo stimo come idea, lo uso meno del dovuto.",
    "Il mio verdetto è diviso fra il valore del progetto e la frequenza d'uso.",
    "Il concetto mi piace, l'uso non segue con la stessa intensità.",
    "Apprezzo il progetto più di quanto lo traduca in uso.",
    "Il gap fra idea e utilizzo è il centro del mio giudizio.",
    "Il giudizio resta a metà: grande idea, uso discontinuo.",
    "Mi trovo fra l'ammirazione per il progetto e la discontinuità dell'uso.",
    "Lo stimo come prodotto, lo scelgo meno di quanto vorrei.",
]

# "Hanno quel tipo di design che fa sembrare tutto più pensato." (11x)
PATTERNS["Hanno quel tipo di design che fa sembrare tutto pi\u00f9 pensato."] = [
    "Hanno un design che aggiunge intenzione a qualsiasi look.",
    "Il loro design fa sembrare ogni outfit più curato.",
    "Danno un'aria di maggiore cura a qualsiasi abbinamento.",
    "Il design trasmette un senso di intenzionalità al resto del look.",
    "Fanno sembrare ogni scelta di outfit più deliberata.",
    "Il loro stile conferisce al look un'apparenza di maggiore ricercatezza.",
    "Aggiungono un livello di cura percepita a qualsiasi combinazione.",
    "Il design comunica attenzione e fa sembrare il look più ragionato.",
    "Hanno quel tipo di linea che rende tutto il look più intenzionale.",
    "L'effetto del loro design è di elevare la percezione di cura complessiva.",
    "Danno al look un'aria di progettazione che prima non c'era.",
]

# "Ci vedo valore, semplicemente non sempre per il mio modo di vestirmi o di usarlo." (11x)
PATTERNS["Ci vedo valore, semplicemente non sempre per il mio modo di vestirmi o di usarlo."] = [
    "Riconosco il valore, ma non sempre si sposa con il mio stile.",
    "Il merito c'è, solo non sempre compatibile con le mie abitudini.",
    "Il valore lo vedo, la compatibilità col mio modo di vestire meno.",
    "Ha delle qualità, che però non sempre si allineano al mio uso.",
    "Riconosco ciò che offre, non sempre si adatta al mio modo di portarlo.",
    "Il valore è innegabile, la sintonia con il mio stile non sempre.",
    "Oggettivamente valido, soggettivamente non sempre adatto a me.",
    "Ha merito, che però si scontra a volte con il mio modo di vestire.",
    "Lo stimo per quel che è, ma non si adatta sempre al mio uso.",
    "Il valore è reale, la compatibilità con il mio stile variabile.",
    "Apprezzo ciò che offre, anche se non sempre funziona per me.",
]

# "Sulla carta interessante, nella pratica molto meno." (11x)
PATTERNS["Sulla carta interessante, nella pratica molto meno."] = [
    "In teoria promettente, in pratica deludente.",
    "Interessante a livello concettuale, meno nella resa.",
    "L'idea è buona, la traduzione pratica meno.",
    "Sulla carta funziona, nella realtà perde quota.",
    "Il progetto convince, la pratica molto meno.",
    "In astratto interessante, nel concreto meno convincente.",
    "Bello da pensare, meno da vivere.",
    "L'interesse teorico non si traduce in soddisfazione pratica.",
    "Più affascinante in teoria che efficace nella pratica.",
    "La realtà non tiene il passo della premessa.",
    "L'idea è più forte dell'esecuzione pratica.",
]

# ═══════════════════════════════════════════════════════════
# FRASI 10x
# ═══════════════════════════════════════════════════════════

# "Molto dipende dal volto, ancora più dallo stile personale." (10x)
PATTERNS["Molto dipende dal volto, ancora pi\u00f9 dallo stile personale."] = [
    "Il risultato varia col viso e ancor più con lo stile.",
    "Il volto conta, lo stile personale ancora di più.",
    "La resa cambia molto in base al viso e allo stile di chi lo porta.",
    "È un modello dove il viso e lo stile personale pesano enormemente.",
    "Il giudizio dipende dal volto ma soprattutto dal modo di vestirsi.",
    "La variabile più forte è il viso, seguita dallo stile personale.",
    "Il viso è importante, lo stile lo è ancora di più nella resa.",
    "Il risultato è molto legato al volto e al guardaroba di chi lo indossa.",
    "Il tipo di viso conta, ma lo stile personale è ancora più determinante.",
    "La resa è profondamente influenzata dal viso e dal modo di vestire.",
]

# "Non lo boccio, ma non è il paio che cerco istintivamente." (10x)
PATTERNS["Non lo boccio, ma non \u00e8 il paio che cerco istintivamente."] = [
    "Non lo rifiuto, ma non è quello a cui mi rivolgo d'istinto.",
    "Non è una bocciatura, ma nemmeno la mia prima scelta.",
    "Non lo scarto, ma il mio istinto non lo cerca.",
    "Non lo escludo, ma non è il paio a cui penso per primo.",
    "Non è un no, ma l'istinto mi porta altrove.",
    "Non lo condanno, ma non lo scelgo d'impulso.",
    "Non è bocciato, eppure non è il paio che la mano cerca per primo.",
    "Non lo rigetto, ma non è quello che scelgo spontaneamente.",
    "Non lo respingo, ma il riflesso non è di cercarlo.",
    "Non lo metto in discussione, ma l'istinto non va verso di lui.",
]

# "Lo capisco, ma non lo vivo con naturalezza." (10x)
PATTERNS["Lo capisco, ma non lo vivo con naturalezza."] = [
    "Ne comprendo il senso, ma non mi viene naturale portarlo.",
    "Intellettualmente ci arrivo, nella pratica non scorre.",
    "Lo capisco razionalmente, non lo sento spontaneo.",
    "Il progetto lo apprezzo, il feeling naturale manca.",
    "Lo comprendo ma non lo vivo con spontaneità.",
    "Razionalmente lo accetto, istintivamente non scorre.",
    "Ne colgo il valore, ma non mi viene naturale usarlo.",
    "Lo capisco con la testa, il corpo non segue con la stessa naturalezza.",
    "Comprendo le sue qualità senza viverle con scioltezza.",
    "L'idea la capisco, la naturalezza nell'uso manca.",
]

# "Li valuto bene come oggetto, un po' meno come risposta universale." (10x)
PATTERNS["Li valuto bene come oggetto, un po\u2019 meno come risposta universale."] = [
    "Come prodotto li apprezzo, come scelta universale meno.",
    "Il valore come oggetto c'è, la trasversalità meno.",
    "Come prodotto li promuovo, come consiglio universale no.",
    "Oggettivamente validi, universalmente meno.",
    "Come artefatto li rispetto, come scelta per tutti meno.",
    "Li giudico bene come prodotto, meno come scelta generalizzabile.",
    "La qualità dell'oggetto è alta, la sua universalità meno.",
    "Come oggetto sono validi, come risposta trasversale parzialmente.",
    "Il merito come prodotto c'è, quello come scelta universale meno.",
    "Come oggetto eccellenti, come raccomandazione generica un po' meno.",
]
PATTERNS["Li valuto bene come oggetto, un po' meno come risposta universale."] = PATTERNS["Li valuto bene come oggetto, un po\u2019 meno come risposta universale."]

# "Mi piace che non cerchino di piacere a tutti, ma a chi li capisce sì." (10x)
PATTERNS["Mi piace che non cerchino di piacere a tutti, ma a chi li capisce s\u00ec."] = [
    "Apprezzo che non puntino alla massa ma a chi ha la sensibilità per apprezzarli.",
    "Il bello è che non cercano il consenso universale, ma parlano al loro pubblico.",
    "Mi piace il fatto che non siano democratici ma selettivi nel loro appeal.",
    "Il loro bello è che non inseguono tutti: parlano a chi li sa leggere.",
    "Apprezzo la loro coerenza nel non cercare di piacere indistintamente.",
    "Non cercano il plauso generale, e a chi li capisce offrono molto.",
    "Il fatto che non siano per tutti è parte del loro fascino.",
    "Mi piace che parlino a un pubblico preciso invece che a tutti.",
    "La loro forza è non inseguire l'universalità ma la coerenza.",
    "Apprezzo che scelgano il proprio pubblico invece di corteggiare tutti.",
]

# ═══════════════════════════════════════════════════════════
# SEGMENTI INTERNI FREQUENTI (≥12x)
# ═══════════════════════════════════════════════════════════

# "mi interessa il giorno dopo" (27x) — segmento interno (es: "se mi interessa il giorno dopo")
PATTERNS["mi interessa il giorno dopo"] = [
    "mi convince anche a distanza di un giorno",
    "regge il giudizio del giorno seguente",
    "supera la prova del giorno dopo",
    "mi piace ancora il mattino seguente",
    "resiste al ripensamento del giorno successivo",
    "mantiene il suo appeal anche a freddo",
    "continua a piacermi anche dopo averci dormito su",
    "mi convince ancora ripensandoci il giorno dopo",
    "passa il test del ripensamento notturno",
    "mi interessa ancora quando ci torno sopra",
    "resiste alla riflessione del giorno seguente",
    "mi piace ancora ripensandoci con calma",
    "supera il vaglio del giorno successivo",
    "mi convince ancora con la mente fresca",
    "mantiene il fascino a distanza di ore",
    "regge il giudizio a mente fredda",
    "mi piace ancora quando ci ripenso",
    "passa il test del giudizio a freddo",
    "mi convince anche a distanza di tempo",
    "resta valido anche ripensandoci con lucidità",
    "mi persuade ancora il mattino dopo",
    "mantiene la sua presa anche a distanza",
    "mi interessa ancora con il senno di poi",
    "mi piace anche a freddo, il giorno seguente",
    "il mio interesse resta anche dopo la prima emozione",
    "mi fa tornare con la mente anche dopo ore",
    "il fascino non svanisce col passare delle ore",
]

# "e lì si è comportato meglio del previsto" (13x)
PATTERNS["e l\u00ec si \u00e8 comportato meglio del previsto"] = [
    "e in quel contesto ha superato le mie aspettative",
    "e lì ha dato una resa migliore di quanto mi aspettassi",
    "e in quella situazione mi ha sorpreso positivamente",
    "e lì ha mostrato più di quanto pensassi",
    "e in quel frangente ha reso oltre le aspettative",
    "e proprio lì ha dato il meglio di sé",
    "e in quella circostanza ha performato sopra le attese",
    "e lì ha dato una resa inaspettatamente buona",
    "e in quell'occasione ha sorpreso in positivo",
    "e lì ha espresso una qualità superiore alle attese",
    "e proprio lì mi ha convinto più del previsto",
    "e in quel contesto ha mostrato il suo lato migliore",
    "e lì ha superato ciò che immaginavo",
]

# "ma non abbastanza da farmi sciogliere del tutto" (12x)
PATTERNS["ma non abbastanza da farmi sciogliere del tutto"] = [
    "ma non abbastanza da convincermi completamente",
    "ma non al punto da farmi cedere del tutto",
    "ma non quanto basta per il mio sì pieno",
    "ma non abbastanza da vincere tutte le mie resistenze",
    "ma non fino al punto di farmi capitolare",
    "ma non tanto da dissolvermi le ultime riserve",
    "ma non a sufficienza per ottenere la mia resa totale",
    "ma non quanto basta per farmi arrendere completamente",
    "ma non al livello da farmi cedere ogni riserva",
    "ma non in misura sufficiente a conquistarmi del tutto",
    "ma non abbastanza da eliminare le mie ultime perplessità",
    "ma senza riuscire a farmi superare ogni esitazione",
]

print(f"Parte 7 caricata: totale {len(PATTERNS)} pattern definiti")
