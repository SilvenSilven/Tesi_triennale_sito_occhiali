import { NextRequest, NextResponse } from "next/server";
import sql from "@/lib/db";

/**
 * POST /api/cron/publish-reviews
 *
 * Endpoint chiamato dal cron job ogni giorno alle 08:00 (ora italiana).
 * Pubblica tutte le recensioni con publish_date <= oggi che non sono ancora pubblicate.
 *
 * Autenticazione: header Authorization: Bearer <CRON_SECRET>
 */
export async function POST(req: NextRequest) {
  const authHeader = req.headers.get("authorization");
  const expectedToken = `Bearer ${process.env.CRON_SECRET}`;

  if (!authHeader || authHeader !== expectedToken) {
    return NextResponse.json({ error: "Non autorizzato" }, { status: 401 });
  }

  // Pubblica tutte le recensioni con data <= oggi
  const result = await sql`
    UPDATE reviews
    SET is_published = TRUE
    WHERE is_published = FALSE
      AND publish_date <= CURRENT_DATE
    RETURNING id, product_id, product_name, username, publish_date::text
  `;

  return NextResponse.json(
    {
      published: result.length,
      reviews: result,
      timestamp: new Date().toISOString(),
    },
    { status: 200 }
  );
}

// Permetti anche GET per facilitare l'integrazione con cron-job.org (che preferisce GET)
export async function GET(req: NextRequest) {
  const { searchParams } = new URL(req.url);
  const secret = searchParams.get("secret");

  if (!secret || secret !== process.env.CRON_SECRET) {
    return NextResponse.json({ error: "Non autorizzato" }, { status: 401 });
  }

  const result = await sql`
    UPDATE reviews
    SET is_published = TRUE
    WHERE is_published = FALSE
      AND publish_date <= CURRENT_DATE
    RETURNING id, product_id, product_name, username, publish_date::text
  `;

  return NextResponse.json(
    {
      published: result.length,
      reviews: result,
      timestamp: new Date().toISOString(),
    },
    { status: 200 }
  );
}
