"use client";

import { motion, useScroll, useTransform } from "framer-motion";
import Image from "next/image";
import Link from "next/link";
import { useRef } from "react";
import { PRODUCTS } from "@/data/products";
import SolaraHero from "@/components/SolaraHero";

const EASE: [number, number, number, number] = [0.25, 0.1, 0.25, 1];

/* Featured products — pick 4 varied ones */
const FEATURED = [PRODUCTS[0], PRODUCTS[3], PRODUCTS[5], PRODUCTS[7]];

/* Perks row */
const PERKS = [
  {
    icon: (
      <svg width="28" height="28" viewBox="0 0 28 28" fill="none" className="text-accent">
        <circle cx="14" cy="14" r="6" stroke="currentColor" strokeWidth="1.5" />
        <path d="M14 3v3M14 22v3M3 14h3M22 14h3M6.34 6.34l2.12 2.12M19.54 19.54l2.12 2.12M6.34 21.66l2.12-2.12M19.54 8.46l2.12-2.12" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" />
      </svg>
    ),
    label: "UV400 Certificato",
  },
  {
    icon: (
      <svg width="28" height="28" viewBox="0 0 28 28" fill="none" className="text-accent">
        <path d="M4 14C7 8 10.5 5 14 5s7 3 10 9c-3 6-6.5 9-10 9S7 20 4 14Z" stroke="currentColor" strokeWidth="1.5" />
        <circle cx="14" cy="14" r="3" stroke="currentColor" strokeWidth="1.5" />
      </svg>
    ),
    label: "Lenti Polarizzate",
  },
  {
    icon: (
      <svg width="28" height="28" viewBox="0 0 28 28" fill="none" className="text-accent">
        <path d="M14 4l2 6h6l-5 4 2 6-5-4-5 4 2-6-5-4h6l2-6Z" stroke="currentColor" strokeWidth="1.5" strokeLinejoin="round" />
      </svg>
    ),
    label: "Made in Italy",
  },
  {
    icon: (
      <svg width="28" height="28" viewBox="0 0 28 28" fill="none" className="text-accent">
        <rect x="6" y="9" width="16" height="11" rx="2" stroke="currentColor" strokeWidth="1.5" />
        <path d="M10 9V7a4 4 0 018 0v2" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" />
      </svg>
    ),
    label: "Spedizione Gratuita",
  },
];

export default function HomeLanding() {
  const parallaxRef = useRef<HTMLDivElement>(null);
  const { scrollYProgress } = useScroll({
    target: parallaxRef,
    offset: ["start start", "end start"],
  });
  const heroY = useTransform(scrollYProgress, [0, 1], [0, 120]);
  const heroScale = useTransform(scrollYProgress, [0, 0.5], [1, 1.08]);

  return (
    <div className="bg-sand">
      {/* ── FRAME ANIMATION HERO ──────────────────────── */}
      <SolaraHero />

      {/* ── HERO ──────────────────────────────────────── */}
      <section
        ref={parallaxRef}
        className="relative min-h-screen flex flex-col items-center justify-center overflow-hidden pt-20"
      >
        {/* Background gradient mesh */}
        <div className="absolute inset-0 pointer-events-none">
          <div className="absolute top-0 right-0 w-[60vw] h-[60vw] rounded-full bg-gradient-to-br from-sun/15 via-accent/5 to-transparent blur-3xl" />
          <div className="absolute bottom-0 left-0 w-[50vw] h-[50vw] rounded-full bg-gradient-to-tr from-sea/8 via-transparent to-transparent blur-3xl" />
        </div>

        {/* Floating glasses mosaic */}
        <motion.div
          className="absolute inset-0 pointer-events-none opacity-[0.07]"
          style={{ y: heroY, scale: heroScale }}
        >
          {[1, 3, 6, 8, 10].map((id, i) => (
            <div
              key={id}
              className="absolute"
              style={{
                top: `${15 + (i * 17) % 60}%`,
                left: `${5 + (i * 23) % 85}%`,
                width: "clamp(120px, 15vw, 220px)",
                height: "clamp(120px, 15vw, 220px)",
                transform: `rotate(${-15 + i * 10}deg)`,
              }}
            >
              <Image
                src={`/products/${id}.webp`}
                alt=""
                fill
                className="object-contain"
                sizes="220px"
              />
            </div>
          ))}
        </motion.div>

        {/* Hero Content */}
        <div className="relative z-10 mx-auto max-w-5xl px-6 text-center">
          <motion.p
            className="text-xs font-semibold uppercase tracking-[0.4em] text-accent mb-6"
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.6, delay: 0.1 }}
          >
            Eyewear di lusso — Estate 2026
          </motion.p>

          <motion.h1
            className="font-playfair text-6xl font-bold tracking-tighter text-warm/90 leading-[0.92] sm:text-7xl md:text-8xl lg:text-9xl"
            initial={{ opacity: 0, y: 30 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.8, ease: EASE }}
          >
            Stile che
            <br />
            <span className="italic text-accent">protegge.</span>
          </motion.h1>

          <motion.p
            className="mx-auto mt-8 max-w-xl text-warm/50 text-lg md:text-xl leading-relaxed"
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.7, delay: 0.3 }}
          >
            Dieci modelli unici, una manifattura italiana impeccabile.
            Ogni paio di Solara è disegnato per illuminare il tuo sguardo.
          </motion.p>

          <motion.div
            className="mt-10 flex flex-col sm:flex-row items-center justify-center gap-4"
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.7, delay: 0.5 }}
          >
            <Link
              href="/catalogo"
              className="rounded-full bg-accent px-10 py-4 font-body text-sm font-semibold text-white shadow-[0_0_28px_#FF6B2B55] transition-all duration-300 hover:scale-[1.03] hover:shadow-[0_0_36px_#FFD16688]"
            >
              Esplora il catalogo →
            </Link>
            <Link
              href="/chi-siamo"
              className="rounded-full border border-warm/15 px-8 py-4 text-sm font-medium text-warm/60 transition-colors hover:border-accent hover:text-accent"
            >
              La nostra storia
            </Link>
          </motion.div>
        </div>

        {/* Scroll cue */}
        <motion.div
          className="absolute bottom-10 flex flex-col items-center gap-2"
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ delay: 1.2 }}
        >
          <span className="text-[10px] tracking-[0.25em] uppercase text-warm/30">
            Scorri
          </span>
          <motion.svg
            width="18"
            height="18"
            viewBox="0 0 18 18"
            fill="none"
            className="text-warm/25"
            animate={{ y: [0, 5, 0] }}
            transition={{ duration: 1.6, repeat: Infinity, ease: "easeInOut" }}
          >
            <path d="M4 7l5 5 5-5" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round" />
          </motion.svg>
        </motion.div>
      </section>

      {/* ── PERKS BAR ─────────────────────────────────── */}
      <section className="border-y border-warm/5 bg-card-bg/30 py-8">
        <div className="mx-auto max-w-6xl px-6">
          <div className="flex flex-wrap items-center justify-center gap-8 md:gap-16">
            {PERKS.map((perk, i) => (
              <motion.div
                key={perk.label}
                className="flex items-center gap-3"
                initial={{ opacity: 0, y: 10 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true }}
                transition={{ delay: i * 0.1, duration: 0.4 }}
              >
                {perk.icon}
                <span className="text-xs font-semibold tracking-wide text-warm/50 uppercase">
                  {perk.label}
                </span>
              </motion.div>
            ))}
          </div>
        </div>
      </section>

      {/* ── FEATURED PRODUCTS ─────────────────────────── */}
      <section className="py-28 px-6">
        <div className="mx-auto max-w-7xl">
          <motion.div
            className="text-center mb-16"
            initial={{ opacity: 0, y: 30 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true, margin: "-80px" }}
            transition={{ duration: 0.7, ease: EASE }}
          >
            <p className="text-xs font-semibold uppercase tracking-[0.3em] text-accent mb-4">
              Selezione
            </p>
            <h2 className="font-playfair text-5xl font-bold tracking-tighter text-warm/90 md:text-6xl">
              I nostri bestseller.
            </h2>
            <p className="mx-auto mt-5 max-w-xl text-warm/50">
              Quattro modelli che definiscono lo stile Solara. Scopri la collezione completa.
            </p>
          </motion.div>

          <div className="grid gap-8 sm:grid-cols-2 lg:grid-cols-4">
            {FEATURED.map((product, i) => (
              <motion.div
                key={product.id}
                initial={{ opacity: 0, y: 40 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true, margin: "-40px" }}
                transition={{ delay: i * 0.1, duration: 0.6, ease: EASE }}
              >
                <Link href={`/prodotto/${product.id}`} className="group block">
                  <div className="relative aspect-square overflow-hidden rounded-2xl bg-[#F5EDE3] border border-warm/5">
                    <Image
                      src={product.immagine}
                      alt={product.nome_modello}
                      fill
                      className="object-contain p-6 transition-transform duration-700 ease-out group-hover:scale-110"
                      sizes="(max-width: 640px) 100vw, (max-width: 1024px) 50vw, 25vw"
                    />
                    <div className="absolute inset-0 flex items-end justify-center pb-5 opacity-0 transition-opacity duration-300 group-hover:opacity-100">
                      <span className="rounded-full bg-warm/90 px-5 py-2 text-xs font-semibold tracking-wide text-sand">
                        Dettagli →
                      </span>
                    </div>
                    <span className="absolute top-4 left-4 rounded-full bg-sand/80 backdrop-blur-sm px-3 py-1 text-[10px] font-semibold uppercase tracking-[0.15em] text-warm/50">
                      {product.categoria}
                    </span>
                  </div>
                  <div className="mt-4 px-1">
                    <h3 className="font-playfair text-lg font-bold text-warm/85 group-hover:text-accent transition-colors duration-300">
                      {product.nome_modello}
                    </h3>
                    <div className="mt-1 flex items-center justify-between">
                      <span className="text-sm text-warm/45">{product.montatura}</span>
                      <span className="font-playfair text-lg font-bold text-warm/75">{product.prezzo}</span>
                    </div>
                  </div>
                </Link>
              </motion.div>
            ))}
          </div>

          <motion.div
            className="mt-14 text-center"
            initial={{ opacity: 0 }}
            whileInView={{ opacity: 1 }}
            viewport={{ once: true }}
            transition={{ delay: 0.3, duration: 0.5 }}
          >
            <Link
              href="/catalogo"
              className="inline-block rounded-full border border-warm/15 px-10 py-4 text-sm font-medium text-warm/60 transition-all hover:border-accent hover:text-accent hover:shadow-[0_0_20px_#FF6B2B22]"
            >
              Vedi tutta la collezione →
            </Link>
          </motion.div>
        </div>
      </section>

      {/* ── WHY SOLARA ────────────────────────────────── */}
      <section className="py-28 px-6 bg-gradient-to-b from-sand via-card-bg/20 to-sand">
        <div className="mx-auto max-w-6xl">
          <motion.div
            className="text-center mb-16"
            initial={{ opacity: 0, y: 30 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            transition={{ duration: 0.7 }}
          >
            <h2 className="font-playfair text-5xl font-bold tracking-tighter text-warm/90 md:text-6xl">
              Perché Solara.
            </h2>
            <p className="mx-auto mt-5 max-w-xl text-warm/50">
              Ogni dettaglio pensato per chi cerca l&apos;eccellenza sotto il sole.
            </p>
          </motion.div>

          <div className="grid gap-8 md:grid-cols-3">
            {[
              {
                icon: (
                  <svg width="40" height="40" viewBox="0 0 40 40" fill="none" className="text-accent">
                    <circle cx="20" cy="20" r="8" stroke="currentColor" strokeWidth="2" />
                    <path d="M20 4v4M20 32v4M4 20h4M32 20h4M8.93 8.93l2.83 2.83M28.24 28.24l2.83 2.83M8.93 31.07l2.83-2.83M28.24 11.76l2.83-2.83" stroke="currentColor" strokeWidth="2" strokeLinecap="round" />
                  </svg>
                ),
                title: "Protezione UV 400",
                desc: "Blocca il 100% dei raggi UVA e UVB. Protezione certificata per i tuoi occhi, dalla mattina al tramonto.",
              },
              {
                icon: (
                  <svg width="40" height="40" viewBox="0 0 40 40" fill="none" className="text-accent">
                    <ellipse cx="20" cy="20" rx="14" ry="10" stroke="currentColor" strokeWidth="2" />
                    <path d="M12 16c2 4 8 6 14 2" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" />
                    <circle cx="20" cy="20" r="3" fill="currentColor" opacity="0.2" />
                  </svg>
                ),
                title: "Lenti Polarizzate",
                desc: "Eliminano il riflesso abbagliante su acqua e asfalto. Massima nitidezza, zero affaticamento visivo.",
              },
              {
                icon: (
                  <svg width="40" height="40" viewBox="0 0 40 40" fill="none" className="text-accent">
                    <rect x="8" y="12" width="24" height="16" rx="3" stroke="currentColor" strokeWidth="2" />
                    <path d="M14 12V9a6 6 0 0112 0v3" stroke="currentColor" strokeWidth="2" strokeLinecap="round" />
                    <circle cx="20" cy="22" r="2" fill="currentColor" />
                  </svg>
                ),
                title: "Design Artigianale Italiano",
                desc: "Acetato premium, cerniere a molla, ogni paio fatto a mano. L'eccellenza manifatturiera italiana.",
              },
            ].map((feature, i) => (
              <motion.div
                key={feature.title}
                className="group rounded-2xl border border-sun/40 bg-card-bg p-8 transition-shadow duration-300 hover:shadow-lg hover:shadow-sun/10"
                initial={{ opacity: 0, y: 40 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true, margin: "-60px" }}
                transition={{ delay: i * 0.15, duration: 0.6, ease: EASE }}
              >
                <div className="mb-5 flex h-14 w-14 items-center justify-center rounded-xl bg-sand">
                  {feature.icon}
                </div>
                <h3 className="font-playfair text-xl font-bold tracking-tight text-warm/90">
                  {feature.title}
                </h3>
                <p className="mt-3 text-sm leading-relaxed text-warm/55">
                  {feature.desc}
                </p>
              </motion.div>
            ))}
          </div>
        </div>
      </section>

      {/* ── CTA BANNER ────────────────────────────────── */}
      <section className="py-24 px-6">
        <motion.div
          className="mx-auto max-w-4xl text-center"
          initial={{ opacity: 0, y: 30 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.7 }}
        >
          <h2 className="font-playfair text-4xl font-bold tracking-tighter text-warm/90 md:text-6xl">
            Trova il tuo modello.
          </h2>
          <p className="mx-auto mt-6 max-w-lg text-warm/50 text-lg">
            Dai classici aviator alle maschere sportive. C&apos;è un Solara
            per ogni personalità.
          </p>
          <Link
            href="/catalogo"
            className="mt-10 inline-block rounded-full bg-accent px-12 py-5 font-body text-sm font-semibold text-white shadow-[0_0_28px_#FF6B2B55] transition-all duration-300 hover:scale-[1.03] hover:shadow-[0_0_36px_#FFD16688]"
          >
            Sfoglia la collezione →
          </Link>
        </motion.div>
      </section>
    </div>
  );
}
