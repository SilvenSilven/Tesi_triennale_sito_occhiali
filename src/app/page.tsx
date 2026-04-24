import HomeLanding from "@/components/HomeLanding";
import sql from "@/lib/db";

export const revalidate = 3600;

export default async function Home() {
  const allPrices = await sql`
    SELECT product_id, price FROM product_prices
    WHERE price_date = CURRENT_DATE
    ORDER BY product_id
  `;
  const pricesMap: Record<number, number> = {};
  allPrices.forEach((row) => {
    pricesMap[Number(row.product_id)] = Number(row.price);
  });

  return <HomeLanding pricesMap={pricesMap} />;
}
