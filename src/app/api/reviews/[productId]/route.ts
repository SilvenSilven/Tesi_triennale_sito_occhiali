import { NextRequest, NextResponse } from "next/server";
import sql from "@/lib/db";
import { Review } from "@/types/review";

/**
 * GET /api/reviews/[productId]
 *
 * Restituisce tutte le recensioni pubblicate per un prodotto.
 * Struttura parsabile per scraping:
 *   - ogni recensione ha: id, product_id, product_name, username, stars, body, publish_date
 */
export async function GET(
  _req: NextRequest,
  { params }: { params: { productId: string } }
) {
  const productId = parseInt(params.productId, 10);

  if (isNaN(productId)) {
    return NextResponse.json({ error: "ID prodotto non valido" }, { status: 400 });
  }

  const rows = (await sql`
    SELECT id, product_id, product_name, username, stars, body, publish_date::text, created_at::text
    FROM reviews
    WHERE product_id = ${productId}
      AND is_published = TRUE
    ORDER BY publish_date DESC, id DESC
  `) as Review[];

  const avgStars =
    rows.length > 0
      ? Math.round((rows.reduce((s, r) => s + r.stars, 0) / rows.length) * 10) / 10
      : null;

  return NextResponse.json(
    {
      product_id: productId,
      total_reviews: rows.length,
      average_stars: avgStars,
      reviews: rows,
    },
    {
      status: 200,
      headers: {
        "Cache-Control": "public, max-age=60, stale-while-revalidate=300",
      },
    }
  );
}
