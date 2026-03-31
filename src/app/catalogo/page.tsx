"use client";

import { motion } from "framer-motion";
import Image from "next/image";
import Link from "next/link";
import { PRODUCTS } from "@/data/products";

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

export default function CatalogoPage() {
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
                {/* Image container */}
                <div className="relative aspect-square overflow-hidden rounded-2xl bg-[#F5EDE3] border border-warm/5">
                  <Image
                    src={product.immagine}
                    alt={product.nome_modello}
                    fill
                    className="object-contain p-6 transition-transform duration-700 ease-out group-hover:scale-110"
                    sizes="(max-width: 640px) 100vw, (max-width: 1024px) 50vw, 25vw"
                  />

                  {/* Hover overlay */}
                  <div className="absolute inset-0 flex items-end justify-center pb-6 opacity-0 transition-opacity duration-300 group-hover:opacity-100">
                    <span className="rounded-full bg-warm/90 px-5 py-2 text-xs font-semibold tracking-wide text-sand">
                      Scopri →
                    </span>
                  </div>

                  {/* Category tag */}
                  <span className="absolute top-4 left-4 rounded-full bg-sand/80 backdrop-blur-sm px-3 py-1 text-[10px] font-semibold uppercase tracking-[0.15em] text-warm/50">
                    {product.categoria}
                  </span>
                </div>

                {/* Info */}
                <div className="mt-4 px-1">
                  <h3 className="font-playfair text-lg font-bold tracking-tight text-warm/85 group-hover:text-accent transition-colors duration-300">
                    {product.nome_modello}
                  </h3>
                  <div className="mt-1.5 flex items-center justify-between">
                    <span className="text-sm text-warm/50">
                      {product.montatura}
                    </span>
                    <span className="font-playfair text-lg font-bold text-warm/80">
                      {product.prezzo}
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
