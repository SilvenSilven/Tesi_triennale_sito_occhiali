"use client";

import { motion } from "framer-motion";

/* ── Feature data ──────────────────────────────────── */
interface Feature {
  icon: React.ReactNode;
  title: string;
  description: string;
}

const SunIcon = () => (
  <svg
    width="40"
    height="40"
    viewBox="0 0 40 40"
    fill="none"
    className="text-accent"
  >
    <circle cx="20" cy="20" r="8" stroke="currentColor" strokeWidth="2" />
    <path
      d="M20 4v4M20 32v4M4 20h4M32 20h4M8.93 8.93l2.83 2.83M28.24 28.24l2.83 2.83M8.93 31.07l2.83-2.83M28.24 11.76l2.83-2.83"
      stroke="currentColor"
      strokeWidth="2"
      strokeLinecap="round"
    />
  </svg>
);

const LensIcon = () => (
  <svg
    width="40"
    height="40"
    viewBox="0 0 40 40"
    fill="none"
    className="text-accent"
  >
    <ellipse
      cx="20"
      cy="20"
      rx="14"
      ry="10"
      stroke="currentColor"
      strokeWidth="2"
    />
    <path
      d="M12 16c2 4 8 6 14 2"
      stroke="currentColor"
      strokeWidth="1.5"
      strokeLinecap="round"
    />
    <circle cx="20" cy="20" r="3" fill="currentColor" opacity="0.2" />
  </svg>
);

const CraftIcon = () => (
  <svg
    width="40"
    height="40"
    viewBox="0 0 40 40"
    fill="none"
    className="text-accent"
  >
    <rect
      x="8"
      y="12"
      width="24"
      height="16"
      rx="3"
      stroke="currentColor"
      strokeWidth="2"
    />
    <path
      d="M14 12V9a6 6 0 0112 0v3"
      stroke="currentColor"
      strokeWidth="2"
      strokeLinecap="round"
    />
    <circle cx="20" cy="22" r="2" fill="currentColor" />
  </svg>
);

const FEATURES: Feature[] = [
  {
    icon: <SunIcon />,
    title: "Protezione UV 400",
    description:
      "Blocca il 100% dei raggi UVA e UVB. Protezione certificata per i tuoi occhi, dalla mattina al tramonto.",
  },
  {
    icon: <LensIcon />,
    title: "Lenti Polarizzate",
    description:
      "Eliminano il riflesso abbagliante su acqua e asfalto. Massima nitidezza, zero affaticamento visivo.",
  },
  {
    icon: <CraftIcon />,
    title: "Design Artigianale Italiano",
    description:
      "Acetato premium, cerniere a molla, ogni paio fatto a mano. L'eccellenza manifatturiera italiana.",
  },
];

/* ── Card animation variants ───────────────────────── */
const EASE: [number, number, number, number] = [0.25, 0.1, 0.25, 1];

const cardVariants = {
  hidden: { opacity: 0, y: 40 },
  visible: (i: number) => ({
    opacity: 1,
    y: 0,
    transition: { delay: i * 0.15, duration: 0.6, ease: EASE },
  }),
};

export default function Features() {
  return (
    <section id="features" className="bg-sand py-32 px-6">
      <div className="mx-auto max-w-6xl">
        {/* Section heading */}
        <motion.div
          className="mb-16 text-center"
          initial={{ opacity: 0, y: 30 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true, margin: "-80px" }}
          transition={{ duration: 0.7, ease: [0.25, 0.1, 0.25, 1] }}
        >
          <h2 className="font-playfair text-5xl font-bold tracking-tighter text-warm/90 md:text-6xl">
            Perché Solara.
          </h2>
          <p className="mx-auto mt-5 max-w-xl text-warm/55">
            Ogni dettaglio pensato per chi cerca l&apos;eccellenza sotto il sole
            del Mediterraneo.
          </p>
        </motion.div>

        {/* Cards grid */}
        <div className="grid gap-8 md:grid-cols-3">
          {FEATURES.map((feature, i) => (
            <motion.div
              key={feature.title}
              className="group rounded-2xl border border-sun/40 bg-card-bg p-8 transition-shadow duration-300 hover:shadow-lg hover:shadow-sun/10"
              custom={i}
              variants={cardVariants}
              initial="hidden"
              whileInView="visible"
              viewport={{ once: true, margin: "-60px" }}
            >
              <div className="mb-5 flex h-14 w-14 items-center justify-center rounded-xl bg-sand">
                {feature.icon}
              </div>
              <h3 className="font-playfair text-xl font-bold tracking-tight text-warm/90">
                {feature.title}
              </h3>
              <p className="mt-3 text-sm leading-relaxed text-warm/55">
                {feature.description}
              </p>
            </motion.div>
          ))}
        </div>
      </div>
    </section>
  );
}
