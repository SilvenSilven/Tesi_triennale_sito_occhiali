import CatalogoClient from "./CatalogoClient";
import sql from "@/lib/db";

export const revalidate = 3600; // 1 hour

export const metadata = {
  title: "Catalogo — Solara",
  description: "Esplora la collezione completa di occhiali da sole Solara.",
};

export default async function Page() {
  const reviewsStats = await sql`
    SELECT 
      product_id, 
      ROUND(AVG(stars)::numeric, 1) AS avg_stars, 
      COUNT(*) AS count
    FROM reviews 
    WHERE is_published = TRUE 
    GROUP BY product_id
  `;

  const ratingsMap: Record<number, { avg: number; count: number }> = {};
  
  reviewsStats.forEach((stat) => {
    ratingsMap[Number(stat.product_id)] = {
      avg: Number(stat.avg_stars),
      count: Number(stat.count),
    };
  });

  // Prezzi dinamici dalla tabella product_prices (prezzo di oggi)
  const todayPrices = await sql`
    SELECT product_id, price
    FROM product_prices
    WHERE price_date = CURRENT_DATE
    ORDER BY product_id
  `;

  const pricesMap: Record<number, number> = {};
  todayPrices.forEach((row) => {
    pricesMap[Number(row.product_id)] = Number(row.price);
  });

  return <CatalogoClient ratingsMap={ratingsMap} pricesMap={pricesMap} />;
}
