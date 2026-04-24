"use client";

import { motion } from "framer-motion";
import { PRODUCTS } from "@/data/products";

/* ── Plan data ─────────────────────────────────────── */
interface Plan {
  name: string;
  price: string;
  description: string;
  badge?: string;
  features: string[];
  cta: string;
  highlighted: boolean;
}

const prices = PRODUCTS.map((p) => p.prezzoNumero);
const minPrice = Math.min(...prices);
const midPrice = [...prices].sort((a, b) => a - b)[Math.floor(prices.length / 2)];

const PLANS: Plan[] = [
  {
    name: "Solara Classic",
    price: `da ${minPrice}€`,
    description: "Stile senza tempo, protezione garantita.",
    features: [
      "Lenti UV400",
      "Montatura in acetato",
      "Custodia in microfibra",
      "Garanzia 2 anni",
    ],
    cta: "Scegli Classic",
    highlighted: false,
  },
  {
    name: "Solara Prestige",
    price: `da ${midPrice}€`,
    description: "L'esperienza completa. Ogni dettaglio, curato.",
    badge: "Best seller estate",
    features: [
      "Tutto di Classic +",
      "Lenti polarizzate grado 3",
      "Montatura titanio ultraleggera",
      "Incisione personalizzata",
      "Custodia rigida in ecopelle",
      "Spedizione express",
    ],
    cta: "Scegli Prestige",
    highlighted: true,
  },
];

const CheckIcon = () => (
  <svg
    width="16"
    height="16"
    viewBox="0 0 16 16"
    fill="none"
    className="mt-0.5 shrink-0 text-sea"
  >
    <path
      d="M3.5 8.5L6.5 11.5L12.5 5"
      stroke="currentColor"
      strokeWidth="1.5"
      strokeLinecap="round"
      strokeLinejoin="round"
    />
  </svg>
);

const EASE: [number, number, number, number] = [0.25, 0.1, 0.25, 1];

const cardVariants = {
  hidden: { opacity: 0, y: 40 },
  visible: (i: number) => ({
    opacity: 1,
    y: 0,
    transition: { delay: i * 0.2, duration: 0.6, ease: EASE },
  }),
};

export default function Pricing() {
  return (
    <section id="pricing" className="bg-sand px-6 py-32">
      <div className="mx-auto max-w-5xl">
        {/* Section heading */}
        <motion.div
          className="mb-16 text-center"
          initial={{ opacity: 0, y: 30 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true, margin: "-80px" }}
          transition={{ duration: 0.7, ease: [0.25, 0.1, 0.25, 1] }}
        >
          <h2 className="font-playfair text-5xl font-bold tracking-tighter text-warm/90 md:text-6xl">
            Scegli il tuo stile.
          </h2>
          <p className="mx-auto mt-5 max-w-xl text-warm/55">
            Due collezioni, un unico standard di eccellenza.
          </p>
        </motion.div>

        {/* Cards */}
        <div className="grid gap-8 md:grid-cols-2">
          {PLANS.map((plan, i) => (
            <motion.div
              key={plan.name}
              custom={i}
              variants={cardVariants}
              initial="hidden"
              whileInView="visible"
              viewport={{ once: true, margin: "-60px" }}
              className={`relative flex flex-col rounded-2xl p-8 md:p-10 transition-shadow duration-300 ${
                plan.highlighted
                  ? "border border-accent bg-card-bg shadow-[0_0_40px_rgba(255,107,43,0.08)]"
                  : "border border-warm/10 bg-sand"
              }`}
            >
              {/* Badge */}
              {plan.badge && (
                <span className="absolute -top-3 left-8 rounded-full bg-accent px-4 py-1 text-xs font-semibold tracking-wide text-white">
                  {plan.badge}
                </span>
              )}

              <h3 className="font-playfair text-2xl font-bold tracking-tight text-warm/90">
                {plan.name}
              </h3>
              <p className="mt-2 text-sm text-warm/55">{plan.description}</p>

              {/* Price */}
              <div className="mt-6 flex items-baseline gap-1">
                <span className="font-playfair text-5xl font-bold tracking-tight text-warm/90">
                  {plan.price}
                </span>
              </div>

              {/* Features list */}
              <ul className="mt-8 flex flex-col gap-3 flex-1">
                {plan.features.map((feat) => (
                  <li
                    key={feat}
                    className="flex items-start gap-3 text-sm text-warm/70"
                  >
                    <CheckIcon />
                    {feat}
                  </li>
                ))}
              </ul>

              {/* CTA button */}
              <a
                href="#"
                className={`mt-10 block rounded-full px-8 py-4 text-center font-body text-sm font-semibold transition-all duration-300 ${
                  plan.highlighted
                    ? "bg-accent text-white shadow-[0_0_28px_#FF6B2B55] hover:scale-[1.02] hover:shadow-[0_0_36px_#FFD16688]"
                    : "border border-warm/80 text-warm/80 hover:bg-warm/5"
                }`}
              >
                {plan.cta}
              </a>
            </motion.div>
          ))}
        </div>
      </div>
    </section>
  );
}
