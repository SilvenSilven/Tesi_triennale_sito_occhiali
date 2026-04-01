#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fix round 6 — pattern residui 21-23x."""

import psycopg2

DATABASE_URL = (
    "postgresql://neondb_owner:npg_uFxVSRoTj95w"
    "@ep-damp-sea-anvn4fw4.c-6.us-east-1.aws.neon.tech"
    "/neondb?sslmode=require"
)

PATTERNS = {

    # 23x — frase completa
    "Non li considero sbagliati, ma nemmeno inevitabili.": [
        "Non li ritengo un errore, ma neppure una necessità.",
        "Non li vedo come sbagliati, eppure non li sento obbligatori.",
        "Non sono un passo falso, ma neanche un'esigenza vera.",
        "Non un acquisto errato, ma nemmeno un impulso inevitabile.",
        "Non li giudico difettosi, ma non li percepisco come inevitabili.",
        "Non li boccio, ma non li sento necessari.",
        "Non commetto un errore tenerli, ma non li eleggevo nemmeno necessari.",
        "Non sono il modello sbagliato: semplicemente non sono quello necessario.",
        "Non li condanno, ma non li sento indispensabili.",
        "Non è un acquisto di cui pentirsi, ma nemmeno uno obbligato.",
        "Non sono errati per me: solo non imprescindibili.",
        "Non li classifico come errori, ma neanche come certezze.",
        "Non è stato un passo falso acquistarli, solo un passo non necessario.",
        "Non li respingo: non li sento però insostituibili.",
        "Non è un fallimento averli presi: semplicemente non erano obbligatori.",
        "Non li considero un errore: li considero semplicemente non urgenti.",
        "Non è una scelta sbagliata, solo non era una scelta necessaria.",
        "Non vedo dove abbiano sbagliato: vedo solo che non erano inevitabili.",
        "Non portano un errore con sé: portano solo una domanda aperta.",
        "Non è un cattivo acquisto: è semplicemente uno non indispensabile.",
        "Non li boccerei: li metterei però nella categoria 'non urgente'.",
        "Non c'è niente di sbagliato: c'è solo qualcosa che non chiude il cerchio.",
        "Non costituiscono un errore: restano però un acquisto facoltativo.",
        "Non li vedo come un fallimento stilistico, solo come una scelta revocabile.",
    ],

    # 22x — frase completa
    "Ho capito che ammirarlo e abitarlo sono due cose diverse.": [
        "Ho realizzato che apprezzarlo e portarlo sono esperienze separate.",
        "Ho capito che vederlo bello e sentirsi bene non coincidono.",
        "Ho scoperto che la stima estetica e il comfort non vanno per forza insieme.",
        "Ho compreso che l'ammirazione visiva e il vissuto quotidiano sono piani diversi.",
        "Ho distinto tra il trovarlo bello e il trovarlo mio.",
        "Ho capito la differenza tra apprezzare e scegliere.",
        "Ho notato che guardarlo con piacere non basta: serve abitarlo.",
        "Ho scoperto che il giudizio estetico e quello d'uso non si sommano automaticamente.",
        "Ho capito che ammirare un oggetto non equivale a volerlo addosso ogni giorno.",
        "Ho distinto il piacere visivo dal piacere nell'uso.",
        "Ho compreso che esiste una distanza tra ammirare e adottare.",
        "Ho realizzato che essere bella è diverso dall'essere giusta per me.",
        "Ho capito che apprezzare un design e abitarlo sono fasi separate.",
        "Ho scoperto che il mio gradimento estetico non coincide con l'appropriazione.",
        "Ho distinto l'ammirazione dall'adesione vera e propria.",
        "Ho preso atto che guardarlo con piacere non significa indossarlo con piacere.",
        "Ho capito che vedere bene un prodotto non è lo stesso che farselo proprio.",
        "Ho realizzato che tra il piacere visivo e il comfort quotidiano c'è un passo.",
        "Ho distinto il fascino del design dalla compatibilità con chi sono.",
        "Ho capito che essere attratti da qualcosa non significa appartenersi.",
        "Ho compreso che ammirare una forma non implica farla propria.",
        "Ho realizzato la differenza sottile tra 'è bello' e 'è mio'.",
        "Ho distinto il rispetto per il progetto dall'adozione quotidiana.",
    ],

    # 22x — frase completa
    "Hanno un'identità leggibile senza diventare caricatura.": [
        "Hanno un carattere preciso senza scadere nel grottesco.",
        "Comunicano qualcosa di definito senza esagerare.",
        "Hanno una personalità riconoscibile senza sopraffare.",
        "Portano un linguaggio chiaro senza diventare invadenti.",
        "Mostrano una direzione stilistica senza cadere nell'eccesso.",
        "Hanno un tono proprio senza gridarlo.",
        "Esprimono un punto di vista senza diventare caricatura.",
        "Parlano un linguaggio riconoscibile senza imporsi.",
        "Hanno un carattere leggibile senza dominare.",
        "Evocano uno stile preciso senza iperbole.",
        "Comunicano un'identità senza sovrastare il viso.",
        "Hanno una firma stilistica senza eccedere.",
        "Mostrano chi sono senza esplodere in un effetto teatro.",
        "Portano con sé un codice senza sovraccaricarlo.",
        "Hanno una voce riconoscibile senza alzare i toni.",
        "Esprimono una cifra stilistica senza tracimare.",
        "Sono riconoscibili nel loro DNA senza essere ostentati.",
        "Parlano chiaro senza urlare.",
        "Hanno un'estetica definita senza diventare costume.",
        "Portano un'idea precisa senza gonfiare.",
        "Hanno un linguaggio che si capisce subito senza fare scena.",
        "Esprimono senza sfidare: è una qualità rara.",
        "Comunicano un'intenzione senza diventarne prigionieri.",
        "Hanno un'idea ben formata senza cedere all'eccesso.",
    ],

    # 22x — frammento inizio frase
    "Li sto usando più del previsto,": [
        "Li porto più frequentemente di quanto pensassi,",
        "Li uso con una regolarità superiore alle aspettative,",
        "Li indosso con più costanza del previsto,",
        "Li scelgo più spesso di quanto avessi immaginato,",
        "Li ho inseriti nella rotazione con più frequenza del previsto,",
        "Li metto più di quanto inizialmente supposto,",
        "Li prendo di mano con una frequenza che non mi aspettavo,",
        "Li utilizzo con una continuità che non avevo previsto,",
        "Mi ritrovo a sceglierli più del previsto,",
        "Li indosso con una frequenza che supera le mie aspettative iniziali,",
        "Li ho adottati con più regolarità di quanto immaginassi,",
        "Li prendo molto più spesso di quanto pensavo,",
        "Li scelgo in modo quasi automatico, più del previsto,",
        "Mi ritrovo a metterli spesso, più di quanto anticipassi,",
        "Li ho messi in rotazione più attiva del previsto,",
        "Mi ritrovo con loro addosso con alta frequenza,",
        "Li ho usati con una continuità inaspettata,",
        "Li indosso con sorprendente regolarità,",
        "Li sto portando con frequenza maggiore di quanto pensavo,",
        "Mi ritrovo a sceglierli con inaspettata costanza,",
        "Li indosso più regolarmente di quanto avessi previsto,",
        "Li ho usati più del previsto e la sorpresa è positiva,",
        "Mi ritrovo a portarli spesso, superando le aspettative iniziali,",
    ],

    # 22x — frammento inizio frase
    "Avevo voglia di farmeli piacere, soprattutto per": [
        "Speravo di convincermi, specialmente per",
        "Volevo trovare il modo di amarli, soprattutto per",
        "Cercavo di farmeli andare bene, specialmente per",
        "Mi sforzavo di apprezzarli, in particolare per",
        "Speravo in un innamoramento, soprattutto per",
        "Volevo che mi convincessero davvero, specialmente per",
        "Cercavo argomenti per tenerli, in particolare per",
        "Qualcosa in me voleva che funzionassero, specialmente per",
        "Avevo una spinta a farmeli piacere, soprattutto per",
        "Speravo di trovare la quadra, specialmente per",
        "Cercavo di darmi una ragione per amarli, soprattutto per",
        "Volevo cedergli il beneficio del dubbio, specialmente per",
        "Avevo speranza che si rivelassero giusti, soprattutto per",
        "Mi aspettavo di convincermi, specialmente per",
        "Ci speravo davvero, in particolare per",
        "Lavoravo mentalmente per farcela, soprattutto grazie a",
        "Provavo a costruire un argomento per sì, specialmente per",
        "Aspettavo un click, soprattutto per",
        "Volevo che la risposta fosse positiva, specialmente per",
        "Desideravo trovare il filo che li legava a me, soprattutto per",
        "Aspiravo a trovare una ragione per tenerli, specialmente per",
        "Cercavo il motivo giusto per convincermi, soprattutto per",
        "Mi auspicavo una svolta, specialmente per",
    ],

    # 21x — frase completa
    "Non è un disastro concettuale, è un disastro di compatibilità.": [
        "Non è sbagliato di per sé: è sbagliato per me.",
        "Non è un fallimento di progetto: è un fallimento di adattamento.",
        "Non è il design il problema: è la compatibilità con la mia faccia.",
        "Non è una questione di qualità: è una questione di adattamento.",
        "Non fallisce come progetto: fallisce come scelta per me.",
        "Non è un errore concettuale: è un disallineamento personale.",
        "Il problema non è nel modello: è nell'incastro tra noi.",
        "Non è sbagliato in assoluto: è sbagliato in relazione a me.",
        "Non è un difetto di design: è un'incompatibilità di morfologia.",
        "Non manca di progetto: manca di sintonia con il mio profilo.",
        "Non è una brutta idea: è solo l'idea sbagliata per questa testa.",
        "Non è un errore oggettivo: è un mismatch soggettivo.",
        "Non delude come oggetto: delude come scelta per me.",
        "Non ha difetti di costruzione: ha difetti di compatibilità.",
        "Non è il prodotto a fallire: siamo noi due a non funzionare insieme.",
        "Non è mal concepito: è semplicemente non adatto a me.",
        "Non è un nato storto: è nato storto per la mia morfologia.",
        "Non ha errori propri: ha un errore nella destinazione.",
        "Non è colpa del design: è colpa dell'incontro sbagliato.",
        "Non è il prodotto il problema: sono io il profilo sbagliato.",
        "Non manca di qualità: manca di adattabilità al mio viso.",
        "Non è un cattivo prodotto: è il prodotto sbagliato per me.",
    ],

    # 21x — frammento finale frase
    "ma non abbastanza da farmi sciogliere del tutto": [
        "ma non al punto da rendersi definitivo",
        "ma non fino al punto di conquistarmi pienamente",
        "ma non abbastanza da chiudere ogni dubbio",
        "ma non quanto basta per il pieno convincimento",
        "ma senza raggiungere la soglia dell'amore totale",
        "ma non fino a spazzare via ogni riserva",
        "ma non abbastanza per eliminare ogni incertezza",
        "ma non al livello del convincimento assoluto",
        "ma non nel modo necessario per la certezza piena",
        "ma non fino a quel punto di non ritorno",
        "ma non in misura sufficiente per il giudizio definitivo",
        "ma non tanto da svuotare ogni perplessità",
        "ma non abbastanza per togliermi tutti i dubbi",
        "ma non al livello della piena soddisfazione",
        "ma senza arrivare alla soglia dell'entusiasmo totale",
        "ma non quanto mi sarei aspettato per dirlo mio",
        "ma non in maniera sufficiente per rinunciare a ogni riserva",
        "ma non fino alla piena approvazione",
        "ma senza raggiungere l'adesione completa",
        "ma non abbastanza per considerarlo definitivo",
        "ma non a quel livello di certezza che cercavo",
        "ma non così tanto da eliminare il margine critico",
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
print("✅ Round 6 completato!" if errors == 0 else f"⚠️ {errors} errori.")
