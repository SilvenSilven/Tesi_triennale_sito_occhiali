import ProductDetail from "./ProductDetail";
import { PRODUCTS, getProductById } from "@/data/products";
import { notFound } from "next/navigation";

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

export default function ProdottoPage({ params }: { params: { id: string } }) {
  const product = getProductById(Number(params.id));
  if (!product) notFound();
  return <ProductDetail product={product} />;
}
