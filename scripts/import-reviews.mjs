/**
 * Script di importazione recensioni da Excel nel database Neon.
 * Salta le prime 3 recensioni per prodotto (già inserite con date 29-31 marzo 2026)
 * e assegna le restanti a partire dal 1 aprile 2026, 1 al giorno per prodotto.
 */

import { createRequire } from 'module';
import { neon } from '@neondatabase/serverless';

const require = createRequire(import.meta.url);
const XLSX = require('xlsx');

// Connection string diretta (unpooled per script one-shot)
const DATABASE_URL = 'postgresql://neondb_owner:npg_uFxVSRoTj95w@ep-damp-sea-anvn4fw4.c-6.us-east-1.aws.neon.tech/neondb?sslmode=require';

// Mapping nome modello (Excel) → product_id (DB)
const PRODUCT_MAP = {
  'Aureum Pilot Verde':   1,
  'Amber Crest Oversize': 2,
  'Lunaris Ice Mirror':   3,
  'Nebula Square Blu':    4,
  'Torque Shield Blue':   5,
  'Selene Havana Cat':    6,
  'Astra Verde Ottagono': 7,
  'Auric Wood Green':     8,
  'Vector Prism Shield':  9,
  'Helios Gold Fade':     10,
};

// Numero di recensioni già inserite per prodotto
const ALREADY_INSERTED = 3;

// Primo giorno futuro: 1 aprile 2026
const START_DATE = new Date('2026-04-01T00:00:00.000Z');

function addDays(date, days) {
  const d = new Date(date);
  d.setUTCDate(d.getUTCDate() + days);
  return d;
}

function toISODate(date) {
  return date.toISOString().slice(0, 10);
}

async function main() {
  // 1. Leggi Excel
  const wb = XLSX.readFile('recensioni_occhiali.xlsx');
  const ws = wb.Sheets[wb.SheetNames[0]];
  const rows = XLSX.utils.sheet_to_json(ws);
  console.log(`Lette ${rows.length} righe dall'Excel.`);

  // 2. Raggruppa per modello e salta le prime ALREADY_INSERTED
  const byProduct = {};
  for (const row of rows) {
    const name = row['Modello'];
    if (!byProduct[name]) byProduct[name] = [];
    byProduct[name].push(row);
  }

  // 3. Prepara i record da inserire
  const toInsert = [];
  for (const [modelName, reviews] of Object.entries(byProduct)) {
    const productId = PRODUCT_MAP[modelName];
    if (!productId) {
      console.warn(`Modello non trovato nel mapping: "${modelName}" — saltato`);
      continue;
    }
    const remaining = reviews.slice(ALREADY_INSERTED);
    console.log(`${modelName} (id=${productId}): ${reviews.length} totali, ${remaining.length} da inserire`);

    for (let i = 0; i < remaining.length; i++) {
      const r = remaining[i];
      const publishDate = toISODate(addDays(START_DATE, i));
      toInsert.push({
        product_id: productId,
        product_name: modelName,
        username: r['Nome Utente'],
        stars: Number(r['Stelle']),
        body: r['Recensione'],
        publish_date: publishDate,
        is_published: false,
      });
    }
  }

  console.log(`\nTotale record da inserire: ${toInsert.length}`);

  // 4. Inserisci in batch nel DB
  const sql = neon(DATABASE_URL);

  const BATCH_SIZE = 100;
  let inserted = 0;

  for (let i = 0; i < toInsert.length; i += BATCH_SIZE) {
    const batch = toInsert.slice(i, i + BATCH_SIZE);
    // Costruisci VALUES manualmente per compatibilità con neon http driver
    const values = batch.map((r, idx) => {
      const base = idx * 7;
      return `($${base+1},$${base+2},$${base+3},$${base+4},$${base+5},$${base+6},$${base+7})`;
    }).join(',');
    const params = batch.flatMap(r => [
      r.product_id,
      r.product_name,
      r.username,
      r.stars,
      r.body,
      r.publish_date,
      r.is_published,
    ]);
    await sql.query(
      `INSERT INTO reviews (product_id, product_name, username, stars, body, publish_date, is_published) VALUES ${values}`,
      params
    );
    inserted += batch.length;
    process.stdout.write(`\rInseriti: ${inserted}/${toInsert.length}`);
  }

  console.log('\n\nImportazione completata!');

  // 5. Verifica finale
  const counts = await sql.query(
    `SELECT product_id, product_name, COUNT(*) as total,
            MIN(publish_date)::text as first_date,
            MAX(publish_date)::text as last_date
     FROM reviews 
     GROUP BY product_id, product_name 
     ORDER BY product_id`
  );
  console.log('\nRiepilogo nel DB:');
  for (const row of counts) {
    console.log(`  [${row.product_id}] ${row.product_name}: ${row.total} recensioni (${row.first_date} → ${row.last_date})`);
  }
}

main().catch(err => {
  console.error('Errore:', err);
  process.exit(1);
});
