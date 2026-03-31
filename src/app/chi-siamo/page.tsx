"use client";

import { motion } from "framer-motion";
import Image from "next/image";

const EASE: [number, number, number, number] = [0.25, 0.1, 0.25, 1];

const values = [
  {
    title: "Artigianalità",
    description:
      "Ogni paio di occhiali Solara nasce dalla sapienza manifatturiera italiana. Selezioniamo personalmente ogni materiale, dall'acetato al titanio, per garantire una qualità che si sente al primo tocco.",
    icon: (
      <svg width="36" height="36" viewBox="0 0 36 36" fill="none" className="text-accent">
        <path d="M18 3L21.5 13H31L23.5 19.5L26 30L18 23.5L10 30L12.5 19.5L5 13H14.5L18 3Z" stroke="currentColor" strokeWidth="1.5" strokeLinejoin="round"/>
      </svg>
    ),
  },
  {
    title: "Protezione",
    description:
      "Lenti certificate UV400 e polarizzate di grado 3 in ogni modello premium. Proteggere i tuoi occhi è la nostra priorità assoluta, dalla mattina al tramonto.",
    icon: (
      <svg width="36" height="36" viewBox="0 0 36 36" fill="none" className="text-accent">
        <path d="M18 4C12 4 6 8 3 18C6 28 12 32 18 32C24 32 30 28 33 18C30 8 24 4 18 4Z" stroke="currentColor" strokeWidth="1.5"/>
        <circle cx="18" cy="18" r="5" stroke="currentColor" strokeWidth="1.5"/>
      </svg>
    ),
  },
  {
    title: "Sostenibilità",
    description:
      "Packaging riciclato, custodie in ecopelle e una filiera corta che riduce l'impatto ambientale. Crediamo in un lusso che rispetta il mondo che ci circonda.",
    icon: (
      <svg width="36" height="36" viewBox="0 0 36 36" fill="none" className="text-accent">
        <path d="M18 4C10 4 6 12 6 18C6 26 12 32 18 32C24 32 30 26 30 18" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round"/>
        <path d="M30 4L30 14H20" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round"/>
      </svg>
    ),
  },
];

const timeline = [
  { year: "2019", event: "Nasce l'idea Solara sulla costa amalfitana" },
  { year: "2020", event: "Primo prototipo in collaborazione con artigiani di Cadore" },
  { year: "2022", event: "Lancio della prima collezione con 4 modelli" },
  { year: "2024", event: "Espansione a 10 modelli e distribuzione in 12 paesi" },
  { year: "2026", event: "Nuova collezione estiva e apertura showroom Milano" },
];

export default function ChiSiamoPage() {
  return (
    <div className="bg-sand pt-28 pb-20">
      {/* Hero */}
      <section className="mx-auto max-w-6xl px-6 mb-24">
        <motion.div
          initial={{ opacity: 0, y: 30 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.7, ease: EASE }}
        >
          <p className="text-xs font-semibold uppercase tracking-[0.3em] text-accent mb-4">
            La nostra storia
          </p>
          <h1 className="font-playfair text-5xl font-bold tracking-tighter text-warm/90 md:text-7xl lg:text-8xl max-w-4xl">
            Nati dal sole del
            <br />
            <span className="italic text-accent">Mediterraneo.</span>
          </h1>
          <p className="mt-8 max-w-2xl text-warm/55 text-lg leading-relaxed">
            Solara nasce dall&apos;incontro tra la tradizione ottica italiana e
            un&apos;estetica contemporanea. Ogni paio di occhiali è un omaggio
            alla luce, al colore e all&apos;eleganza rilassata della vita sul mare.
          </p>
        </motion.div>
      </section>

      {/* Decorative image band */}
      <motion.section
        className="relative overflow-hidden mb-28"
        initial={{ opacity: 0 }}
        whileInView={{ opacity: 1 }}
        viewport={{ once: true }}
        transition={{ duration: 0.8 }}
      >
        <div className="flex gap-3 animate-marquee">
          {[1, 3, 5, 7, 10, 2, 6, 8, 4, 9].map((id, i) => (
            <div
              key={i}
              className="relative h-48 w-48 flex-shrink-0 overflow-hidden rounded-2xl bg-[#F5EDE3] border border-warm/5 md:h-64 md:w-64"
            >
              <Image
                src={`/products/${id}.webp`}
                alt=""
                fill
                className="object-contain p-4"
                sizes="256px"
              />
            </div>
          ))}
        </div>
      </motion.section>

      {/* Mission */}
      <section className="mx-auto max-w-6xl px-6 mb-28">
        <div className="grid gap-16 lg:grid-cols-2 items-center">
          <motion.div
            initial={{ opacity: 0, x: -30 }}
            whileInView={{ opacity: 1, x: 0 }}
            viewport={{ once: true }}
            transition={{ duration: 0.6 }}
          >
            <h2 className="font-playfair text-4xl font-bold tracking-tighter text-warm/90 md:text-5xl">
              La missione
            </h2>
            <div className="h-px w-16 bg-sun/60 mt-6 mb-8" />
            <p className="text-warm/60 leading-relaxed mb-6">
              Crediamo che un paio di occhiali da sole non sia solo un accessorio
              funzionale, ma un&apos;estensione della personalità. Per questo ogni
              modello Solara è progettato per essere unico: dal concept iniziale
              alla manifattura finale, nessun dettaglio è lasciato al caso.
            </p>
            <p className="text-warm/60 leading-relaxed">
              Il nostro laboratorio sul Lago di Cadore, nel cuore del distretto
              ottico italiano, unisce tecniche tradizionali e innovazione
              tecnologica per creare occhiali che durano nel tempo — nello stile
              e nella qualità.
            </p>
          </motion.div>

          <motion.div
            className="grid grid-cols-2 gap-4"
            initial={{ opacity: 0, x: 30 }}
            whileInView={{ opacity: 1, x: 0 }}
            viewport={{ once: true }}
            transition={{ duration: 0.6, delay: 0.15 }}
          >
            {[
              { number: "10", label: "Modelli unici" },
              { number: "12", label: "Paesi distribuiti" },
              { number: "100%", label: "Made in Italy" },
              { number: "UV400", label: "Protezione certificata" },
            ].map((stat) => (
              <div
                key={stat.label}
                className="rounded-2xl border border-warm/8 bg-card-bg/50 p-6 text-center"
              >
                <p className="font-playfair text-3xl font-bold text-accent">
                  {stat.number}
                </p>
                <p className="mt-2 text-xs tracking-wide text-warm/45">
                  {stat.label}
                </p>
              </div>
            ))}
          </motion.div>
        </div>
      </section>

      {/* Values */}
      <section className="mx-auto max-w-6xl px-6 mb-28">
        <motion.h2
          className="font-playfair text-4xl font-bold tracking-tighter text-warm/90 md:text-5xl text-center mb-16"
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.6 }}
        >
          I nostri valori
        </motion.h2>

        <div className="grid gap-8 md:grid-cols-3">
          {values.map((v, i) => (
            <motion.div
              key={v.title}
              className="rounded-2xl border border-sun/30 bg-card-bg/40 p-8"
              initial={{ opacity: 0, y: 30 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ delay: i * 0.12, duration: 0.5, ease: EASE }}
            >
              <div className="mb-5 flex h-14 w-14 items-center justify-center rounded-xl bg-sand">
                {v.icon}
              </div>
              <h3 className="font-playfair text-xl font-bold text-warm/85 mb-3">
                {v.title}
              </h3>
              <p className="text-sm text-warm/50 leading-relaxed">
                {v.description}
              </p>
            </motion.div>
          ))}
        </div>
      </section>

      {/* Timeline */}
      <section className="mx-auto max-w-3xl px-6">
        <motion.h2
          className="font-playfair text-4xl font-bold tracking-tighter text-warm/90 md:text-5xl text-center mb-16"
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.6 }}
        >
          Il nostro percorso
        </motion.h2>

        <div className="relative">
          {/* Vertical line */}
          <div className="absolute left-[22px] top-0 bottom-0 w-px bg-warm/10 md:left-1/2 md:-translate-x-px" />

          {timeline.map((item, i) => (
            <motion.div
              key={item.year}
              className="relative flex gap-6 mb-12 last:mb-0 md:even:flex-row-reverse md:gap-12"
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ delay: i * 0.1, duration: 0.5, ease: EASE }}
            >
              {/* Dot */}
              <div className="relative flex-shrink-0 w-11 flex items-start justify-center md:absolute md:left-1/2 md:-translate-x-1/2">
                <div className="h-3 w-3 rounded-full bg-accent mt-1.5 ring-4 ring-sand" />
              </div>

              {/* Content */}
              <div className="md:w-[calc(50%-2rem)]">
                <span className="font-playfair text-2xl font-bold text-accent">
                  {item.year}
                </span>
                <p className="mt-1 text-sm text-warm/60">
                  {item.event}
                </p>
              </div>
            </motion.div>
          ))}
        </div>
      </section>
    </div>
  );
}
