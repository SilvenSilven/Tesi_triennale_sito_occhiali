import { neon } from '@neondatabase/serverless';

const sql = neon(process.env.DATABASE_URL);

async function test() {
  try {
    console.log('Controllo stato database...');
    let published = await sql`SELECT count(*) as total FROM reviews WHERE is_published = true`;
    console.log('Già pubblicate:', published[0].total);
    
    let readyToPublish = await sql`SELECT count(*) as total FROM reviews WHERE is_published = false AND publish_date <= CURRENT_DATE`;
    console.log('Pronte da pubblicare prima del test cron:', readyToPublish[0].total);
    
    console.log('Inserisco una recensione finta...');
    const fakeReview = await sql`
      INSERT INTO reviews (product_id, product_name, username, rating, text, date, is_verified_purchase, status, is_published, publish_date)
      VALUES ('test-product', 'Test Product', 'CronTester', 5, 'Great for cron test', CURRENT_DATE, true, 'approved', false, CURRENT_DATE - INTERVAL '1 day')
      RETURNING id
    `;
    console.log('Nuovo ID inserito:', fakeReview[0].id);

    console.log('Eseguo logica di /api/cron/publish-reviews ...');
    const cronResult = await sql`
      UPDATE reviews
      SET is_published = TRUE
      WHERE is_published = FALSE AND publish_date <= CURRENT_DATE
      RETURNING id, product_id, username, publish_date::text
    `;
    console.log('Cron ha pubblicato', cronResult.length, 'recensioni:');
    console.dir(cronResult);
    
    await sql`DELETE FROM reviews WHERE id = ${fakeReview[0].id}`;
    console.log('Pulizia fatta. Finito.');
  } catch (error) {
    console.error('Errore:', error);
  } finally {
    process.exit(0);
  }
}
test();