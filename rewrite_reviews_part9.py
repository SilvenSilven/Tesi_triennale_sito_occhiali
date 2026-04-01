#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Parte 9: Pattern residui quarto passaggio (8-9x dopo terzo passaggio + alcune 7x)
"""
from rewrite_reviews_part8 import PATTERNS

# ═══════════════════════════════════════════════════════════
# FRASI 9x
# ═══════════════════════════════════════════════════════════

PATTERNS["Riescono a essere distintivi senza diventare stancanti."] = [
    "Hanno personalità senza risultare eccessivi.",
    "Si distinguono senza affaticare l'occhio.",
    "Hanno carattere senza mai stancare.",
    "Sono riconoscibili senza diventare invadenti.",
    "Riescono a farsi notare senza pesare.",
    "Hanno identità forte ma mai eccessiva.",
    "Colpiscono senza generare saturazione.",
    "Sanno distinguersi mantenendo leggerezza.",
    "Sono originali senza essere opprimenti.",
]

PATTERNS["Resto in una zona di mezzo: capisco il progetto, non lo amo del tutto."] = [
    "Sono a metà strada: comprendo l'idea ma non mi conquista.",
    "Capisco il concetto senza arrivare ad amarlo.",
    "Rimango in bilico tra apprezzamento razionale e trasporto mancante.",
    "Il progetto mi arriva alla testa, non al cuore.",
    "Lo comprendo ma non lo sento mio fino in fondo.",
    "Sto nel mezzo: stima sì, amore no.",
    "Il progetto lo capisco, il feeling rimane tiepido.",
    "Apprezzo l'idea senza innamorarmene.",
    "Sono in una terra di mezzo: rispetto senza passione.",
]

PATTERNS["Pi\u00f9 che universali, li definirei coerenti con un gusto preciso."] = [
    "Non sono per tutti, ma per chi ha un gusto definito sono perfetti.",
    "Più che trasversali, li direi fatti per un gusto specifico.",
    "Non pretendono universalità: parlano a una sensibilità precisa.",
    "Il loro bello è che non cercano di piacere a tutti.",
    "Più che adattabili, sono fedeli a un'estetica definita.",
    "Li definirei mirati più che universali.",
    "Non sono democratici: sono coerenti con una visione estetica.",
    "Funzionano per chi condivide un certo gusto, non per chiunque.",
    "Il target è preciso e la coerenza con quel target è totale.",
]

PATTERNS["Nel loro linguaggio estetico, sono centrati in pieno."] = [
    "All'interno del loro codice estetico colpiscono il bersaglio.",
    "Il loro linguaggio visivo è pienamente centrato.",
    "Rispetto alla loro cifra stilistica sono impeccabili.",
    "Nel loro registro espressivo non sbagliano nulla.",
    "Dentro il loro universo estetico sono perfetti.",
    "Il loro codice stilistico è eseguito alla perfezione.",
    "Nel quadro della loro estetica non c'è nulla fuori posto.",
    "La coerenza col proprio linguaggio estetico è totale.",
    "All'interno della loro grammatica visiva sono centratissimi.",
]

PATTERNS["Sono un bel s\u00ec, con qualche piccola riserva."] = [
    "Il verdetto è positivo, con qualche piccola nota a margine.",
    "É un sì convinto, con qualche minima riserva.",
    "Li promuovo con qualche piccola annotazione.",
    "Il giudizio è favorevole, con qualche leggera sfumatura.",
    "Sono un sì solido, non immacolato.",
    "Li approvo, pur con qualche lieve perplessità.",
    "La risposta è sì, con qualche postilla minore.",
    "Un parere positivo con qualche piccola eccezione.",
    "Il bilancio è positivo, con qualche riserva marginale.",
]

# ═══════════════════════════════════════════════════════════
# FRASI 8x
# ═══════════════════════════════════════════════════════════

PATTERNS["Per me sono pieni di personalit\u00e0 ma restano portabili."] = [
    "Hanno moltissimo carattere senza smettere di essere indossabili.",
    "La personalità è forte ma non compromette la portabilità.",
    "Riescono ad avere identità senza sacrificare la praticità d'uso.",
    "Sono espressivi ma restano comodi da indossare ogni giorno.",
    "L'identità è marcata ma non ostacola l'uso quotidiano.",
    "Hanno personalità da vendere senza mai diventare scomodi da portare.",
    "La personalità c'è tutta, senza penalizzare la vestibilità.",
    "Sono caratteriali ma perfettamente portabili nel quotidiano.",
]

PATTERNS["La qualit\u00e0 dell\u2019idea c\u2019\u00e8, la compatibilit\u00e0 con me meno."] = [
    "L'idea è valida, la compatibilità col mio viso meno.",
    "Il progetto è buono, il riscontro personale no.",
    "L'idea non è in discussione: è la resa su di me a deludere.",
    "Di base il concept funziona, su di me meno.",
    "L'idea è ben concepita, la sua traduzione sul mio viso no.",
    "Il progetto è interessante, la resa nella mia esperienza meno.",
    "Come idea è valido, come esperienza su di me meno.",
    "L'idea merita, la compatibilità con la mia persona meno.",
]
PATTERNS["La qualit\u00e0 dell'idea c'\u00e8, la compatibilit\u00e0 con me meno."] = PATTERNS["La qualit\u00e0 dell\u2019idea c\u2019\u00e8, la compatibilit\u00e0 con me meno."]

PATTERNS["Sono uno di quei paia che continuano a crescermi addosso."] = [
    "Continuano a piacermi di più col passare del tempo.",
    "Col tempo li apprezzo sempre di più.",
    "Sono di quei modelli che guadagnano nel tempo.",
    "Ogni volta che li riprendo li trovo un po' migliori.",
    "Il gradimento cresce a ogni utilizzo.",
    "L'apprezzamento continua a salire col tempo.",
    "Sono di quei paia il cui valore si scopre nell'uso prolungato.",
    "Col passare delle settimane li apprezzo sempre di più.",
]

# ═══════════════════════════════════════════════════════════
# FRASI 7x (più frequenti / fastidiose)
# ═══════════════════════════════════════════════════════════

PATTERNS["Mi sembrano occhiali da scegliere con intenzione, non per automatismo."] = [
    "Richiedono una scelta consapevole, non istintiva.",
    "Non sono il paio che si prende per abitudine: vanno scelti con criterio.",
    "Sono un acquisto che richiede consapevolezza nella scelta.",
    "Vanno scelti con cognizione di causa, non come ripiego.",
    "Richiedono una decisione ragionata, non un impulso.",
    "Sono un paio da prendere con intenzione, non per default.",
    "L'acquisto va ponderato: non sono occhiali da scelta automatica.",
]

PATTERNS["Mi piacciono abbastanza da usarli spesso comunque."] = [
    "Nonostante tutto li uso con una certa frequenza.",
    "Li apprezzo abbastanza da portarli regolarmente.",
    "L'uso frequente resta, malgrado le riserve.",
    "Le piccole imperfezioni non mi impediscono di usarli spesso.",
    "Li scelgo regolarmente nonostante le mie perplessità.",
    "L'uso frequente la dice lunga, al di là delle mie riserve.",
    "Malgrado qualche dubbio, finiscono spesso addosso a me.",
]

PATTERNS["Dal vivo hanno una misura che le foto non restituiscono bene."] = [
    "Le foto non catturano le proporzioni che si vedono dal vivo.",
    "La resa dal vivo rivela proporzioni che le immagini nascondono.",
    "Le foto non rendono giustizia alla misura reale.",
    "La dimensione percepita dal vivo è diversa da quella in foto.",
    "Le proporzioni reali sono diverse da come appaiono in foto.",
    "Dal vivo le misure hanno un equilibrio che le foto non trasmettono.",
    "La resa dimensionale dal vivo supera quella fotografica.",
]

PATTERNS["Li vedo bene soprattutto in citt\u00e0."] = [
    "Il loro habitat naturale è il contesto urbano.",
    "Funzionano al meglio in ambito cittadino.",
    "Sono al loro meglio nel contesto cittadino.",
    "Il contesto urbano è quello dove brillano di più.",
    "Danno il meglio in scenari cittadini.",
    "In città sono nel loro elemento.",
    "Rendono al massimo nel contesto della vita urbana.",
]

PATTERNS["Su di me restano pi\u00f9 belli da vedere che da portare."] = [
    "Sul mio viso sono più estetici che funzionali.",
    "L'estetica vince sulla praticità d'uso, almeno su di me.",
    "Li trovo più belli in mano che addosso.",
    "Sono più un piacere visivo che un piacere d'uso, per me.",
    "Sul mio viso funzionano più come oggetto da ammirare.",
    "Per me restano più belli nel cassetto che addosso.",
    "Sono più belli da guardare che da indossare, sul mio volto.",
]

PATTERNS["Il dettaglio legno cambia davvero la temperatura del modello."] = [
    "Il legno dona al modello un calore che altrimenti non avrebbe.",
    "L'inserto in legno trasforma completamente la percezione termica del design.",
    "Il tocco di legno aggiunge una dimensione calda che definisce il modello.",
    "Il legno sposta tutto il registro del modello verso toni più caldi.",
    "L'elemento ligneo regala un carattere caldo che trasforma la percezione.",
    "Il dettaglio in legno cambia l'intero registro cromatico del modello.",
    "Il legno dona un calore unico che eleva il design ad un altro livello.",
]

PATTERNS["Ha una calma che molti aviator moderni hanno perso."] = [
    "Trasmette una serenità che la maggior parte degli aviator attuali non ha.",
    "Ha una compostezza che negli aviator moderni è rara.",
    "Possiede una pacatezza che molti aviator di oggi hanno dimenticato.",
    "Emana una calma che gli aviator moderni faticano a raggiungere.",
    "Ha una quiete stilistica che la maggior parte degli aviator recenti ha perso.",
    "Conserva una tranquillità estetica rara tra gli aviator contemporanei.",
    "Ha un aplomb che molti aviator recenti non riescono a trasmettere.",
]

PATTERNS["Sembra costruito per il movimento e per l\u2019effetto scenico insieme."] = [
    "Funziona sia in movimento che come puro impatto visivo.",
    "È pensato tanto per essere portato quanto per essere visto.",
    "Combina dinamismo e spettacolarità in un unico design.",
    "Funziona in azione e in posa con la stessa efficacia.",
    "Unisce la resa in movimento all'impatto scenografico.",
    "È al contempo funzionale nel movimento e scenografico da fermo.",
    "La resa è impeccabile sia in dinamica che in statica.",
]
PATTERNS["Sembra costruito per il movimento e per l'effetto scenico insieme."] = PATTERNS["Sembra costruito per il movimento e per l\u2019effetto scenico insieme."]

print(f"Parte 9 caricata: totale {len(PATTERNS)} pattern definiti")
