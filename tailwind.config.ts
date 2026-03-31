import type { Config } from "tailwindcss";

const config: Config = {
  content: [
    "./src/pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/components/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      colors: {
        sand: "#FFF8F0",
        warm: "#1A1200",
        accent: "#FF6B2B",
        sun: "#FFD166",
        sea: "#00B4A6",
        "card-bg": "#FFF0E0",
      },
      fontFamily: {
        playfair: ["Playfair Display", "serif"],
        body: ["Inter", "sans-serif"],
      },
    },
  },
  plugins: [],
};
export default config;
