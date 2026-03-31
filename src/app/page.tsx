import Navbar from "@/components/Navbar";
import SolaraGlasses from "@/components/SolaraGlasses";
import Features from "@/components/Features";
import Pricing from "@/components/Pricing";
import Footer from "@/components/Footer";

export default function Home() {
  return (
    <main className="min-h-screen bg-sand">
      <Navbar />
      <SolaraGlasses />
      <Features />
      <Pricing />
      <Footer />
    </main>
  );
}
