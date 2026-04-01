import { neon } from "@neondatabase/serverless";
import { writeFileSync } from "fs";

const sql = neon("postgresql://neondb_owner:npg_uFxVSRoTj95w@ep-damp-sea-anvn4fw4-pooler.c-6.us-east-1.aws.neon.tech/neondb?sslmode=require");

const rows = await sql`SELECT id, body, stars, product_name FROM reviews ORDER BY id`;
writeFileSync("all_reviews.json", JSON.stringify(rows, null, 2), "utf-8");
console.log(`Esportate ${rows.length} recensioni in all_reviews.json`);
