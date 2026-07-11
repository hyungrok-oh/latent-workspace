import { defineCollection, z } from "astro:content";

const blog = defineCollection({
  type: "content",
  schema: z.object({
    title: z.string(),
    description: z.string(),
    date: z.date(),
    paper: z.string(),
    track: z.string(),
    tags: z.array(z.string()),
    status: z.string(),
    sourceUrl: z.string().url().optional(),
    codeUrl: z.string().url().optional(),
  }),
});

const experiments = defineCollection({
  type: "content",
  schema: z.object({
    title: z.string(),
    description: z.string(),
    date: z.date(),
    status: z.string(),
    target: z.string(),
    compute: z.string(),
    sourcePath: z.string().optional(),
  }),
});

export const collections = { blog, experiments };
