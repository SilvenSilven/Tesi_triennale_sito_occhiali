import type { Metadata } from "next";
import { Playfair_Display, Inter } from "next/font/google";
import "./globals.css";

const playfair = Playfair_Display({
  subsets: ["latin"],
  variable: "--font-playfair",
  display: "swap",
});
const inter = Inter({
  subsets: ["latin"],
  variable: "--font-inter",
  display: "swap",
});

export const metadata: Metadata = {
  title: "Solara — Luxury Summer Eyewear",
  description:
    "Occhiali da sole estivi di lusso. Stile Mediterraneo, protezione premium.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="it">
      <body
        className={`${playfair.variable} ${inter.variable} font-body antialiased bg-sand`}
      >
        {children}
      </body>
    </html>
  );
}
