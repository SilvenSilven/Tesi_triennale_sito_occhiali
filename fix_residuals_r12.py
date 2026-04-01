#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fix round 12 — pattern n-gram 10-14x residui post round 11."""

import psycopg2

DATABASE_URL = (
    "postgresql://neondb_owner:npg_uFxVSRoTj95w"
    "@ep-damp-sea-anvn4fw4.c-6.us-east-1.aws.neon.tech"
    "/neondb?sslmode=require"
)

PATTERNS = {

    # 14x — frammento ponte
    "sul mio naso il doppio ponte": [
        "sul mio profilo il doppio ponte",
        "per il mio naso il doppio ponte",
        "sul mio viso il doppio ponte",
        "nel mio caso il doppio ponte",
        "per me il doppio ponte",
        "sulla mia conformazione il doppio ponte",
        "sul mio naso la struttura a doppio ponte",
        "per il mio profilo il doppio ponte",
        "per la mia struttura il doppio ponte",
        "nel mio caso specifico il doppio ponte",
        "per la morfologia del mio naso il doppio ponte",
        "sulla mia forma il doppio ponte",
        "in relazione al mio naso il doppio ponte",
        "per la forma del mio viso il doppio ponte",
        "rispetto alla struttura del mio naso il doppio ponte",
    ],

    # 13x — frammento inizio frase con connettore "è che"
    "Appena tolti dalla custodia, è che": [
        "Appena estratti dalla custodia, constato che",
        "Non appena aperti, emerge che",
        "Appena fuori dalla scatola, si nota che",
        "Al primo utilizzo, si capisce che",
        "Subito dopo averli presi in mano, si vede che",
        "Appena indossati per la prima volta, appare chiaro che",
        "Al primo contatto, risulta evidente che",
        "Appena aperti, si capisce immediatamente che",
        "Non appena estratti, si rivela che",
        "Appena tolti dall'astuccio, si nota che",
        "Al primo sguardo ravvicinato, si capisce che",
        "Non appena tenuti in mano, emerge subito che",
        "Aprendo la custodia, si vede già che",
        "Subito dopo l'apertura, è evidente che",
    ],

    # 13x — connettore temporale con "è che"
    "Col passare dei giorni, è che": [
        "Col trascorrere dei giorni, emerge che",
        "Nel corso del tempo, si capisce che",
        "Passati i giorni iniziali, si nota che",
        "Con l'uso continuato, si capisce che",
        "A distanza di qualche giorno, risulta che",
        "Dopo qualche giorno di uso, si chiarisce che",
        "Andando avanti nel tempo, si nota che",
        "Con l'uso ripetuto, emerge chiaramente che",
        "Dopo i primi giorni, si capisce che",
        "Con il passare del tempo, si vede che",
        "A uso prolungato, emerge che",
        "Procedendo con l'uso, si nota che",
        "Dopo qualche settimana, si capisce che",
        "Nel tempo, emerge che",
    ],

    # 12x — connettore descrittivo
    "Capisco la proposta perché la montatura": [
        "Comprendo il progetto perché la montatura",
        "Capisco l'idea perché la struttura",
        "Intuisco il senso perché la montatura",
        "Leggo il concept perché la montatura",
        "Apprezzo la logica perché la montatura",
        "Capisco l'intenzione perché la montatura",
        "Ha senso il progetto perché la montatura",
        "Comprendo l'approccio perché la struttura",
        "La proposta ha logica perché la montatura",
        "Capisco la scelta perché la montatura",
        "Ha senso: la montatura",
        "Il progetto è comprensibile: la montatura",
        "Se ne capisce il senso: la montatura",
    ],

    # 11x — cross-sentence (versione maschile)
    "Invece hanno un": [
        "In realtà hanno un",
        "Sorprendentemente hanno un",
        "Contro ogni aspettativa, hanno un",
        "Eppure mostrano un",
        "A sorpresa rivelano un",
        "Al contrario mostrano un",
        "Inaspettatamente hanno un",
        "Nonostante tutto hanno un",
        "Diversamente da quanto temevo, hanno un",
        "La realtà è che hanno un",
        "A ben guardare hanno un",
        "Alla prova dei fatti hanno un",
        "Si rivela invece che hanno un",
    ],

    # 11x — frase ripetuta
    "Li sto usando più del previsto": [
        "Li indosso più spesso di quanto mi aspettassi",
        "Li utilizzo più frequentemente del previsto",
        "Li porto più di quanto avrei detto",
        "Finisco per indossarli più di quanto immaginavo",
        "Li uso più di quanto pensassi",
        "Li sto portando con una frequenza inaspettata",
        "Li metto più spesso del previsto",
        "Li indosso più di quanto avessi pianificato",
        "Li sto usando con una continuità che non avevo previsto",
        "Li porto con più costanza di quanto mi aspettassi",
        "Li utilizzo ben più di quanto prevedevo",
        "Li scelgo più spesso di quanto immaginassi",
    ],

    # 11x — frammento temporale
    "del giorno dopo, e qui ha": [
        "del giorno seguente, e lì emerge",
        "il giorno dopo, e in quel contesto si è",
        "il giorno successivo, e qui si è",
        "del secondo giorno, e qui emerge",
        "il giorno successivo, e qui ha",
        "della seconda giornata, e lì ha",
        "nel giorno seguente, e in quel frangente ha",
        "nella giornata successiva, e qui emerge",
        "del giorno dopo, e in quella occasione ha",
        "del secondo utilizzo, e lì ha",
        "dopo il primo giorno, e in quel contesto ha",
        "nel secondo giorno d'uso, e qui emerge",
    ],

    # 11x — cross-sentence
    "quasi per niente. Avevo immaginato che": [
        "quasi per niente. Non pensavo che",
        "quasi per niente. Credevo che",
        "quasi per niente. Avevo l'idea che",
        "quasi per niente. Mi aspettavo che",
        "quasi per niente. La mia impressione iniziale era che",
        "quasi per niente. Partivo dall'idea che",
        "quasi per niente. Pensavo inizialmente che",
        "quasi per niente. Mi ero convinto che",
        "quasi per niente. Avevo ipotizzato che",
        "quasi per niente. In origine pensavo che",
        "quasi per niente. Prima di provarli credevo che",
        "quasi per niente. Partendo dalle premesse, pensavo che",
    ],

    # 11x — frammento
    "il ponte alto è selettivo e": [
        "la sella alta è selettiva e",
        "questa struttura del ponte è esigente e",
        "il ponte rialzato è selettivo e",
        "una sella così alta risulta selettiva e",
        "il pontale alto è selettivo e",
        "questa sella è molto selettiva e",
        "il ponte in quel punto è esigente e",
        "una sella così è di certo selettiva e",
        "il naso alto del modello è selettivo e",
        "la conformazione del ponte è selettiva e",
        "il ponte elevato di questo modello è selettivo e",
        "questa configurazione del ponte è selettiva e",
    ],

    # 10x — fine frase
    "non sono affatto un paio democratico.": [
        "non sono adatti a ogni tipologia di viso.",
        "non si adattano a qualsiasi profilo.",
        "non sono una scelta universale.",
        "richiedono una specificità del viso.",
        "non vanno bene per tutti.",
        "non sono pensati per chiunque.",
        "hanno esigenze precise di conformazione.",
        "non risultano adatti a tutti i visi.",
        "sono selettivi in termini di fit.",
        "non sono per tutti i profili.",
        "pongono condizioni di compatibilità precise.",
        "richiedono il giusto tipo di viso.",
    ],

    # 10x — fine frase con carattere specifico
    "hanno una personalità forte ma studiata.": [
        "mostrano una personalità forte ma calibrata.",
        "esprimono un carattere deciso ma equilibrato.",
        "hanno una presenza robusta ma misurata.",
        "portano una personalità netta ma non aggressiva.",
        "hanno una cifra rilevante ma non urlata.",
        "esprimono una personalità marcata ma non eccessiva.",
        "hanno carattere ma lo gestiscono con misura.",
        "portano identità forte ma senza stridere.",
        "hanno una personalità che si impone senza esagerare.",
        "mostrano forza senza perdere eleganza.",
        "hanno una personalità distinta ma controllata.",
        "portano carattere forte ma con un certo controllo.",
    ],

    # 10x — frase completa
    "sembrano fatti per entrare prima della persona.": [
        "sembrano disegnati per farsi notare prima di chi li indossa.",
        "hanno la presenza di chi arriva sempre prima degli altri.",
        "si fanno annunciare prima ancora di essere visti da vicino.",
        "sono il tipo di accessorio che precede il suo portatore.",
        "entrano nella stanza prima di chi li porta.",
        "hanno quella presenza che si avverte prima dell'arrivo.",
        "si presentano da soli, prima ancora dell'occhio di chi li guarda.",
        "sono fatti per farsi vedere prima della persona che li porta.",
        "creano un'impressione che precede l'incontro.",
        "sembrano pensati per precedere chi li indossa.",
        "hanno una presenza che anticipa quella di chi li porta.",
        "sembrano costruiti per occupare la scena prima del loro portatore.",
    ],

    # 10x — fine frase
    "mi coprono fin troppo la zona sopraccigliare.": [
        "coprono in modo eccessivo il sopracciglio.",
        "nascondono troppo la zona del sopracciglio.",
        "oscurano la zona sopraccigliare oltre il necessario.",
        "coprono il sopracciglio più del dovuto.",
        "nascondono il sopracciglio in maniera eccessiva.",
        "coprono troppo la parte alta del viso.",
        "invadono la zona sopraccigliare in eccesso.",
        "nascondono troppo la zona delle sopracciglia.",
        "coprono la zona sopraccigliare in macrodose.",
        "coprono eccessivamente la zona alta del viso.",
        "coprono il sopracciglio fin troppo.",
        "invadono la zona sopraccigliare in modo eccessivo.",
    ],

    # 10x — fine frase
    "rispetto più di quanto ami davvero.": [
        "apprezzo come prodotto più di quanto ami indossarlo.",
        "stimo più come progetto che come compagna quotidiana.",
        "rispetto come oggetto più di quanto lo ami sul viso.",
        "apprezzo il design più di quanto lo ami nell'uso.",
        "stimo il lavoro fatto più di quanto li ami da portare.",
        "rispetto l'idea più di quanto ami il risultato addosso.",
        "apprezzo la concezione più di quanto li ami realmente.",
        "stimo il progetto più di quanto li ami da indossare.",
        "rispetto il prodotto più di quanto ne sia innamorato.",
        "li apprezzo in modo intellettuale più che emotivo.",
        "li rispetto senza amarli davvero.",
        "li stimo come oggetto senza amarli come scelta.",
    ],

    # 10x — inizio frase
    "Li ho portati per un pranzo": [
        "Li ho indossati per un pranzo",
        "Li ho usati per un pranzo",
        "Li ho portati a pranzo",
        "Li ho messi per un pranzo",
        "Li ho scelti per un pranzo",
        "Li ho calzati per un pranzo",
        "Li ho utilizzati per un pranzo",
        "Li ho provati per un pranzo",
        "Li ho portati in occasione di un pranzo",
        "Li ho abbinati a un pranzo",
        "Li ho portati durante un pranzo",
        "Li ho indossati in occasione di un pranzo",
    ],

    # 10x — frammento
    "La parte migliore è che il": [
        "Il punto più riuscito è che il",
        "L'aspetto migliore è che il",
        "L'elemento più positivo è che il",
        "Il dato migliore è che il",
        "La nota più positiva è che il",
        "La voce più rilevante è che il",
        "Il punto di forza principale è che il",
        "Il lato migliore è che il",
        "La qualità più evidente è che il",
        "Il pregio principale è che il",
        "Il vantaggio più chiaro è che il",
        "L'osservazione più positiva è che il",
    ],

    # 10x
    "Su di me funzionano bene quando": [
        "Per me danno il meglio quando",
        "Sul mio profilo si esprimono al meglio quando",
        "Per la mia morfologia rendono quando",
        "Sul mio viso funzionano quando",
        "Per me rendono di più quando",
        "Nel mio caso funzionano bene quando",
        "Per come mi vesto, riescono meglio quando",
        "Per il mio stile funzionano quando",
        "Sul mio profilo funzionano meglio quando",
        "Per la mia testa danno il meglio quando",
        "Nel mio uso quotidiano funzionano bene quando",
        "Per me è un buon risultato quando",
    ],

    # 10x — frammento valutativo
    "Per me è uno di quegli acquisti": [
        "Nel mio caso è uno di quegli acquisti",
        "Per me rientra in quella categoria di acquisti",
        "Sul mio giudizio è uno di quegli acquisti",
        "Si tratta per me di uno di quegli acquisti",
        "Lo classifico tra quegli acquisti",
        "È per me uno di quei prodotti",
        "Per il mio profilo è uno di quegli acquisti",
        "Nelle mie valutazioni rientra tra quegli acquisti",
        "Nella mia esperienza è uno di quegli acquisti",
        "Lo considero uno di quegli acquisti",
        "Per me appartiene alla categoria di acquisti",
        "Nel mio bilancio è uno di quegli acquisti",
    ],

    # 10x — frase completa
    "sui visi allungati la forma va provata con attenzione.": [
        "per i profili lunghi è necessario provarla con cura.",
        "sui visi stretti e lunghi occorre verificare la compatibilità.",
        "chi ha un viso allungato deve provare prima di decidere.",
        "per i visi ovali allungati la compatibilità non è automatica.",
        "su un profilo allungato il modello richiede una prova.",
        "sui visi lunghi la forma non è universalmente adatta.",
        "per la struttura allungata del viso serve una prova attenta.",
        "sui profili allungati la fit va verificata sul posto.",
        "chi ha un viso lungo deve valutare con cura.",
        "la forma non si adatta automaticamente ai visi allungati.",
        "per i visi allungati la compatibilità non è scontata.",
        "per un viso lungo serve cautela prima dell'acquisto.",
    ],

    # 10x
    "senza costruirgli attorno una scenografia, e": [
        "senza allestire una scenografia intorno a lui, e",
        "senza costruire un contesto scenico, e",
        "senza creare un palcoscenico ad hoc, e",
        "senza mettere in scena nulla di costruito, e",
        "senza bisogno di allestimento, e",
        "senza costruire un palcoscenico intorno, e",
        "senza una scenografia forzata, e",
        "senza allestire nulla di artificiale, e",
        "senza creare un'architettura visiva intorno, e",
        "senza mettere in scena nulla di artefatto, e",
        "senza bisogno di supporto scenico, e",
    ],

    # 10x — frammento su colore
    "il verde non si abbina con": [
        "questo verde non dialoga con",
        "la tinta verde non va con",
        "il tono verde non si sposa con",
        "il verde delle lenti non si abbina a",
        "questo filtro verde non funziona con",
        "la gradazione verde stona con",
        "il colore verde scelto non si abbina con",
        "il verde specifico delle lenti non si accorda con",
        "questa tonalità verde non va bene con",
        "il verde di questo modello non si accoppia con",
        "la colorazione verde non si abbina facilmente a",
    ],

    # 10x — fine frase (pressione)
    "dopo un po' mi accorgo della pressione sul ponte.": [
        "col tempo avverto fastidio al ponte.",
        "dopo qualche ora percepisco pressione sul naso.",
        "con l'uso prolungato il ponte diventa scomodo.",
        "a lungo andare il ponte pesa.",
        "dopo un po' il ponte si fa sentire.",
        "continuando a portarli avverto il ponte.",
        "nel corso della giornata il ponte diventa un problema.",
        "andando avanti la sella inizia a dare fastidio.",
        "più li porto, più sento il peso sul naso.",
        "dopo qualche ora di uso il ponte si fa sentire.",
        "a distanza di tempo avverto la pressione sul ponte.",
        "nel lungo periodo la sella pesa.",
    ],

    # 10x — frammento design
    "linea aperta senza bordo pieno e": [
        "struttura aperta senza bordo completo e",
        "lente senza montatura piena e",
        "montatura aperta priva di bordo completo e",
        "forma semi-rimless senza bordo chiuso e",
        "design aperto senza piena chiusura e",
        "contorno senza bordo pieno e",
        "stile aperto privo di bordo integrale e",
        "segno aperto senza chiusura piena e",
        "modello a struttura aperta privo di bordo e",
        "configurazione senza bordo completo e",
        "morfologia aperta priva di bordo chiuso e",
    ],

    # 10x — fin di frase positiva
    "è il paio più memorabile del": [
        "è il modello più indimenticabile del",
        "è il pezzo più memorabile del",
        "è l'occhiale più memorabile del",
        "è in assoluto il più memorabile del",
        "è senz'altro il più ricordabile del",
        "è il modello che si dimentica meno nel",
        "è il modello che resta impresso nel",
        "è il più distinto del",
        "è l'acquisto più duraturo nel ricordo del",
        "è il paio che rimane impresso nel",
        "è senz'altro il più forte del",
        "è il modello che lascia più traccia nel",
    ],

    # 10x — fine frase su oro
    "è che oro lucido ma sobrio": [
        "è che l'oro lucido rimane comunque sobrio",
        "è che il dorato lucido mantiene sobrietà",
        "è che l'oro brillante non perde eleganza",
        "è che il tono oro lucido sa essere discreto",
        "è che l'oro brillante eppure contenuto",
        "è che il dorato non trabocca",
        "è che un oro così lucido sa restare elegante",
        "è che l'oro rimane misurato nonostante la lucentezza",
        "è che si tratta di un oro lucido ma mai esagerato",
        "è che la finitura oro mantiene una sua discrezione",
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
print("Round 12 completato!" if errors == 0 else f"ATTENZIONE: {errors} errori.")
