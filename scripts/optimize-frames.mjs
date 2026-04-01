import sharp from "sharp";
import { readdir, mkdir } from "fs/promises";
import path from "path";

const INPUT_DIR = "public/frames";
const OUTPUT_DIR = "public/frames-optimized";
const TARGET_WIDTH = 1280;
const TARGET_HEIGHT = 720;
const WEBP_QUALITY = 75;

// Use every other frame to halve the total count
const SKIP_EVERY_OTHER = true;

async function main() {
  await mkdir(OUTPUT_DIR, { recursive: true });

  const files = (await readdir(INPUT_DIR))
    .filter((f) => f.endsWith(".jpg"))
    .sort();

  const selected = SKIP_EVERY_OTHER
    ? files.filter((_, i) => i % 2 === 0)
    : files;

  console.log(
    `Processing ${selected.length} of ${files.length} frames → WebP ${TARGET_WIDTH}x${TARGET_HEIGHT} @ q${WEBP_QUALITY}`
  );

  let done = 0;
  const CONCURRENCY = 8;

  for (let i = 0; i < selected.length; i += CONCURRENCY) {
    const batch = selected.slice(i, i + CONCURRENCY);
    await Promise.all(
      batch.map(async (file) => {
        const idx = selected.indexOf(file);
        const outName = `frame_${String(idx).padStart(3, "0")}.webp`;
        await sharp(path.join(INPUT_DIR, file))
          .resize(TARGET_WIDTH, TARGET_HEIGHT, { fit: "contain", background: { r: 255, g: 248, b: 240, alpha: 1 } })
          .webp({ quality: WEBP_QUALITY })
          .toFile(path.join(OUTPUT_DIR, outName));
        done++;
        if (done % 10 === 0 || done === selected.length) {
          process.stdout.write(`\r  ${done}/${selected.length}`);
        }
      })
    );
  }

  console.log("\nDone! Optimized frames saved to", OUTPUT_DIR);
}

main().catch(console.error);
