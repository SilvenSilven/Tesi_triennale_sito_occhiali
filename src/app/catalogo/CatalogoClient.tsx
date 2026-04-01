"use client";

import { motion } from "framer-motion";
import Image from "next/image";
import Link from "next/link";
import { useRef, useState, useCallback } from "react";
import { PRODUCTS } from "@/data/products";

/** Stelle stile Amazon: riempite, metà, vuote */
function StarRating({ stars, size = "md" }: { stars: number; size?: "sm" | "md" | "lg" }) {
  const sz = size === "sm" ? "w-3.5 h-3.5" : size === "lg" ? "w-6 h-6" : "w-5 h-5";
  return (
    <span
      className="inline-flex items-center gap-0.5"
      aria-label={`${stars} stelle su 5`}
      data-stars={stars}
    >
      {Array.from({ length: 5 }, (_, i) => {
        const filled = stars >= i + 1;
        const half = !filled && stars >= i + 0.5;
        return (
          <svg key={i} className={`${sz} flex-shrink-0`} viewBox="0 0 20 20" aria-hidden="true">
            {half ? (
              <>
                <defs>
                  <linearGradient id={`half-cat-${i}`}>
                    <stop offset="50%" stopColor="#FF6B2B" />
                    <stop offset="50%" stopColor="#d1c4b8" />
                  </linearGradient>
                </defs>
                <path
                  fill={`url(#half-cat-${i})`}
                  d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"
                />
              </>
            ) : (
              <path
                fill={filled ? "#FF6B2B" : "#d1c4b8"}
                d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"
              />
            )}
          </svg>
        );
      })}
    </span>
  );
}

const EASE: [number, number, number, number] = [0.25, 0.1, 0.25, 1];

const cardVariants = {
  hidden: { opacity: 0, y: 50, scale: 0.97 },
  visible: (i: number) => ({
    opacity: 1,
    y: 0,
    scale: 1,
    transition: { delay: i * 0.08, duration: 0.6, ease: EASE },
  }),
};

function HoverCarousel({
  immagini,
  nome_modello,
}: {
  immagini: string[];
  nome_modello: string;
}) {
  const [activeIdx, setActiveIdx] = useState(0);
  const intervalRef = useRef<ReturnType<typeof setInterval> | null>(null);

  const startCycle = useCallback(() => {
    setActiveIdx(0);
    let idx = 0;
    intervalRef.current = setInterval(() => {
      idx = (idx + 1) % immagini.length;
      setActiveIdx(idx);
    }, 600);
  }, [immagini.length]);

  const stopCycle = useCallback(() => {
    if (intervalRef.current) {
      clearInterval(intervalRef.current);
      intervalRef.current = null;
    }
    setActiveIdx(0);
  }, []);

  return (
    <div
      className="relative aspect-square overflow-hidden rounded-2xl bg-[#F5EDE3] border border-warm/5"
      onMouseEnter={startCycle}
      onMouseLeave={stopCycle}
      onTouchStart={startCycle}
      onTouchEnd={stopCycle}
    >
      {immagini.map((src, i) => (
        <Image
          key={src}
          src={src}
          alt={`${nome_modello} — vista ${i + 1}`}
          fill
          className={`object-contain p-6 transition-opacity duration-300 ${
            i === activeIdx ? "opacity-100" : "opacity-0"
          }`}
          sizes="(max-width: 640px) 100vw, (max-width: 1024px) 50vw, 25vw"
          priority={i === 0}
        />
      ))}

      {/* Dot indicators */}
      <div className="absolute bottom-3 left-0 right-0 flex justify-center gap-1.5 pointer-events-none">
        {immagini.map((_, i) => (
          <span
            key={i}
            className={`block h-1.5 w-1.5 rounded-full transition-all duration-300 ${
              i === activeIdx ? "bg-warm/70 scale-125" : "bg-warm/25"
            }`}
          />
        ))}
      </div>
    </div>
  );
}

export default function CatalogoClient({
  ratingsMap,
  pricesMap,
}: {
  ratingsMap: Record<number, { avg: number; count: number }>;
  pricesMap: Record<number, number>;
}) {
  return (
    <div className="bg-sand pt-28 pb-20">
      {/* Header */}
      <motion.div
        className="mx-auto max-w-6xl px-6 mb-16"
        initial={{ opacity: 0, y: 30 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.7, ease: EASE }}
      >
        <p className="text-xs font-semibold uppercase tracking-[0.3em] text-accent mb-4">
          Collezione 2026
        </p>
        <h1 className="font-playfair text-5xl font-bold tracking-tighter text-warm/90 md:text-7xl">
          Il Catalogo
        </h1>
        <p className="mt-5 max-w-xl text-warm/55 text-lg">
          Dieci modelli, un unico standard. Ogni paio racconta una storia
          di stile, artigianalità e protezione.
        </p>

        {/* Filter line */}
        <div className="mt-10 flex items-center gap-3">
          <div className="h-px flex-1 bg-warm/10" />
          <span className="text-xs tracking-[0.2em] text-warm/35 uppercase">
            {PRODUCTS.length} modelli
          </span>
          <div className="h-px flex-1 bg-warm/10" />
        </div>
      </motion.div>

      {/* Product Grid */}
      <div className="mx-auto max-w-7xl px-6">
        <div className="grid gap-x-6 gap-y-12 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4">
          {PRODUCTS.map((product, i) => (
            <motion.div
              key={product.id}
              custom={i}
              variants={cardVariants}
              initial="hidden"
              whileInView="visible"
              viewport={{ once: true, margin: "-40px" }}
            >
              <Link
                href={`/prodotto/${product.id}`}
                className="group block"
              >
                {/* Image carousel on hover */}
                <div className="relative">
                  <HoverCarousel
                    immagini={product.immagini}
                    nome_modello={product.nome_modello}
                  />

                  {/* Hover overlay */}
                  <div className="absolute inset-0 flex items-end justify-center pb-6 opacity-0 transition-opacity duration-300 group-hover:opacity-100 pointer-events-none">
                    <span className="rounded-full bg-warm/90 px-5 py-2 text-xs font-semibold tracking-wide text-sand">
                      Scopri →
                    </span>
                  </div>

                  {/* Category tag */}
                  <span className="absolute top-4 left-4 rounded-full bg-sand/80 backdrop-blur-sm px-3 py-1 text-[10px] font-semibold uppercase tracking-[0.15em] text-warm/50 pointer-events-none">
                    {product.categoria}
                  </span>
                </div>

                {/* Info */}
                <div className="mt-4 px-1">
                  <h3 className="font-playfair text-lg font-bold tracking-tight text-warm/85 group-hover:text-accent transition-colors duration-300">
                    {product.nome_modello}
                  </h3>
                  <div className="mt-1 flex items-center gap-1">
                    {ratingsMap[product.id] && ratingsMap[product.id].count > 0 ? (
                      <>
                        <StarRating stars={ratingsMap[product.id].avg} size="sm" />
                        <span className="text-xs text-warm/50 flex items-center pt-0.5">
                          {ratingsMap[product.id].avg.toFixed(1)}
                        </span>
                      </>
                    ) : (
                      <span className="text-[10px] text-warm/40 uppercase tracking-[0.1em] font-semibold pt-1">
                        Nuovo
                      </span>
                    )}
                  </div>
                  <div className="mt-2 flex items-center justify-between gap-3">
                    <span className="text-sm text-warm/50 truncate">
                      {product.montatura}
                    </span>
                    <span className="font-playfair text-lg font-bold text-warm/80 whitespace-nowrap shrink-0">
                      {pricesMap[product.id]
                        ? `€ ${pricesMap[product.id].toFixed(2)}`
                        : product.prezzo}
                    </span>
                  </div>
                </div>
              </Link>
            </motion.div>
          ))}
        </div>
      </div>
    </div>
  );
}
