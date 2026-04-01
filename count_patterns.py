import json

with open('reviews_with_patterns.json', 'r', encoding='utf-8') as f:
    r = json.load(f)

# Trova tipo apostrofo in "colpo d'occhio"
for rev in r:
    b = rev['body']
    if 'colpo' in b:
        idx = b.index('colpo')
        snippet = b[idx:idx+40]
        print(repr(snippet))
        break

# Trova tipo apostrofo in "l'equilibrio"
for rev in r:
    b = rev['body']
    if 'equilibrio' in b and 'funziona' in b:
        idx = b.index('funziona')
        snippet = b[idx:idx+40]
        print(repr(snippet))
        break

# Conta TUTTI i pattern con apostrofo dritto
test_patterns = [
    "e il colpo d'occhio \u00e8 buono, ma",
    "Qui la cosa che funziona \u00e8 l'equilibrio:",
    "Qui la cosa che funziona \u00e8 l\u2019equilibrio:",
]
for p in test_patterns:
    count = sum(1 for rev in r if p in rev['body'])
    print(f"{count:4d}x  {repr(p)}")

# Conta tutti i pattern principali - lista completa
all_patterns = {
    "qui hanno trovato un equilibrio raro": 0,
    "d\u00e0 identit\u00e0, ma la cosa migliore \u00e8 che": 0,
    "Il motivo per cui mi fermo a quattro \u00e8 che": 0,
    "lavorano insieme in un modo che mi piace molto": 0,
    "e il colpo d'occhio \u00e8 buono, ma": 0,
    "Per questo resta un s\u00ec con riserva, non un s\u00ec assoluto": 0,
    "Qui la cosa che funziona \u00e8 l'equilibrio:": 0,
    "senza bisogno di costruirgli attorno una sceneggiatura": 0,
    "Si vede che il disegno \u00e8 curato, anche se non tutto \u00e8 perfetto": 0,
    "Ha delle qualit\u00e0 evidenti, sarebbe disonesto negarlo": 0,
    "ha tirato fuori una personalit\u00e0 pi\u00f9 matura di quanto": 0,
    "Lo capisco, semplicemente non lo sento mio fino in fondo": 0,
    "mi aveva incuriosito parecchio. Dal vivo per\u00f2": 0,
    "ma non basta per salvarlo nel mio uso": 0,
    "Alla fine resto in equilibrio instabile": 0,
    "Mi sono piaciuti diversi aspetti": 0,
    "ha trovato il suo senso in modo molto": 0,
    "ha confermato il suo carattere senza diventare": 0,
    "Mi ci \u00e8 voluto meno del previsto per inquadrarli.": 0,
    "Li ho giudicati in dieci secondi e poi li ho rivalutati con calma.": 0,
    "Li ho infilati per la prima volta senza aspettarmi troppo e invece": 0,
    "La prova vera non l'ho fatta davanti allo specchio, ma fuori, e l\u00ec": 0,
    "Il test decisivo per me \u00e8 sempre la seconda uscita, quella senza entusiasmo iniziale, e l\u00ec": 0,
    "La cosa pi\u00f9 onesta che posso dire \u00e8": 0,
    "Li ho comprati per un motivo e li": 0,
    "Il primo impatto non dice tutta la verit\u00e0 su questo paio.": 0,
    "In foto mi piacevano, ma dal vivo la lettura cambia parecchio.": 0,
    "La prima impressione \u00e8 stata migliore del previsto.": 0,
    "Ho aspettato qualche uscita prima di farmi un'idea": 0,
    "Non mi interessa mai il colpo di fulmine": 0,
    "Non sono uno che cambia occhiali ogni mese.": 0,
    "Pensavo di aver capito tutto dalle immagini, invece no.": 0,
    "Appena aperta la custodia ho capito che non era un paio banale.": 0,
    "All'inizio li guardavo con curiosit\u00e0 pi\u00f9 che con": 0,
    "Sono entrato nella prova con un pregiudizio e": 0,
    "Non cerco mai l'effetto influencer, cerco il paio": 0,
    "Sono di quei modelli che vanno raccontati dopo": 0,
    "Non compro per collezione, compro per uso reale.": 0,
    "Ho un viso che non perdona molto e": 0,
    "Di solito capisco subito se un paio mi": 0,
    "A forza di provarne, ho capito che il": 0,
    "Io parto sempre malissimo con i modelli troppo": 0,
    "Ho quarantadue anni e di solito diffido dei": 0,
    "Ho gusti abbastanza selettivi e faccio pochi acquisti": 0,
    "Mi conosco: se un occhiale mi complica la": 0,
    "All'inizio ero pi\u00f9 scettico che convinto.": 0,
}

for p in all_patterns:
    for rev in r:
        if p in rev['body']:
            all_patterns[p] += 1

print("\n=== CONTEGGIO DEFINITIVO ===")
for p, cnt in sorted(all_patterns.items(), key=lambda x: -x[1]):
    if cnt > 0:
        print(f"{cnt:4d}x  {p[:70]}")

# Conta recensioni senza nessun pattern
no_pattern = 0
for rev in r:
    found = False
    for p in all_patterns:
        if p in rev['body']:
            found = True
            break
    if not found:
        no_pattern += 1
print(f"\nRecensioni senza pattern noti: {no_pattern}")
