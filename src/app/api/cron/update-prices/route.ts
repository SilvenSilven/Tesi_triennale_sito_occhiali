import { NextRequest, NextResponse } from "next/server";
import { revalidatePath } from "next/cache";
import sql from "@/lib/db";

/**
 * GET /api/cron/update-prices
 *
 * Cron job eseguito ogni giorno alle 08:05 (Europa/Roma) via cron-job.org.
 * Invalida la cache ISR del catalogo e delle pagine prodotto
 * in modo che i prezzi aggiornati vengano mostrati.
 *
 * I prezzi sono già pre-caricati nella tabella product_prices.
 * Questo endpoint si limita a invalidare la cache per forzare il ri-rendering.
 *
 * Autenticazione: query param ?secret= oppure header Authorization: Bearer <CRON_SECRET>
 */
export async function GET(req: NextRequest) {
  const authHeader = req.headers.get("authorization");
  const expectedToken = `Bearer ${process.env.CRON_SECRET}`;

  const { searchParams } = new URL(req.url);
  const secret = searchParams.get("secret");

  const authorized =
    (authHeader && authHeader === expectedToken) ||
    (secret && secret === process.env.CRON_SECRET);

  if (!authorized) {
    return NextResponse.json({ error: "Non autorizzato" }, { status: 401 });
  }

  // Verifica che ci siano prezzi per oggi
  const todayPrices = await sql`
    SELECT product_id, product_name, price
    FROM product_prices
    WHERE price_date = CURRENT_DATE
    ORDER BY product_id
  `;

  // Invalida la cache ISR del catalogo
  revalidatePath("/catalogo");

  // Invalida la cache ISR di ogni pagina prodotto
  for (let pid = 1; pid <= 10; pid++) {
    revalidatePath(`/prodotto/${pid}`);
  }

  return NextResponse.json(
    {
      message: "Prezzi aggiornati e cache invalidata",
      date: new Date().toISOString(),
      pricesFound: todayPrices.length,
      prices: todayPrices,
    },
    { status: 200 }
  );
}
