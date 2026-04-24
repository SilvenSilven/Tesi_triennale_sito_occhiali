import { readFileSync } from "fs";
import { neon } from "@neondatabase/serverless";

const DATABASE_URL =
  "postgresql://neondb_owner:npg_uFxVSRoTj95w@ep-damp-sea-anvn4fw4-pooler.c-6.us-east-1.aws.neon.tech/neondb?sslmode=require";

const sql = neon(DATABASE_URL);

// Map product name -> product_id (matches products.ts ids)
const PRODUCT_MAP = {
  "Aureum Pilot Verde": 1,
  "Amber Crest Oversize": 2,
  "Lunaris Ice Mirror": 3,
  "Nebula Square Blu": 4,
  "Torque Shield Blue": 5,
  "Selene Havana Cat": 6,
  "Astra Verde Ottagono": 7,
  "Auric Wood Green": 8,
  "Vector Prism Shield": 9,
  "Helios Gold Fade": 10,
};

// Day 1 = 2026-04-01
const BASE_DATE = new Date("2026-04-01");

function dayToDate(giorno) {
  const d = new Date(BASE_DATE);
  d.setDate(d.getDate() + (giorno - 1));
  return d.toISOString().split("T")[0]; // YYYY-MM-DD
}

async function main() {
  const raw = readFileSync(
    new URL("../andamento_prezzi.json", import.meta.url),
    "utf-8"
  );
  const data = JSON.parse(raw);
  const productNames = data.prodotti;

  console.log(`Inserting prices for ${data.dati.length} days × ${productNames.length} products...`);

  // Build VALUES for batch insert (50 days at a time)
  const BATCH_SIZE = 50;
  const days = data.dati;

  for (let batchStart = 0; batchStart < days.length; batchStart += BATCH_SIZE) {
    const batch = days.slice(batchStart, batchStart + BATCH_SIZE);
    const values = [];

    for (const dayData of batch) {
      const dateStr = dayToDate(dayData.giorno);
      for (const name of productNames) {
        const productId = PRODUCT_MAP[name];
        const price = dayData[name];
        // Escape single quotes in product names (none here, but safe)
        const safeName = name.replace(/'/g, "''");
        values.push(
          `(${productId}, '${safeName}', '${dateStr}', ${price})`
        );
      }
    }

    const insertSQL = `
      INSERT INTO product_prices (product_id, product_name, price_date, price)
      VALUES ${values.join(",\n")}
      ON CONFLICT (product_id, price_date) DO UPDATE SET price = EXCLUDED.price
    `;

    await sql.query(insertSQL);
    console.log(
      `  Batch ${Math.floor(batchStart / BATCH_SIZE) + 1}: days ${batch[0].giorno}-${batch[batch.length - 1].giorno} ✓`
    );
  }

  // Verify
  const count = await sql`SELECT COUNT(*) AS total FROM product_prices`;
  console.log(`\nDone! Total rows in product_prices: ${count[0].total}`);

  // Show sample
  const sample = await sql`
    SELECT product_name, price_date, price 
    FROM product_prices 
    WHERE price_date IN ('2026-04-01', '2026-04-02', '2026-12-06')
    ORDER BY price_date, product_id
    LIMIT 20
  `;
  console.log("\nSample data:");
  console.table(sample);
}

main().catch(console.error);
