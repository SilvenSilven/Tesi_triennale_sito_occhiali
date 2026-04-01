#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fix round 11 — frammenti ad alta frequenza (non catturati da frasi complete)."""

import psycopg2

DATABASE_URL = (
    "postgresql://neondb_owner:npg_uFxVSRoTj95w"
    "@ep-damp-sea-anvn4fw4.c-6.us-east-1.aws.neon.tech"
    "/neondb?sslmode=require"
)

PATTERNS = {

    # ── Frase completa mancante da r10 ────────────────────────────────────────
    # 5x (exact sentence, non terminata con virgola)
    "Ha qualcosa di quasi acquatico.": [
        "Ha qualcosa di quasi subacqueo.",
        "Porta l'aria di qualcosa di marino.",
        "Ha una qualità quasi liquida.",
        "Ha qualcosa che fa pensare all'acqua.",
        "Trasmette una sensazione quasi bagnata.",
        "Ha una nota quasi acquea.",
    ],

    # 3x (variante con continuazione specifica)
    "Ha qualcosa di quasi acquatico, anche se la lente specchiata richiede più attenzione di una lente normale.": [
        "Ha una qualità marina sottile, anche se la lente a specchio chiede più cura rispetto a una lente standard.",
        "Porta qualcosa di quasi liquido, anche se la lente riflettente richiede una manutenzione maggiore.",
        "Ha una nota quasi acquea, anche se le lenti a specchio necessitano di più attenzione di quelle normali.",
        "Ricorda qualcosa di subacqueo, anche se la lente riflettente esige più accortezza di un vetro comune.",
    ],

    # ── Frammenti ad alta frequenza (16x) ────────────────────────────────────

    # 16x — scena urbana
    "tra metro, marciapiedi e tavolini al sole,": [
        "tra fermate del bus, vicoli e dehors al sole,",
        "tra semafori, commissioni e pause all'aperto,",
        "tra marciapiedi affollati, negozi e caffè,",
        "tra tragitti urbani, spostamenti e soste al sole,",
        "tra incroci, strade piene e tavoli all'esterno,",
        "tra la metro, il rumore del centro e il sole in piazza,",
        "tra mezzi pubblici e soste ai bar sotto il sole,",
        "tra corsia preferenziale, marciapiedi e terrazze,",
        "tra tragitti a piedi, frenesia urbana e tavolini fuori,",
        "tra l'agitazione della città e le pause in piazzetta,",
        "tra quartieri, attraversamenti e dehors in pieno sole,",
        "tra uscite quotidiane, spostamenti e caffè all'aperto,",
        "tra ritmi frenetici, strade affollate e pause soleggiate,",
        "tra salite, discese urbane e tavoli en plein air,",
        "tra tragitti e pause sulla terrazza del bar,",
        "tra gli spostamenti del giorno e le soste al sole,",
        "tra giornate piene di movimenti e momenti all'esterno,",
    ],

    # 16x — cross-sentence: fine di "temevo che... fosse troppo evidente."
    # → si interviene sull'inizio della frase successiva
    "Invece hanno una": [
        "In realtà hanno una",
        "Sorprendentemente hanno una",
        "Contro ogni aspettativa, hanno una",
        "Eppure mostrano una",
        "A sorpresa hanno una",
        "Al contrario hanno una",
        "Inaspettatamente rivelano una",
        "Nonostante tutto hanno una",
        "Diversamente da quanto temevo, hanno una",
        "La realtà è che hanno una",
        "A ben guardare hanno una",
        "Scoprire che hanno una",
        "Portandoli si capisce che hanno una",
        "L'esito però è che hanno una",
        "Alla prova dei fatti hanno una",
        "Più li guardi, più noti che hanno una",
        "Si rivela invece che hanno una",
    ],

    # ── Frammenti 12-15x ─────────────────────────────────────────────────────

    # 15x — interno frase
    "in un modo che mi piace": [
        "in modo che trovo riuscito",
        "in una combinazione che mi convince",
        "con un esito che apprezzo",
        "in modo che funziona per me",
        "in modo soddisfacente",
        "con una fusione che ritengo valida",
        "in modo che mi risulta gradevole",
        "in una sintesi che mi convince",
        "con un risultato che trovo buono",
        "in un modo che mi soddisfa",
        "in modo che percepisco come riuscito",
        "con un'armonia che mi convince",
        "in modo tale da convincermi",
        "con un effetto che trovo apprezzabile",
        "in modo che funziona davvero",
        "in una combinazione che mi piace davvero",
    ],

    # 15x — interno frase, struttura descrittiva
    "non vive da sola: la montatura": [
        "non si regge da sola: la montatura",
        "non basta da sola: la montatura",
        "non funziona in isolamento: la montatura",
        "non ha senso senza il contorno: la montatura",
        "non è mai indipendente: la montatura",
        "ha bisogno del resto: la montatura",
        "non si sostiene in solitudine: la montatura",
        "non può fare a meno del resto: la montatura",
        "esiste in relazione al tutto: la montatura",
        "trova senso nell'insieme: la montatura",
        "parla solo in coppia con: la montatura",
        "ha senso solo nel complesso: la montatura",
        "non é mai un fatto solo formale: la montatura",
        "non si legge da sola: la montatura",
        "non parla da sola: la montatura",
        "ha bisogno di supporto: la montatura",
    ],

    # 14x — inizio frase
    "La prima cosa che ho notato": [
        "Il primo elemento che mi ha colpito",
        "La prima osservazione da fare",
        "Il primo dato evidente",
        "Il dettaglio che si vede subito",
        "La prima impressione",
        "Quel che ho percepito per primo",
        "L'aspetto che emerge immediato",
        "Il primo elemento che salta all'occhio",
        "Il fatto che ho notato subito",
        "La prima considerazione",
        "Il particolare che ho colto per primo",
        "L'elemento che emerge al primo sguardo",
        "Il primo elemento osservabile",
        "L'aspetto che si nota immediatamente",
        "La nota che ho registrato per prima",
    ],

    # 13x — inizio frase
    "Appena tolti dalla custodia, temevo che": [
        "Al primo sguardo, temevo che",
        "Subito dopo averli estratti, avevo paura che",
        "Non appena aperti, la mia preoccupazione era che",
        "Al primo esame, sospettavo che",
        "Guardandoli prima di indossarli, temevo che",
        "Appena estratti, mi chiedevo se",
        "Quando li ho visti la prima volta, temevo che",
        "Alla prima occhiata, il timore era che",
        "Prima ancora di provarli, pensavo che",
        "Non appena li ho presi in mano, mi preoccupava che",
        "Al primo contatto, la sensazione era che",
        "Appena fuori dalla scatola, temevo che",
        "Dall'immagine online, pensavo che",
        "Prima di indossarli, avevo il sospetto che",
    ],

    # 13x — frase specifica su lenti verdi
    "il verde delle lenti richiede un minimo di": [
        "il colore verde delle lenti chiede una certa",
        "le lenti dal tono verde esigono un minimo di",
        "la tonalità delle lenti richiede almeno un po' di",
        "il tono verde-lente necessita un minimo di",
        "il filtro cromatico verde richiede una minima",
        "le lenti con questa gradazione chiedono un po' di",
        "la tinta verde delle lenti domanda un minimo di",
        "questo verde sulle lenti esige un certo livello di",
        "il tono verdognolo delle lenti richiede un certo",
        "le lenti colorate così chiedono quantomeno",
        "la tonalità verde necessita di una soglia minima di",
        "il filtro verde sulle lenti esige almeno",
        "il tono deciso delle lenti verdi chiede un minimo di",
        "le lenti dalla gradazione verde richiedono un po' di",
    ],

    # 12x — fine frase: il ponte
    "il ponte alto sul mio viso resta complicato": [
        "la sella alta rimane problematica per il mio profilo",
        "il ponte rialzato non trova pace sul mio naso",
        "la struttura del ponte si conferma un nodo per me",
        "il ponte elevato rimane un punto critico per il mio viso",
        "la sella rialzata continua a non funzionare per me",
        "il ponte alto non si adatta al mio profilo",
        "la sella alta è ancora una questione aperta per me",
        "il ponte rialzato sul mio naso non si risolve",
        "il ponte elevato resta fuori dai miei parametri",
        "la sella alta rimane un ostacolo sul mio viso",
        "il ponte non centrato sul mio naso rimane un problema",
        "la sella di quel tipo rimane difficile da portare",
        "il ponte alto non dialoga con la mia struttura",
    ],

    # 12x — inizio frase
    "Li ho presi quasi d'impulso,": [
        "Non era un acquisto pianificato,",
        "L'acquisto non era programmato,",
        "L'ho deciso in modo spontaneo,",
        "Non avevo meditato la scelta,",
        "È stato un acquisto repentino,",
        "L'ho comprato senza troppa riflessione,",
        "La decisione è stata veloce,",
        "Non lo avevo pianificato,",
        "È stato un acquisto non premeditato,",
        "Ho deciso senza lunghe riflessioni,",
        "È stato un atto d'acquisto immediato,",
        "La scelta è stata istintiva,",
        "Non l'ho ragionato a lungo,",
    ],

    # 12x — interno frase contesto urbano
    "in una giornata piena di spostamenti,": [
        "in una giornata densa di movimenti,",
        "in una giornata di corse e commissioni,",
        "in una giornata di spostamenti intensi,",
        "durante una giornata piena di attività,",
        "in una giornata ricca di giri,",
        "in una giornata ad alto regime,",
        "nel mezzo di una giornata movimentata,",
        "in un pomeriggio pieno di spostamenti,",
        "durante una giornata con molti tragitti,",
        "in un giro intenso tra più luoghi,",
        "nel corso di una giornata piena,",
        "in un giorno di spostamenti continui,",
        "in un contesto quotidiano frenetico,",
    ],

    # 12x — inizio+fine frase
    "Sono di quei paia che ti": [
        "Fanno parte di quella categoria di occhiali che ti",
        "Rientrano tra quei modelli capaci di",
        "Appartengono a quella famiglia di paia che",
        "È uno di quegli occhiali che",
        "Si tratta di quei pezzi rari che",
        "È quel tipo di occhiale che",
        "Sono tra quei modelli che",
        "Fa parte di quei paia che",
        "Rientra tra gli occhiali capaci di",
        "È uno di quei pezzi da indossare che",
        "Appartiene a quella classe di occhiali che",
        "Si tratta di uno di quegli accessori che",
        "È tra i modelli di quelli che",
    ],

    # 12x — interno frase
    "con il caldo si muovono un po'": [
        "nelle giornate calde tendono a scivolare un po'",
        "con il calore si spostano leggermente",
        "con il caldo si allentano leggermente",
        "nelle temperature alte si spostano un poco",
        "con il caldo c'è qualche scivolamento",
        "al caldo girano leggermente",
        "con il sole intenso si muovono un poco",
        "nelle giornate estive scivolare appena",
        "con il caldo estivo perdono qualcosa di stabilità",
        "con il caldo tendono a non stare fermi",
        "in caso di afa tendono a scivolare",
        "con le temperature alte si allentano",
        "nelle giornate calde si spostano mini",
    ],

    # 12x — inizio frase
    "Ha una presenza che sembra da editoriale": [
        "Ha un impatto visivo da set fotografico",
        "Porta l'atmosfera di un accessorio editoriale",
        "Ha una presenza da campagna moda",
        "Ha un'aura da shooting creativo",
        "Porta quell'energia da servizio fotografico",
        "Ha la presenza di un pezzo da editorial",
        "Ha un'atmosfera da produzione fashion",
        "Porta quella cifra da immagine di moda",
        "Ha qualcosa che rimanda a un editorial di stile",
        "Ha l'impatto di un accessorio da lookbook",
        "Porta l'aria di qualcosa visto su una rivista di moda",
        "Ha una forza visiva da redazionale di moda",
        "Porta una presenza da book fotografico",
    ],

    # 11x — fine frase
    "e in quel momento la qualità del progetto viene fuori": [
        "e in quel frangente la solidità costruttiva emerge",
        "e in quell'istante la cura del prodotto si rivela",
        "e in quell'occasione il valore reale si manifesta",
        "e in quel contesto la differenza qualitativa emerge",
        "e proprio lì si capisce la differenza rispetto al comune",
        "e in quel momento la qualità diventa tangibile",
        "e lì si avverte tutta la cura nella costruzione",
        "e in quell'istante il livello si percepisce chiaramente",
        "e lì la qualità smette di essere teorica",
        "e in quel punto la qualità si fa percepire",
        "e in quell'uso il vero livello del prodotto emerge",
        "ed è lì che si rivela il lavoro fatto",
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
        print(f"  '{p[:55]}' → {cnt}x")
print("✅ Round 11 completato!" if errors == 0 else f"⚠️ {errors} errori.")
