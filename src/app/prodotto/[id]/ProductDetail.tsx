"use client";

import { motion } from "framer-motion";
import Image from "next/image";
import Link from "next/link";
import { Product, PRODUCTS } from "@/data/products";
import { useMemo, useState } from "react";

const EASE: [number, number, number, number] = [0.25, 0.1, 0.25, 1];

function getRecommendations(excludeId: number): Product[] {
  const filtered = PRODUCTS.filter((p) => p.id !== excludeId);
  // Deterministic shuffle based on excludeId so it's consistent per product
  const shuffled = [...filtered].sort(
    (a, b) => ((a.id * 7 + excludeId * 3) % 10) - ((b.id * 7 + excludeId * 3) % 10)
  );
  return shuffled.slice(0, 5);
}

export default function ProductDetail({ product }: { product: Product }) {
  const recommended = useMemo(
    () => getRecommendations(product.id),
    [product.id]
  );
  const [activeIdx, setActiveIdx] = useState(0);
  const immagini = product.immagini;

  const goPrev = () => setActiveIdx((i) => (i - 1 + immagini.length) % immagini.length);
  const goNext = () => setActiveIdx((i) => (i + 1) % immagini.length);

  const viste = ["Principale", "Frontale aperta", "Frontale chiusa", "Laterale"];

  const specs = [
    { label: "Montatura", value: product.montatura },
    { label: "Lenti", value: product.lenti },
    { label: "Vestibilità", value: product.geofit },
    { label: "Categoria", value: product.categoria },
  ];

  return (
    <div className="bg-sand pt-24 pb-20">
      {/* Breadcrumb */}
      <div className="mx-auto max-w-7xl px-6 mb-8">
        <motion.nav
          className="flex items-center gap-2 text-xs text-warm/40"
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ duration: 0.5 }}
        >
          <Link href="/" className="hover:text-accent transition-colors">
            Home
          </Link>
          <span>/</span>
          <Link href="/catalogo" className="hover:text-accent transition-colors">
            Catalogo
          </Link>
          <span>/</span>
          <span className="text-warm/60">{product.nome_modello}</span>
        </motion.nav>
      </div>

      {/* Product hero */}
      <div className="mx-auto max-w-7xl px-6">
        <div className="grid gap-12 lg:grid-cols-2 lg:gap-16">
          {/* Image carousel */}
          <motion.div
            className="flex flex-col gap-4"
            initial={{ opacity: 0, x: -40 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ duration: 0.7, ease: EASE }}
          >
            {/* Main image */}
            <div className="relative aspect-square overflow-hidden rounded-3xl bg-[#F5EDE3] border border-warm/5">
              {immagini.map((src, i) => (
                <Image
                  key={src}
                  src={src}
                  alt={`${product.nome_modello} — ${viste[i] ?? `Vista ${i + 1}`}`}
                  fill
                  className={`object-contain p-10 md:p-16 transition-opacity duration-400 ${
                    i === activeIdx ? "opacity-100" : "opacity-0"
                  }`}
                  sizes="(max-width: 1024px) 100vw, 50vw"
                  priority={i === 0}
                />
              ))}

              {/* Category badge */}
              <span className="absolute top-6 left-6 rounded-full bg-sand/80 backdrop-blur-sm px-4 py-1.5 text-[11px] font-semibold uppercase tracking-[0.15em] text-warm/50 z-10">
                {product.categoria}
              </span>

              {/* Vista label */}
              <span className="absolute bottom-6 left-0 right-0 text-center text-[11px] font-semibold uppercase tracking-[0.2em] text-warm/40 z-10">
                {viste[activeIdx] ?? `Vista ${activeIdx + 1}`}
              </span>

              {/* Prev / Next arrows */}
              <button
                onClick={goPrev}
                aria-label="Immagine precedente"
                className="absolute left-4 top-1/2 -translate-y-1/2 z-10 flex h-9 w-9 items-center justify-center rounded-full bg-sand/80 backdrop-blur-sm border border-warm/10 text-warm/60 shadow-sm transition hover:bg-sand hover:text-accent"
              >
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" className="w-4 h-4">
                  <path fillRule="evenodd" d="M12.79 5.23a.75.75 0 01-.02 1.06L8.832 10l3.938 3.71a.75.75 0 11-1.04 1.08l-4.5-4.25a.75.75 0 010-1.08l4.5-4.25a.75.75 0 011.06.02z" clipRule="evenodd" />
                </svg>
              </button>
              <button
                onClick={goNext}
                aria-label="Immagine successiva"
                className="absolute right-4 top-1/2 -translate-y-1/2 z-10 flex h-9 w-9 items-center justify-center rounded-full bg-sand/80 backdrop-blur-sm border border-warm/10 text-warm/60 shadow-sm transition hover:bg-sand hover:text-accent"
              >
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" className="w-4 h-4">
                  <path fillRule="evenodd" d="M7.21 14.77a.75.75 0 01.02-1.06L11.168 10 7.23 6.29a.75.75 0 111.04-1.08l4.5 4.25a.75.75 0 010 1.08l-4.5 4.25a.75.75 0 01-1.06-.02z" clipRule="evenodd" />
                </svg>
              </button>
            </div>

            {/* Thumbnail strip */}
            <div className="flex gap-3 justify-center">
              {immagini.map((src, i) => (
                <button
                  key={src}
                  onClick={() => setActiveIdx(i)}
                  aria-label={viste[i] ?? `Vista ${i + 1}`}
                  className={`relative h-16 w-16 flex-shrink-0 overflow-hidden rounded-xl border-2 transition-all duration-200 bg-[#F5EDE3] ${
                    i === activeIdx
                      ? "border-accent shadow-[0_0_12px_#FF6B2B44]"
                      : "border-warm/10 hover:border-warm/30"
                  }`}
                >
                  <Image
                    src={src}
                    alt={viste[i] ?? `Vista ${i + 1}`}
                    fill
                    className="object-contain p-2"
                    sizes="64px"
                  />
                </button>
              ))}
            </div>
          </motion.div>

          {/* Details */}
          <motion.div
            className="flex flex-col justify-center"
            initial={{ opacity: 0, x: 40 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ duration: 0.7, ease: EASE, delay: 0.15 }}
          >
            <p className="text-xs font-semibold uppercase tracking-[0.3em] text-accent mb-3">
              Collezione Solara
            </p>

            <h1 className="font-playfair text-4xl font-bold tracking-tighter text-warm/90 md:text-5xl lg:text-6xl">
              {product.nome_modello}
            </h1>

            <div className="mt-6 flex items-baseline gap-3">
              <span className="font-playfair text-4xl font-bold text-warm/90 md:text-5xl">
                {product.prezzo}
              </span>
            </div>

            {/* Specs grid */}
            <div className="mt-10 grid grid-cols-2 gap-4">
              {specs.map((spec) => (
                <div
                  key={spec.label}
                  className="rounded-xl border border-warm/8 bg-card-bg/50 p-4"
                >
                  <p className="text-[10px] font-semibold uppercase tracking-[0.2em] text-warm/35 mb-1">
                    {spec.label}
                  </p>
                  <p className="text-sm font-medium text-warm/75">
                    {spec.value}
                  </p>
                </div>
              ))}
            </div>

            {/* CTA */}
            <div className="mt-10 flex flex-col gap-3 sm:flex-row">
              <button className="rounded-full bg-accent px-10 py-4 font-body text-sm font-semibold text-white shadow-[0_0_28px_#FF6B2B55] transition-all duration-300 hover:scale-[1.02] hover:shadow-[0_0_36px_#FFD16688]">
                Aggiungi al carrello
              </button>
              <Link
                href="/catalogo"
                className="rounded-full border border-warm/15 px-8 py-4 text-center text-sm font-medium text-warm/60 transition-colors hover:border-accent hover:text-accent"
              >
                ← Torna al catalogo
              </Link>
            </div>
          </motion.div>
        </div>

        {/* Description */}
        <motion.div
          className="mt-20 mx-auto max-w-4xl"
          initial={{ opacity: 0, y: 30 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.6 }}
        >
          <h2 className="font-playfair text-2xl font-bold tracking-tight text-warm/85 mb-6">
            Dettagli
          </h2>
          <div className="h-px w-16 bg-sun/60 mb-8" />
          <p className="text-warm/60 leading-relaxed text-base">
            {product.descrizione}
          </p>
        </motion.div>
      </div>

      {/* Recommendations */}
      <section className="mt-28 mx-auto max-w-7xl px-6">
        <motion.div
          initial={{ opacity: 0, y: 30 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.6 }}
        >
          <div className="flex items-center gap-4 mb-12">
            <div className="h-px flex-1 bg-warm/8" />
            <h2 className="font-playfair text-3xl font-bold tracking-tighter text-warm/85 md:text-4xl whitespace-nowrap">
              Vedi anche
            </h2>
            <div className="h-px flex-1 bg-warm/8" />
          </div>
        </motion.div>

        <div className="grid gap-6 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-5">
          {recommended.map((rec, i) => (
            <motion.div
              key={rec.id}
              initial={{ opacity: 0, y: 30 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ delay: i * 0.08, duration: 0.5, ease: EASE }}
            >
              <Link
                href={`/prodotto/${rec.id}`}
                className="group block"
              >
                <div className="relative aspect-square overflow-hidden rounded-2xl bg-[#F5EDE3] border border-warm/5">
                  <Image
                    src={rec.immagine}
                    alt={rec.nome_modello}
                    fill
                    className="object-contain p-4 transition-transform duration-500 group-hover:scale-110"
                    sizes="(max-width: 640px) 50vw, 20vw"
                  />
                </div>
                <div className="mt-3 px-1">
                  <h3 className="text-sm font-bold text-warm/80 group-hover:text-accent transition-colors duration-300 truncate">
                    {rec.nome_modello}
                  </h3>
                  <p className="mt-1 font-playfair text-base font-bold text-warm/70">
                    {rec.prezzo}
                  </p>
                </div>
              </Link>
            </motion.div>
          ))}
        </div>
      </section>
    </div>
  );
}
