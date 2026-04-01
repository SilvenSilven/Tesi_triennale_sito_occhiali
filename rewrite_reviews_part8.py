#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Parte 8: Pattern residui terzo passaggio (5-9x dopo secondo passaggio)
"""
from rewrite_reviews_part7 import PATTERNS

# ═══════════════════════════════════════════════════════════
# FRASI 9x
# ═══════════════════════════════════════════════════════════

# "Li raccomanderei soprattutto a chi è stanco dell'ennesimo occhiale generico." (9x)
PATTERNS["Li raccomanderei soprattutto a chi \u00e8 stanco dell\u2019ennesimo occhiale generico."] = [
    "Li consiglio a chi vuole uscire dall'anonimato degli occhiali seriali.",
    "Perfetti per chi cerca un'alternativa alla solita proposta generica.",
    "Li suggerisco a chi è stufo del design da grande distribuzione.",
    "Ideali per chi vuole qualcosa che non sia il solito occhiale anonimo.",
    "Li raccomando a chi cerca personalità invece della solita forma neutra.",
    "Li consiglio a chi vuole rompere la monotonia degli occhiali standard.",
    "Per chi cerca un'identità chiara nell'occhiale, sono perfetti.",
    "Li suggerisco a chi è alla ricerca di qualcosa con più carattere.",
    "Li consiglio a chi desidera distinguersi dall'oceano di modelli anonimi.",
]
PATTERNS["Li raccomanderei soprattutto a chi è stanco dell'ennesimo occhiale generico."] = PATTERNS["Li raccomanderei soprattutto a chi \u00e8 stanco dell\u2019ennesimo occhiale generico."]

# "Un modello che funziona meglio nella realtà che nelle foto." (9x)
PATTERNS["Un modello che funziona meglio nella realt\u00e0 che nelle foto."] = [
    "Reso molto meglio dal vivo che in foto.",
    "È un modello che le foto non rendono giustizia.",
    "La resa reale supera di molto l'immagine fotografica.",
    "Le foto lo penalizzano rispetto all'esperienza dal vivo.",
    "È di quei modelli che si capiscono solo indossandoli.",
    "L'immagine non gli rende merito: dal vivo è tutt'altra cosa.",
    "È molto più convincente addosso che in foto.",
    "La fotogenia non è il suo forte, ma la resa dal vivo sì.",
    "Un caso in cui la realtà supera le foto.",
]

# "Li vedo bene soprattutto in città, meno in contesti sportivi o informali." (9x)
PATTERNS["Li vedo bene soprattutto in citt\u00e0, meno in contesti sportivi o informali."] = [
    "Funzionano in contesti urbani ma meno in quelli casual.",
    "In città brillano, fuori dal contesto urbano meno.",
    "Perfetti per la vita cittadina, meno per il casual sportivo.",
    "Il loro habitat è la città: in contesti informali perdono.",
    "Sono pensati per il contesto urbano: in altri scenari meno adatti.",
    "In ambito cittadino sono al meglio: altrove meno.",
    "L'ambiente urbano li esalta, il contesto sportivo li svilisce.",
    "Ideali per la città, fuori metrica per il casual.",
    "Il loro terreno è l'asfalto, meno il tempo libero.",
]

# "Tutto sommato è un buon tentativo, con margini evidenti di crescita." (9x)
PATTERNS["Tutto sommato \u00e8 un buon tentativo, con margini evidenti di crescita."] = [
    "È un tentativo apprezzabile che può ancora migliorare molto.",
    "La base è buona, il margine di crescita altrettanto.",
    "Un piccolo passo nella direzione giusta, con tanto spazio per crescere.",
    "Il tentativo è lodevole, il potenziale di evoluzione ampio.",
    "Un buon punto di partenza con evidenti spazi di miglioramento.",
    "Lo sforzo c'è e si vede, così come il margine per fare meglio.",
    "Il tentativo è valido, la strada per affinarlo ancora lunga.",
    "Apprezzo il tentativo, pur vedendo dove può migliorare.",
    "Buon inizio, con diverse aree dove può ancora crescere.",
]

# "Tra quelli nella mia collezione, è fra i più affidabili in qualsiasi contesto." (9x)
PATTERNS["Tra quelli nella mia collezione, \u00e8 fra i pi\u00f9 affidabili in qualsiasi contesto."] = [
    "Nella mia collezione è uno dei più versatili.",
    "Tra i miei, è uno dei più affidabili in ogni situazione.",
    "Nella mia rotazione è fra i più costanti.",
    "È uno dei pezzi più trasversali nella mia collezione.",
    "Tra tutti i miei occhiali è fra i più universali.",
    "Nella mia collezione si distingue per l'affidabilità contestuale.",
    "È uno dei modelli che funzionano sempre, nella mia esperienza.",
    "Tra quelli che possiedo, è fra quelli su cui conto di più.",
    "Nella mia raccolta è fra i più polivalenti.",
]

# ═══════════════════════════════════════════════════════════
# FRASI 8x
# ═══════════════════════════════════════════════════════════

# "Non è il paio più comodo che abbia, ma il design compensa il sacrificio." (8x)
PATTERNS["Non \u00e8 il paio pi\u00f9 comodo che abbia, ma il design compensa il sacrificio."] = [
    "Il comfort non è il massimo, ma il design vale il compromesso.",
    "Non è il più comodo, eppure il design giustifica ogni piccolo fastidio.",
    "Qualcosa in comfort lo sacrifica, ma il design ripaga.",
    "Il comfort non è il suo forte, ma l'estetica bilancia il tutto.",
    "Non eccelle in comodità, ma il valore estetico compensa.",
    "Col comfort si poteva fare meglio, ma il design copre la differenza.",
    "Non è il massimo della comodità, ma il design rende il sacrificio accettabile.",
    "Per la comodità non è il top, ma la linea basta e avanza a compensare.",
]

# "Mi fermo poco sotto l'entusiasmo pieno." (8x)
PATTERNS["Mi fermo poco sotto l\u2019entusiasmo pieno."] = [
    "Resto appena al di sotto dell'entusiasmo totale.",
    "Arrivo vicino al massimo dell'entusiasmo, ma non ci arrivo.",
    "Manca un soffio per la promozione a pieni voti.",
    "Sono quasi entusiasta, ma non del tutto.",
    "L'entusiasmo pieno è lì, non lo raggiungo.",
    "Resto a un passo dall'entusiasmo totale.",
    "Sfioro l'entusiasmo completo senza toccarlo.",
    "Ci arrivo quasi, ma il pieno entusiasmo mi sfugge di poco.",
]
PATTERNS["Mi fermo poco sotto l'entusiasmo pieno."] = PATTERNS["Mi fermo poco sotto l\u2019entusiasmo pieno."]

# "Il mio è un giudizio contingente, non una sentenza." (8x)
PATTERNS["Il mio \u00e8 un giudizio contingente, non una sentenza."] = [
    "Il mio è un parere soggettivo, non un verdetto assoluto.",
    "Parlo per la mia esperienza, non emetto sentenze universali.",
    "Il mio è un giudizio personale, non una verità oggettiva.",
    "La mia è una valutazione individuale, non un verdetto.",
    "Il mio parere riflette la mia esperienza, non pretende generalità.",
    "Esprimo una lettura personale, non un giudizio definitivo.",
    "Il mio è un punto di vista circostanziale, non un verdetto immutabile.",
    "Offro una prospettiva personale, non una sentenza universale.",
]

# "Non entusiasma, ma neppure delude in modo netto." (8x)
PATTERNS["Non entusiasma, ma neppure delude in modo netto."] = [
    "Non esalta, ma non affonda neanche.",
    "Non scalda ma nemmeno raffredda.",
    "Resta in una zona neutra: né entusiasmante né deludente.",
    "Non provoca slancio né delusione marcata.",
    "Non fa brillare gli occhi ma nemmeno storcere il naso.",
    "Non conquista ma nemmeno respinge.",
    "Non colpisce ma nemmeno delude davvero.",
    "La reazione è tiepida in entrambe le direzioni.",
]

# "È uno di quei paia che apprezzo in silenzio, senza raccontarlo a nessuno." (8x)
PATTERNS["\u00c8 uno di quei paia che apprezzo in silenzio, senza raccontarlo a nessuno."] = [
    "Lo apprezzo in modo discreto, senza sentire il bisogno di parlarne.",
    "È un piacere silenzioso che non sento di dover condividere.",
    "Lo scelgo senza farne un evento, con soddisfazione silenziosa.",
    "È un apprezzamento intimo, non da condividere a voce alta.",
    "Lo porto con una soddisfazione discreta, tutta mia.",
    "Lo godo in silenzio, senza sentire il bisogno di pubblicizzarlo.",
    "È un piacere privato che non cerco di giustificare a nessuno.",
    "Lo apprezzo nella mia quiete, senza necessità di condivisione.",
]

# ═══════════════════════════════════════════════════════════
# FRASI 7x
# ═══════════════════════════════════════════════════════════

# "Ho comprato per il design, ho tenuto per il comfort." (7x)
PATTERNS["Ho comprato per il design, ho tenuto per il comfort."] = [
    "L'estetica mi ha attirato, il comfort mi ha fatto restare.",
    "Il design mi ha convinto all'acquisto, il comfort alla fedeltà.",
    "Comprato per la linea, confermato per la comodità.",
    "L'occhio li ha scelti, il comfort li ha confermati.",
    "Il design ha fatto la prima mossa, la comodità ha chiuso la partita.",
    "Il motivo iniziale era il design, quello per cui restano è il comfort.",
    "Li ho presi per l'estetica, li conservo per la calzata.",
]

# "C'è un equilibrio raro tra leggerezza e solidità percepita." (7x)
PATTERNS["C\u2019\u00e8 un equilibrio raro tra leggerezza e solidit\u00e0 percepita."] = [
    "Coniugano leggerezza e sensazione di solidità in modo insolito.",
    "Rara combinazione di leggerezza e percezione di robustezza.",
    "Leggeri senza sembrare fragili: un bilanciamento non scontato.",
    "Riescono a essere leggeri pur trasmettendo solidità.",
    "Peso contennuto e sensazione di robustezza: un mix non facile.",
    "La leggerezza non va a scapito della solidità percepita.",
    "Trovano quel punto raro dove il peso leggero convive con la percezione di robustezza.",
]
PATTERNS["C'\u00e8 un equilibrio raro tra leggerezza e solidit\u00e0 percepita."] = PATTERNS["C\u2019\u00e8 un equilibrio raro tra leggerezza e solidit\u00e0 percepita."]

# "È il tipo di modello che userei come esempio di buon design a chi non se ne intende." (7x)
PATTERNS["\u00c8 il tipo di modello che userei come esempio di buon design a chi non se ne intende."] = [
    "Lo userei come caso studio di buon design con chi non è del settore.",
    "Lo mostrerei a un neofita come esempio di design ben riuscito.",
    "È perfetto per spiegare cosa sia il buon design a chi non lo conosce.",
    "Lo porterei come esempio se dovessi spiegare il buon design a un profano.",
    "Lo userei come dimostrazione pratica di cosa significhi buon design.",
    "Se dovessi illustrare il buon design a qualcuno, partirei da questo.",
    "È l'esempio che farei per spiegare a uno che non se ne intende cos'è il buon design.",
]

# "Mi son trovato a portarli in situazioni in cui non avrei mai pensato di metterli." (7x)
PATTERNS["Mi son trovato a portarli in situazioni in cui non avrei mai pensato di metterli."] = [
    "Li ho indossati in contesti che non avrei previsto.",
    "Ho finito per usarli in situazioni inaspettate.",
    "Li ho ritrovati addosso in contesti impensati.",
    "Sono finiti in occasioni dove non avrei immaginato di portarli.",
    "Li ho indossati ben oltre i contesti inizialmente previsti.",
    "Mi son ritrovato a sceglierli anche in circostanze inattese.",
    "Hanno coperto occasioni che non avevo messo in conto.",
]

# "Non li prendo a cuor leggero: la fascia di prezzo chiede un certo livello, e lo offre." (7x)
PATTERNS["Non li prendo a cuor leggero: la fascia di prezzo chiede un certo livello, e lo offre."] = [
    "Il prezzo è impegnativo ma il livello qualitativo lo giustifica.",
    "Non è un acquisto leggero, ma la qualità è all'altezza del prezzo.",
    "Il prezzo chiede qualità e questa la restituisce.",
    "L'investimento è significativo ma proporzionato a ciò che si ottiene.",
    "Il costo non è trascurabile, ma il prodotto regge il confronto.",
    "Il prezzo impone aspettative alte che vengono rispettate.",
    "Non sono economici, ma la qualità è coerente col prezzo chiesto.",
]

# "Per certi look è praticamente la scelta ideale." (7x)
PATTERNS["Per certi look \u00e8 praticamente la scelta ideale."] = [
    "In certi contesti stilistici è la scelta perfetta.",
    "Per alcuni abbinamenti è esattamente ciò che serve.",
    "Ci sono look per cui è la scelta d'elezione.",
    "Per determinati stili è la risposta ideale.",
    "In certi look è la scelta più azzeccata possibile.",
    "Per alcune combinazioni stilistiche è la soluzione perfetta.",
    "Per certi outfit è la risposta più giusta.",
]

# "Il primo impatto è stato forte: non capita spesso." (7x)
PATTERNS["Il primo impatto \u00e8 stato forte: non capita spesso."] = [
    "L'impatto iniziale è stato intenso, e non mi succede spesso.",
    "Il colpo d'occhio iniziale è stato notevole, cosa rara per me.",
    "Il primo impatto mi ha colpito più del solito.",
    "L'impressione iniziale è stata molto forte, e non è frequente.",
    "Ha fatto un'ottima prima impressione: cosa non scontata.",
    "Il primo impatto è stato significativo, cosa che per me non è la norma.",
    "Mi ha colpito subito: non capita spesso con un paio di occhiali.",
]

# ═══════════════════════════════════════════════════════════
# FRASI 6x
# ═══════════════════════════════════════════════════════════

# "Si integra nel volto in modo naturale, senza dare l'impressione di 'portare gli occhiali'." (6x)
PATTERNS["Si integra nel volto in modo naturale, senza dare l\u2019impressione di \u2018portare gli occhiali\u2019."] = [
    "Si fondono col viso senza dare l'impressione di avere addosso un accessorio.",
    "L'integrazione col volto è così naturale da dimenticarseli.",
    "Si mimetizzano sul viso come se fossero sempre stati lì.",
    "Non danno l'impressione di essere un accessorio aggiunto: fanno parte del volto.",
    "L'effetto è di naturalezza totale: non sembra di portare occhiali.",
    "Si integrano col viso come se non ci fossero.",
]
PATTERNS["Si integra nel volto in modo naturale, senza dare l'impressione di 'portare gli occhiali'."] = PATTERNS["Si integra nel volto in modo naturale, senza dare l\u2019impressione di \u2018portare gli occhiali\u2019."]

# "C'è una cura dei dettagli che si scopre solo al secondo sguardo." (6x)
PATTERNS["C\u2019\u00e8 una cura dei dettagli che si scopre solo al secondo sguardo."] = [
    "I dettagli si rivelano solo con un'osservazione più attenta.",
    "La cura dei particolari emerge con il tempo, non al primo sguardo.",
    "I dettagli migliori si notano solo guardando con più attenzione.",
    "C'è una ricchezza di dettagli che si svela gradualmente.",
    "I particolari più curati escono allo scoperto al secondo esame.",
    "La cura si scopre solo osservando con maggiore attenzione.",
]
PATTERNS["C'\u00e8 una cura dei dettagli che si scopre solo al secondo sguardo."] = PATTERNS["C\u2019\u00e8 una cura dei dettagli che si scopre solo al secondo sguardo."]

# "È uno di quei modelli che avrei voluto vedere su uno scaffale reale prima di comprare." (6x)
PATTERNS["\u00c8 uno di quei modelli che avrei voluto vedere su uno scaffale reale prima di comprare."] = [
    "Lo avrei preferito provare dal vivo prima dell'acquisto.",
    "Un modello che richiede la prova in negozio per giudicarlo bene.",
    "Lo avrei comprato più volentieri dopo averlo provato di persona.",
    "È di quei modelli che chiedono una prova dal vivo.",
    "L'acquisto online nasconde aspetti che solo la prova fisica svela.",
    "Avrei voluto poterlo toccare e provare prima di decidere.",
]

# "Restano nella mia rotazione quotidiana, il che è il complimento più alto che possa fare." (6x)
PATTERNS["Restano nella mia rotazione quotidiana, il che \u00e8 il complimento pi\u00f9 alto che possa fare."] = [
    "Sono entrati nella mia selezione di tutti i giorni, e per me è il massimo riconoscimento.",
    "Il fatto che siano nella mia rotazione quotidiana dice tutto.",
    "Li uso tutti i giorni: è il complimento più grande che possa fare.",
    "Fanno parte del mio quotidiano: per me non c'è complimento più alto.",
    "Sono nella mia rotazione giornaliera: il massimo che possa dire.",
    "Il loro posto nella rotazione quotidiana è il mio più grande elogio.",
]

# "Se potessi cambiargli una cosa sola, sarebbe il ponte: un millimetro più stretto e sarebbe perfetto." (6x)
PATTERNS["Se potessi cambiargli una cosa sola, sarebbe il ponte: un millimetro pi\u00f9 stretto e sarebbe perfetto."] = [
    "L'unica modifica che farei è sul ponte: appena più stretto e sarebbe perfetto.",
    "Se potessi intervenire su un dettaglio, stringerei il ponte di poco.",
    "Un ponte leggermente più stretto e il quadro sarebbe completo.",
    "L'unico aggiustamento desiderato: un ponte leggermente più stretto.",
    "L'unica cosa che cambierei è la larghezza del ponte: un filo meno.",
    "Il ponte è l'unico punto dove un millimetro in meno cambierebbe tutto.",
]

# "Non è il modello più appariscente, ed è esattamente per questo che lo scelgo." (6x)
PATTERNS["Non \u00e8 il modello pi\u00f9 appariscente, ed \u00e8 esattamente per questo che lo scelgo."] = [
    "La sua discrezione è il motivo per cui lo scelgo.",
    "Non urla, e proprio per questo mi attira.",
    "La sua sobrietà è ciò che me lo fa preferire.",
    "È la sua mancanza di clamore a farmelo scegliere.",
    "Lo scelgo proprio perché non cerca di farsi notare.",
    "L'assenza di vistosità è il suo punto di forza ai miei occhi.",
]

# ═══════════════════════════════════════════════════════════
# FRASI 5x
# ═══════════════════════════════════════════════════════════

# "Ogni tanto apro il cassetto solo per guardarli." (5x)
PATTERNS["Ogni tanto apro il cassetto solo per guardarli."] = [
    "Mi capita di aprire il cassetto solo per il piacere di vederli.",
    "A volte li tiro fuori senza nessun bisogno, solo per ammirarli.",
    "Ogni tanto li prendo in mano solo per il gusto di osservarli.",
    "A volte li guardo nel cassetto senza motivo, solo per piacere.",
    "Il cassetto si apre a volte anche solo per il piacere dell'occhiata.",
]

# "Il compromesso tra estetica e praticità è riuscito." (5x)
PATTERNS["Il compromesso tra estetica e praticit\u00e0 \u00e8 riuscito."] = [
    "L'equilibrio fra bellezza e praticità è centrato.",
    "La sintesi fra estetica e funzionalità è ben riuscita.",
    "Il bilanciamento tra forma e funzione è convincente.",
    "Hanno trovato un buon punto di incontro fra bello e pratico.",
    "L'intersezione fra estetica e funzionalità è azzeccata.",
]

# "In certi giorni lo amo, in altri mi chiedo perché l'ho preso." (5x)
PATTERNS["In certi giorni lo amo, in altri mi chiedo perch\u00e9 l\u2019ho preso."] = [
    "Il rapporto è altalenante: un giorno sì e uno no.",
    "Alcuni giorni lo adoro, altri non capisco la mia scelta.",
    "Alterno momenti di entusiasmo a momenti di perplessità.",
    "L'opinione oscilla: a volte totale, a volte inspiegabile.",
    "Il giudizio cambia con l'umore del giorno.",
]
PATTERNS["In certi giorni lo amo, in altri mi chiedo perch\u00e9 l'ho preso."] = PATTERNS["In certi giorni lo amo, in altri mi chiedo perch\u00e9 l\u2019ho preso."]

# "Non è un modello per chi cerca il colpo d'occhio, ma per chi lo vuole trovare." (5x)
PATTERNS["Non \u00e8 un modello per chi cerca il colpo d\u2019occhio, ma per chi lo vuole trovare."] = [
    "Non è per chi vuole stupire, ma per chi sa dove guardare.",
    "Il suo bello emerge con l'attenzione, non con il clamore.",
    "È per chi cerca con calma, non per chi vuole l'effetto subito.",
    "Non è da passerella: è da secondo sguardo.",
    "Chi cerca lo spettacolo passi oltre; chi sa apprezzare, resti.",
]
PATTERNS["Non \u00e8 un modello per chi cerca il colpo d'occhio, ma per chi lo vuole trovare."] = PATTERNS["Non \u00e8 un modello per chi cerca il colpo d\u2019occhio, ma per chi lo vuole trovare."]

# "L'ho confrontato con modelli più costosi e tiene il passo senza vergogna." (5x)
PATTERNS["L\u2019ho confrontato con modelli pi\u00f9 costosi e tiene il passo senza vergogna."] = [
    "Regge il confronto con modelli di fascia superiore.",
    "Anche accanto a modelli più costosi non sfigura.",
    "Il confronto con modelli più cari non lo penalizza.",
    "Si difende bene anche paragonato a modelli di prezzo maggiore.",
    "In confronto con fasce più alte, non arretra.",
]
PATTERNS["L'ho confrontato con modelli pi\u00f9 costosi e tiene il passo senza vergogna."] = PATTERNS["L\u2019ho confrontato con modelli pi\u00f9 costosi e tiene il passo senza vergogna."]

# "Il colore è più profondo dal vivo: le foto non gli rendono giustizia." (5x)
PATTERNS["Il colore \u00e8 pi\u00f9 profondo dal vivo: le foto non gli rendono giustizia."] = [
    "Dal vivo il colore ha più profondità di quanto le foto mostrino.",
    "Le foto non catturano la ricchezza cromatica reale.",
    "Il colore dal vivo è molto più intenso di quanto appaia in foto.",
    "La resa cromatica dal vivo supera di molto quella fotografica.",
    "Le foto non rendono l'idea della profondità del colore reale.",
]

# "È quel tipo di occhiale che non chiede mai permesso: sta bene e basta." (5x)
PATTERNS["\u00c8 quel tipo di occhiale che non chiede mai permesso: sta bene e basta."] = [
    "Non ha bisogno di giustificazioni: calza e funziona, punto.",
    "Funziona senza bisogno di spiegazioni o abbinamenti studiati.",
    "Non chiede contesto: sta bene e non serve altro.",
    "È il tipo che indossi e non devi pensarci: funziona da solo.",
    "Ha quella qualità rara di funzionare senza alcun bisogno di contesto.",
]

# "Dopo tre mesi di uso regolare, la posizione non è cambiata." (5x)
PATTERNS["Dopo tre mesi di uso regolare, la posizione non \u00e8 cambiata."] = [
    "Tre mesi dopo, il giudizio è lo stesso di prima.",
    "A distanza di tre mesi di uso, l'opinione è confermata.",
    "L'uso prolungato non ha cambiato il mio parere.",
    "Dopo mesi di utilizzo, il giudizio resiste.",
    "La posizione è la stessa di tre mesi fa.",
]

# "Ha quel modo di stare su che comunica qualcosa anche stando fermi." (5x)
PATTERNS["Ha quel modo di stare su che comunica qualcosa anche stando fermi."] = [
    "Ha una presenza che comunica anche nell'immobilità.",
    "Riesce a trasmettere carattere anche senza movimento.",
    "La sua presenza si percepisce anche da fermo.",
    "Ha un linguaggio visivo che parla anche in assenza di gesti.",
    "Comunica qualcosa anche nel silenzio dell'immobilità.",
]

# "Non è il paio universale, ma è quello che manca alla collezione di chi lo cerca." (5x)
PATTERNS["Non \u00e8 il paio universale, ma \u00e8 quello che manca alla collezione di chi lo cerca."] = [
    "Non è per tutti, ma per chi lo cerca è il pezzo mancante.",
    "Non è universale, ma nella collezione giusta è indispensabile.",
    "Non è per chiunque, ma chi lo cerca troverà il tassello perfetto.",
    "Il suo pubblico è specifico, e per quel pubblico è il pezzo chiave.",
    "Non punta alla massa, ma al collezionista che sa cosa gli manca.",
]

# "Mi aspettavo meno, e l'ho scoperto migliore di quanto immaginassi." (5x)
PATTERNS["Mi aspettavo meno, e l\u2019ho scoperto migliore di quanto immaginassi."] = [
    "Le aspettative erano basse, la realtà le ha superate.",
    "Ho scoperto più di quanto mi aspettassi.",
    "La sorpresa è stata positiva: aspettavo meno.",
    "Ha superato le mie aspettative iniziali in modo netto.",
    "L'ho scoperto migliore di ogni mia aspettativa.",
]
PATTERNS["Mi aspettavo meno, e l'ho scoperto migliore di quanto immaginassi."] = PATTERNS["Mi aspettavo meno, e l\u2019ho scoperto migliore di quanto immaginassi."]

# ═══════════════════════════════════════════════════════════
# SEGMENTI RESIDUI ≥ 8x (non coperti in part7)
# ═══════════════════════════════════════════════════════════

# "e lì ha mostrato un equilibrio che in foto non avevo capito fino in fondo" (10x)
PATTERNS["e l\u00ec ha mostrato un equilibrio che in foto non avevo capito fino in fondo"] = [
    "e lì ha rivelato un bilanciamento che le foto non suggerivano",
    "e in quel momento ho notato un equilibrio invisibile nelle foto",
    "e proprio lì ho scoperto un bilanciamento che le immagini nascondevano",
    "e lì si è svelato un equilibrio che nelle foto sfuggiva",
    "e in quell'occasione ho colto un bilanciamento non visibile in foto",
    "e lì ho percepito un equilibrio che nessuna foto poteva trasmettere",
    "e in quel contesto è emerso un equilibrio impensabile dalle foto",
    "e proprio lì si è manifestato un bilanciamento che le foto non rendevano",
    "e lì ho notato un equilibrio che in foto mi era sfuggito completamente",
    "e lì ha rivelato una resa che le foto non potevano anticipare",
]

# "e lì ha funzionato soprattutto nel passaggio dal tavolo al viso" (9x)
PATTERNS["e l\u00ec ha funzionato soprattutto nel passaggio dal tavolo al viso"] = [
    "e proprio nel passaggio dal tavolo al viso ha dato il meglio",
    "e la differenza si è vista nel momento dell'indossata",
    "e il salto dal tavolo all'indossata ha fatto la differenza",
    "e dal tavolo al viso il miglioramento è stato evidente",
    "e la sorpresa è arrivata proprio nel momento di metterli su",
    "e l'effetto migliore si è visto passando dalla mano al viso",
    "e nel passaggio dal guardarlo al portarlo è cambiato tutto",
    "e proprio il momento dell'indossata ha ribaltato la percezione",
    "e la resa è cambiata totalmente dall'osservazione all'indossata",
]

# "e lì ha confermato l'impressione iniziale" (8x)
PATTERNS["e l\u00ec ha confermato l\u2019impressione iniziale"] = [
    "e in quell'occasione ha ribadito la prima impressione",
    "e lì ha consolidato ciò che pensavo all'inizio",
    "e proprio lì ha dato conferma di quanto percepito subito",
    "e in quel contesto ha validato il giudizio della prima volta",
    "e lì ha mantenuto ciò che la prima impressione prometteva",
    "e l'impressione iniziale ha trovato conferma anche lì",
    "e in quel momento il primo giudizio si è riconfermato",
    "e lì ha ribadito la sensazione avuta fin dal primo istante",
]
PATTERNS["e l\u00ec ha confermato l'impressione iniziale"] = PATTERNS["e l\u00ec ha confermato l\u2019impressione iniziale"]

# "e lì ha dato il meglio" (8x)
PATTERNS["e l\u00ec ha dato il meglio"] = [
    "e in quel contesto si è espresso al massimo",
    "e lì ha offerto la sua resa migliore",
    "e proprio lì ha mostrato tutto il suo valore",
    "e in quel frangente ha dato il meglio di sé",
    "e lì ha espresso pienamente le sue qualità",
    "e in quell'occasione ha brillato davvero",
    "e lì ha mostrato la sua versione migliore",
    "e proprio lì ha espresso il suo massimo potenziale",
]

print(f"Parte 8 caricata: totale {len(PATTERNS)} pattern definiti")
