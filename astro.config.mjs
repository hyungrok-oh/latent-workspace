import { defineConfig, passthroughImageService } from "astro/config";
import mdx from "@astrojs/mdx";

export default defineConfig({
  integrations: [mdx()],
  image: {
    service: passthroughImageService(),
  },
  site: "https://hyungrok-oh.github.io",
  base: "/latent-workspace",
});
