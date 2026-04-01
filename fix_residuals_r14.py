# -*- coding: utf-8 -*-
import psycopg2, sys
from collections import defaultdict

sys.stdout.reconfigure(encoding='utf-8')

DATABASE_URL = "postgresql://neondb_owner:npg_uFxVSRoTj95w@ep-damp-sea-anvn4fw4.c-6.us-east-1.aws.neon.tech/neondb?sslmode=require"

PATTERNS = {
    "non è il modello per chi cerca discrezione": [
        "non fa per chi vuole restare discreto",
        "non si presta a chi vuole passare inosservato",
        "non è pensato per chi preferisce un profilo basso",
        "non appartiene al repertorio degli accessori neutri",
        "non è la scelta di chi cerca sobrietà visiva",
        "non si adatta a chi evita di attirare l'attenzione",
        "non è adatto a chi punta all'understatement",
        "non è l'occhiale per chi vuole restare in secondo piano",
        "chi preferisce non essere notato troverà di meglio",
        "non si presta a un look riservato",
        "non si confà a chi cerca invisibilità stilistica",
        "non è per chi punta a un registro sobrio",
    ],
    "dal vivo il blu è più acceso di quanto immaginassi": [
        "di persona il blu risulta più vivace di quanto sembri in foto",
        "indossati, il blu si rivela molto più saturo del previsto",
        "a vederli dal vivo, il blu è più brillante di quanto lasciasse capire",
        "quando li ho indossati il blu era decisamente più deciso di quanto atteso",
        "dal vivo il blu ha una vivacità superiore alle aspettative",
        "togliendoli dalla custodia, il blu era più carico di quanto prevedessi",
        "in mano il blu è notevolmente più intenso di quanto si percepisca in foto",
        "guardandoli in luce diretta, il blu si rivela più vivo del previsto",
        "di persona il colore risulta più acceso di qualsiasi immagine",
        "una volta indossati, il blu era molto più saturo di quanto immaginavo",
        "la tinta blu dal vivo è più intensa di quanto suggerisca qualsiasi foto",
    ],
    "costruiscono qualcosa di molto riuscito": [
        "formano un insieme davvero ben riuscito",
        "creano un abbinamento efficace e curato",
        "danno vita a un risultato visivamente solido",
        "producono un effetto complessivo convincente",
        "compongono un quadro esteticamente ben costruito",
        "generano un equilibrio visivo di qualità",
        "mettono insieme qualcosa di piacevolmente armonico",
        "realizzano un progetto estetico molto riuscito",
        "restituiscono un'immagine complessiva di buon livello",
        "concorrono a un'identità visiva riconoscibile",
        "si combinano in un risultato degno di nota",
        "costruiscono un insieme coerente e ben calibrato",
    ],
    "non c'è modo di farli passare per neutri": [
        "è impossibile farli sembrare accessori sobri",
        "nessuno li scambierebbe per occhiali discreti",
        "non esiste contesto in cui diventino invisibili",
        "è fuori luogo sperare che passino inosservati",
        "non si prestano a nessuna lettura discreta",
        "è impossibile integrarli in un look neutro senza che si notino",
        "chi li indossa non passerà mai inosservato",
        "non diventano mai accessori da sfondo",
        "non c'è outfit in grado di renderli discreti",
        "sparire in secondo piano è semplicemente impossibile con loro",
    ],
    "la leggerezza del metallo mi fa temere di doverlo trattare con troppa cautela": [
        "la struttura in metallo così sottile mi impone un'attenzione quasi eccessiva",
        "la fragilità percepita del telaio mi tiene sempre un po' in allerta",
        "una montatura così delicata chiede una cura che non sempre posso garantire",
        "tanta finezza costruttiva si porta dietro il timore di essere troppo brusco",
        "il telaio così esile mi fa maneggiare il tutto con più rispetto del solito",
        "quella leggerezza estrema mi fa sentire come se portassi qualcosa di fragile",
        "la sottigliezza del telaio richiede attenzioni che non sempre ho",
        "uno spessore così ridotto mi porta a trattarli con eccessiva delicatezza",
        "la struttura così fine mi mette in ansia ogni volta che li appoggio da qualche parte",
    ],
    "con una giacca destrutturata e sneakers pulite": [
        "con un blazer morbido e scarpe sportive pulite",
        "abbinato a un cappotto leggero e calzature minimal",
        "con una giacca leggera e scarpe da ginnastica essenziali",
        "portato con un capo spalla casual e sneakers sobrie",
        "con qualcosa di strutturato ma non rigido e calzature clean",
        "con un soprabito informale e scarpe semplici",
        "con una giacca fluida e scarpe minimaliste",
        "abbinato a qualcosa di casual e discretamente sportivo",
        "con un look easy fatto di giacca sciolta e sneakers",
    ],
    "richiedono un gusto un minimo definito": [
        "non si indossano senza avere un'idea chiara di sé",
        "pretendono una sensibilità estetica già formata",
        "necessitano di un senso dello stile già sviluppato",
        "chiedono all'utente una certa consapevolezza visiva",
        "esigono un approccio al look già maturo",
        "richiedono di sapere bene cosa si vuole comunicare",
        "non perdonano un abbigliamento circostante privo di direzione",
        "non si indossano a caso: il contesto deve essere pensato",
        "vanno di pari passo con un'identità stilistica chiara",
        "non sono per chi sta ancora cercando il proprio linguaggio visivo",
    ],
    "funzionano bene su chi ama il design": [
        "sono perfetti per chi ha una sensibilità per il progetto formale",
        "si adattano bene a chi apprezza l'estetica contemporanea",
        "piacciono a chi ha un occhio per i dettagli costruttivi",
        "trovano il pubblico ideale in chi presta attenzione alle forme",
        "risuonano con chi ha una predilezione per il design d'autore",
        "incontrerebbero il favore di chi conosce il progetto di moda",
        "chi frequenta il mondo del design li apprezzerà subito",
        "hanno il loro senso pieno per chi ha un background visivo",
        "parlano direttamente a chi ha gusto per le forme studiate",
        "si rivolgono a un pubblico con sensibilità estetica sviluppata",
    ],
    "è che montatura oversize ambra traslucida": [
        "è che questo frontale oversize dall'ambra translucida",
        "è che la struttura ampia in acetato color ambra",
        "è che il telaio oversize nell'acetato ambrato semitrasparente",
        "è che questa montatura larga color miele traslucido",
        "è che la forma oversize in ambra chiaro",
        "è che il design oversize dalla tinta ambrata",
        "è che questa struttura grande in tonalità miele",
        "è che il frontale largo nell'ambra traslucente",
        "è che la montatura ampia nell'acetato color ambra",
        "è che questo telaio oversize dalla sfumatura ambrata",
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
print("Round 14 OK" if errors == 0 else "Round 14 ERRORI")
