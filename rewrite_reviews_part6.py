#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Parte 6: Pattern residui a bassa frequenza (5–19x) - frasi chiusura/apertura restanti
"""
from rewrite_reviews_part5 import PATTERNS

# ═══════════════════════════════════════════════════════════
# PATTERN 10-19x
# ═══════════════════════════════════════════════════════════

# "Lo promuovo senza esitazioni" — variante breve (può apparire anche in parte 5, gestiamo duplicato)
# Saltiamo per evitare conflitto con la frase lunga in parte 5.

# "Mi ha dato subito fiducia" — variante breve (coperta in parte 4)
# Saltiamo.

# "Non è una condanna universale" — coperta in parte 4
# Saltiamo.

# "È il genere di acquisto che mi fa venire voglia" — più breve (coperta)
# Saltiamo.

# "Con i suoi limiti" — già coperta in parte 4
# Saltiamo.

# Frasi nuove non coperte:

# "Non lo boccio, ma non lo scelgo nemmeno con slancio." (~18x)
PATTERNS["Non lo boccio, ma non lo scelgo nemmeno con slancio."] = [
    "Non lo condanno, ma non lo prendo neppure con entusiasmo.",
    "Non è bocciato, ma neanche scelto con convinzione.",
    "Non lo scarto, ma non lo scelgo con particolare entusiasmo.",
    "Non lo rifiuto, ma non è nemmeno la mia prima scelta.",
    "Non lo rigetto, ma manca lo slancio nel sceglierlo.",
    "Non è un no, ma neanche un sì convinto.",
    "Non lo escludo, ma non lo prendo con trasporto.",
    "Non lo metto da parte, ma neanche lo scelgo per primo.",
    "Non lo boccio, ma lo scelgo senza grande entusiasmo.",
    "Non è da scartare, ma non è nemmeno da prendere per primo.",
    "Non lo respingo, ma non lo porto nemmeno con entusiasmo.",
    "Non lo ignoro, ma la mia scelta non è entusiasta.",
    "Non è un rifiuto, ma manca la voglia spontanea di prenderlo.",
    "Non è negativo, ma il mio impulso non è di sceglierlo.",
    "Non lo condanno, ma non mi viene naturale preferirlo.",
    "Non lo rigetto, ma non mi scatta la voglia di portarlo.",
    "Non è un no deciso, ma nemmeno un sì sentito.",
    "Non è una bocciatura, ma manca la voglia spontanea.",
]

# "Mi sembra onesto riconoscerlo." (~15x)
PATTERNS["Mi sembra onesto riconoscerlo."] = [
    "È giusto ammettere questo punto.",
    "Sarebbe disonesto non riconoscerlo.",
    "Per onestà lo dico chiaramente.",
    "Mi sembra corretto evidenziarlo.",
    "Sarebbe scorretto non ammetterlo.",
    "Per trasparenza lo sottolineo.",
    "Doveroso ammetterlo.",
    "Per correttezza lo segnalo.",
    "Onestamente lo riconosco.",
    "Non posso evitare di ammetterlo.",
    "Mi sento in dovere di sottolinearlo.",
    "Sarebbe sleale non riconoscerlo.",
    "L'onestà mi impone di ammetterlo.",
    "Devo per correttezza evidenziarlo.",
    "Per trasparenza, va riconosciuto.",
]

# "Non è che non capisca il progetto, è che non lo sento mio." (~16x)
PATTERNS["Non \u00e8 che non capisca il progetto, \u00e8 che non lo sento mio."] = [
    "Comprendo l'idea, ma non mi appartiene.",
    "Capisco il concetto, ma non mi parla.",
    "Il progetto è chiaro, ma non è per me.",
    "Ne capisco le ragioni, ma non risuono con loro.",
    "Intellettualmente apprezzo, ma emotivamente non è il mio.",
    "Vedo il valore ma non mi rappresenta.",
    "L'idea la colgo, la connessione personale meno.",
    "Il concetto lo capisco: è la mia adesione che manca.",
    "Razionalmente capisco: personalmente non lo sento.",
    "Il progetto lo comprendo, ma non lo faccio mio.",
    "Non è una questione di comprensione, è di affinità.",
    "Rispetto l'intenzione, ma non mi ci ritrovo.",
    "L'idea è giusta, il feeling con me no.",
    "Il concetto arriva, la mia connessione no.",
    "Capisco cosa vuole fare, ma la mia risposta emotiva è tiepida.",
    "Apprezzo il progetto per quel che è, ma non è per me.",
]

# "La mia opinione non è una sentenza definitiva, è un racconto d'uso." (~14x)
PATTERNS["La mia opinione non \u00e8 una sentenza definitiva, \u00e8 un racconto d\u2019uso."] = [
    "Il mio parere è la cronaca di un'esperienza, non un verdetto universale.",
    "Non pretendo di dare un giudizio assoluto: racconto come è andata.",
    "Più che un verdetto, è la narrazione della mia esperienza.",
    "La mia è una testimonianza personale, non un giudizio definitivo.",
    "Racconto ciò che ho vissuto, senza pretese di generalizzare.",
    "È la cronaca del mio uso, non una sentenza irrevocabile.",
    "Il mio è un racconto pratico, non una valutazione universale.",
    "Non è un verdetto: è la storia del mio rapporto con questo modello.",
    "La mia opinione è figlia dell'uso, non della teoria.",
    "Più che giudicare, racconto la mia esperienza.",
    "Non emetto sentenze: condivido la mia esperienza diretta.",
    "È un diario d'uso, non un tribunale.",
    "La mia testimonianza è pratica, non dogmatica.",
    "Racconto come è andata, senza pretendere di avere l'ultima parola.",
]
PATTERNS["La mia opinione non \u00e8 una sentenza definitiva, \u00e8 un racconto d'uso."] = PATTERNS["La mia opinione non \u00e8 una sentenza definitiva, \u00e8 un racconto d\u2019uso."]

# "Ha pregi che riconosco e limiti che sento." (~13x)
PATTERNS["Ha pregi che riconosco e limiti che sento."] = [
    "Ha qualità che apprezzo e difetti che avverto.",
    "I meriti li vedo, le mancanze le percepisco.",
    "Ha lati positivi evidenti e limiti altrettanto reali.",
    "Le qualità sono innegabili così come le debolezze.",
    "Ha punti di forza che apprezzo e limiti che non ignoro.",
    "Ha meriti tangibili e limiti altrettanto concreti.",
    "Riconosco le qualità e avverto i limiti con uguale chiarezza.",
    "Ha pregi che rispetto e limiti che noto.",
    "Le qualità le riconosco, i limiti li sento sulla pelle.",
    "Ha aspetti positivi che colgo e mancanze che percepisco.",
    "I meriti sono là, così come i limiti.",
    "Ha qualità che non discuto e limiti che non nascondo.",
    "Ha pregi reali e limiti altrettanto reali.",
]

# "Non è il modello che porto più spesso, ma è quello che metto quando voglio sentirmi preciso." (~12x)
PATTERNS["Non \u00e8 il modello che porto pi\u00f9 spesso, ma \u00e8 quello che metto quando voglio sentirmi preciso."] = [
    "Non è il più frequente nella rotazione, ma è la scelta quando voglio essere impeccabile.",
    "Non lo scelgo ogni giorno, ma per i momenti dove conta è il mio preferito.",
    "Lo uso meno spesso, ma nei momenti giusti è l'unica scelta.",
    "Non è l'abituale, ma quando voglio essere al massimo è il primo che prendo.",
    "Lo porto meno spesso ma con più intenzione degli altri.",
    "Non è il quotidiano, ma la scelta riservata ai momenti che contano.",
    "Non è il più usato, ma è quello che metto quando voglio distinguermi.",
    "Lo uso meno ma meglio: è il pezzo delle occasioni giuste.",
    "Non lo prendo ogni mattina, ma quando lo scelgo è sempre con convinzione.",
    "È meno frequente nella mia rotazione, ma ha il peso maggiore.",
    "Non è il primo che afferro, ma è il primo quando voglio fare colpo.",
    "Lo porto in modo selettivo, il che paradossalmente ne aumenta il valore.",
]

# "Tra chi cerca qualcosa di misurato ma con personalità, questo modello ha il suo pubblico." (~11x)
PATTERNS["Tra chi cerca qualcosa di misurato ma con personalit\u00e0, questo modello ha il suo pubblico."] = [
    "Ha il suo target: chi vuole equilibrio e carattere insieme.",
    "Per chi cerca sobrietà con un tocco di personalità, è il modello giusto.",
    "Il suo pubblico ideale è chi apprezza la misura senza rinunciare al carattere.",
    "Per chi preferisce la discrezione con personalità, questo modello è centrato.",
    "Ha un target chiaro: chi vuole eleganza misurata con un'anima.",
    "Il modello parla a chi cerca equilibrio senza banalità.",
    "Per chi desidera qualcosa di sobrio ma non anonimo, il modello funziona.",
    "Ha il suo spazio tra chi apprezza la misura e il carattere.",
    "Il target è chi cerca raffinatezza senza rinunciare alla personalità.",
    "Parla a chi vuole essere misurato senza essere noioso.",
    "Il pubblico ideale è chi apprezza il buon gusto con un pizzico di originalità.",
]

# "Non lo amo, non lo odio: lo registro come un'esperienza utile." (~10x)
PATTERNS["Non lo amo, non lo odio: lo registro come un\u2019esperienza utile."] = [
    "Non mi entusiasma né mi delude: ne prendo nota come esperienza.",
    "Non è amore e non è rifiuto: è un dato che archivio.",
    "Non lo amo e non lo respingo: lo catalogo come esperienza.",
    "Non mi scalda né mi raffredda: ne tengo traccia come prova utile.",
    "Non è passione e non è antipatia: è un'esperienza da registrare.",
    "Non è né un colpo di fulmine né una delusione: è un punto di osservazione.",
    "Non provoca entusiasmo né rifiuto: lo archivio come esperienza formativa.",
    "Non mi convince del tutto e non mi allontana: è una conoscenza acquisita.",
    "Non lo amo e non lo condanno: è un capitolo di esperienza.",
    "Le emozioni non sono estreme: lo catalogo come prova concreta.",
]
PATTERNS["Non lo amo, non lo odio: lo registro come un'esperienza utile."] = PATTERNS["Non lo amo, non lo odio: lo registro come un\u2019esperienza utile."]

# "Il comfort è il suo punto più debole, e purtroppo per me è un parametro non negoziabile." (~10x)
PATTERNS["Il comfort \u00e8 il suo punto pi\u00f9 debole, e purtroppo per me \u00e8 un parametro non negoziabile."] = [
    "Il comfort è la nota dolente, e per me la comodità non è trattabile.",
    "La comodità è dove cede, e nel mio metro il comfort è essenziale.",
    "Il punto debole è il comfort, e io sul comfort non transigo.",
    "Il comfort lascia a desiderare, e per me è un aspetto irrinunciabile.",
    "Dove cede è nel comfort, e questo per me è un criterio non negoziabile.",
    "La comodità è il suo tallone d'Achille, e io non faccio sconti sul comfort.",
    "Il comfort non è all'altezza, e per me è la prima cosa che conta.",
    "Il suo punto debole è la comodità, che nel mio metro viene prima di tutto.",
    "Il comfort non regge, e io sul comfort non accetto compromessi.",
    "La resa in termini di comfort è insufficiente, e la comodità per me è fondamentale.",
]

# "La cosa che mi colpisce di più è l'equilibrio generale." (~10x)
PATTERNS["La cosa che mi colpisce di pi\u00f9 \u00e8 l\u2019equilibrio generale."] = [
    "Ciò che mi impressiona maggiormente è la coerenza complessiva.",
    "L'aspetto più sorprendente è l'armonia d'insieme.",
    "Quello che mi colpisce è il bilanciamento del tutto.",
    "Il tratto più notevole è la coesione complessiva.",
    "L'aspetto più convincente è l'equilibrio tra i vari elementi.",
    "Quello che mi resta è la calibratura dell'insieme.",
    "Il punto forte è l'armonia generale.",
    "Ciò che più mi convince è la coerenza del quadro d'insieme.",
    "Il tratto più meritevole è il bilanciamento complessivo.",
    "L'elemento più sorprendente è la riuscita armonia dell'insieme.",
]
PATTERNS["La cosa che mi colpisce di pi\u00f9 \u00e8 l'equilibrio generale."] = PATTERNS["La cosa che mi colpisce di pi\u00f9 \u00e8 l\u2019equilibrio generale."]

# "Il risultato è un modello che ammiro più di quanto viva." (~9x)
PATTERNS["Il risultato \u00e8 un modello che ammiro pi\u00f9 di quanto viva."] = [
    "Il bilancio è di un modello che rispetto più di quanto porti.",
    "Il risultato è un oggetto che stimo ma non vivo a pieno.",
    "Finisco per ammirarlo più che utilizzarlo concretamente.",
    "Il giudizio è di ammirazione più che di uso effettivo.",
    "Resto con un modello che apprezzo più di quanto indossi.",
    "Il risultato è un rispetto teorico più alto dell'uso pratico.",
    "Finisco per stimarlo più di quanto lo scelga davvero.",
    "Il modello guadagna più la mia stima che il mio tempo.",
    "La mia ammirazione supera il mio utilizzo concreto.",
]

# "È un modello che ha bisogno del contesto giusto per esprimersi." (~10x)
PATTERNS["\u00c8 un modello che ha bisogno del contesto giusto per esprimersi."] = [
    "Si esprime al meglio solo nel contesto adatto.",
    "Richiede la situazione giusta per mostrare il suo valore.",
    "Non è un modello da ogni circostanza: ha bisogno del setting giusto.",
    "Il suo potenziale emerge solo quando il contesto lo permette.",
    "Non è universale: dà il meglio nel contesto giusto.",
    "La sua resa dipende molto dal contesto in cui lo si porta.",
    "Ha bisogno dell'occasione adatta per esprimersi al meglio.",
    "Il contesto è fondamentale per far emergere le sue qualità.",
    "Non brilla ovunque: chiede il setting giusto per funzionare.",
    "Il suo talento si manifesta solo nell'ambiente adatto.",
]

# "Non è l'occhiale che va bene con tutto, ma quando funziona funziona davvero." (~8x)
PATTERNS["Non \u00e8 l\u2019occhiale che va bene con tutto, ma quando funziona funziona davvero."] = [
    "Non è versatile per ogni occasione, ma nel suo territorio eccelle.",
    "Non è universale, ma dove è nella sua zona di comfort brilla.",
    "Non lo metti con tutto, ma quando è nel contesto giusto è perfetto.",
    "Non è per ogni occasione, ma nell'occasione giusta dà il massimo.",
    "Non è il jolly del cassetto, ma quando è nella partita giusta vince.",
    "Non è per tutte le situazioni, ma in quella giusta è imbattibile.",
    "Non è un tuttofare, ma nel suo ambito è eccellente.",
    "Non è un passepartout, ma quando è al posto giusto fa meraviglie.",
]
PATTERNS["Non \u00e8 l'occhiale che va bene con tutto, ma quando funziona funziona davvero."] = PATTERNS["Non \u00e8 l\u2019occhiale che va bene con tutto, ma quando funziona funziona davvero."]

# "Ci vedo pensiero, ci vedo ricerca." (~8x)
PATTERNS["Ci vedo pensiero, ci vedo ricerca."] = [
    "Si percepisce la cura e la progettazione dietro.",
    "Si nota la ricerca e la riflessione nel design.",
    "C'è lavoro di pensiero dietro, e si vede.",
    "Si avverte l'impegno progettuale e la ricerca.",
    "La cura nel design e la ricerca si percepiscono.",
    "Si sente che dietro c'è pensiero e attenzione.",
    "Emerge una progettazione ragionata e curata.",
    "Si legge la ricerca e la cura nel dettaglio.",
]

# "Per il prezzo, offre più di quanto promette." (~7x)
PATTERNS["Per il prezzo, offre pi\u00f9 di quanto promette."] = [
    "Rispetto al prezzo, la resa è superiore alle aspettative.",
    "Il rapporto qualità-prezzo è sorprendentemente buono.",
    "A quel prezzo, offre molto più di quanto ci si aspetti.",
    "Il prezzo non rende giustizia a ciò che offre realmente.",
    "Considerato il costo, la qualità è sopra le attese.",
    "A questo prezzo, ha davvero poco da invidiare a modelli più costosi.",
    "Il prezzo è modesto rispetto a ciò che dà.",
]

# "Non ha niente di sbagliato dal punto di vista tecnico." (~7x)
PATTERNS["Non ha niente di sbagliato dal punto di vista tecnico."] = [
    "Tecnicamente non ha difetti da segnalare.",
    "Sul piano tecnico non c'è nulla da dire.",
    "Da un punto di vista tecnico è inattaccabile.",
    "Non ci sono carenze tecniche da rilevare.",
    "Il lato tecnico è impeccabile.",
    "Sul piano della fattura non c'è nulla da contestare.",
    "Tecnicamente è al di sopra di ogni critica.",
]

# "Il mio giudizio è personale, lo so." (~6x)
PATTERNS["Il mio giudizio \u00e8 personale, lo so."] = [
    "So che il mio parere è soggettivo.",
    "Riconosco la soggettività del mio giudizio.",
    "La mia valutazione è personale, ne sono consapevole.",
    "Il mio verdetto è soggettivo, lo ammetto.",
    "So bene che parlo solo per me.",
    "La mia opinione è personale, non generale.",
]

# "Il bilancio resta sospeso." (~8x)
PATTERNS["Il bilancio resta sospeso."] = [
    "Il verdetto rimane in bilico.",
    "Il giudizio resta aperto.",
    "La mia valutazione non si chiude del tutto.",
    "Il mio verdetto rimane irrisolto.",
    "La sentenza è ancora in sospeso.",
    "Il giudizio non trova un approdo definitivo.",
    "La mia opinione resta incompiuta.",
    "Il bilancio non si chiude in modo netto.",
]

# "alla fine questa cosa alla lunga pesa" (variante con "e questa cosa alla lunga pesa") (~20x)
PATTERNS["e questa cosa alla lunga pesa."] = [
    "e alla lunga questo dettaglio si fa sentire.",
    "e col tempo questo aspetto diventa un peso.",
    "e nel lungo periodo questo elemento pesa.",
    "e con l'uso questa mancanza si avverte.",
    "e alla lunga questa nota diventa rilevante.",
    "e col tempo questo limite emerge con forza.",
    "e nel lungo periodo questo aspetto si fa sentire.",
    "e con l'uso quotidiano questo punto si amplifica.",
    "e questa mancanza diventa più evidente col tempo.",
    "e alla lunga questo difetto si accumula.",
    "e col passare dei giorni questo elemento pesa sempre di più.",
    "e alla lunga questa nota dolente diventa importante.",
    "e col tempo questo svantaggio si fa notare.",
    "e alla lunga questo aspetto incide sul giudizio.",
    "e con l'uso ripetuto questo difetto emerge.",
    "e nel lungo termine questo problema si amplifica.",
    "e alla lunga questo dettaglio non si può ignorare.",
    "e col tempo questo aspetto diventa un fattore.",
    "e alla lunga questa cosa pesa più del previsto.",
    "e con l'uso questo difetto diventa più pesante.",
]

# "questa cosa alla lunga pesa." (alternativa senza "e")
PATTERNS["questa cosa alla lunga pesa."] = [
    "col tempo questo dettaglio si fa sentire.",
    "alla lunga questo aspetto si avverte.",
    "con l'uso questo limite emerge.",
    "nel lungo periodo questa nota pesa.",
    "alla lunga questa mancanza incide.",
    "col tempo questo difetto si accumula.",
    "alla lunga questo svantaggio si fa notare.",
    "con l'uso quotidiano questo aspetto si amplifica.",
    "alla lunga questo dettaglio diventa rilevante.",
    "col passare del tempo questa cosa pesa di più.",
    "nel lungo periodo questo punto si fa sentire.",
    "alla lunga questo difetto non si ignora.",
    "col tempo questa pecca diventa critica.",
    "alla lunga questo elemento incide sul giudizio.",
    "con l'uso questo aspetto emerge in modo più chiaro.",
    "nel lungo termine questa nota pesa più del previsto.",
    "col tempo questa mancanza si amplifica.",
    "alla lunga questo punto diventa significativo.",
    "con l'uso questa mancanza diventa un fattore.",
    "col tempo questo aspetto diventa un limite.",
]

print(f"Parte 6 caricata: totale {len(PATTERNS)} pattern definiti")
