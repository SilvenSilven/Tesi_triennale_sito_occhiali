# -*- coding: utf-8 -*-
import psycopg2, sys
from collections import defaultdict

sys.stdout.reconfigure(encoding='utf-8')

DATABASE_URL = "postgresql://neondb_owner:npg_uFxVSRoTj95w@ep-damp-sea-anvn4fw4.c-6.us-east-1.aws.neon.tech/neondb?sslmode=require"

PATTERNS = {
    "la montatura così fine mi trasmette una delicatezza che non adoro": [
        "la struttura così sottile comunica una fragilità che stona con il mio uso",
        "il telaio così esile mi passa un senso di precarietà che non coincide con le mie abitudini",
        "una struttura così fine suggerisce inevitabilmente fragilità, cosa che preferirei evitare",
        "il profilo così sottile evoca una leggerezza che sconfina nel fragile",
        "una montatura così eterea mi fa venir voglia di tenerli sempre in custodia",
        "la finezza del telaio mi trasmette un senso di vulnerabilità che non si addice al mio carattere",
        "una struttura così delicata mi impone un'attenzione che non dovrei dover avere",
        "la leggerezza estrema della struttura mi comunica una fragilità che avrei preferito non sentire",
        "il telaio sottilissimo mi porta a trattarli come oggetti preziosi più che come occhiali quotidiani",
        "quella finura costruttiva mi trasmette un senso di precarietà che non mi appartiene",
    ],
    "assomigliano a un archetipo che esiste già da tempo": [
        "ricordano un modello di riferimento già molto consolidato nel settore",
        "rimandano a un design che esiste nel panorama ottico da decenni",
        "richiamano un prototipo che ha già fatto la sua storia",
        "si inseriscono in una tradizione formale tutt'altro che nuova",
        "rispecchiano un linguaggio ottico già ampiamente esplorato",
        "parlano di un vocabolario visivo già visto molte volte",
        "si rifanno a un template estetico già consolidato in catalogo",
        "evocano una silhouette già presente in molti archivi ottici",
        "riprendono una forma che ha già i suoi classici ben affermati",
        "richiamano una silhouette che appartiene ormai alla storia dell'occhiale",
    ],
    "le lenti marroni sfumate": [
        "le lenti color miele sfumate",
        "le lenti ambrate con sfumatura calda",
        "le lenti marroni con degradé graduale",
        "le lenti dal marrone caldo sfumato",
        "le lenti con il filtro marrone sfumato",
        "le lenti in marrone caldo degradé",
        "le lenti dal tono brunito sfumato",
        "le lenti ambrate a sfumatura discendente",
        "le lenti con gradazione marrone calda",
        "le lenti con il filtro brunito a sfumatura",
    ],
    "che ho capito il resto:": [
        "che ho compreso il valore reale di questo paio:",
        "che ho realizzato cosa li rendesse speciali:",
        "che ho afferrato il senso complessivo del progetto:",
        "che ho capito il perché del prezzo:",
        "che ho compreso il livello del prodotto:",
        "che mi sono fatto un'idea precisa:",
        "che ho valutato per bene cosa stessi portando:",
        "che ho colto la vera identità di questo modello:",
        "che ho capito perché meritasse attenzione:",
        "che ho compreso appieno ciò che avevo tra le mani:",
        "che ho visto davvero di che si trattasse:",
        "che ho capito cosa distinguesse questo paio dagli altri:",
    ],
    "funzionano meglio dal vivo che in foto": [
        "dal vivo rendono assai meglio che nelle immagini online",
        "in uso superano nettamente le aspettative create dalle foto",
        "visti di persona sorprendono rispetto a come appaiono fotografati",
        "indossati rendono più di qualsiasi scatto",
        "dal vero convincono più di quanto facciano nelle immagini",
        "nella realtà superano le foto in modo evidente",
        "portandoli si capisce che funzionano oltre le aspettative fotografiche",
        "la realtà d'uso supera le foto in modo inaspettato",
        "il vivo smentisce positivamente le immagini sul sito",
        "la resa in uso si rivela superiore a qualsiasi immagine",
    ],
    "il doppio ponte sul mio naso non è perfetto": [
        "il doppio ponte non si assesta perfettamente sulla mia conformazione",
        "il profilo a doppio ponte crea qualche difficoltà sulla mia struttura nasale",
        "il doppio ponte non si adatta del tutto alla forma del mio naso",
        "la presenza del doppio ponte sulla mia fisionomia non è ottimale",
        "il doppio ponte sul mio naso crea una piccola asimmetria che noto sempre",
        "la struttura a doppio ponte sulla mia conformazione risulta imperfetta",
        "il ponte doppio non si sposa alla perfezione con il mio naso",
        "sul mio naso il doppio ponte lascia qualcosa a desiderare",
        "la sensazione con il doppio ponte sulla mia fisionomia non è ideale",
        "il doppio ponte sul mio profilo non trova mai la posizione perfetta",
    ],
    "Sul viso appare più leggero del previsto": [
        "Indossato risulta più leggero di quanto la struttura lasci intuire",
        "Portato, si fa meno pesante di quanto ci si aspetterebbe",
        "Sul naso si avverte una leggerezza inaspettata rispetto all'aspetto",
        "Una volta addosso, la pesantezza temuta non si manifesta",
        "Indossato pesa meno di quanto il design visivo suggerisca",
        "Portato, il peso si percepisce molto meno del previsto",
        "Sul viso si alleggerisce notevolmente rispetto all'aspetto statico",
        "In uso risulta assai più bilanciato di quanto sembri da solo",
        "Addosso appare più aereo di quanto la struttura visiva lasci pensare",
        "Calzato, sorprende per la leggerezza rispetto all'impatto strutturale",
    ],
    "Non tradisce mai la promessa del classico,": [
        "Mantiene sempre il patto con il gusto classico,",
        "Resta coerente con la propria natura tradizionale,",
        "Conferma in ogni contesto la sua vocazione al classico,",
        "Non delude mai il senso di eleganza che promette,",
        "Continua a essere affidabile come solo i classici sanno fare,",
        "Non manca all'appuntamento con l'eleganza,",
        "Mantiene fede alla sua essenza classica,",
        "Non tradisce il senso della buona tradizione estetica,",
        "Porta a termine la sua promessa di sobrietà,",
        "Resta fedele al carattere formale che lo definisce,",
    ],
    "la lente chiara in basso e più intensa sopra": [
        "la lente con la parte bassa quasi cristallina e quella alta più carica di colore",
        "la lente che degrada dal chiaro in basso verso il tono pieno in alto",
        "la lente sfumata dal basso leggero all'alto più saturo",
        "la lente con gradazione ascendente dal quasi trasparente verso l'intenso",
        "la lente con il degradé che va dal chiaro verso l'alto più scuro",
        "la lente con il filtro che si intensifica progressivamente verso la cima",
        "la lente bicolore con il basso quasi incolore e l'alto dalla tinta piena",
        "la lente dal basso delicato e l'alto dalla tinta più presente",
        "la lente con il contrasto tra la parte alta più carica e quella bassa più aperta",
        "la lente che schiarisce verso il basso e si densifica verso la sommità",
    ],
    "vorrei qualche segnale in più di unicità": [
        "avrei apprezzato un elemento in più che li distinguesse davvero",
        "mi aspettavo qualcosa di meno prevedibile da questo progetto",
        "avrei preferito un dettaglio che li rendesse più originali",
        "qualcosa che li differenziasse di più dalla concorrenza non avrebbe guastato",
        "un tocco in più di personalità avrebbe fatto la differenza",
        "avrei voluto trovare qualcosa di più distintivo tra le mani",
        "manca un elemento che li renda davvero irripetibili",
        "un dettaglio progettuale in più li avrebbe resi più memorabili",
        "mi sarei aspettato una firma visiva più marcata",
        "la loro identità avrebbe potuto essere più definita e riconoscibile",
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
print("Round 15 OK" if errors == 0 else "Round 15 ERRORI")
