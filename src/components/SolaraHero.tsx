"use client";

import { useRef, useEffect, useState, useCallback } from "react";
import {
  motion,
  useScroll,
  useSpring,
  useTransform,
  useMotionValueEvent,
  AnimatePresence,
} from "framer-motion";

/* ── Constants ──────────────────────────────────────── */
const FIRST_FRAME = 28;
const LAST_FRAME = 191;
const TOTAL_FRAMES = LAST_FRAME - FIRST_FRAME + 1; // 164
const MAX_INDEX = TOTAL_FRAMES - 1; // 163

const FRAME_PATHS = Array.from({ length: TOTAL_FRAMES }, (_, i) => {
  const idx = String(i + FIRST_FRAME).padStart(3, "0");
  return `/frames/frame_${idx}_delay-0.041s.jpg`;
});

/* ── Narrative beats ────────────────────────────────── */
interface Beat {
  title: string;
  subtitle: string;
  start: number;
  end: number;
  align: "center" | "left" | "right";
  sizeClass: string;
  cta?: { label: string; href: string };
}

const BEATS: Beat[] = [
  {
    title: "L'ESTATE INIZIA QUI.",
    subtitle: "La luce perfetta. Il frame giusto. Il tuo momento.",
    start: 0.0,
    end: 0.2,
    align: "center",
    sizeClass: "text-5xl sm:text-7xl md:text-9xl",
  },
  {
    title: "LUCE FILTRATA.",
    subtitle:
      "Lenti polarizzate di grado 3. Il sole da un'altra prospettiva.",
    start: 0.25,
    end: 0.45,
    align: "left",
    sizeClass: "text-4xl sm:text-6xl md:text-8xl",
  },
  {
    title: "FATTO PER DURARE.",
    subtitle:
      "Acetato italiano. Montatura a vita. Stile senza compromessi.",
    start: 0.5,
    end: 0.7,
    align: "right",
    sizeClass: "text-4xl sm:text-6xl md:text-8xl",
  },
  {
    title: "IL TUO PROSSIMO ESTATE.",
    subtitle: "Scopri Solara. Ogni paio, una storia.",
    start: 0.75,
    end: 0.95,
    align: "center",
    sizeClass: "text-5xl sm:text-7xl md:text-9xl",
    cta: { label: "Scegli il tuo modello →", href: "/catalogo" },
  },
];

/* ── Loader ─────────────────────────────────────────── */
function Loader({ progress }: { progress: number }) {
  return (
    <motion.div
      className="fixed inset-0 z-40 flex flex-col items-center justify-center"
      style={{ background: "#FFF8F0" }}
      exit={{ opacity: 0 }}
      transition={{ duration: 0.6, ease: "easeInOut" }}
    >
      <motion.div
        className="mb-8 h-10 w-10 rounded-full border-[3px] border-[#FF6B2B]/20 border-t-[#FF6B2B]"
        animate={{ rotate: 360 }}
        transition={{ duration: 1, repeat: Infinity, ease: "linear" }}
      />
      <div className="h-[3px] w-48 overflow-hidden rounded-full bg-[#1A1200]/10">
        <motion.div
          className="h-full rounded-full"
          style={{ background: "#FFD166", width: `${progress}%` }}
        />
      </div>
      <p className="mt-4 text-xs tracking-widest text-[#1A1200]/40">
        CARICAMENTO
      </p>
    </motion.div>
  );
}

/* ── Beat overlay ───────────────────────────────────── */
function BeatOverlay({
  beat,
  scrollProgress,
}: {
  beat: Beat;
  scrollProgress: ReturnType<typeof useSpring>;
}) {
  const { start, end, align, sizeClass, title, subtitle, cta } = beat;

  const opacity = useTransform(
    scrollProgress,
    [start, start + 0.1, end - 0.1, end],
    [0, 1, 1, 0]
  );
  const y = useTransform(
    scrollProgress,
    [start, start + 0.1, end - 0.1, end],
    [20, 0, 0, -20]
  );

  const alignClass =
    align === "left"
      ? "items-start text-left pl-6 sm:pl-12 md:pl-24"
      : align === "right"
        ? "items-end text-right pr-6 sm:pr-12 md:pr-24"
        : "items-center text-center px-6";

  return (
    <motion.div
      className={`absolute inset-0 flex flex-col justify-center ${alignClass} pointer-events-none`}
      style={{ opacity, y }}
    >
      <h2
        className={`font-playfair font-bold tracking-tighter text-[#1A1200]/90 leading-[0.95] ${sizeClass}`}
      >
        {title}
      </h2>
      <p className="mt-4 max-w-md text-base text-[#1A1200]/60 sm:text-lg md:mt-6 md:max-w-xl md:text-xl">
        {subtitle}
      </p>
      {cta && (
        <a
          href={cta.href}
          className="pointer-events-auto mt-8 inline-block rounded-full px-8 py-4 text-sm font-semibold text-white shadow-[0_0_28px_#FF6B2B66] transition-all duration-300 hover:scale-[1.03] hover:shadow-[0_0_36px_#FFD16688] md:text-base"
          style={{ background: "#FF6B2B" }}
        >
          {cta.label}
        </a>
      )}
    </motion.div>
  );
}

/* ── Scroll indicator ──────────────────────────────── */
function ScrollIndicator({
  scrollProgress,
}: {
  scrollProgress: ReturnType<typeof useSpring>;
}) {
  const opacity = useTransform(scrollProgress, [0, 0.1], [1, 0]);

  return (
    <motion.div
      className="absolute bottom-8 left-1/2 -translate-x-1/2 flex flex-col items-center gap-2 pointer-events-none"
      style={{ opacity }}
    >
      <span className="text-xs tracking-[0.2em] text-[#1A1200]/40 uppercase">
        Scorri per scoprire
      </span>
      <motion.svg
        width="20"
        height="20"
        viewBox="0 0 20 20"
        fill="none"
        className="text-[#1A1200]/30"
        animate={{ y: [0, 6, 0] }}
        transition={{ duration: 1.6, repeat: Infinity, ease: "easeInOut" }}
      >
        <path
          d="M4 7l6 6 6-6"
          stroke="currentColor"
          strokeWidth="1.5"
          strokeLinecap="round"
          strokeLinejoin="round"
        />
      </motion.svg>
    </motion.div>
  );
}

/* ── Main component ────────────────────────────────── */
export default function SolaraHero() {
  const wrapperRef = useRef<HTMLDivElement>(null);
  const canvasRef = useRef<HTMLCanvasElement>(null);
  const imagesRef = useRef<HTMLImageElement[]>([]);
  const [loaded, setLoaded] = useState(false);
  const [loadProgress, setLoadProgress] = useState(0);
  const currentFrameRef = useRef(0);
  const rafRef = useRef<number>(0);

  /* Scroll tracking */
  const { scrollYProgress } = useScroll({
    target: wrapperRef,
    offset: ["start start", "end end"],
  });
  const smoothProgress = useSpring(scrollYProgress, {
    stiffness: 100,
    damping: 30,
  });

  /* Compute frame index from spring value */
  const frameIndex = useTransform(smoothProgress, (v: number) =>
    Math.min(MAX_INDEX, Math.max(0, Math.floor(v * MAX_INDEX)))
  );

  /* ── Preload images ─────────────────────────────── */
  useEffect(() => {
    let loadedCount = 0;
    const images: HTMLImageElement[] = [];
    let cancelled = false;

    FRAME_PATHS.forEach((src, i) => {
      const img = new Image();
      img.src = src;
      img.onload = () => {
        if (cancelled) return;
        loadedCount++;
        setLoadProgress(Math.round((loadedCount / TOTAL_FRAMES) * 100));
        if (loadedCount === TOTAL_FRAMES) {
          imagesRef.current = images;
          setLoaded(true);
        }
      };
      img.onerror = () => {
        if (cancelled) return;
        loadedCount++;
        setLoadProgress(Math.round((loadedCount / TOTAL_FRAMES) * 100));
        if (loadedCount === TOTAL_FRAMES) {
          imagesRef.current = images;
          setLoaded(true);
        }
      };
      images[i] = img;
    });

    return () => {
      cancelled = true;
    };
  }, []);

  /* ── Draw frame on canvas ("contain" logic) ─────── */
  const drawFrame = useCallback((index: number) => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    if (!ctx) return;

    const img = imagesRef.current[index];
    if (!img || !img.complete) return;

    const dpr = window.devicePixelRatio || 1;
    const cw = canvas.clientWidth;
    const ch = canvas.clientHeight;

    if (canvas.width !== cw * dpr || canvas.height !== ch * dpr) {
      canvas.width = cw * dpr;
      canvas.height = ch * dpr;
      ctx.scale(dpr, dpr);
    }

    ctx.clearRect(0, 0, cw, ch);

    const imgRatio = img.naturalWidth / img.naturalHeight;
    const canvasRatio = cw / ch;
    let drawW: number, drawH: number, drawX: number, drawY: number;

    if (imgRatio > canvasRatio) {
      drawW = cw;
      drawH = cw / imgRatio;
      drawX = 0;
      drawY = (ch - drawH) / 2;
    } else {
      drawH = ch;
      drawW = ch * imgRatio;
      drawX = (cw - drawW) / 2;
      drawY = 0;
    }

    ctx.drawImage(img, drawX, drawY, drawW, drawH);
  }, []);

  /* ── Render loop tied to frameIndex motion value ── */
  useMotionValueEvent(frameIndex, "change", (latest: number) => {
    const idx = Math.round(latest);
    if (idx !== currentFrameRef.current) {
      currentFrameRef.current = idx;
      cancelAnimationFrame(rafRef.current);
      rafRef.current = requestAnimationFrame(() => drawFrame(idx));
    }
  });

  /* Draw first frame once loaded */
  useEffect(() => {
    if (loaded) drawFrame(0);
  }, [loaded, drawFrame]);

  /* Handle resize */
  useEffect(() => {
    if (!loaded) return;

    const handleResize = () => {
      const canvas = canvasRef.current;
      if (canvas) {
        const dpr = window.devicePixelRatio || 1;
        canvas.width = canvas.clientWidth * dpr;
        canvas.height = canvas.clientHeight * dpr;
        const ctx = canvas.getContext("2d");
        if (ctx) ctx.scale(dpr, dpr);
      }
      drawFrame(currentFrameRef.current);
    };

    window.addEventListener("resize", handleResize);
    return () => {
      window.removeEventListener("resize", handleResize);
      cancelAnimationFrame(rafRef.current);
    };
  }, [loaded, drawFrame]);

  return (
    <>
      {/* Loader */}
      <AnimatePresence>{!loaded && <Loader progress={loadProgress} />}</AnimatePresence>

      {/* Wrapper — 400vh tall, scroll hijacking zone */}
      <div ref={wrapperRef} className="relative min-h-screen" style={{ height: "400vh" }}>
        {/* Sticky viewport */}
        <div className="sticky top-0 h-screen w-full overflow-hidden">
          {/* Canvas */}
          <canvas
            ref={canvasRef}
            className="absolute inset-0 h-full w-full"
            style={{ background: "#FFF8F0" }}
          />

          {/* Narrative beats */}
          {loaded &&
            BEATS.map((beat, i) => (
              <BeatOverlay
                key={i}
                beat={beat}
                scrollProgress={smoothProgress}
              />
            ))}

          {/* Scroll indicator */}
          {loaded && <ScrollIndicator scrollProgress={smoothProgress} />}
        </div>
      </div>
    </>
  );
}
