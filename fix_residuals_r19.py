# -*- coding: utf-8 -*-
import psycopg2, sys
from collections import defaultdict

sys.stdout.reconfigure(encoding='utf-8')

DATABASE_URL = "postgresql://neondb_owner:npg_uFxVSRoTj95w@ep-damp-sea-anvn4fw4.c-6.us-east-1.aws.neon.tech/neondb?sslmode=require"

PATTERNS = {
    # 12x
    "e hanno una presenza davvero forte": [
        "e trasmettono una forza visiva notevole",
        "e la loro presenza visiva è potente",
        "e il loro impatto sul look è indubbio",
        "e comunicano un'identità fortissima",
        "e hanno un'intensità visiva che non si ignora",
        "e si sentono nello spazio senza bisogno di spiegazioni",
        "e sfoderano un carattere visivo molto netto",
        "e quando sono sul viso, lo sanno",
        "e la loro presenza non chiede permesso",
        "e affermano un'identità decisa senza mezze misure",
        "e non lasciano il viso in secondo piano",
        "e il loro peso visivo è inequivocabile",
        "e rimangono la prima cosa che si nota",
    ],
    # 10x
    "non passano inosservati in nessun modo": [
        "non si mimetizzano in nessun contesto",
        "restano sempre visibili a prescindere dall'outfit",
        "l'impatto è inevitabile in qualunque situazione",
        "catturano gli sguardi invariabilmente",
        "la loro visibilità è costante e indelebile",
        "la presenza è inconfondibile in qualsiasi contesto",
        "si vedono sempre e ovunque",
        "la capacità di farsi notare è intatta in ogni scenario",
        "rifiutano di passare inosservati in qualunque scenario",
        "la loro firma visiva è sempre presente",
        "non ammettono il silenzio visivo in nessun contesto",
    ],
    # 10x
    "e la costruzione da occhiale tecnico": [
        "e il carattere tecnico della struttura",
        "e la struttura da eyewear performante",
        "e l'impronta da prodotto sportivo",
        "e il design da occhiale da performance",
        "e l'architettura da glasses tecnico",
        "e il frame da eyewear sportivo",
        "e la struttura da occhiale performante",
        "e il telaio da prodotto tecnico",
        "e la costruzione tipica da eyewear sport",
        "e l'ossatura da occhiale atletico",
        "e il design da shield performante",
    ],
    # 8x multi-window
    "non sembrano un travestimento se il resto del look regge": [
        "non risultano un costume se il contesto abbigliamento funziona",
        "non sembrano accessori da carnevale se il look intorno ha senso",
        "non si traducono in una maschera se l'outfit complessivo regge",
        "non diventano un accessorio da palco se il guardaroba li supporta",
        "non appaiono fuori da un set se l'abbigliamento ha logica",
        "non sembrano fuori contesto se l'outfit quotidiano li sostiene",
        "non diventano esagerati se l'abbigliamento circostante è solido",
        "non assumono un aspetto da cosplay se il look complessivo è coerente",
        "non risultano eccessivi se il contesto visivo li inquadra bene",
        "non sembrano da costume se il guardaroba è compatibile con loro",
    ],
    # 8x multi-window
    "la lente unica fa tutto il lavoro che deve fare": [
        "la visiera unica assolve perfettamente la sua funzione",
        "la lente panoramica si dimostra all'altezza del compito",
        "la visiera monopezzo funziona esattamente come dovrebbe",
        "la lente senza interruzioni garantisce le prestazioni attese",
        "la visiera integrale assolve il suo ruolo in modo convincente",
        "la lente panoramica fa la sua parte senza tradire",
        "la visiera unica si comporta come ci si aspettava",
        "la lente a visiera unica è all'altezza di ogni aspettativa",
        "la lente singola esprime tutta la sua funzione con precisione",
        "la visiera singola esegue quanto le si chiede con affidabilità",
    ],
    # 8x
    "non mi dimentico mai di averlo addosso": [
        "la sensazione fisica è costantemente presente",
        "il suo peso sul profilo è sempre avvertito",
        "la sua presenza fisica non scompare mai del tutto",
        "rimane sempre percepito come elemento aggiunto",
        "la sensazione di portarlo non si azzera con l'abitudine",
        "il fattore fisico non scompare con il tempo",
        "la sensazione di indossarlo non si normalizza",
        "la sua presenza sul viso è sempre avvertita",
        "mi è sempre presente come qualcosa di indossato",
        "non si azzera mai la consapevolezza di averlo sul viso",
    ],
    # 8x
    "fuori dal contesto sportivo lo percepisco eccessivo": [
        "lontano dall'ambito atletico lo trovo esagerato",
        "in contesti non sportivi risulta fuori luogo",
        "senza un supporto atletico lo sento eccessivo",
        "in situazioni quotidiane lo trovo decisamente fuori misura",
        "al di fuori dello sport diventa difficile da portare",
        "distaccato dall'ambito sportivo mi sembra eccessivo",
        "in un contesto casual lo percepisco sproporzionato",
        "senza un aggancio atletico lo sento inadeguato al contesto",
        "in un look civile risulta ingombrante",
        "lontano dalla performance sportiva perde il suo senso",
    ],
    # 8x 2-window
    "e su di me si sente": [
        "e sulla mia fisionomia si avverte",
        "e sul mio viso lo percepisco sempre",
        "e nel mio caso lo sento chiaramente",
        "e per la mia conformazione non passa inosservato",
        "e sulla mia struttura nasale è un limite",
        "e per me è una presenza fastidiosa",
        "e a livello fisico lo avverto sempre",
        "e sulla mia conformazione è un problema reale",
        "e nel mio caso specifico è un fattore limitante",
        "e con la mia fisionomia continua a farsi sentire",
    ],
    # 8x 2-window
    "il ponte alto resta una questione seria": [
        "il ponte rialzato rimane un elemento critico",
        "il ponte alto continua a essere un fattore problematico",
        "il ponte rialzato resta una variabile non trascurabile",
        "il pontale elevato rimane un punto critico irrisolto",
        "il ponte alto non smette di essere un ostacolo",
        "il ponte rialzato è ancora un problema concreto",
        "il pont elevato rimane un fattore limitante",
        "il ponte alto non risolve la compatibilità",
        "il ponte rialzato resta una criticità reale",
        "l'altezza del ponte porta un vincolo persistente",
    ],
    # 8x
    "con schermo iridescente crea un insieme davvero": [
        "con la visiera iridescente genera un effetto davvero",
        "con lo schermo cangiante dà vita a qualcosa di davvero",
        "con la lente iridescente produce un'estetica davvero",
        "con lo schermo prismatico forma un insieme davvero",
        "con la visiera dai riflessi prismatici costruisce qualcosa di davvero",
        "con la lente effetto iridescente compone un risultato davvero",
        "con il filtro cangiante restituisce un effetto davvero",
        "con la visiera dai riflessi arcobaleno crea qualcosa di davvero",
        "con lo schermo dall'iridescenza raffinata concorre a qualcosa di davvero",
        "con la lente dall'iridescenza marcata genera un insieme davvero",
    ],
    # 8x
    "è che telaio leggero e pulito": [
        "è che questa struttura leggera e ordinata",
        "è che il telaio sottile e minimalista",
        "è che questo frame leggero e lineare",
        "è che la struttura snella e pulita",
        "è che il telaio essenziale e leggero",
        "è che questo telaio minimalista e silenzioso",
        "è che questa costruzione leggera e senza eccessi",
        "è che il frame aereo e pulito",
        "è che la struttura minimale e leggera",
        "è che questo telaio sottile e ordinato",
    ],
    # 8x
    "che profilo rimless molto arioso con": [
        "che profilo rimless molto libero con",
        "che struttura rimless dal respiro ampio con",
        "che disegno rimless dall'aspetto aperto con",
        "che montatura rimless dall'ariosità evidente con",
        "che profilo rimless delicatissimo con",
        "che frame rimless dall'apertura visiva notevole con",
        "che profilo rimless dal taglio aperto con",
        "che architettura rimless dall'aspetto leggero con",
        "che costruzione rimless quasi invisibile con",
        "che profilo rimless dalla leggerezza massima con",
    ],
    # 7x
    "temevo che accessorio protagonista fosse troppo evidente": [
        "avevo il timore che l'accessorio da primo piano fosse esagerato",
        "mi preoccupava che la presenza da hero-piece fosse eccessiva",
        "sospettavo che questo design così protagonista fosse fuori misura",
        "avevo paura che un accessorio così visibile fosse troppo invasivo",
        "mi preoccupava che l'impatto da centrostage fosse ingombrante",
        "sospettavo che un ruolo così dominante finisse per pesare",
        "dubitavo che l'evidenza dell'accessorio potesse integrarsi bene",
        "temevo che la sua forza come hero-piece risultasse opprimente",
        "mi preoccupava che un elemento così presente fosse difficile da gestire",
        "avevo il dubbio che un accessorio così in vista fosse eccessivo",
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
print("Round 19 OK" if errors == 0 else "Round 19 ERRORI")
