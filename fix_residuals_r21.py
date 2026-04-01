# -*- coding: utf-8 -*-
"""Round 21 – Sostituzione n-gram ripetuti >=5x direttamente dal DB."""
import psycopg2, sys
from collections import defaultdict

sys.stdout.reconfigure(encoding='utf-8')

DATABASE_URL = "postgresql://neondb_owner:npg_uFxVSRoTj95w@ep-damp-sea-anvn4fw4.c-6.us-east-1.aws.neon.tech/neondb?sslmode=require"

PATTERNS = {
    # ── 7x ──
    "su un viso molto tondo la salita dell\u2019angolo va misurata bene.": [
        "su un viso con curve marcate la salita dell\u2019angolo richiede attenzione.",
        "su un viso dai tratti morbidi l\u2019angolo va calibrato con cura.",
        "su un volto rotondo la curva dell\u2019angolo merita una prova attenta.",
        "su conformazioni tonde l\u2019inclinazione dell\u2019angolo va verificata con precisione.",
        "su un viso pieno l\u2019angolo ascendente diventa un elemento da valutare con cura.",
        "su visi rotondi attenzione alla salita dell\u2019angolo: non \u00e8 scontata.",
        "su una conformazione tonda l\u2019angolo pu\u00f2 risultare scivoloso se non calibrato.",
    ],

    "su un viso stretto possono sembrare un po\u2019 lontani dal naso.": [
        "su una conformazione stretta rischiano di apparire un po\u2019 larghi al ponte.",
        "su un viso sottile la distanza dal naso pu\u00f2 risultare eccessiva.",
        "su un volto affusolato possono dare la sensazione di non aderire al ponte.",
        "su visi stretti possono creare un lieve senso di distacco al centro.",
        "su una fisionomia sottile il ponte potrebbe non aderire come dovrebbe.",
        "su un viso esile la distanza al centro si fa notare.",
        "su un viso snello il feeling al ponte potrebbe non essere perfetto.",
    ],

    "sul mio viso la forma rotonda non \u00e8 la pi\u00f9 valorizzante.": [
        "sulla mia conformazione la forma tonda non \u00e8 la scelta ideale.",
        "sul mio volto la geometria rotonda non \u00e8 la pi\u00f9 riuscita.",
        "con la mia struttura facciale la forma circolare rende meno del previsto.",
        "per la mia fisionomia la forma tonda non \u00e8 la pi\u00f9 adatta.",
        "sulla mia faccia le linee tonde non trovano il giusto equilibrio.",
        "per il mio viso la curvatura rotonda non d\u00e0 il massimo.",
        "sul mio volto la scelta della forma circolare risulta penalizzante.",
    ],

    "il verde salvia non va d\u2019accordo con ogni guardaroba.": [
        "il verde salvia richiede un guardaroba specifico per funzionare.",
        "il tono salvia non si integra facilmente con tutti gli abbinamenti.",
        "la nuance salvia \u00e8 selettiva in termini di abbinabilit\u00e0.",
        "il salvia delle lenti impone limiti cromatici all\u2019outfit.",
        "il verde salvia \u00e8 bello ma esigente come abbinamento.",
        "il tono salvia non \u00e8 il pi\u00f9 versatile come palette d\u2019accompagnamento.",
        "la colorazione salvia richiede scelte cromatiche precise nel vestirsi.",
    ],

    "il prezzo li espone al confronto con tanti aviator.": [
        "a questo prezzo il confronto con altri aviator \u00e8 inevitabile.",
        "il prezzo li mette di fronte a una concorrenza aviator agguerrita.",
        "nella fascia di prezzo il panorama aviator offre molte alternative.",
        "il prezzo li posiziona in un segmento aviator molto competitivo.",
        "a questo livello di prezzo i competitors aviator non mancano.",
        "la fascia di prezzo li espone al confronto diretto con molti aviator.",
        "il posizionamento economico impone il paragone con aviator di pari livello.",
    ],

    "su un viso molto lungo l\u2019ottagono pu\u00f2 irrigidire.": [
        "su volti allungati la forma ottagonale rischia di indurire i tratti.",
        "su un viso dal profilo lungo l\u2019ottagono tende a irrigidire l\u2019insieme.",
        "su una conformazione allungata le linee ottagonali possono risultare troppo dure.",
        "su visi lunghi la geometria dell\u2019ottagono pu\u00f2 aggiungere rigidit\u00e0.",
        "su un volto slanciato l\u2019ottagono rischia di appesantire l\u2019espressione.",
        "su conformazioni lunghe le linee ottagonali possono risultare severe.",
        "su un viso allungato la rigidit\u00e0 dell\u2019ottagono si fa sentire.",
    ],

    "con lenti verde bottiglia crea un insieme davvero": [
        "con lenti verde bottiglia genera un effetto davvero",
        "con il tono verde bottiglia produce un risultato davvero",
        "con la lente verde scuro costruisce qualcosa di davvero",
        "con il filtro verde bottiglia d\u00e0 vita a un insieme davvero",
        "con lenti di un verde profondo forma un risultato davvero",
        "con il verde intenso delle lenti compone qualcosa di davvero",
        "con la tonalit\u00e0 verde bottiglia delle lenti raggiunge un effetto davvero",
    ],

    "sul mio viso rotondo l\u2019angolo sale un po\u2019 troppo.": [
        "sulla mia conformazione tonda la curva dell\u2019angolo \u00e8 un po\u2019 eccessiva.",
        "sul mio volto rotondo l\u2019angolo ascendente risulta troppo accentuato.",
        "con il mio viso tondo la salita dell\u2019angolo eccede un po\u2019.",
        "sulla mia fisionomia rotonda l\u2019angolo va troppo in alto.",
        "per il mio viso pieno la salita delle linee \u00e8 troppo evidente.",
        "sul mio volto dalle proporzioni tonde l\u2019angolo sale pi\u00f9 del dovuto.",
        "sulla mia faccia rotonda l\u2019angolo verso l\u2019alto diventa troppo marcato.",
    ],

    "va portato con sicurezza o prende il sopravvento.": [
        "richiede personalit\u00e0 spiccata altrimenti domina chi lo indossa.",
        "chiede una certa sicurezza di stile o finisce per sopraffare.",
        "esige disinvoltura: senza di essa, prende il comando.",
        "pretende fermezza nello stile altrimenti diventa troppo protagonista.",
        "funziona se chi lo porta ha una presenza forte, altrimenti domina.",
        "richiede un atteggiamento assertivo oppure rischia di prevalere sullo stile.",
        "necessita di chi sa portarlo con decisione, o detta legge da solo.",
    ],

    "sono il tipo di paio che salva la giornata.": [
        "sono quell\u2019occhiale da cui sai che non verrai tradito.",
        "sono il paio che risolve le giornate complicate.",
        "sono quel tipo di accessorio che non ti lascia mai a piedi.",
        "sono il paio su cui contare quando serve una certezza.",
        "sono il genere di occhiale che ti tira fuori dai guai stilistici.",
        "sono il tipo di accessorio che si rende sempre utile.",
        "sono quelli da cui parti quando non sai cosa metterti.",
    ],

    # ── 6x ──
    "chi cerca originalit\u00e0 pura qui trover\u00e0 pi\u00f9 comfort che sorpresa.": [
        "chi vuole vera originalit\u00e0 trover\u00e0 pi\u00f9 comfort che innovazione.",
        "chi \u00e8 in cerca di qualcosa di insolito trover\u00e0 pi\u00f9 tranquillit\u00e0 che audacia.",
        "chi insegue l\u2019effetto sorpresa trover\u00e0 pi\u00f9 quiete che sperimentazione.",
        "chi cerca spiazzamento qui trover\u00e0 pi\u00f9 rassicurazione che scompiglio.",
        "chi vuole l\u2019effetto wow trover\u00e0 piuttosto una rassicurante normalit\u00e0.",
        "chi aspira all\u2019originalit\u00e0 assoluta trover\u00e0 pi\u00f9 un comodo classico che un azzardo.",
    ],

    "mi aspettavo una sensazione di solidit\u00e0 un po\u2019 maggiore.": [
        "speravo in una sensazione di robustezza pi\u00f9 marcata.",
        "mi attendevo un po\u2019 pi\u00f9 di struttura al tatto.",
        "avrei voluto percepire una solidit\u00e0 costruttiva superiore.",
        "la sensazione di consistenza \u00e8 leggermente sotto le aspettative.",
        "mi sarebbe piaciuta una solidit\u00e0 pi\u00f9 convincente al tatto.",
        "la percezione di robustezza \u00e8 un filo pi\u00f9 bassa del previsto.",
    ],

    "montatura dorata classica e degrad\u00e9 bruno molto naturale": [
        "telaio dorato dal sapore classico e sfumatura bruna molto organica",
        "struttura dorata tradizionale e degrad\u00e9 marrone dalla resa naturale",
        "montatura classica color oro e gradazione bruna dall\u2019effetto molto naturale",
        "telaio dorato dal taglio classico e sfumatura marrone molto morbida",
        "frame dorato classico e lente bruna sfumata dall\u2019aspetto naturale",
        "ossatura dorata classica e gradazione bruna molto fluida",
    ],

    "parlano la lingua del sole e dell\u2019eccesso controllato.": [
        "esprimono un linguaggio solare e di eccesso dosato.",
        "comunicano un\u2019estetica solare con un eccesso calibrato.",
        "trasmettono un\u2019energia estiva e un\u2019esuberanza controllata.",
        "hanno un vocabolario fatto di sole e teatralit\u00e0 contenuta.",
        "raccontano una storia di luce e di esuberanza misurata.",
        "incarnano un\u2019idea di sole e di esagerazione elegante.",
    ],

    "dorato con lente sfumata, montatura dorata classica e": [
        "dorato con lente sfumata, frame dorato dal taglio tradizionale e",
        "dorato con lente sfumata, struttura dorata classica e",
        "dorato con lente sfumata, telaio dorato dal sapore classico e",
        "dorato con lente sfumata, ossatura dorata di taglio tradizionale e",
        "dorato con lente sfumata, montatura in oro classico e",
        "dorato con lente sfumata, frame classico dorato e",
    ],

    "con lenti azzurro specchiate crea un insieme davvero": [
        "con lenti azzurro specchiate genera un effetto davvero",
        "con il filtro azzurro specchiato produce un risultato davvero",
        "con le lenti azzurre a specchio costruisce un insieme davvero",
        "con la lente specchiata azzurra d\u00e0 vita a un risultato davvero",
        "con l\u2019azzurro specchiato delle lenti compone qualcosa di davvero",
        "con le lenti specchiate in azzurro forma un effetto davvero",
    ],

    "dopo molte ore sento il ponte pi\u00f9 di quanto vorrei.": [
        "dopo un uso prolungato il ponte inizia a farsi sentire.",
        "nelle sessioni lunghe il ponte esercita una pressione percepibile.",
        "col passare delle ore la pressione al ponte diventa evidente.",
        "dopo molte ore la zona del ponte richiede una pausa.",
        "nelle lunghe sessioni d\u2019uso il ponte crea un fastidio progressivo.",
        "dopo parecchie ore il peso al ponte \u00e8 troppo presente.",
    ],

    "Equilibrio tra vintage e attuale si sente subito e": [
        "Il bilanciamento tra r\u00e9tro e contemporaneo \u00e8 immediato e",
        "La sintesi tra passato e presente si percepisce subito e",
        "L\u2019equilibrio tra spirito vintage e modernit\u00e0 si avverte al primo sguardo e",
        "Il dialogo tra elementi classici e attuali si legge subito e",
        "Il mix tra nostalgia e contemporaneit\u00e0 colpisce immediatamente e",
        "La fusione tra registro vintage e sensibilit\u00e0 moderna \u00e8 evidente e",
    ],

    "i dettagli effetto legno vanno trattati con cura.": [
        "le finiture effetto legno richiedono attenzione nella manutenzione.",
        "gli inserti in stile legno chiedono un minimo di cautela.",
        "il dettaglio legno esige un trattamento delicato nel tempo.",
        "le finiture effetto legno sono belle ma richiedono riguardo.",
        "gli elementi in stile legno necessitano di cure specifiche.",
        "le parti con effetto legno vogliono qualche accorgimento in pi\u00f9.",
    ],

    "non creano mai attrito con il resto del look.": [
        "non entrano mai in conflitto con il resto dell\u2019abbigliamento.",
        "si integrano senza frizioni con qualsiasi outfit.",
        "non disturbano mai l\u2019equilibrio del look complessivo.",
        "convivono pacificamente con qualunque stile indossi.",
        "si armonizzano sempre con ci\u00f2 che hai addosso.",
        "non generano mai contrasto con il resto dell\u2019abbigliamento.",
    ],

    "il prezzo mi fa essere pi\u00f9 severa del solito.": [
        "il prezzo alza le mie aspettative e quindi il mio giudizio.",
        "a questo prezzo divento pi\u00f9 esigente nel valutare.",
        "il livello di prezzo mi porta a essere pi\u00f9 critica.",
        "il prezzo mi spinge a pretendere di pi\u00f9.",
        "a questa cifra il metro di giudizio si alza inevitabilmente.",
        "il prezzo giustifica un livello di critica pi\u00f9 alto.",
    ],

    "non sono quelli da mettere a occhi chiusi.": [
        "non sono il tipo di paio che indossi senza pensarci.",
        "non funzionano in modalit\u00e0 pilota automatico.",
        "non sono il paio da prendere distrattamente al mattino.",
        "richiedono una scelta consapevole, non un gesto automatico.",
        "non sono quelli che afferri per inerzia uscendo di casa.",
        "non fanno parte di quegli occhiali che metti senza rifletterci.",
    ],

    "e illuminano subito il viso. Li ho portati": [
        "e danno subito luce al volto. Li ho testati",
        "e rischiarano il viso immediatamente. Li ho usati",
        "e accendono il viso al primo istante. Li ho provati",
        "e donano luminosit\u00e0 immediata al volto. Li ho indossati",
        "e portano subito freschezza al viso. Li ho testati",
        "e ravvivano il viso all\u2019istante. Li ho messi",
    ],

    "Per me \u00e8 uno di quei rari acquisti che": [
        "Per me \u00e8 una di quelle rare scelte che",
        "Per me appartiene a quella rara categoria di acquisti che",
        "Per me fa parte di quei pochissimi acquisti che",
        "Lo colloco tra quei rarissimi acquisti che",
        "Per me \u00e8 uno dei pochi acquisti memorabili che",
        "Per me rientra tra quegli acquisti eccezionali che",
    ],

    "il ponte non \u00e8 amico di tutti i": [
        "il ponte seleziona severamente i tipi di",
        "il ponte esclude una parte dei",
        "il ponte ha una compatibilit\u00e0 limitata con certi",
        "il ponte discrimina tra i diversi tipi di",
        "il ponte non si adatta a ogni tipo di",
        "il ponte limita l\u2019universalit\u00e0 del modello su molti",
    ],

    # ── 5x ──
    "la superficie specchiata chiede un po\u2019 di attenzione in pi\u00f9.": [
        "la finitura specchiata richiede qualche cura aggiuntiva.",
        "le lenti specchiate pretendono un po\u2019 pi\u00f9 di manutenzione.",
        "la superficie a specchio necessita di attenzione extra nella pulizia.",
        "il rivestimento specchiato vuole qualche accorgimento in pi\u00f9.",
        "le lenti specchiate esigono un trattamento un po\u2019 pi\u00f9 attento.",
    ],

    "temevo che presenza da fashion piece fosse troppo evidente.": [
        "temevo che l\u2019anima da pezzo fashion risultasse eccessiva.",
        "avevo paura che il lato fashion piece fosse troppo invadente.",
        "pensavo che il carattere da fashion piece potesse eccedere.",
        "temevo che il temperamento da pezzo moda fosse troppo marcato.",
        "mi preoccupava che l\u2019identit\u00e0 da fashion piece fosse ingombrante.",
    ],

    "si sente subito e danno carattere senza essere rumorosi.": [
        "si avverte subito e aggiungono personalit\u00e0 con discrezione.",
        "si percepisce subito e conferiscono identit\u00e0 senza eccedere.",
        "\u00e8 immediato e danno tono al look senza strepitare.",
        "si legge al primo sguardo e comunicano carattere con misura.",
        "si coglie immediatamente e portano personalit\u00e0 senza gridare.",
    ],

    "hanno una personalit\u00e0 forte ma studiata, grazie anche a": [
        "possiedono un\u2019identit\u00e0 marcata ma calibrata, anche per merito di",
        "hanno un carattere deciso ma ponderato, anche grazie a",
        "mostrano una personalit\u00e0 spiccata ma ragionata, anche in virt\u00f9 di",
        "esprimono un temperamento forte ma controllato, merito anche di",
        "presentano una personalit\u00e0 intensa ma costruita con criterio, complice anche",
    ],

    "con lente multicolor specchiata crea un insieme davvero": [
        "con lente multicolor specchiata genera un risultato davvero",
        "con il filtro multicolor specchiato produce un effetto davvero",
        "con la lente specchiata multicolore d\u00e0 vita a un insieme davvero",
        "con il multicolor specchiato delle lenti compone qualcosa di davvero",
        "con la finitura multicolor specchiata ottiene un risultato davvero",
    ],

    "e reggono bene il tempo stilisticamente. Li ho portati": [
        "e resistono bene al passare delle stagioni. Li ho provati",
        "e mantengono la loro freschezza stilistica nel tempo. Li ho testati",
        "e invecchiano bene dal punto di vista dello stile. Li ho indossati",
        "e non subiscono il passare delle tendenze. Li ho usati",
        "e mantengono il loro posto nel guardaroba anche col tempo. Li ho messi",
    ],

    "con marrone molto confortevole crea un insieme davvero": [
        "con marrone molto confortevole genera un effetto davvero",
        "con la lente marrone confortevole produce un risultato davvero",
        "con il tono marrone rilassante costruisce un insieme davvero",
        "con il marrone riposante delle lenti compone qualcosa di davvero",
        "con il filtro marrone comfort d\u00e0 vita a un effetto davvero",
    ],

    "Ha il coraggio del pezzo che entra in stanza prima di": [
        "Ha la grinta di un accessorio che precede chi lo indossa nella",
        "Ha l\u2019audacia del pezzo che arriva prima di",
        "Ha la sfrontatezza dell\u2019accessorio che si fa notare prima di",
        "Ha l\u2019impatto del pezzo che anticipa l\u2019ingresso di",
        "Ha la forza scenica del complemento che buca la stanza prima di",
    ],

    "Presenza delicata ma riconoscibile si sente subito e": [
        "Presenza sottile ma distinguibile si avverte immediatamente e",
        "Un\u2019impronta delicata ma inconfondibile si coglie subito e",
        "Presenza sommessa ma chiara si percepisce al primo sguardo e",
        "Un\u2019identit\u00e0 leggera ma precisa si legge subito e",
        "Presenza morbida ma ben definita si nota subito e",
    ],

    "si sente subito e non sembrano mai un travestimento.": [
        "si percepisce subito e non danno mai l\u2019idea di un costume.",
        "si avverte immediatamente e restano sempre credibili.",
        "\u00e8 immediato e non scivolano mai nel d\u00e9guisement.",
        "si coglie subito e mantengono sempre autenticit\u00e0.",
        "si legge al primo sguardo e non risultano mai artefatti.",
    ],

    "non \u00e8 il paio pi\u00f9 spontaneo per la routine veloce.": [
        "non sono l\u2019occhiale pi\u00f9 istintivo per il quotidiano frenetico.",
        "non sono la scelta pi\u00f9 naturale per le mattine di corsa.",
        "non si prestano alle uscite rapide senza pensarci.",
        "non sono quelli da afferrare in fretta nelle giornate caotiche.",
        "non sono la soluzione pi\u00f9 pratica per la routine veloce.",
    ],

    "quando scivola perde subito met\u00e0 del suo fascino.": [
        "scivolando dal naso perde gran parte del suo appeal.",
        "se cala sul naso il suo charme dimezza all\u2019istante.",
        "nel momento in cui scivola, l\u2019effetto estetico crolla.",
        "lo scivolamento cancella buona parte della sua attrattiva.",
        "perdendo aderenza, perde anche gran parte della sua bellezza.",
    ],

    "e trovano un buon equilibrio tra tecnica e stile.": [
        "e raggiungono una bella sintesi tra costruzione tecnica e gusto estetico.",
        "e bilanciano bene la componente tecnica con quella stilistica.",
        "e centrano un equilibrio efficace tra ingegneria e design.",
        "e trovano il giusto compromesso tra funzionalit\u00e0 e gusto.",
        "e riescono a coniugare il lato tecnico con quello estetico.",
    ],

    "nel quotidiano per me sono quasi troppo teatrali.": [
        "nella routine di ogni giorno per me eccedono in teatralit\u00e0.",
        "per il mio uso quotidiano risultano un po\u2019 troppo scenici.",
        "per la vita di tutti i giorni li trovo troppo performativi.",
        "nel quotidiano il loro lato teatrale per me \u00e8 eccessivo.",
        "per l\u2019uso giornaliero il registro scenico \u00e8 troppo alto.",
    ],

    "al tatto non danno una sensazione super premium.": [
        "la sensazione tattile non raggiunge il livello premium.",
        "al tocco non comunicano una qualit\u00e0 al vertice.",
        "manualmente non trasmettono quella sensazione di lusso assoluto.",
        "la resa tattile \u00e8 buona ma non ai massimi livelli.",
        "il tatto non restituisce l\u2019idea di un prodotto ultra premium.",
    ],

    "si \u00e8 comportato meglio del previsto. Sulla carta": [
        "ha reso pi\u00f9 del previsto. Sulla carta",
        "ha funzionato meglio di quanto mi aspettassi. Sulla carta",
        "mi ha sorpreso in positivo. Sulla carta",
        "ha superato le mie aspettative. A giudicare dalla scheda",
        "ha dato risultati migliori del previsto. Leggendo le specifiche",
    ],

    "Li ho portati in citt\u00e0 nelle giornate luminose e": [
        "Li ho testati in contesto urbano nelle giornate soleggiate e",
        "Li ho provati in citt\u00e0 con il sole e",
        "Li ho indossati per le strade nelle giornate di pieno sole e",
        "Li ho usati in citt\u00e0 durante le giornate pi\u00f9 luminose e",
        "Li ho messi nel contesto cittadino con la luce forte e",
    ],

    "e stanno bene in tante situazioni. Li ho portati": [
        "e funzionano in molteplici contesti. Li ho testati",
        "e si adattano a parecchie occasioni. Li ho provati",
        "e risultano versatili in diverse situazioni. Li ho indossati",
        "e reggono bene in contesti diversi. Li ho usati",
        "e sono adatti a molte circostanze. Li ho messi",
    ],

    "e il gusto seventies hanno un fascino discreto.": [
        "e lo spirito anni Settanta esercitano un fascino riservato.",
        "e il richiamo seventies aggiungono una nota di fascino sommesso.",
        "e la vena anni \u201970 comunicano un fascino misurato.",
        "e l\u2019anima seventies portano con s\u00e9 un fascino silenzioso.",
        "e il sapore anni Settanta trasmettono un fascino pacato.",
    ],

    "telaio leggero in argento e lenti verde salvia": [
        "struttura leggera argentata e lenti nel tono verde salvia",
        "frame sottile color argento e lenti verde salvia",
        "montatura leggera in argento e filtro verde salvia",
        "ossatura leggera argentata con lenti salvia",
        "telaio argento dal peso piuma e lenti salvia",
    ],

    "cerca un cat-eye pi\u00f9 estremo lo trover\u00e0 troppo": [
        "cerca un cat-eye pi\u00f9 aggressivo lo giudicher\u00e0 troppo",
        "vuole un cat-eye pi\u00f9 spinto lo considerer\u00e0 troppo",
        "esige un cat-eye pi\u00f9 estremo lo riterr\u00e0 troppo",
        "desidera un cat-eye pi\u00f9 deciso lo trover\u00e0 troppo",
        "pretende un cat-eye pi\u00f9 marcato lo classifier\u00e0 troppo",
    ],

    "si sente subito e funzionano con quasi tutto.": [
        "si avverte al primo sguardo e si abbinano facilmente.",
        "\u00e8 immediato e si adattano a quasi ogni outfit.",
        "si coglie subito e vanno d\u2019accordo con tutto.",
        "si nota dal primo istante e la versatilit\u00e0 \u00e8 totale.",
        "si percepisce immediatamente e sono compatibili con quasi tutto.",
    ],

    "Li ho portati nelle occasioni pi\u00f9 sceniche e": [
        "Li ho testati nelle situazioni pi\u00f9 scenografiche e",
        "Li ho provati negli appuntamenti pi\u00f9 teatrali e",
        "Li ho indossati nelle circostanze pi\u00f9 d\u2019impatto e",
        "Li ho usati nelle occasioni pi\u00f9 vistose e",
        "Li ho messi nei contesti pi\u00f9 esposti e",
    ],

    "quadrato ampio e fashion esce bene grazie a": [
        "quadrato ampio e fashion rende bene grazie a",
        "quadrato ampio e fashion d\u00e0 il suo meglio grazie a",
        "quadrato ampio e fashion funziona bene complice",
        "quadrato ampio dal taglio fashion risulta efficace grazie a",
        "quadrato ampio e fashion mostra il suo valore grazie a",
    ],

    "non li vedo come occhiali da tutto l\u2019anno.": [
        "non li considero un paio da portare in ogni stagione.",
        "non hanno la versatilit\u00e0 stagionale che cerco.",
        "non sono il tipo di occhiale per tutte le stagioni.",
        "li vedo pi\u00f9 adatti a una stagione specifica.",
        "non li immagino come il mio paio per dodici mesi.",
    ],

    "la forma non \u00e8 favorevole su ogni volto.": [
        "la forma non \u00e8 universale nel valorizzare ogni viso.",
        "la geometria non si adatta a tutte le conformazioni.",
        "la forma richiede una certa compatibilit\u00e0 con il viso.",
        "geometricamente non va bene per ogni tipologia di volto.",
        "la forma esclude alcune tipologie di viso.",
    ],

    "Li ho portati con look urban bold e": [
        "Li ho testati con outfit urban decisi e",
        "Li ho provati con look audacemente urbani e",
        "Li ho indossati con abbinamenti urban dal taglio forte e",
        "Li ho usati con look di strada dal carattere marcato e",
        "Li ho messi con outfit urban bold e",
    ],

    "Sono il tipo di paia che ti fanno": [
        "Sono il genere di occhiali che ti portano a",
        "Sono quegli occhiali che ti fanno",
        "Sono quel tipo di paio che ti spinge a",
        "Sono il modello che ti fa",
        "Sono la categoria di occhiali che ti invita a",
    ],

    "che su un viso struccato e capelli raccolti che": [
        "che su un volto senza trucco e capelli tirati indietro",
        "che su un viso pulito e capelli raccolti",
        "che su un viso naturale con capelli legati che",
        "che con il viso struccato e i capelli su che",
        "che su un volto al naturale con capelli raccolti",
    ],

    "che con camicia aperta e jeans chiari che": [
        "che con camicia aperta e denim chiaro",
        "che con camicia sbottonata e jeans chiari",
        "che con una camicia aperta e pantaloni chiari che",
        "che con camicia casual e jeans chiaro che",
        "che con camicia slacciata e jeans di tono chiaro che",
    ],

    "che insieme a un look minimale che da solo diceva poco che": [
        "che abbinato a un outfit sobrio che da solo era anonimo",
        "che con un look essenziale che da solo non diceva niente",
        "che affiancato a un look minimale silenzioso",
        "che unito a un look sobrio che da solo era piatto",
        "che con un outfit minimal poco espressivo di suo",
    ],

    "la struttura scura molto essenziale e il riflesso prism": [
        "la struttura scura minimal e la rifrazione prism",
        "il telaio scuro essenziale e il gioco prismatico",
        "la struttura scura lineare e l\u2019effetto prismatico",
        "l\u2019ossatura scura e minimale col riflesso prismatico",
        "il frame scuro puro e la luce prismatica",
    ],

    "struttura grigio carbone, la lente blu specchiata e": [
        "struttura grigio carbone, il filtro blu specchiato e",
        "telaio grigio carbone, la lente specchiata blu e",
        "ossatura grigio carbone, la specchiatura blu e",
        "frame grigio carbone, la lente a specchio blu e",
        "struttura in grigio carbone, il blu specchiato delle lenti e",
    ],

    "e panoramica multicolor. Su di me funzionano bene": [
        "e panoramica multicolor. Nel mio caso funzionano bene",
        "e panoramica multicolor. Su di me rendono bene",
        "e panoramica multicolor. Con me vanno bene",
        "e panoramica multicolor. Personalmente li trovo efficaci",
        "e panoramica multicolor. Sul mio viso rendono bene",
    ],

    "e lente blu specchiata. Su di me funzionano bene": [
        "e lente blu specchiata. Nel mio caso funzionano bene",
        "e lente blu specchiata. Su di me rendono bene",
        "e lente blu specchiata. Con me vanno bene",
        "e lente blu specchiata. Personalmente li trovo efficaci",
        "e lente blu specchiata. Sul mio viso rendono bene",
    ],

    "e riflesso azzurro. Su di me funzionano bene": [
        "e riflesso azzurro. Nel mio caso funzionano bene",
        "e riflesso azzurro. Su di me rendono bene",
        "e riflesso azzurro. Con me vanno bene",
        "e riflesso azzurro. Personalmente li trovo efficaci",
        "e riflesso azzurro. Sul mio viso rendono bene",
    ],
}

print(f"Pattern da sostituire: {len(PATTERNS)}")
print("Connessione al DB...")
conn = psycopg2.connect(DATABASE_URL)
cur = conn.cursor()
cur.execute("SELECT id, body FROM reviews ORDER BY id")
rows = cur.fetchall()
print(f"Caricate: {len(rows)}")

pattern_occurrence = defaultdict(int)
updates = []

for rid, body in rows:
    new_body = body
    modified = False
    for pattern, alternatives in PATTERNS.items():
        if pattern in new_body:
            idx = pattern_occurrence[pattern]
            pattern_occurrence[pattern] += 1
            alt = alternatives[idx % len(alternatives)]
            new_body = new_body.replace(pattern, alt, 1)
            modified = True
    if modified:
        updates.append((new_body, rid))

print(f"\nOccorrenze trovate per pattern:")
for p, c in sorted(pattern_occurrence.items(), key=lambda x: -x[1]):
    print(f"  {c:4d}x | {p[:80]}")

total_occ = sum(pattern_occurrence.values())
print(f"\nTotale occorrenze: {total_occ}")
print(f"Recensioni da aggiornare: {len(updates)}")

errors = 0
for i in range(0, len(updates), 50):
    batch = updates[i:i+50]
    try:
        cur.executemany("UPDATE reviews SET body=%s WHERE id=%s", batch)
        conn.commit()
        print(f"  Batch {i//50+1}: {len(batch)}/{len(updates)}")
    except Exception as e:
        conn.rollback()
        errors += 1
        print(f"  Errore batch {i//50+1}: {e}")

cur.close()
conn.close()
print(f"\nAggiornate: {len(updates)} | Errori: {errors}")
print("Round 21 OK" if errors == 0 else "Round 21 ERRORI")
