# -*- coding: utf-8 -*-
"""Round 21b - Ripete la sostituzione con apostrofi dritti (il DB usa ' non \u2019)."""
import psycopg2, sys
from collections import defaultdict

sys.stdout.reconfigure(encoding='utf-8')

DATABASE_URL = "postgresql://neondb_owner:npg_uFxVSRoTj95w@ep-damp-sea-anvn4fw4.c-6.us-east-1.aws.neon.tech/neondb?sslmode=require"

# Helper: normalize curly quotes to straight
def s(text):
    return text.replace("\u2019", "'").replace("\u2018", "'")

PATTERNS = {
    # -- 7x --
    s("su un viso molto tondo la salita dell\u2019angolo va misurata bene."): [
        s("su un viso con curve marcate la salita dell\u2019angolo richiede attenzione."),
        s("su un viso dai tratti morbidi l\u2019angolo va calibrato con cura."),
        s("su un volto rotondo la curva dell\u2019angolo merita una prova attenta."),
        s("su conformazioni tonde l\u2019inclinazione dell\u2019angolo va verificata con precisione."),
        s("su un viso pieno l\u2019angolo ascendente diventa un elemento da valutare con cura."),
        s("su visi rotondi attenzione alla salita dell\u2019angolo: non \u00e8 scontata."),
        s("su una conformazione tonda l\u2019angolo pu\u00f2 risultare scivoloso se non calibrato."),
    ],

    s("su un viso stretto possono sembrare un po\u2019 lontani dal naso."): [
        s("su una conformazione stretta rischiano di apparire un po\u2019 larghi al ponte."),
        s("su un viso sottile la distanza dal naso pu\u00f2 risultare eccessiva."),
        s("su un volto affusolato possono dare la sensazione di non aderire al ponte."),
        s("su visi stretti possono creare un lieve senso di distacco al centro."),
        s("su una fisionomia sottile il ponte potrebbe non aderire come dovrebbe."),
        s("su un viso esile la distanza al centro si fa notare."),
        s("su un viso snello il feeling al ponte potrebbe non essere perfetto."),
    ],

    s("sul mio viso la forma rotonda non \u00e8 la pi\u00f9 valorizzante."): [
        s("sulla mia conformazione la forma tonda non \u00e8 la scelta ideale."),
        s("sul mio volto la geometria rotonda non \u00e8 la pi\u00f9 riuscita."),
        s("con la mia struttura facciale la forma circolare rende meno del previsto."),
        s("per la mia fisionomia la forma tonda non \u00e8 la pi\u00f9 adatta."),
        s("sulla mia faccia le linee tonde non trovano il giusto equilibrio."),
        s("per il mio viso la curvatura rotonda non d\u00e0 il massimo."),
        s("sul mio volto la scelta della forma circolare risulta penalizzante."),
    ],

    s("il verde salvia non va d\u2019accordo con ogni guardaroba."): [
        s("il verde salvia richiede un guardaroba specifico per funzionare."),
        s("il tono salvia non si integra facilmente con tutti gli abbinamenti."),
        s("la nuance salvia \u00e8 selettiva in termini di abbinabilit\u00e0."),
        s("il salvia delle lenti impone limiti cromatici all\u2019outfit."),
        s("il verde salvia \u00e8 bello ma esigente come abbinamento."),
        s("il tono salvia non \u00e8 il pi\u00f9 versatile come palette d\u2019accompagnamento."),
        s("la colorazione salvia richiede scelte cromatiche precise nel vestirsi."),
    ],

    s("il prezzo li espone al confronto con tanti aviator."): [
        s("a questo prezzo il confronto con altri aviator \u00e8 inevitabile."),
        s("il prezzo li mette di fronte a una concorrenza aviator agguerrita."),
        s("nella fascia di prezzo il panorama aviator offre molte alternative."),
        s("il prezzo li posiziona in un segmento aviator molto competitivo."),
        s("a questo livello di prezzo i competitors aviator non mancano."),
        s("la fascia di prezzo li espone al confronto diretto con molti aviator."),
        s("il posizionamento economico impone il paragone con aviator di pari livello."),
    ],

    s("su un viso molto lungo l\u2019ottagono pu\u00f2 irrigidire."): [
        s("su volti allungati la forma ottagonale rischia di indurire i tratti."),
        s("su un viso dal profilo lungo l\u2019ottagono tende a irrigidire l\u2019insieme."),
        s("su una conformazione allungata le linee ottagonali possono risultare troppo dure."),
        s("su visi lunghi la geometria dell\u2019ottagono pu\u00f2 aggiungere rigidit\u00e0."),
        s("su un volto slanciato l\u2019ottagono rischia di appesantire l\u2019espressione."),
        s("su conformazioni lunghe le linee ottagonali possono risultare severe."),
        s("su un viso allungato la rigidit\u00e0 dell\u2019ottagono si fa sentire."),
    ],

    s("con lenti verde bottiglia crea un insieme davvero"): [
        s("con lenti verde bottiglia genera un effetto davvero"),
        s("con il tono verde bottiglia produce un risultato davvero"),
        s("con la lente verde scuro costruisce qualcosa di davvero"),
        s("con il filtro verde bottiglia d\u00e0 vita a un insieme davvero"),
        s("con lenti di un verde profondo forma un risultato davvero"),
        s("con il verde intenso delle lenti compone qualcosa di davvero"),
        s("con la tonalit\u00e0 verde bottiglia delle lenti raggiunge un effetto davvero"),
    ],

    s("sul mio viso rotondo l\u2019angolo sale un po\u2019 troppo."): [
        s("sulla mia conformazione tonda la curva dell\u2019angolo \u00e8 un po\u2019 eccessiva."),
        s("sul mio volto rotondo l\u2019angolo ascendente risulta troppo accentuato."),
        s("con il mio viso tondo la salita dell\u2019angolo eccede un po\u2019."),
        s("sulla mia fisionomia rotonda l\u2019angolo va troppo in alto."),
        s("per il mio viso pieno la salita delle linee \u00e8 troppo evidente."),
        s("sul mio volto dalle proporzioni tonde l\u2019angolo sale pi\u00f9 del dovuto."),
        s("sulla mia faccia rotonda l\u2019angolo verso l\u2019alto diventa troppo marcato."),
    ],

    s("va portato con sicurezza o prende il sopravvento."): [
        s("richiede personalit\u00e0 spiccata altrimenti domina chi lo indossa."),
        s("chiede una certa sicurezza di stile o finisce per sopraffare."),
        s("esige disinvoltura: senza di essa, prende il comando."),
        s("pretende fermezza nello stile altrimenti diventa troppo protagonista."),
        s("funziona se chi lo porta ha una presenza forte, altrimenti domina."),
        s("richiede un atteggiamento assertivo oppure rischia di prevalere sullo stile."),
        s("necessita di chi sa portarlo con decisione, o detta legge da solo."),
    ],

    s("sono il tipo di paio che salva la giornata."): [
        s("sono quell\u2019occhiale da cui sai che non verrai tradito."),
        s("sono il paio che risolve le giornate complicate."),
        s("sono quel tipo di accessorio che non ti lascia mai a piedi."),
        s("sono il paio su cui contare quando serve una certezza."),
        s("sono il genere di occhiale che ti tira fuori dai guai stilistici."),
        s("sono il tipo di accessorio che si rende sempre utile."),
        s("sono quelli da cui parti quando non sai cosa metterti."),
    ],

    # -- 6x --
    s("chi cerca originalit\u00e0 pura qui trover\u00e0 pi\u00f9 comfort che sorpresa."): [
        s("chi vuole vera originalit\u00e0 trover\u00e0 pi\u00f9 comfort che innovazione."),
        s("chi \u00e8 in cerca di qualcosa di insolito trover\u00e0 pi\u00f9 tranquillit\u00e0 che audacia."),
        s("chi insegue l\u2019effetto sorpresa trover\u00e0 pi\u00f9 quiete che sperimentazione."),
        s("chi cerca spiazzamento qui trover\u00e0 pi\u00f9 rassicurazione che scompiglio."),
        s("chi vuole l\u2019effetto wow trover\u00e0 piuttosto una rassicurante normalit\u00e0."),
        s("chi aspira all\u2019originalit\u00e0 assoluta trover\u00e0 pi\u00f9 un comodo classico che un azzardo."),
    ],

    s("mi aspettavo una sensazione di solidit\u00e0 un po\u2019 maggiore."): [
        s("speravo in una sensazione di robustezza pi\u00f9 marcata."),
        s("mi attendevo un po\u2019 pi\u00f9 di struttura al tatto."),
        s("avrei voluto percepire una solidit\u00e0 costruttiva superiore."),
        s("la sensazione di consistenza \u00e8 leggermente sotto le aspettative."),
        s("mi sarebbe piaciuta una solidit\u00e0 pi\u00f9 convincente al tatto."),
        s("la percezione di robustezza \u00e8 un filo pi\u00f9 bassa del previsto."),
    ],

    s("montatura dorata classica e degrad\u00e9 bruno molto naturale"): [
        s("telaio dorato dal sapore classico e sfumatura bruna molto organica"),
        s("struttura dorata tradizionale e degrad\u00e9 marrone dalla resa naturale"),
        s("montatura classica color oro e gradazione bruna dall\u2019effetto molto naturale"),
        s("telaio dorato dal taglio classico e sfumatura marrone molto morbida"),
        s("frame dorato classico e lente bruna sfumata dall\u2019aspetto naturale"),
        s("ossatura dorata classica e gradazione bruna molto fluida"),
    ],

    s("parlano la lingua del sole e dell\u2019eccesso controllato."): [
        s("esprimono un linguaggio solare e di eccesso dosato."),
        s("comunicano un\u2019estetica solare con un eccesso calibrato."),
        s("trasmettono un\u2019energia estiva e un\u2019esuberanza controllata."),
        s("hanno un vocabolario fatto di sole e teatralit\u00e0 contenuta."),
        s("raccontano una storia di luce e di esuberanza misurata."),
        s("incarnano un\u2019idea di sole e di esagerazione elegante."),
    ],

    s("dorato con lente sfumata, montatura dorata classica e"): [
        s("dorato con lente sfumata, frame dorato dal taglio tradizionale e"),
        s("dorato con lente sfumata, struttura dorata classica e"),
        s("dorato con lente sfumata, telaio dorato dal sapore classico e"),
        s("dorato con lente sfumata, ossatura dorata di taglio tradizionale e"),
        s("dorato con lente sfumata, montatura in oro classico e"),
        s("dorato con lente sfumata, frame classico dorato e"),
    ],

    s("con lenti azzurro specchiate crea un insieme davvero"): [
        s("con lenti azzurro specchiate genera un effetto davvero"),
        s("con il filtro azzurro specchiato produce un risultato davvero"),
        s("con le lenti azzurre a specchio costruisce un insieme davvero"),
        s("con la lente specchiata azzurra d\u00e0 vita a un risultato davvero"),
        s("con l\u2019azzurro specchiato delle lenti compone qualcosa di davvero"),
        s("con le lenti specchiate in azzurro forma un effetto davvero"),
    ],

    s("dopo molte ore sento il ponte pi\u00f9 di quanto vorrei."): [
        s("dopo un uso prolungato il ponte inizia a farsi sentire."),
        s("nelle sessioni lunghe il ponte esercita una pressione percepibile."),
        s("col passare delle ore la pressione al ponte diventa evidente."),
        s("dopo molte ore la zona del ponte richiede una pausa."),
        s("nelle lunghe sessioni d\u2019uso il ponte crea un fastidio progressivo."),
        s("dopo parecchie ore il peso al ponte \u00e8 troppo presente."),
    ],

    s("Equilibrio tra vintage e attuale si sente subito e"): [
        s("Il bilanciamento tra r\u00e9tro e contemporaneo \u00e8 immediato e"),
        s("La sintesi tra passato e presente si percepisce subito e"),
        s("L\u2019equilibrio tra spirito vintage e modernit\u00e0 si avverte al primo sguardo e"),
        s("Il dialogo tra elementi classici e attuali si legge subito e"),
        s("Il mix tra nostalgia e contemporaneit\u00e0 colpisce immediatamente e"),
        s("La fusione tra registro vintage e sensibilit\u00e0 moderna \u00e8 evidente e"),
    ],

    s("i dettagli effetto legno vanno trattati con cura."): [
        s("le finiture effetto legno richiedono attenzione nella manutenzione."),
        s("gli inserti in stile legno chiedono un minimo di cautela."),
        s("il dettaglio legno esige un trattamento delicato nel tempo."),
        s("le finiture effetto legno sono belle ma richiedono riguardo."),
        s("gli elementi in stile legno necessitano di cure specifiche."),
        s("le parti con effetto legno vogliono qualche accorgimento in pi\u00f9."),
    ],

    s("non creano mai attrito con il resto del look."): [
        s("non entrano mai in conflitto con il resto dell\u2019abbigliamento."),
        s("si integrano senza frizioni con qualsiasi outfit."),
        s("non disturbano mai l\u2019equilibrio del look complessivo."),
        s("convivono pacificamente con qualunque stile indossi."),
        s("si armonizzano sempre con ci\u00f2 che hai addosso."),
        s("non generano mai contrasto con il resto dell\u2019abbigliamento."),
    ],

    s("il prezzo mi fa essere pi\u00f9 severa del solito."): [
        s("il prezzo alza le mie aspettative e quindi il mio giudizio."),
        s("a questo prezzo divento pi\u00f9 esigente nel valutare."),
        s("il livello di prezzo mi porta a essere pi\u00f9 critica."),
        s("il prezzo mi spinge a pretendere di pi\u00f9."),
        s("a questa cifra il metro di giudizio si alza inevitabilmente."),
        s("il prezzo giustifica un livello di critica pi\u00f9 alto."),
    ],

    s("non sono quelli da mettere a occhi chiusi."): [
        s("non sono il tipo di paio che indossi senza pensarci."),
        s("non funzionano in modalit\u00e0 pilota automatico."),
        s("non sono il paio da prendere distrattamente al mattino."),
        s("richiedono una scelta consapevole, non un gesto automatico."),
        s("non sono quelli che afferri per inerzia uscendo di casa."),
        s("non fanno parte di quegli occhiali che metti senza rifletterci."),
    ],

    s("e illuminano subito il viso. Li ho portati"): [
        s("e danno subito luce al volto. Li ho testati"),
        s("e rischiarano il viso immediatamente. Li ho usati"),
        s("e accendono il viso al primo istante. Li ho provati"),
        s("e donano luminosit\u00e0 immediata al volto. Li ho indossati"),
        s("e portano subito freschezza al viso. Li ho testati"),
        s("e ravvivano il viso all\u2019istante. Li ho messi"),
    ],

    s("Per me \u00e8 uno di quei rari acquisti che"): [
        s("Per me \u00e8 una di quelle rare scelte che"),
        s("Per me appartiene a quella rara categoria di acquisti che"),
        s("Per me fa parte di quei pochissimi acquisti che"),
        s("Lo colloco tra quei rarissimi acquisti che"),
        s("Per me \u00e8 uno dei pochi acquisti memorabili che"),
        s("Per me rientra tra quegli acquisti eccezionali che"),
    ],

    s("il ponte non \u00e8 amico di tutti i"): [
        s("il ponte seleziona severamente i tipi di"),
        s("il ponte esclude una parte dei"),
        s("il ponte ha una compatibilit\u00e0 limitata con certi"),
        s("il ponte discrimina tra i diversi tipi di"),
        s("il ponte non si adatta a ogni tipo di"),
        s("il ponte limita l\u2019universalit\u00e0 del modello su molti"),
    ],

    # -- 5x --
    s("la superficie specchiata chiede un po\u2019 di attenzione in pi\u00f9."): [
        s("la finitura specchiata richiede qualche cura aggiuntiva."),
        s("le lenti specchiate pretendono un po\u2019 pi\u00f9 di manutenzione."),
        s("la superficie a specchio necessita di attenzione extra nella pulizia."),
        s("il rivestimento specchiato vuole qualche accorgimento in pi\u00f9."),
        s("le lenti specchiate esigono un trattamento un po\u2019 pi\u00f9 attento."),
    ],

    s("temevo che presenza da fashion piece fosse troppo evidente."): [
        s("temevo che l\u2019anima da pezzo fashion risultasse eccessiva."),
        s("avevo paura che il lato fashion piece fosse troppo invadente."),
        s("pensavo che il carattere da fashion piece potesse eccedere."),
        s("temevo che il temperamento da pezzo moda fosse troppo marcato."),
        s("mi preoccupava che l\u2019identit\u00e0 da fashion piece fosse ingombrante."),
    ],

    s("si sente subito e danno carattere senza essere rumorosi."): [
        s("si avverte subito e aggiungono personalit\u00e0 con discrezione."),
        s("si percepisce subito e conferiscono identit\u00e0 senza eccedere."),
        s("\u00e8 immediato e danno tono al look senza strepitare."),
        s("si legge al primo sguardo e comunicano carattere con misura."),
        s("si coglie immediatamente e portano personalit\u00e0 senza gridare."),
    ],

    s("hanno una personalit\u00e0 forte ma studiata, grazie anche a"): [
        s("possiedono un\u2019identit\u00e0 marcata ma calibrata, anche per merito di"),
        s("hanno un carattere deciso ma ponderato, anche grazie a"),
        s("mostrano una personalit\u00e0 spiccata ma ragionata, anche in virt\u00f9 di"),
        s("esprimono un temperamento forte ma controllato, merito anche di"),
        s("presentano una personalit\u00e0 intensa ma costruita con criterio, complice anche"),
    ],

    s("con lente multicolor specchiata crea un insieme davvero"): [
        s("con lente multicolor specchiata genera un risultato davvero"),
        s("con il filtro multicolor specchiato produce un effetto davvero"),
        s("con la lente specchiata multicolore d\u00e0 vita a un insieme davvero"),
        s("con il multicolor specchiato delle lenti compone qualcosa di davvero"),
        s("con la finitura multicolor specchiata ottiene un risultato davvero"),
    ],

    s("e reggono bene il tempo stilisticamente. Li ho portati"): [
        s("e resistono bene al passare delle stagioni. Li ho provati"),
        s("e mantengono la loro freschezza stilistica nel tempo. Li ho testati"),
        s("e invecchiano bene dal punto di vista dello stile. Li ho indossati"),
        s("e non subiscono il passare delle tendenze. Li ho usati"),
        s("e mantengono il loro posto nel guardaroba anche col tempo. Li ho messi"),
    ],

    s("con marrone molto confortevole crea un insieme davvero"): [
        s("con marrone molto confortevole genera un effetto davvero"),
        s("con la lente marrone confortevole produce un risultato davvero"),
        s("con il tono marrone rilassante costruisce un insieme davvero"),
        s("con il marrone riposante delle lenti compone qualcosa di davvero"),
        s("con il filtro marrone comfort d\u00e0 vita a un effetto davvero"),
    ],

    s("Ha il coraggio del pezzo che entra in stanza prima di"): [
        s("Ha la grinta di un accessorio che precede chi lo indossa nella"),
        s("Ha l\u2019audacia del pezzo che arriva prima di"),
        s("Ha la sfrontatezza dell\u2019accessorio che si fa notare prima di"),
        s("Ha l\u2019impatto del pezzo che anticipa l\u2019ingresso di"),
        s("Ha la forza scenica del complemento che buca la stanza prima di"),
    ],

    s("Presenza delicata ma riconoscibile si sente subito e"): [
        s("Presenza sottile ma distinguibile si avverte immediatamente e"),
        s("Un\u2019impronta delicata ma inconfondibile si coglie subito e"),
        s("Presenza sommessa ma chiara si percepisce al primo sguardo e"),
        s("Un\u2019identit\u00e0 leggera ma precisa si legge subito e"),
        s("Presenza morbida ma ben definita si nota subito e"),
    ],

    s("si sente subito e non sembrano mai un travestimento."): [
        s("si percepisce subito e non danno mai l\u2019idea di un costume."),
        s("si avverte immediatamente e restano sempre credibili."),
        s("\u00e8 immediato e non scivolano mai nel d\u00e9guisement."),
        s("si coglie subito e mantengono sempre autenticit\u00e0."),
        s("si legge al primo sguardo e non risultano mai artefatti."),
    ],

    s("non \u00e8 il paio pi\u00f9 spontaneo per la routine veloce."): [
        s("non sono l\u2019occhiale pi\u00f9 istintivo per il quotidiano frenetico."),
        s("non sono la scelta pi\u00f9 naturale per le mattine di corsa."),
        s("non si prestano alle uscite rapide senza pensarci."),
        s("non sono quelli da afferrare in fretta nelle giornate caotiche."),
        s("non sono la soluzione pi\u00f9 pratica per la routine veloce."),
    ],

    s("quando scivola perde subito met\u00e0 del suo fascino."): [
        s("scivolando dal naso perde gran parte del suo appeal."),
        s("se cala sul naso il suo charme dimezza all\u2019istante."),
        s("nel momento in cui scivola, l\u2019effetto estetico crolla."),
        s("lo scivolamento cancella buona parte della sua attrattiva."),
        s("perdendo aderenza, perde anche gran parte della sua bellezza."),
    ],

    s("e trovano un buon equilibrio tra tecnica e stile."): [
        s("e raggiungono una bella sintesi tra costruzione tecnica e gusto estetico."),
        s("e bilanciano bene la componente tecnica con quella stilistica."),
        s("e centrano un equilibrio efficace tra ingegneria e design."),
        s("e trovano il giusto compromesso tra funzionalit\u00e0 e gusto."),
        s("e riescono a coniugare il lato tecnico con quello estetico."),
    ],

    s("nel quotidiano per me sono quasi troppo teatrali."): [
        s("nella routine di ogni giorno per me eccedono in teatralit\u00e0."),
        s("per il mio uso quotidiano risultano un po\u2019 troppo scenici."),
        s("per la vita di tutti i giorni li trovo troppo performativi."),
        s("nel quotidiano il loro lato teatrale per me \u00e8 eccessivo."),
        s("per l\u2019uso giornaliero il registro scenico \u00e8 troppo alto."),
    ],

    s("al tatto non danno una sensazione super premium."): [
        s("la sensazione tattile non raggiunge il livello premium."),
        s("al tocco non comunicano una qualit\u00e0 al vertice."),
        s("manualmente non trasmettono quella sensazione di lusso assoluto."),
        s("la resa tattile \u00e8 buona ma non ai massimi livelli."),
        s("il tatto non restituisce l\u2019idea di un prodotto ultra premium."),
    ],

    s("si \u00e8 comportato meglio del previsto. Sulla carta"): [
        s("ha reso pi\u00f9 del previsto. Sulla carta"),
        s("ha funzionato meglio di quanto mi aspettassi. Sulla carta"),
        s("mi ha sorpreso in positivo. Sulla carta"),
        s("ha superato le mie aspettative. A giudicare dalla scheda"),
        s("ha dato risultati migliori del previsto. Leggendo le specifiche"),
    ],

    s("Li ho portati in citt\u00e0 nelle giornate luminose e"): [
        s("Li ho testati in contesto urbano nelle giornate soleggiate e"),
        s("Li ho provati in citt\u00e0 con il sole e"),
        s("Li ho indossati per le strade nelle giornate di pieno sole e"),
        s("Li ho usati in citt\u00e0 durante le giornate pi\u00f9 luminose e"),
        s("Li ho messi nel contesto cittadino con la luce forte e"),
    ],

    s("e stanno bene in tante situazioni. Li ho portati"): [
        s("e funzionano in molteplici contesti. Li ho testati"),
        s("e si adattano a parecchie occasioni. Li ho provati"),
        s("e risultano versatili in diverse situazioni. Li ho indossati"),
        s("e reggono bene in contesti diversi. Li ho usati"),
        s("e sono adatti a molte circostanze. Li ho messi"),
    ],

    s("e il gusto seventies hanno un fascino discreto."): [
        s("e lo spirito anni Settanta esercitano un fascino riservato."),
        s("e il richiamo seventies aggiungono una nota di fascino sommesso."),
        s("e la vena anni '70 comunicano un fascino misurato."),
        s("e l\u2019anima seventies portano con s\u00e9 un fascino silenzioso."),
        s("e il sapore anni Settanta trasmettono un fascino pacato."),
    ],

    s("telaio leggero in argento e lenti verde salvia"): [
        s("struttura leggera argentata e lenti nel tono verde salvia"),
        s("frame sottile color argento e lenti verde salvia"),
        s("montatura leggera in argento e filtro verde salvia"),
        s("ossatura leggera argentata con lenti salvia"),
        s("telaio argento dal peso piuma e lenti salvia"),
    ],

    s("cerca un cat-eye pi\u00f9 estremo lo trover\u00e0 troppo"): [
        s("cerca un cat-eye pi\u00f9 aggressivo lo giudicher\u00e0 troppo"),
        s("vuole un cat-eye pi\u00f9 spinto lo considerer\u00e0 troppo"),
        s("esige un cat-eye pi\u00f9 estremo lo riterr\u00e0 troppo"),
        s("desidera un cat-eye pi\u00f9 deciso lo trover\u00e0 troppo"),
        s("pretende un cat-eye pi\u00f9 marcato lo classifier\u00e0 troppo"),
    ],

    s("si sente subito e funzionano con quasi tutto."): [
        s("si avverte al primo sguardo e si abbinano facilmente."),
        s("\u00e8 immediato e si adattano a quasi ogni outfit."),
        s("si coglie subito e vanno d\u2019accordo con tutto."),
        s("si nota dal primo istante e la versatilit\u00e0 \u00e8 totale."),
        s("si percepisce immediatamente e sono compatibili con quasi tutto."),
    ],

    s("Li ho portati nelle occasioni pi\u00f9 sceniche e"): [
        s("Li ho testati nelle situazioni pi\u00f9 scenografiche e"),
        s("Li ho provati negli appuntamenti pi\u00f9 teatrali e"),
        s("Li ho indossati nelle circostanze pi\u00f9 d\u2019impatto e"),
        s("Li ho usati nelle occasioni pi\u00f9 vistose e"),
        s("Li ho messi nei contesti pi\u00f9 esposti e"),
    ],

    s("quadrato ampio e fashion esce bene grazie a"): [
        s("quadrato ampio e fashion rende bene grazie a"),
        s("quadrato ampio e fashion d\u00e0 il suo meglio grazie a"),
        s("quadrato ampio e fashion funziona bene complice"),
        s("quadrato ampio dal taglio fashion risulta efficace grazie a"),
        s("quadrato ampio e fashion mostra il suo valore grazie a"),
    ],

    s("non li vedo come occhiali da tutto l\u2019anno."): [
        s("non li considero un paio da portare in ogni stagione."),
        s("non hanno la versatilit\u00e0 stagionale che cerco."),
        s("non sono il tipo di occhiale per tutte le stagioni."),
        s("li vedo pi\u00f9 adatti a una stagione specifica."),
        s("non li immagino come il mio paio per dodici mesi."),
    ],

    s("la forma non \u00e8 favorevole su ogni volto."): [
        s("la forma non \u00e8 universale nel valorizzare ogni viso."),
        s("la geometria non si adatta a tutte le conformazioni."),
        s("la forma richiede una certa compatibilit\u00e0 con il viso."),
        s("geometricamente non va bene per ogni tipologia di volto."),
        s("la forma esclude alcune tipologie di viso."),
    ],

    s("Li ho portati con look urban bold e"): [
        s("Li ho testati con outfit urban decisi e"),
        s("Li ho provati con look audacemente urbani e"),
        s("Li ho indossati con abbinamenti urban dal taglio forte e"),
        s("Li ho usati con look di strada dal carattere marcato e"),
        s("Li ho messi con outfit urban bold e"),
    ],

    s("Sono il tipo di paia che ti fanno"): [
        s("Sono il genere di occhiali che ti portano a"),
        s("Sono quegli occhiali che ti fanno"),
        s("Sono quel tipo di paio che ti spinge a"),
        s("Sono il modello che ti fa"),
        s("Sono la categoria di occhiali che ti invita a"),
    ],

    s("che su un viso struccato e capelli raccolti che"): [
        s("che su un volto senza trucco e capelli tirati indietro"),
        s("che su un viso pulito e capelli raccolti"),
        s("che su un viso naturale con capelli legati che"),
        s("che con il viso struccato e i capelli su che"),
        s("che su un volto al naturale con capelli raccolti"),
    ],

    s("che con camicia aperta e jeans chiari che"): [
        s("che con camicia aperta e denim chiaro"),
        s("che con camicia sbottonata e jeans chiari"),
        s("che con una camicia aperta e pantaloni chiari che"),
        s("che con camicia casual e jeans chiaro che"),
        s("che con camicia slacciata e jeans di tono chiaro che"),
    ],

    s("che insieme a un look minimale che da solo diceva poco che"): [
        s("che abbinato a un outfit sobrio che da solo era anonimo"),
        s("che con un look essenziale che da solo non diceva niente"),
        s("che affiancato a un look minimale silenzioso"),
        s("che unito a un look sobrio che da solo era piatto"),
        s("che con un outfit minimal poco espressivo di suo"),
    ],

    s("la struttura scura molto essenziale e il riflesso prism"): [
        s("la struttura scura minimal e la rifrazione prism"),
        s("il telaio scuro essenziale e il gioco prismatico"),
        s("la struttura scura lineare e l\u2019effetto prismatico"),
        s("l\u2019ossatura scura e minimale col riflesso prismatico"),
        s("il frame scuro puro e la luce prismatica"),
    ],

    s("struttura grigio carbone, la lente blu specchiata e"): [
        s("struttura grigio carbone, il filtro blu specchiato e"),
        s("telaio grigio carbone, la lente specchiata blu e"),
        s("ossatura grigio carbone, la specchiatura blu e"),
        s("frame grigio carbone, la lente a specchio blu e"),
        s("struttura in grigio carbone, il blu specchiato delle lenti e"),
    ],

    s("e panoramica multicolor. Su di me funzionano bene"): [
        s("e panoramica multicolor. Nel mio caso funzionano bene"),
        s("e panoramica multicolor. Su di me rendono bene"),
        s("e panoramica multicolor. Con me vanno bene"),
        s("e panoramica multicolor. Personalmente li trovo efficaci"),
        s("e panoramica multicolor. Sul mio viso rendono bene"),
    ],

    s("e lente blu specchiata. Su di me funzionano bene"): [
        s("e lente blu specchiata. Nel mio caso funzionano bene"),
        s("e lente blu specchiata. Su di me rendono bene"),
        s("e lente blu specchiata. Con me vanno bene"),
        s("e lente blu specchiata. Personalmente li trovo efficaci"),
        s("e lente blu specchiata. Sul mio viso rendono bene"),
    ],

    s("e riflesso azzurro. Su di me funzionano bene"): [
        s("e riflesso azzurro. Nel mio caso funzionano bene"),
        s("e riflesso azzurro. Su di me rendono bene"),
        s("e riflesso azzurro. Con me vanno bene"),
        s("e riflesso azzurro. Personalmente li trovo efficaci"),
        s("e riflesso azzurro. Sul mio viso rendono bene"),
    ],

    s("la superficie specchiata chiede un po' di attenzione in pi\u00f9."): [
        s("la finitura specchiata richiede qualche cura aggiuntiva."),
        s("le lenti specchiate pretendono un po' pi\u00f9 di manutenzione."),
        s("la superficie a specchio necessita di attenzione extra nella pulizia."),
        s("il rivestimento specchiato vuole qualche accorgimento in pi\u00f9."),
        s("le lenti specchiate esigono un trattamento un po' pi\u00f9 attento."),
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

if len(updates) == 0:
    print("Nessuna sostituzione necessaria.")
    cur.close()
    conn.close()
    sys.exit(0)

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
print("Round 21b OK" if errors == 0 else "Round 21b ERRORI")
