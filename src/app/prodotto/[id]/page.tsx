import ProductDetail from "./ProductDetail";
import { PRODUCTS, getProductById } from "@/data/products";
import { notFound } from "next/navigation";
import sql from "@/lib/db";
import { Review } from "@/types/review";

// Rivalidazione ogni ora — le recensioni vengono pubblicate 1 volta al giorno
export const revalidate = 3600;

export function generateStaticParams() {
  return PRODUCTS.map((p) => ({ id: String(p.id) }));
}

export function generateMetadata({ params }: { params: { id: string } }) {
  const product = getProductById(Number(params.id));
  if (!product) return { title: "Prodotto non trovato" };
  return {
    title: `${product.nome_modello} — Solara`,
    description: product.descrizione.slice(0, 160),
  };
}

export default async function ProdottoPage({ params }: { params: { id: string } }) {
  const product = getProductById(Number(params.id));
  if (!product) notFound();

  // Solo 3 recensioni per l'anteprima — la pagina /recensioni mostra tutte
  const reviews = (await sql`
    SELECT id, product_id, product_name, username, stars, body,
           publish_date::text, created_at::text
    FROM reviews
    WHERE product_id = ${product.id}
      AND is_published = TRUE
    ORDER BY publish_date DESC, id DESC
    LIMIT 3
  `) as Review[];

  const totalReviews = (await sql`
    SELECT COUNT(*) AS count FROM reviews
    WHERE product_id = ${product.id} AND is_published = TRUE
  `)[0] as { count: string };

  const avgStars = reviews.length > 0
    ? (await sql`
        SELECT ROUND(AVG(stars)::numeric, 1) AS avg FROM reviews
        WHERE product_id = ${product.id} AND is_published = TRUE
      `)[0] as { avg: string }
    : null;

  return (
    <ProductDetail
      product={product}
      reviews={reviews}
      totalReviews={Number(totalReviews.count)}
      avgStars={avgStars ? Number(avgStars.avg) : 0}
    />
  );
}
