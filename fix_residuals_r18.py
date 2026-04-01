# -*- coding: utf-8 -*-
import psycopg2, sys
from collections import defaultdict

sys.stdout.reconfigure(encoding='utf-8')

DATABASE_URL = "postgresql://neondb_owner:npg_uFxVSRoTj95w@ep-damp-sea-anvn4fw4.c-6.us-east-1.aws.neon.tech/neondb?sslmode=require"

PATTERNS = {
    # 11x → alta priorità
    "non perdona un viso troppo piccolo": [
        "penalizza fortemente i visi più piccoli",
        "va male su un viso piccolo",
        "risulta sproporzionato su visi di piccola taglia",
        "non è adatto a chi ha un viso piccolo",
        "su una fisionomia piccola diventa ingombrante",
        "crea squilibrio su visi con dimensioni ridotte",
        "su un viso piccolo occupa troppo spazio",
        "non lascia i visi piccoli liberi di respirare",
        "rischia di sovrastare una fisionomia esile",
        "su conformazioni minute risulta esagerato",
        "non va d'accordo con i visi poco sviluppati",
        "un viso piccolo fatica a sostenerlo",
    ],
    # 11x
    "la costruzione a doppio ponte": [
        "il telaio con doppio ponte",
        "la struttura dal doppio archetto",
        "il disegno a doppio ponte",
        "il profilo con doppio ponte",
        "la montatura col doppio ponte",
        "la barra superiore doppia del telaio",
        "i due ponti che caratterizzano il telaio",
        "il doppio archetto metallico",
        "la struttura con ponte duplice",
        "l'architettura a doppio ponte",
        "l'elemento a doppio ponte",
        "il frontale con doppia barra",
    ],
    # 8x cross-sentence
    "Invece sembrano più raffinati che appariscenti, grazie anche a": [
        "Alla fine risultano più sobri del previsto, merito anche di",
        "Al contrario si rivelano più contenuti che vistosi, grazie anche a",
        "In realtà sono più eleganti che ostentati, in parte grazie a",
        "Invece si dimostrano più misurati che esibiti, anche per via di",
        "In realtà appaiono più raffinati che sgargianti, merito di",
        "Alla prova dei fatti sono più discreti di quanto temessi, grazie a",
        "Diversamente da quanto pensavo, risultano più sobri che stravaganti, anche grazie a",
        "In realtà sembrano più calibrati che eccessivi, merito anche di",
        "Al contrario si mostrano più composti che appariscenti, grazie anche a",
        "Invece si rivelano più eleganti che impegnativi, anche per merito di",
    ],
    # 8x multi-window
    "il rimless sul mio viso tende a muoversi": [
        "la montatura rimless sulla mia fisionomia tende a scivolare",
        "la struttura senza bordo sul mio naso tende a spostarsi",
        "il telaio rimless sul mio viso non rimane fisso",
        "la forma rimless sulla mia conformazione tende a scorrere",
        "il rimless sulla mia fisionomia fatica a restare stabile",
        "il frame senza bordo tende a scivolare sul mio naso",
        "il rimless non si assesta sul mio naso come vorrei",
        "la montatura priva di bordo sul mio viso perde posizione facilmente",
        "il telaio rimless tende a spostarsi sulla mia conformazione nasale",
        "questa tipologia rimless tende a non tenersi ferma sul mio naso",
    ],
    # 8x multi-window
    "su un viso piccolo diventano il centro di tutto": [
        "su una fisionomia piccola finiscono per dominare la scena",
        "su un viso di piccole dimensioni prendono tutta la scena",
        "su una struttura facciale ridotta si impongono con forza eccessiva",
        "su un viso piccolo occupano troppo spazio",
        "su una fisionomia esile diventano l'unico elemento visibile",
        "su un viso di piccola taglia sovrastano tutto il resto",
        "su una conformazione piccola diventano dominanti in modo eccessivo",
        "su un viso con poca superficie diventano ingombranti",
        "sulle fisionomie più piccole tendono a prendere il sopravvento",
        "su un viso piccolo risultano sproporzionati rispetto al contesto",
    ],
    # 8x
    "Funziona meglio quando il resto del look resta asciutto": [
        "Trova il suo equilibrio quando l'abbigliamento intorno è sobrio",
        "Funziona al meglio con un look circostante essenziale",
        "Si esprime al massimo quando il contesto visivo è minimale",
        "Rende bene su look dall'estetica pulita e non sovraccarica",
        "Funziona quando il guardaroba intorno è neutro e contenuto",
        "Si valorizza con un abbigliamento che non compete con lui",
        "Funziona meglio su look che non chiedono troppa attenzione visiva",
        "Funziona davvero bene con abbinamenti dall'impostazione sobria",
        "Si trova a suo agio con un look che lascia spazio al silenzio visivo",
        "Rende il meglio di sé quando non compete con altri elementi forti",
    ],
    # 8x
    "con il caldo li devo sistemare spesso": [
        "quando fa caldo tendono a scivolare",
        "con le alte temperature scivolano più del solito",
        "nel caldo richiedono frequenti riposizionamenti",
        "col calore estivo perdono stabilità",
        "nelle giornate molto calde si spostano facilmente",
        "con il sudore da calore non tengono bene la posizione",
        "nelle temperature alte faticano a stare fermi",
        "col caldo non mantengono il posizionamento come vorrei",
        "durante le giornate afose perdono aderenza",
        "in estate il caldo le fa scivolare più del necessario",
    ],
    # 9x
    "il verde bottiglia è molto caratterizzante": [
        "il tono bottiglia non si abbina con facilità a tutto",
        "il verde bottiglia richiede capi compatibili per funzionare",
        "il verde bottiglia è un colore che si fa notare sempre",
        "la tonalità bottiglia è piuttosto esigente con il guardaroba",
        "il verde bottiglia non è un colore neutro da abbinare ovunque",
        "il tono verde bottiglia è selettivo con gli abbinamenti",
        "il verde bottiglia è un colore forte che guida le scelte del look",
        "la tonalità bottiglia ha una presenza che non si ignora",
        "il verde bottiglia esclude una fetta degli outfit normali",
        "il tono bottiglia non è per guardarobe generiche",
        "il verde bottiglia impone qualche riflessione sugli abbinamenti",
    ],
    # 8x
    "il posizionamento premium mi rende più esigente": [
        "il prezzo premium alza l'asticella delle mie aspettative",
        "il fatto di essere un prodotto di fascia alta mi porta a essere più critico",
        "la fascia di prezzo alta mi fa valutare ogni aspetto con più attenzione",
        "la proposta di lusso mi spinge ad aspettarmi di più",
        "chiamarsi premium significa che ogni limite pesa di più",
        "il costo elevato mi porta a guardare con occhio più severo",
        "la collocazione alta di prezzo mi fa diventare più esigente",
        "pagare questo importo mi fa pretendere qualcosa in più",
        "il segmento alto in cui si colloca mi porta ad aspettarmi di più",
        "il prezzo selezionato innalza le mie aspettative in modo naturale",
    ],
    # 8x
    "il blu è più vivido dal vivo": [
        "il blu dal vero è molto più acceso rispetto alle foto",
        "in mano il blu risulta più brillante del previsto",
        "indossati, il blu è notevolmente più intenso di quanto sembri nelle immagini",
        "visti di persona, il blu si mostra più saturo di quanto atteso",
        "a vederli di persona il blu gareggia con qualcosa di più vivace",
        "il blu visto di persona è molto più carico di quanto le foto suggeriscano",
        "dal vivo il blu ha un'intensità che le fotografie tradiscono",
        "di persona il blu è decisamente più vivo di quanto si capisca online",
        "una volta indossati il blu si rivela ben più intenso del previsto",
        "in condizioni reali il blu è molto più maturo di quanto suggerissero le foto",
    ],
    # 8x
    "se il naso non è compatibile si capisce subito": [
        "se la conformazione nasale non è adatta, si percepisce immediatamente",
        "se il naso non è adatto per questa montatura, lo si scopre in pochi minuti",
        "se la fisionomia nasale non è compatibile, il disagio è immediato",
        "chi ha un naso particolare se ne accorge subito",
        "se il profilo nasale non si adatta, la realtà emerge presto",
        "chi ha una conformazione nasale specifica capisce subito se funziona",
        "se il naso non si allinea con la montatura, si capisce presto",
        "se la forma del naso non corrisponde, l'incompatibilità è evidente fin da subito",
        "basta una breve prova per capire se la conformazione è compatibile",
        "se la struttura nasale non è quella giusta, ci si accorge in pochissimo tempo",
    ],
    # 8x
    "la lente specchiata non è per tutti": [
        "il finish specchiato non à adatto a ogni tipo di look",
        "le lenti a specchio non si adattano a ogni gusto",
        "lo specchio non è per chi vuole passare inosservato",
        "l'effetto mirror non funziona su ogni tipo di viso",
        "le lenti specchiate non sono una scelta universale",
        "non tutti riescono a portare il finish specchiato",
        "lo specchio è una scelta di campo che non si adatta a tutti",
        "il mirror non è un'opzione democratica",
        "le lenti riflettenti funzionano bene solo su alcuni tipi di look",
        "il finish a specchio è un'opzione selettiva",
    ],
    # 9x
    "La prima occasione è stata un": [
        "La prima uscita vera è stata un",
        "Il primo utilizzo reale è stato un",
        "La prima prova sul campo è stata un",
        "Il debutto vero è stato un",
        "Il primo contesto d'uso è stato un",
        "Il primo test fuori casa è stato un",
        "La prima uscita concreta è stata un",
        "L'esordio vero è stato un",
        "Il primo collaudo è stato un",
        "La prima situazione reale è stata un",
    ],
    # 9x - fragment in different sentences
    "le punte con finitura legnosa": [
        "le aste con effetto legno",
        "le punte con texture legnosa",
        "le aste rifinite in materiale legnoso",
        "le stanghette con rivestimento effetto legno",
        "le punte con finitura in legno naturale",
        "le aste con l'effetto in legno",
        "le punte rivestite con finitura che imita il legno",
        "le stanghette con la fattura lignea",
        "le aste con la finitura in legno a contrasto",
        "le punte con il rivestimento look legno",
    ],
    # 8x each unique continuation
    "Li ho usati durante un weekend": [
        "Li ho portati durante un fine settimana",
        "Li ho indossati durante un weekend",
        "Li ho messi durante un fine settimana",
        "Li ho sfoggiati durante un weekend",
        "Li ho testati nel corso di un fine settimana",
        "Li ho mandati in missione durante un weekend",
        "Li ho usati nel corso di un fine settimana",
        "Li ho scelti per un intero weekend",
        "Li ho portati per tutto il weekend",
        "Li ho adottati durante un fine settimana",
    ],
    # 8x
    "non vive da sola: la struttura": [
        "non basta da sola: la struttura",
        "non si sostiene da sola: la struttura",
        "non funziona mai isolata: la struttura",
        "non ha vita propria: la struttura",
        "non esprime il meglio da sola: la struttura",
        "non esiste indipendentemente: la struttura",
        "non afferma il suo valore da sola: la struttura",
        "non completa il progetto da sola: la struttura",
        "non si regge da sola: la struttura",
        "non si legge come elemento singolo: la struttura",
    ],
    # 8x - each with different continuation
    "struttura aviator in metallo lucido e": [
        "telaio aviator in metallo brillante e",
        "profilo aviator nel metallo lucidato e",
        "costruzione aviator nel metallo rifinito e",
        "telaio da aviator in metallo brillante e",
        "architettura aviator del metallo lucido e",
        "struttura da aviator nel metallo rifinito e",
        "forma aviator nel metallo lustrato e",
        "linea aviator del telaio in metallo lucido e",
        "ossatura aviator in metallo riflettente e",
        "disegno aviator in metallo lucido e",
    ],
    # 8x
    "delle lenti crea un insieme davvero": [
        "delle lenti forma un abbinamento davvero",
        "delle lenti genera un effetto davvero",
        "delle lenti produce un'estetica davvero",
        "delle lenti costruisce qualcosa di davvero",
        "delle lenti compone un insieme davvero",
        "delle lenti dà vita a qualcosa di davvero",
        "delle lenti restituisce un effetto davvero",
        "delle lenti contribuisce a qualcosa di davvero",
        "delle lenti concorre a un risultato davvero",
        "delle lenti genera un insieme davvero",
    ],
    # 8x
    "è che linea femminile ma misurata": [
        "è che questa linea femminile ma contenuta",
        "è che questo profilo femminile ma sobrio",
        "è che la forma femminile ma calibrata",
        "è che questo disegno femminile ma discreto",
        "è che questa silhouette femminile ma misurata",
        "è che questo tratto femminile ma non esagerato",
        "è che questo stile femminile ma non invadente",
        "è che questa curva femminile ma trattenuta",
        "è che questo taglio femminile ma non sgargiante",
        "è che questa linea dolce ma non eccessiva",
    ],
    # 8x
    "la lente in gradazione calda e": [
        "la lente col degradé caldo e",
        "la lente con sfumatura calda e",
        "la lente dal tono ambrato sfumato e",
        "la lente in tono caldo degradé e",
        "la lente dalla gradazione in toni caldi e",
        "la lente con il degradé nelle tonalità calde e",
        "la lente nel tono warm sfumato e",
        "la lente dalla progressione calda e",
        "la lente con la sfumatura dei toni caldi e",
        "la lente con la gradazione color miele e",
    ],
    # 8x
    "chi cerca un cat-eye molto aggressivo potrebbe trovarlo troppo delicato": [
        "chi vuole un cat-eye più pronunciato potrebbe trovarlo eccessivamente sobrio",
        "chi predilige un cat-eye tagliente potrebbe trovarlo troppo morbido",
        "per chi preferisce linee più aggressive il cat-eye potrebbe sembrare poco deciso",
        "chi ama un cat-eye netto e silenzioso potrebbe considerarlo troppo educato",
        "chi punta a un cat-eye molto marcato potrebbe trovarlo timido",
        "per chi cerca qualcosa di più audace, il cat-eye qui è contenuto",
        "chi desidera un cat-eye dai bordi netti potrebbe trovarlo poco incisivo",
        "per chi vuole un cat-eye vistoso, questo è più raffinato che appariscente",
        "chi preferisce un eye-liner di taglio deciso potrebbe sentirne la mancanza",
        "per chi ama il cat-eye estremo, questo è troppo composto",
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
print("Round 18 OK" if errors == 0 else "Round 18 ERRORI")
