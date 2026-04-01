#!/usr/bin/env node
// Applica tutti i batch SQL v2 al database Neon
import pg from 'pg';
import fs from 'fs';
import path from 'path';

const { Client } = pg;

const connectionString = 'postgresql://neondb_owner:npg_uFxVSRoTj95w@ep-damp-sea-anvn4fw4-pooler.c-6.us-east-1.aws.neon.tech/neondb?sslmode=require';

async function main() {
  const client = new Client({ connectionString });
  await client.connect();
  console.log('Connesso al database Neon');

  // Trova tutti i file batch v2
  const files = fs.readdirSync('.')
    .filter(f => f.match(/^update_v2_batch_\d+\.sql$/))
    .sort();

  console.log(`Trovati ${files.length} file batch`);

  let totalUpdated = 0;
  let totalErrors = 0;

  for (const file of files) {
    const sql = fs.readFileSync(file, 'utf-8');
    
    // Estrai i singoli UPDATE dal file (rimuovi BEGIN/COMMIT)
    const statements = sql
      .split('\n')
      .filter(line => line.trim().startsWith('UPDATE'))
      .map(line => line.trim());

    try {
      await client.query('BEGIN');
      for (const stmt of statements) {
        await client.query(stmt);
      }
      await client.query('COMMIT');
      totalUpdated += statements.length;
      console.log(`✅ ${file}: ${statements.length} UPDATE applicati`);
    } catch (err) {
      await client.query('ROLLBACK');
      totalErrors++;
      console.error(`❌ ${file}: ERRORE - ${err.message}`);
    }
  }

  console.log(`\nTotale: ${totalUpdated} UPDATE applicati, ${totalErrors} errori`);
  
  // Verifica conteggio
  const res = await client.query('SELECT COUNT(*) FROM reviews');
  console.log(`Recensioni nel database: ${res.rows[0].count}`);

  await client.end();
}

main().catch(err => {
  console.error('Errore fatale:', err);
  process.exit(1);
});
