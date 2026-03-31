import { notFound } from "next/navigation";
import Link from "next/link";
import { PRODUCTS, getProductById } from "@/data/products";
import sql from "@/lib/db";
import { Review } from "@/types/review";

export const revalidate = 3600;

export function generateStaticParams() {
  return PRODUCTS.map((p) => ({ id: String(p.id) }));
}

export function generateMetadata({ params }: { params: { id: string } }) {
  const product = getProductById(Number(params.id));
  if (!product) return { title: "Prodotto non trovato" };
  return {
    title: `Recensioni ${product.nome_modello} — Solara`,
    description: `Leggi tutte le recensioni di ${product.nome_modello}. Opinioni verificate dei nostri clienti.`,
  };
}

/** Stelle SVG pure — 0 dipendenze client, ottimali per SSR/scraping */
function Stars({ value, size = 20 }: { value: number; size?: number }) {
  return (
    <span
      className="inline-flex items-center gap-[3px]"
      aria-label={`${value} stelle su 5`}
      data-stars={value}
    >
      {Array.from({ length: 5 }, (_, i) => {
        const filled = value >= i + 1;
        const half = !filled && value >= i + 0.5;
        const id = `h-${i}-${value}`;
        return (
          <svg
            key={i}
            width={size}
            height={size}
            viewBox="0 0 20 20"
            aria-hidden="true"
          >
            {half && (
              <defs>
                <linearGradient id={id} x1="0" x2="1" y1="0" y2="0">
                  <stop offset="50%" stopColor="#FF6B2B" />
                  <stop offset="50%" stopColor="#d1c4b8" />
                </linearGradient>
              </defs>
            )}
            <path
              fill={half ? `url(#${id})` : filled ? "#FF6B2B" : "#d1c4b8"}
              d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"
            />
          </svg>
        );
      })}
    </span>
  );
}

/** Barra distribuzione stelle stile Amazon */
function StarBar({ count, total, label }: { count: number; total: number; label: string }) {
  const pct = total > 0 ? Math.round((count / total) * 100) : 0;
  return (
    <div className="flex items-center gap-3 group" aria-label={`${label}: ${count} recensioni (${pct}%)`}>
      <span className="text-xs font-medium text-[#FF6B2B] w-12 shrink-0 text-right">
        {label}
      </span>
      <div className="flex-1 h-2 rounded-full bg-[#1A1200]/8 overflow-hidden">
        <div
          className="h-full rounded-full bg-[#FF6B2B] transition-all"
          style={{ width: `${pct}%` }}
        />
      </div>
      <span className="text-xs text-[#1A1200]/40 w-8 shrink-0">{count}</span>
    </div>
  );
}

export default async function RecensioniPage({ params }: { params: { id: string } }) {
  const product = getProductById(Number(params.id));
  if (!product) notFound();

  const reviews = (await sql`
    SELECT id, product_id, product_name, username, stars, body,
           publish_date::text, created_at::text
    FROM reviews
    WHERE product_id = ${product.id}
      AND is_published = TRUE
    ORDER BY publish_date DESC, id DESC
  `) as Review[];

  const total = reviews.length;
  const avg = total > 0
    ? Math.round((reviews.reduce((s, r) => s + r.stars, 0) / total) * 10) / 10
    : 0;

  // Distribuzione per stelle
  const dist = [5, 4, 3, 2, 1].map((star) => ({
    star,
    count: reviews.filter((r) => r.stars === star).length,
  }));

  return (
    <div
      className="min-h-screen bg-[#FFF8F0] pt-24 pb-24"
      itemScope
      itemType="https://schema.org/Product"
    >
      {/* Meta nascosta per Schema.org */}
      <meta itemProp="name" content={product.nome_modello} />

      {/* ─── HEADER ──────────────────────────────────────────── */}
      <header className="mx-auto max-w-5xl px-6 mb-14">
        {/* Breadcrumb */}
        <nav className="flex items-center gap-2 text-xs text-[#1A1200]/35 mb-8">
          <Link href="/" className="hover:text-[#FF6B2B] transition-colors">Home</Link>
          <span>/</span>
          <Link href="/catalogo" className="hover:text-[#FF6B2B] transition-colors">Catalogo</Link>
          <span>/</span>
          <Link href={`/prodotto/${product.id}`} className="hover:text-[#FF6B2B] transition-colors">
            {product.nome_modello}
          </Link>
          <span>/</span>
          <span className="text-[#1A1200]/55">Recensioni</span>
        </nav>

        {/* Titolo */}
        <div className="flex flex-col sm:flex-row sm:items-end sm:justify-between gap-4">
          <div>
            <p className="text-[11px] font-semibold uppercase tracking-[0.3em] text-[#FF6B2B] mb-2">
              Solara Eyewear
            </p>
            <h1 className="font-playfair text-3xl font-bold tracking-tight text-[#1A1200]/90 md:text-4xl">
              Recensioni — {product.nome_modello}
            </h1>
          </div>
          <Link
            href={`/prodotto/${product.id}`}
            className="inline-flex items-center gap-2 self-start sm:self-auto shrink-0 rounded-full border border-[#1A1200]/12 px-5 py-2.5 text-sm font-medium text-[#1A1200]/55 transition-all hover:border-[#FF6B2B] hover:text-[#FF6B2B]"
          >
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" className="w-4 h-4">
              <path fillRule="evenodd" d="M17 10a.75.75 0 01-.75.75H5.612l4.158 3.96a.75.75 0 11-1.04 1.08l-5.5-5.25a.75.75 0 010-1.08l5.5-5.25a.75.75 0 111.04 1.08L5.612 9.25H16.25A.75.75 0 0117 10z" clipRule="evenodd" />
            </svg>
            Torna al prodotto
          </Link>
        </div>

        {/* Divisore */}
        <div className="mt-8 h-px bg-[#1A1200]/6" />
      </header>

      {/* ─── BODY ────────────────────────────────────────────── */}
      <main
        className="mx-auto max-w-5xl px-6"
        data-section="reviews"
        data-product-id={product.id}
        data-product-name={product.nome_modello}
      >
        {total === 0 ? (
          <p className="text-[#1A1200]/40 italic text-sm">
            Nessuna recensione ancora disponibile per questo modello.
          </p>
        ) : (
          <div className="flex flex-col lg:flex-row gap-12 lg:gap-16">

            {/* ─── SIDEBAR STATS (sticky) ─────────────────────── */}
            <aside
              className="lg:w-64 shrink-0"
              aria-label="Riepilogo valutazioni"
              data-average-stars={avg}
              data-total-reviews={total}
            >
              <div className="lg:sticky lg:top-28 rounded-2xl border border-[#1A1200]/6 bg-white/60 backdrop-blur-sm p-6 shadow-[0_2px_24px_rgba(26,18,0,0.04)]">
                {/* Media grande */}
                <div className="flex flex-col items-center text-center mb-6 pb-6 border-b border-[#1A1200]/6">
                  <span className="font-playfair text-6xl font-bold text-[#1A1200]/90 leading-none mb-2">
                    {avg.toFixed(1)}
                  </span>
                  <Stars value={avg} size={22} />
                  <p className="mt-2 text-xs text-[#1A1200]/40">
                    su {total} {total === 1 ? "recensione" : "recensioni"}
                  </p>
                </div>

                {/* Distribuzione stelle */}
                <div className="space-y-2.5" data-stars-distribution>
                  {dist.map((d) => (
                    <StarBar
                      key={d.star}
                      label={`${d.star} ★`}
                      count={d.count}
                      total={total}
                    />
                  ))}
                </div>

                {/* Back to product */}
                <div className="mt-6 pt-6 border-t border-[#1A1200]/6">
                  <Link
                    href={`/prodotto/${product.id}`}
                    className="block w-full text-center rounded-full bg-[#FF6B2B] px-4 py-3 text-sm font-semibold text-white shadow-[0_0_20px_#FF6B2B40] transition-all hover:shadow-[0_0_28px_#FF6B2B66] hover:scale-[1.02]"
                  >
                    Vedi il prodotto
                  </Link>
                </div>
              </div>
            </aside>

            {/* ─── LISTA RECENSIONI ───────────────────────────── */}
            <section
              className="flex-1 min-w-0"
              aria-label="Lista recensioni"
              itemScope
              itemType="https://schema.org/AggregateRating"
            >
              {/* AggregateRating nascosta ma parsabile */}
              <meta itemProp="ratingValue" content={avg.toFixed(1)} />
              <meta itemProp="reviewCount" content={String(total)} />
              <meta itemProp="bestRating" content="5" />
              <meta itemProp="worstRating" content="1" />

              <ol
                className="space-y-5"
                data-reviews-list
                aria-label={`${total} recensioni per ${product.nome_modello}`}
              >
                {reviews.map((review) => (
                  <li key={review.id}>
                    <article
                      className="rounded-2xl border border-[#1A1200]/6 bg-white/50 p-6 transition-shadow hover:shadow-[0_4px_20px_rgba(26,18,0,0.06)]"
                      data-review-id={review.id}
                      data-product-id={review.product_id}
                      data-product-name={review.product_name}
                      data-stars={review.stars}
                      itemScope
                      itemType="https://schema.org/Review"
                    >
                      {/* Riga superiore */}
                      <div className="flex items-start justify-between gap-4 mb-4">
                        <div className="flex items-center gap-3">
                          {/* Avatar lettera */}
                          <div
                            className="w-9 h-9 rounded-full flex items-center justify-center text-sm font-bold text-white shrink-0"
                            style={{
                              background: `hsl(${(review.username.charCodeAt(0) * 37) % 360}, 55%, 55%)`,
                            }}
                            aria-hidden="true"
                          >
                            {review.username.charAt(0).toUpperCase()}
                          </div>
                          <div>
                            <span
                              className="block font-semibold text-[#1A1200]/80 text-sm leading-tight"
                              data-field="username"
                              itemProp="author"
                              itemScope
                              itemType="https://schema.org/Person"
                            >
                              <span itemProp="name">{review.username}</span>
                            </span>
                            <Stars value={review.stars} size={15} />
                          </div>
                        </div>

                        <time
                          className="text-[11px] text-[#1A1200]/30 shrink-0 mt-0.5"
                          dateTime={review.publish_date}
                          data-field="date"
                          itemProp="datePublished"
                        >
                          {new Date(review.publish_date).toLocaleDateString("it-IT", {
                            day: "numeric",
                            month: "long",
                            year: "numeric",
                          })}
                        </time>
                      </div>

                      {/* Corpo recensione */}
                      <p
                        className="text-sm text-[#1A1200]/60 leading-relaxed"
                        data-field="body"
                        itemProp="reviewBody"
                      >
                        {review.body}
                      </p>

                      {/* Rating inline nascosto per Schema.org */}
                      <div
                        itemProp="reviewRating"
                        itemScope
                        itemType="https://schema.org/Rating"
                        className="hidden"
                      >
                        <meta itemProp="ratingValue" content={String(review.stars)} />
                        <meta itemProp="bestRating" content="5" />
                      </div>
                    </article>
                  </li>
                ))}
              </ol>

              {/* Footer conteggio */}
              <p className="mt-8 text-center text-xs text-[#1A1200]/30">
                {total} {total === 1 ? "recensione" : "recensioni"} per{" "}
                <span className="font-medium text-[#1A1200]/45">{product.nome_modello}</span>
              </p>
            </section>
          </div>
        )}
      </main>
    </div>
  );
}
