import json

with open('reviews_with_patterns.json', 'r', encoding='utf-8') as f:
    reviews = json.load(f)

# Prendo 3 recensioni per ogni livello di stelle per capire la struttura
for stars in [5, 4, 3, 2, 1]:
    subset = [r for r in reviews if r['stars'] == stars]
    print(f"\n{'='*80}")
    print(f"STELLE: {stars} (totale con pattern: {len(subset)})")
    print(f"{'='*80}")
    for r in subset[:3]:
        print(f"\nID={r['id']} - {r['product_name']}")
        print(r['body'])
        print("---")
