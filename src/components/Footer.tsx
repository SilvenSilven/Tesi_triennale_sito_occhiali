"use client";

import { motion } from "framer-motion";
import Link from "next/link";

export default function Footer() {
  return (
    <footer className="bg-sand px-6 pb-10 pt-24">
      <div className="mx-auto max-w-6xl">
        {/* Decorative separator */}
        <div className="mx-auto mb-16 h-px w-24 bg-sun/60" />

        <div className="grid gap-12 md:grid-cols-3">
          {/* Brand column */}
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            transition={{ duration: 0.6 }}
          >
            <h3 className="font-playfair text-2xl font-bold tracking-[0.15em] text-warm/90">
              SOLARA
            </h3>
            <p className="mt-4 max-w-xs text-sm leading-relaxed text-warm/45">
              Occhiali da sole di lusso, ispirati dal Mediterraneo. L&apos;estate
              inizia dal tuo sguardo.
            </p>
          </motion.div>

          {/* Links column */}
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            transition={{ duration: 0.6, delay: 0.1 }}
          >
            <h4 className="text-xs font-semibold uppercase tracking-[0.2em] text-warm/40">
              Esplora
            </h4>
            <ul className="mt-4 flex flex-col gap-3">
              {[
                { label: "Home", href: "/" },
                { label: "Catalogo", href: "/catalogo" },
                { label: "Chi siamo", href: "/chi-siamo" },
              ].map((link) => (
                <li key={link.href}>
                  <Link
                    href={link.href}
                    className="text-sm text-warm/55 transition-colors duration-300 hover:text-accent"
                  >
                    {link.label}
                  </Link>
                </li>
              ))}
            </ul>
          </motion.div>

          {/* Contact column */}
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            transition={{ duration: 0.6, delay: 0.2 }}
          >
            <h4 className="text-xs font-semibold uppercase tracking-[0.2em] text-warm/40">
              Contatti
            </h4>
            <ul className="mt-4 flex flex-col gap-3 text-sm text-warm/55">
              <li>
                <a
                  href="mailto:info@solara.com"
                  className="transition-colors duration-300 hover:text-accent"
                >
                  info@solara.com
                </a>
              </li>
              <li>
                <a
                  href="tel:+390123456789"
                  className="transition-colors duration-300 hover:text-accent"
                >
                  +39 012 345 6789
                </a>
              </li>
              <li className="text-warm/35">
                Côte d&apos;Azur — Milano — Mykonos
              </li>
            </ul>
          </motion.div>
        </div>

        {/* Bottom bar */}
        <div className="mt-16 flex flex-col items-center justify-between gap-4 border-t border-warm/5 pt-8 text-xs text-warm/30 md:flex-row">
          <p>&copy; 2026 Solara. Tutti i diritti riservati.</p>
        </div>
      </div>
    </footer>
  );
}
