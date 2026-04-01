# -*- coding: utf-8 -*-
import psycopg2, sys
from collections import defaultdict

sys.stdout.reconfigure(encoding='utf-8')

DATABASE_URL = "postgresql://neondb_owner:npg_uFxVSRoTj95w@ep-damp-sea-anvn4fw4.c-6.us-east-1.aws.neon.tech/neondb?sslmode=require"

PATTERNS = {
    # 9x patterns
    "sul mio viso quadrato la forma tonda non è la più facile": [
        "con il mio viso dalla struttura squadrata, la forma circolare richiede un occhio attento",
        "la mia conformazione angolosa fatica a ospitare naturalmente questa montatura così tonda",
        "sulla mia fisionomia a spigoli marcati, la linea rotonda non è mai automatica",
        "con un viso come il mio, portare una tonda è sempre un esercizio d'attenzione",
        "la mia struttura facciale squadrata convive con fatica con una forma così rotonda",
        "sul mio viso angoloso, una montatura tonda richiede sempre un certo sforzo",
        "la mia conformazione netta si scontra con la curva tondeggiante di questa montatura",
        "con la fronte e la mascella marcate, il rotondo mi richiede più riflessione",
        "sulla mia geometria facciale decisa, questa forma ovale incontra qualche resistenza",
        "il mio viso squadrato non ha vita facile con le montature così circolari",
    ],
    "nel quotidiano classico per me è quasi troppo": [
        "nel giorno per giorno, un classico così formale tende a risultarmi eccessivo",
        "portato tutti i giorni, il registro tradizionale finisce per pesarmi",
        "nell'uso quotidiano, questo tipo di formalità supera le mie abitudini",
        "nella routine giornaliera, sento che tanta sobrietà classica non fa per me",
        "nell'uso pratico di ogni giorno, un'impostazione così tradizionale eccede il mio stile",
        "giorno dopo giorno, il registro classico così deciso mi risulta oppressivo",
        "nell'uso ordinario, la sobrietà di questo modello va oltre ciò che cerco",
        "nella vita di tutti i giorni, un paio così formale finisce per limitarmi",
        "nel quotidiano senza occasioni speciali, la sua impostazione classica pesa un po' troppo",
        "nell'uso continuativo, la formalità del modello si fa sentire più del previsto",
    ],
    "lo specchio richiede un po' di cura": [
        "la lente specchiata va trattata con qualche attenzione in più",
        "la superficie a specchio ha bisogno di manutenzione regolare",
        "le lenti riflettenti si graffiano con una certa facilità",
        "il finish specchiato si deteriora se non accudito",
        "il trattamento a specchio chiede attenzione quotidiana",
        "la lente con effetto mirror si sporca con facilità",
        "mantenere la specchiatura presentabile non è senza impegno",
        "il rivestimento riflettente è sensibile a graffi e impronte",
        "lo strato specchiato impone qualche precauzione in più rispetto al solito",
        "il coating speculare mostra il deterioramento più rapidamente di altri finish",
    ],
    "specchio ghiaccio crea un insieme davvero": [
        "lente riflettente ghiaccio produce un risultato davvero",
        "lente color ghiaccio forma un abbinamento davvero",
        "effetto ice sulla lente costruisce qualcosa di davvero",
        "specchiatura ghiaccio offre un effetto davvero",
        "rifinitura ghiaccio sulle lenti compone qualcosa di davvero",
        "trattamento specchio in tono ghiaccio dà vita a qualcosa di davvero",
        "lente con riflesso ghiaccio produce un'estetica davvero",
        "visiera riflettente in tonalità ghiaccio genera qualcosa di davvero",
        "coating speculare in tono ghiaccio restituisce un effetto davvero",
        "il mirror ghiaccio sulla lente costruisce un insieme davvero",
    ],
    "su visi molto squadrati vanno provati bene": [
        "su lineamenti molto angolosi è consigliabile provarli prima dell'acquisto",
        "su visi marcatamente squadrati è necessario valutare il fit di persona",
        "su fisionomie molto angolate andrebbero testati con attenzione",
        "su conformazioni facciali molto nette la verifica in store è indispensabile",
        "su strutture facciali molto angolari la prova fisica prima di comprare è obbligatoria",
        "dove la mascella è molto pronunciata, il test diretto è raccomandato",
        "su visi dall'angolatura decisa andrebbero verificati di persona",
        "su fisionomie con spigoli marcati la prova è fondamentale",
        "su conformazioni molto geometriche conviene sempre provare prima",
        "su visi con la conformazione più netta è preferibile testarli prima",
    ],
    "non li trovo ideali per guidare": [
        "non me li vedo indicati in modo particolare per la guida",
        "alla guida non si dimostrano tra le opzioni più adatte",
        "non sarebbero la mia scelta principale in auto",
        "dietro al volante mi sono trovato un po' a disagio con loro",
        "non li definirei occhiali per la guida",
        "in auto si dimostrano meno adatti di quanto pensassi",
        "portarli alla guida non valorizza le loro qualità",
        "al volante si sente che non è il loro contesto migliore",
        "con loro sul naso, guidare non è la situazione più confortevole",
        "la guida non è il loro punto di forza",
    ],
    "il grigio scuro delle lenti e": [
        "il grigio molto profondo delle lenti e",
        "il filtro grigio intenso delle lenti e",
        "la tonalità grigia marcata delle lenti e",
        "il grigio carico delle lenti e",
        "le lenti nel grigio scuro e",
        "le lenti dalla tinta grigio pieno e",
        "il grigio denso del filtro e",
        "la tinta grigio molto scura delle lenti e",
        "la lente grigio quasi antracite e",
        "la lente dal grigio profondo e",
    ],
    "su visi rotondi vanno provati con calma": [
        "su lineamenti circolari è bene valutare con attenzione prima di comprare",
        "su fisionomie molto rotonde andrebbero testati di persona senza fretta",
        "su visi dall'ovale tondeggiante la prova diretta è essenziale",
        "su conformazioni facciali circolari è consigliabile verificare di persona",
        "su visi dall'ovale pieno la valutazione richiede più tempo del solito",
        "su lineamenti arrotondati è preferibile non acquistare senza aver provato",
        "su fisionomie rotonde il fit merita una considerazione attenta",
        "su visi di forma circolare si consiglia un test fisico prima dell'acquisto",
        "su conformazioni più tondeggianti andrebbero verificati in negozio",
        "su un viso molto rotondo l'acquisto merita una prova fisica",
    ],
    "parlano chiaramente il linguaggio dello sport": [
        "comunicano senza dubbi la loro anima sportiva",
        "esprimono con chiarezza l'identità atletica del progetto",
        "dichiarano esplicitamente la loro vocazione all'attività fisica",
        "il loro DNA sportivo è evidente senza ambiguità",
        "si riconoscono immediatamente come accessori per la performance",
        "appartengono senza equivoci al lessico dell'abbigliamento tecnico",
        "la matrice atletica non lascia margini a interpretazioni diverse",
        "il loro carattere agonistico è riconoscibile a prima vista",
        "dichiarano apertamente la vocazione al movimento",
        "la provenienza sportiva si legge con facilità assoluta",
    ],
    "il fit a ponte alto non è": [
        "la configurazione per ponte rialzato non è",
        "il taglio progettato per nasi importanti non è",
        "la montatura a ponte elevato non è",
        "il design per ponte alto non è",
        "la variante a ponte rialzato non è",
        "il profilo per nasi alti non è",
        "la costruzione a ponte alto non è",
        "l'impostazione a ponte rialzato non è",
        "il modello pensato per ponte alto non è",
        "la versione a ponte elevato non è",
    ],
    "è che impianto shield molto deciso": [
        "è che questa costruzione shield molto pronunciata",
        "è che il design a visiera molto deciso",
        "è che l'impostazione shield così marcata",
        "è che la struttura a lente unica molto definita",
        "è che questo telaio a visiera molto netto",
        "è che il progetto shield così assertivo",
        "è che l'architettura a scudo così decisa",
        "è che questa montatura shield molto presente",
        "è che la forma a visiera molto reoluta",
        "è che il concept shield così definito",
    ],
    "Ha una forza visiva quasi da palco": [
        "Ha un'energia visiva che richiama la scenografia da palcoscenico",
        "Ha un impatto quasi da scena teatrale",
        "Ha una presenza che si avverte anche a distanza",
        "Ha un peso visivo che appartiene alla performance",
        "Ha un'enfasi visiva da show più che da quotidiano",
        "Ha una potenza scenica che supera il semplice accessorio",
        "Ha un'audacia visiva che evoca il mondo dello spettacolo",
        "Ha una forza di presenza che non passa mai inosservata",
        "Ha un'intensità visiva che ricorda la scena più che la strada",
        "Ha una statura visiva che appartiene agli spazi aperti",
    ],
    # 8x patterns (preventive)
    "non è il più universale nei mesi freddi": [
        "perde versatilità durante la stagione più fredda",
        "non è il più adatto durante i mesi invernali",
        "nelle stagioni fredde risulta meno polifunzionale",
        "con i cappotti e i maglioni non trova il suo habitat naturale",
        "l'inverno non è il suo periodo di massima efficacia",
        "in inverno il suo campo di utilizzo si restringe notevolmente",
        "non si abbina con la stessa facilità agli outfit invernali",
        "nelle temperature basse la sua versatilità soffre un po'",
        "con l'abbigliamento pesante risulta meno immediato da abbinare",
        "non è il candidato più ovvio per i mesi di freddo intenso",
    ],
    "non sono facili con tutti i visi": [
        "non si adattano a ogni conformazione facciale con uguale facilità",
        "non ogni viso li porta con la stessa naturalezza",
        "la loro forma non è egualmente generosa con tutti i profili",
        "non si prestano allo stesso modo su ogni tipo di viso",
        "richiedono una conformazione specifica per funzionare al meglio",
        "non sono democraticamente adatti a ogni fisionomia",
        "si addicono a certi visi molto meglio che ad altri",
        "non funzionano su ogni conformazione facciale con lo stesso risultato",
        "il loro successo dipende molto dalla fisionomia di chi li porta",
        "non offrono la stessa resa su tutti i profili",
    ],
    "e la parte migliore è che": [
        "e il dettaglio che più mi ha sorpreso è che",
        "e il punto di forza principale è che",
        "e ciò che ho apprezzato di più è che",
        "e il vantaggio che emerge con chiarezza è che",
        "e la qualità che convince di più è che",
        "e la caratteristica più positiva è che",
        "e la sorpresa più grande è che",
        "e l'aspetto che più colpisce è che",
        "e il fatto che più mi ha convinto è che",
        "e tra i pregi quello che emerge di più è che",
    ],
    "in un modo che apprezzo molto": [
        "in modo da convincermi del tutto",
        "con un risultato che trovo soddisfacente",
        "in un modo che ho apprezzato più del previsto",
        "con un equilibrio che ritengo ben calibrato",
        "in una maniera che mi convince",
        "con esiti che trovo piacevolmente coerenti",
        "in una sinergia che reputo riuscita",
        "con risultati migliori di quanto mi aspettassi",
        "in modo da non farmi rimpiangere l'acquisto",
        "con un'armonia che non mi aspettavo così solida",
    ],
    "Sa essere protagonista in modo molto chiaro": [
        "Si impone senza sforzo come pezzo di scena",
        "Riesce a dominare la scena in modo netto",
        "Ottiene attenzione senza costruire nulla intorno",
        "Si mette in primo piano con totale naturalezza",
        "Riempie il campo visivo senza esitazioni",
        "Diventa il centro del look senza dover chiedere permesso",
        "Emerge come protagonista con la massima semplicità",
        "Prende la scena in modo incontestabile",
        "Si fa notare senza fatica e senza scuse",
        "Si impone nel look senza compromessi",
    ],
    "Non lo rifiuto, ma non è": [
        "Non lo escludo, ma non è proprio",
        "Non lo scarto, eppure non è",
        "Non lo boccio in toto, ma non è",
        "Non lo ignoro, però non è",
        "Non lo elimino, anche se non è",
        "Non lo cancello a priori, ma non è",
        "Non lo escludo formalmente, però non è",
        "Non lo rifiuto in blocco, ma non è",
        "Non lo cassetto, sebbene non sia",
        "Non lo boccio, anche se non è",
    ],
}

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
print(f"Aggiornate: {len(updates)} | Errori: {errors}")
print("Round 16 OK" if errors == 0 else "Round 16 ERRORI")
