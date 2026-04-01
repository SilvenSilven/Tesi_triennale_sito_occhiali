# -*- coding: utf-8 -*-
import psycopg2, sys
from collections import defaultdict

sys.stdout.reconfigure(encoding='utf-8')

DATABASE_URL = "postgresql://neondb_owner:npg_uFxVSRoTj95w@ep-damp-sea-anvn4fw4.c-6.us-east-1.aws.neon.tech/neondb?sslmode=require"

PATTERNS = {
    # 14x - altissima priorità
    "sembrano studiati e non casuali": [
        "hanno una coerenza visiva che non sembra frutto del caso",
        "mostrano un progetto preciso, non un'accozzaglia di idee",
        "comunicano un'intenzione progettuale chiara e non casuale",
        "rivelano una firma estetica ponderata",
        "sono il frutto di scelte meitate, non della fortuna",
        "parlano di un approccio progettuale intenzionale",
        "lasciano trasparire una logica estetica solida",
        "tradiscono un'intelligenza formale che non è improvvisata",
        "hanno una qualità compositiva che non viene lasciata al caso",
        "mostrano il segno di decisioni precise, non di scelte casuali",
        "portano il segno di un pensiero progettuale chiaro",
        "evidenziano un metodo formale che si vede",
        "denunciano un lavoro estetico intenzionale e preciso",
        "rispecchiano una direzione di gusto che non è improvvisata",
        "mostrano un asse progettuale coerente e riconoscibile",
    ],
    # 11x
    "hanno un punto di vista chiarissimo": [
        "esprimono un'identità visiva ben definita",
        "parlano con una voce estetica precisa",
        "dichiarano esattamente cosa vogliono essere",
        "hanno un'intenzione progettuale inconfondibile",
        "sanno esattamente cosa sono e lo mostrano",
        "non lasciano dubbi sull'identità che vogliono costruire",
        "esprimono un carattere molto definito e riconoscibile",
        "hanno una direzione estetica che non si presta a confusioni",
        "mostrano una posizione stilistica inequivocabile",
        "comunicano un'identità formale che non accetta compromessi",
        "hanno qualcosa da dire e lo dicono senza esitazione",
        "portano avanti un progetto estetico coerente e preciso",
    ],
    # 9x
    "su visi molto allungati vanno testati": [
        "su fisionomie molto allungate è consigliabile provarli con attenzione",
        "su profili molto stretti e allungati la prova fisica è necessaria",
        "su conformazioni facciali allungate andrebbero valutati di persona",
        "su visi dall'ovale molto stretto andrebbero verificati in negozio",
        "su lineamenti molto verticali è preferibile verificare di persona",
        "su visi dallo sviluppo molto verticale la prova è essenziale",
        "su conformazioni molto allungate andrebbero provati con calma",
        "su fisionomie strette e lunghe il test diretto è raccomandato",
        "su lineamenti molto allungati conviene provare prima dell'acquisto",
        "su visi con sviluppo molto verticale la prova è fondamentale",
    ],
    # 9x
    "e il lato intellettuale del modello": [
        "e il carattere riflessivo del progetto",
        "e la dimensione culturale di questo design",
        "e l'anima pensante di questo modello",
        "e lo spessore progettuale di questa montatura",
        "e la qualità intellettuale di questa forma ottagonale",
        "e la componente concettuale del design",
        "e il profilo colto di questa montatura",
        "e la vena riflessiva del progetto formale",
        "e il registro culturale di questo progetto",
        "e la connotazione intellettuale del modello",
    ],
    # 8x
    "con lenti marroni sfumate crea un insieme davvero": [
        "con filtro marrone sfumato forma un abbinamento davvero",
        "con lenti dal brunito sfumato genera un'estetica davvero",
        "con lenti ambrate sfumate produce qualcosa di davvero",
        "con la gradazione marrone sulle lenti costruisce qualcosa di davvero",
        "con il filtro brunito sulle lenti dà vita a qualcosa di davvero",
        "con le lenti dai toni caldi sfumati offre un risultato davvero",
        "con sfumatura marrone sulle lenti compone un effetto davvero",
        "con il degradé marrone sulle lenti contribuisce a qualcosa di davvero",
        "con le lenti dal caldo brunito sfumato genera un insieme davvero",
        "con lenti dal tono caldo brunito realizza qualcosa di davvero",
    ],
    # 8x
    "mi ha chiarito subito che non era il paio giusto": [
        "mi ha detto di no in modo molto diretto",
        "mi ha rivelato fin da subito che non era quello che cercavo",
        "mi ha confermato presto che non faceva per me",
        "mi ha mostrato immediatamente che non era la scelta giusta",
        "mi ha convinto sin dall'inizio che la scelta era sbagliata",
        "mi ha fatto capire subito che non era la mia montatura",
        "mi ha comunicato fin dalla prima prova che non era il modello adatto",
        "mi ha informato subito che non era il paio adatto a me",
        "mi ha dato un riscontro immediato e inequivocabile",
        "mi ha fatto capire in fretta che non corrispondeva a ciò che cercavo",
    ],
    # 8x
    "verde salvia non ama tutti gli outfit": [
        "il verde salvia ha abbinamenti limitati rispetto ad altri colori",
        "la tonalità salvia non va con tutto ciò che si ha nell'armadio",
        "il verde salvia esclude una buona parte degli outfit",
        "il verde salvia richiede un guardaroba adatto",
        "la tonalità salvia è più esigente di quanto sembri con gli abbinamenti",
        "il verde salvia non si accosta a qualsiasi look",
        "il verde salvia restringe lo spazio degli abbinamenti possibili",
        "la tonalità salvia è selettiva con il guardaroba",
        "il verde salvia chiede outfit mirati per esprimere il meglio",
        "la gamma salvia non è democratica con gli abbinamenti",
    ],
    # 8x
    "nel modo giusto, grazie anche a": [
        "senza eccedere, merito anche di",
        "con equilibrio, sostenuto anche da",
        "con misura, in parte grazie a",
        "con stile, anche per merito di",
        "senza perdere credibilità, grazie anche a",
        "con la giusta misura, anche per via di",
        "in modo centellinato, anche per merito di",
        "in modo calibrato, sostenuto da",
        "con la giusta leggerezza, anche grazie a",
        "senza eccessi, in parte grazie a",
    ],
    # 8x
    "Col passare dei giorni, temevo che": [
        "Con il passare del tempo, avevo paura che",
        "Nei giorni successivi, mi preoccupava che",
        "Dopo qualche settimana d'uso, sospettavo che",
        "Col tempo, ho avuto l'impressione che",
        "Andando avanti con l'uso, ho dubitato che",
        "Man mano che li portavo, avevo il timore che",
        "Con il prolungarsi dell'uso, mi preoccupava che",
        "Nel lungo periodo, mi era venuto il sospetto che",
        "Nel corso delle settimane, stavo per convincermi che",
        "Continuando a portarli, temevo che",
    ],
    # 8x
    "Su di me funzionano bene nelle": [
        "Sul mio viso rendono bene nelle",
        "Addosso a me si trovano a loro agio nelle",
        "Per il mio tipo si comportano bene nelle",
        "Su di me risultano adatti nelle",
        "Sulla mia fisionomia rendono bene nelle",
        "Come li porto io, si adattano perfettamente nelle",
        "Sul mio profilo la resa è buona nelle",
        "Indossati da me, si difendono bene nelle",
        "Per come li uso, la resa è convincente nelle",
        "Con la mia fisionomia, vanno bene nelle",
    ],
    # 8x
    "Li ho messi la prima volta per": [
        "La prima volta che li ho indossati era per",
        "Li ho portati per la prima volta in occasione di",
        "Il primo utilizzo è stato per",
        "Ho scelto di indossarli per la prima volta durante",
        "Li ho inaugurati in occasione di",
        "La prima uscita con loro è stata per",
        "La prima volta in assoluto li ho portati per",
        "Li ho debuttati per",
        "Li ho inaugurati indossandoli per",
        "La prima uscita con loro: erano destinati a",
    ],
    # 8x cross-sentence
    "insieme hanno personalità": [
        "insieme restituiscono un'identità precisa",
        "insieme trasmettono un carattere ben definito",
        "insieme formano qualcosa di riconoscibile",
        "insieme producono un'estetica coerente",
        "insieme danno vita a qualcosa di definito",
        "insieme offrono una personalità formale precisa",
        "insieme compongono un'identità ben calibrata",
        "insieme esprimono un carattere molto riconoscibile",
        "insieme stabiliscono un progetto visivo coerente",
        "insieme portano un messaggio visivo chiaro",
    ],
    # 8x
    "non vive da sola: il telaio": [
        "non viene percepita da sola: il telaio",
        "non basta da sola: il telaio",
        "non funziona mai come elemento isolato: il telaio",
        "non si sostiene da sola: il telaio",
        "non è mai separabile dal contesto: il telaio",
        "non esprime il meglio da sola: il telaio",
        "non afferma il suo valore da sola: il telaio",
        "non completa il look da sola: il telaio",
        "non si deve leggere in modo isolato: il telaio",
        "non esiste come elemento indipendente: il telaio",
    ],
    # 8x
    "però la realtà per me è che": [
        "ma quello che ho vissuto io è che",
        "nel pratico però per me è che",
        "però ciò che ho riscontrato è che",
        "la verità che ho sperimentato è che",
        "tuttavia la mia esperienza mi dice che",
        "nella mia esperienza invece è che",
        "ma l'esperienza concreta mi ha mostrato che",
        "però la mia valutazione personale è che",
        "nella pratica però la sensazione è che",
        "però il riscontro reale è che",
    ],
    # 8x
    "Li ho usati per un fine settimana": [
        "Li ho portati per un weekend",
        "Li ho scelti per un fine settimana",
        "Li ho indossati per un weekend di",
        "Li ho testati durante un fine settimana",
        "Durante un fine settimana li ho portati",
        "Ho usato loro per un weekend",
        "Li ho messi alla prova per un weekend",
        "Un fine settimana è stato il loro primo vero test",
        "Per un weekend li ho provati sul campo",
        "Tra i primi usi seri, un fine settimana",
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
print("Round 17 OK" if errors == 0 else "Round 17 ERRORI")
