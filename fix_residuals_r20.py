# -*- coding: utf-8 -*-
import psycopg2, sys
from collections import defaultdict

sys.stdout.reconfigure(encoding='utf-8')

DATABASE_URL = "postgresql://neondb_owner:npg_uFxVSRoTj95w@ep-damp-sea-anvn4fw4.c-6.us-east-1.aws.neon.tech/neondb?sslmode=require"

PATTERNS = {
    # 8x
    "fuori da certi contesti sono impegnativi": [
        "al di fuori di situazioni appropriate diventano difficili da portare",
        "al di là di contesti precisi risultano impegnativi",
        "lontano dai contesti giusti risultano esigenti",
        "in situazioni ordinarie non si portano con facilità",
        "fuori dal contesto adeguato si trasformano in una sfida",
        "senza il giusto contesto di supporto diventano complicati",
        "in contesti normali richiedono troppo coraggio",
        "al di fuori del loro elemento diventano pesa",
        "in scenari quotidiani convenzionali risultano sopra le righe",
    ],
    # 7x multi-window
    "la struttura sottile mi fa desiderare un po' più di sostanza": [
        "la struttura esile mi porta a voler qualcosa di più consistente",
        "la finezza costruttiva mi fa aspirare a qualcosa di più robusto",
        "la struttura così sottile mi lascia con il desiderio di più solidità",
        "la leggerezza strutturale mi fa venir voglia di maggiore spessore",
        "la struttura così eterea mi fa rimpiangere un po' più di corpo",
        "il telaio sottile mi convince meno di quanto vorrei in termini di solidità",
        "la finezza dell'ossatura mi porta a desiderare più consistenza",
        "la struttura delicata mi lascia con voglia di più concretezza",
        "questa leggerezza costruttiva mi fa preferire qualcosa di più sostanzioso",
    ],
    # 7x 3-window
    "su un viso piccolo risultano davvero enormi": [
        "su una fisionomia piccola risultano davvero sproporzionati",
        "su un viso di piccole dimensioni finiscono per sovrastare tutto",
        "su una struttura facciale ridotta diventano davvero troppo grandi",
        "su una fisionomia esile risultano decisamente sovradimensionati",
        "su un viso piccolo si rivelano davvero ingombranti",
        "su una conformazione piccola sembrano davvero fuori scala",
        "su un viso esile risultano decisamente troppo grandi",
        "su una conformazione facciale ridotta appaiono eccessivamente grandi",
        "su un viso poco sviluppato sembrano molto più grandi del dovuto",
    ],
    # 7x 3-window
    "ponte non è amico di tutti i visi": [
        "ponte rialzato non è adatto a ogni conformazione",
        "ponte elevato non si adatta a ogni profilo facciale",
        "ponte alto non funziona per tutti i tipi di naso",
        "doppio ponte non è compatibile con ogni struttura nasale",
        "ponte rialzato non è per ogni tipo di viso",
        "ponte elevato non va bene su tutte le conformazioni",
        "ponte alto non è universale",
        "doppio ponte non funziona su ogni fisionomia",
        "ponte rialzato ha limitazioni con certe conformazioni",
    ],
    # 7x
    "con filtro marrone crea un insieme davvero": [
        "con filtro marrone genera un effetto davvero",
        "con il tono marrone produce un abbinamento davvero",
        "con la tinta marrone costruisce qualcosa di davvero",
        "con la sfumatura marrone forma un insieme davvero",
        "con il filtro brunito crea un'estetica davvero",
        "con il tono brunito produce qualcosa di davvero",
        "con la lente marrone dà vita a qualcosa di davvero",
        "con il filtro marrone genera qualcosa di davvero",
        "con la colorazione marrone crea un risultato davvero",
    ],
    # 7x
    "e la scala importante del modello": [
        "e le dimensioni rilevanti del modello",
        "e le proporzioni significative del modello",
        "e le misure consistenti del modello",
        "e il formato importante del modello",
        "e la dimensione rilevante del modello",
        "e le proporzioni marcate del modello",
        "e la taglia considerevole del modello",
        "e la grandezza del modello",
        "e le proporzioni decise del modello",
    ],
    # 7x
    "Ha carisma appena lo tiri fuori dalla custodia": [
        "Ha personalità già nel momento in cui lo estrai dall'astuccio",
        "Si fa notare già prima di indossarlo, fuori dalla custodia",
        "Ha qualcosa di magnetico già quando lo togli dall'astuccio",
        "Colpisce appena lo estrai dall'astuccio",
        "Ha un impatto immediato già fuori dalla custodia",
        "Emana carisma ancora prima di stare sul viso",
        "Cattura l'attenzione già nel momento in cui lo prendi in mano",
        "Fa capire subito cosa è appena lo estrai",
        "Ha una forza propria già quando ancora non è sul viso",
        "Si annuncia dal momento in cui lascia la custodia",
    ],
    # 7x
    "si portano più facilmente del previsto": [
        "risultano più facili da indossare del previsto",
        "si portano con meno sforzo del previsto",
        "si indossano più naturalmente di quanto ci si aspetterebbe",
        "si portano senza la difficoltà che si temeva",
        "si rivelano più gestibili del previsto",
        "risultano più abbinabili di quanto si possa pensare",
        "si indossano con più agilità del previsto",
        "risultano molto più pratici da portare di quanto sembrino",
        "si portano meglio di quanto il look suggerisca",
    ],
    # 7x
    "Sembra personale già al primo sguardo,": [
        "Trasmette subito un senso di unicità,",
        "Comunica immediatamente una voce propria,",
        "Ha già dalla prima occhiata qualcosa di suo,",
        "Si distingue già al primo contatto visivo,",
        "Parla di un linguaggio proprio fin dal primo sguardo,",
        "Ha un carattere riconoscibile fin da subito,",
        "Si presenta come qualcosa di individuale già alla prima occhiata,",
        "È riconoscibile come accessorio dalla personalità precisa,",
        "Porta con sé un'identità visiva già al primo sguardo,",
    ],
    # 7x
    "Sembra pensato per essere visto da": [
        "Sembra progettato per catturare gli sguardi, non per passare da",
        "Sembra creato per non passare inosservato da",
        "Sembra concepito per farsi notare da",
        "Nasce per essere visto da",
        "Sembra progettato per emergere da",
        "Sembra disegnato apposta per essere notato da",
        "Sembra costruito per essere riconosciuto da",
        "Appare pensato per attirare l'attenzione da",
        "Sembra realizzato con l'intenzione precisa di farsi vedere da",
    ],
    # 7x
    "Riesce a sembrare elegante senza darsi": [
        "Riesce a comunicare eleganza senza ostentare",
        "Appare raffinato senza sembrare di provarci troppo",
        "Sa essere elegante senza apparire impegnato",
        "Trasmette raffinatezza senza darsi troppa importanza",
        "Risulta elegante senza sforzo apparente",
        "È in grado di apparire elegante senza effort visibile",
        "Riesce a stare nel registro elegante senza costruirsi",
        "Sa sembrare curato senza gridarlo",
        "Porta l'eleganza con una leggerezza che pare naturale",
    ],
    # 7x
    "Rende persino un look semplice più": [
        "Eleva anche un abbigliamento basilare rendendolo più",
        "Sa trasformare anche un look ordinario in qualcosa di più",
        "Arricchisce perfino un outfit semplice diventando più",
        "Trasforma persino il più basico degli outfit in qualcosa di più",
        "Dal look più neutro, riesce a estrarre qualcosa di più",
        "Basta un outfit minimale per rendere tutto più",
        "Alza di tono anche l'abbigliamento più comune diventando più",
        "Porta valore aggiunto anche al look più semplice, rendendolo più",
        "Anche con l'abbigliamento più neutro, restituisce qualcosa di più",
    ],
    # 7x
    "l'ampiezza va accettata fino in fondo": [
        "le dimensioni richiedono una piena accettazione",
        "l'ingombro va accettato per intero",
        "la grandezza va presa per quello che è",
        "l'ampiezza è parte del progetto e va abbracciata",
        "le misure importanti fanno parte del patto con questo modello",
        "l'ingombro non è negoziabile: lo si accetta tutto",
        "la scala dell'occhiale va accettata senza riserve",
        "le dimensioni significative sono parte del carattere e vanno accettate",
        "la taglia importante è inscindibile dal progetto",
    ],
    # 7x cross-sentence "resto diviso"
    "resto diviso. Gli riconosco": [
        "rimango in bilico nel giudizio. Riconosco",
        "resto incerto. Gli riconosco comunque",
        "rimango ambivalente. Al modello riconosco",
        "resto combattuto. Gli do atto",
        "rimango sospeso nel giudizio. Riconosco comunque",
        "resto a metà strada. Gli concedo",
        "rimango diviso tra pro e contro. Gli riconosco",
        "non riesco a schierarmi del tutto. Gli riconosco",
        "resto con un'impressione mista. Riconosco",
    ],
    # 7x windows
    "in modo molto naturale, ma non in modo lineare": [
        "in modo molto naturale, ma non in maniera così diretta",
        "in modo abbastanza naturale, anche se non in modo immediatamente lineare",
        "in un modo che viene da sé, ma non è strettamente lineare",
        "in modo molto spontaneo, anche se non in modo rettilineo",
        "in un modo naturale, ma non necessariamente diretto",
        "in modo quasi automatico, ma non in modo privo di curve",
        "abbastanza naturalmente, ma non secondo un percorso lineare",
        "con naturalezza, pur non seguendo una traiettoria lineare",
        "in modo fluido e spontaneo, ma non in modo rigoroso",
    ],
    # 7x
    "delle lenti e il modo in cui": [
        "delle lenti e il contributo che esse danno",
        "del filtro e il modo in cui si integra",
        "delle lenti e la loro interazione con",
        "delle lenti e il ruolo che assumono nel",
        "della lente e il modo in cui lavora",
        "del filtro e la sua funzione nel",
        "delle lenti e come si relazionano con",
        "della colorazione delle lenti e il modo in cui influisce",
        "delle lenti e il contributo al risultato visivo",
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
print("Round 20 OK" if errors == 0 else "Round 20 ERRORI")
