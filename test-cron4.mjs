import { neon } from '@neondatabase/serverless';

const sql = neon(process.env.DATABASE_URL);

async function test() {
  try {
    console.log('Controllo stato database...');
    let published = await sql`SELECT count(*) as total FROM reviews WHERE is_published = true`;
    console.log('Già pubblicate in partenza:', published[0].total);
    
    let readyToPublish = await sql`SELECT count(*) as total FROM reviews WHERE is_published = false AND publish_date <= CURRENT_DATE`;
    console.log('Pronte da pubblicare prima del test cron:', readyToPublish[0].total);

    console.log('Eseguo logica di /api/cron/publish-reviews ...');
    const cronResult = await sql`
      UPDATE reviews
      SET is_published = TRUE
      WHERE is_published = FALSE AND publish_date <= CURRENT_DATE
      RETURNING id, product_id, username, publish_date::text
    `;
    console.log('Cron ha pubblicato', cronResult.length, 'recensioni:');
    console.dir(cronResult);

    console.log('Controllo stato finale...');
    published = await sql`SELECT count(*) as total FROM reviews WHERE is_published = true`;
    console.log('Già pubblicate alla fine:', published[0].total);

  } catch (error) {
    console.error('Errore:', error);
  } finally {
    process.exit(0);
  }
}
test();