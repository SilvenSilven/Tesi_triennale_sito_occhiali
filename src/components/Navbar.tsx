"use client";

import { useState } from "react";
import { motion, AnimatePresence } from "framer-motion";

const NAV_LINKS = [
  { label: "Features", href: "#features" },
  { label: "Pricing", href: "#pricing" },
  { label: "Contatti", href: "#contatti" },
];

export default function Navbar() {
  const [open, setOpen] = useState(false);

  return (
    <nav className="fixed top-0 left-0 z-50 w-full bg-sand/70 backdrop-blur-md">
      <div className="mx-auto flex max-w-7xl items-center justify-between px-6 py-4 md:px-10">
        {/* Logo */}
        <a
          href="#"
          className="font-playfair text-xl font-bold tracking-[0.25em] text-warm/90 select-none"
        >
          SOLARA
        </a>

        {/* Desktop links */}
        <ul className="hidden gap-8 md:flex">
          {NAV_LINKS.map((link) => (
            <li key={link.href}>
              <a
                href={link.href}
                className="text-sm tracking-wide text-warm/60 transition-colors duration-300 hover:text-accent"
              >
                {link.label}
              </a>
            </li>
          ))}
        </ul>

        {/* Hamburger */}
        <button
          onClick={() => setOpen(!open)}
          className="relative z-50 flex h-8 w-8 flex-col items-center justify-center gap-[5px] md:hidden"
          aria-label="Menu"
        >
          <motion.span
            animate={open ? { rotate: 45, y: 7 } : { rotate: 0, y: 0 }}
            className="block h-[2px] w-5 bg-warm/80"
          />
          <motion.span
            animate={open ? { opacity: 0 } : { opacity: 1 }}
            className="block h-[2px] w-5 bg-warm/80"
          />
          <motion.span
            animate={open ? { rotate: -45, y: -7 } : { rotate: 0, y: 0 }}
            className="block h-[2px] w-5 bg-warm/80"
          />
        </button>
      </div>

      {/* Mobile drawer */}
      <AnimatePresence>
        {open && (
          <motion.div
            initial={{ height: 0, opacity: 0 }}
            animate={{ height: "auto", opacity: 1 }}
            exit={{ height: 0, opacity: 0 }}
            transition={{ duration: 0.35, ease: [0.25, 0.1, 0.25, 1] }}
            className="overflow-hidden border-t border-warm/5 bg-sand/95 backdrop-blur-lg md:hidden"
          >
            <ul className="flex flex-col items-center gap-6 py-8">
              {NAV_LINKS.map((link, i) => (
                <motion.li
                  key={link.href}
                  initial={{ opacity: 0, y: 10 }}
                  animate={{ opacity: 1, y: 0 }}
                  transition={{ delay: 0.08 * i }}
                >
                  <a
                    href={link.href}
                    onClick={() => setOpen(false)}
                    className="font-playfair text-lg tracking-wide text-warm/70 transition-colors duration-300 hover:text-accent"
                  >
                    {link.label}
                  </a>
                </motion.li>
              ))}
            </ul>
          </motion.div>
        )}
      </AnimatePresence>
    </nav>
  );
}
