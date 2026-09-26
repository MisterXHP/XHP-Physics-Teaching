import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

// 四个内容集合：交互动画 / 教学讲义 / 实验演示 / 资源下载
// 字段保持统一，便于共用卡片与列表组件。
const base = {
  title: z.string(),
  topic: z.string(),
  summary: z.string().optional(),
  date: z.coerce.date().optional(),
  featured: z.boolean().default(false),
};

const animations = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/animations' }),
  schema: z.object({
    ...base,
    // iframe 嵌入源：public 下的相对路径（如 animations/xxx.html）或外部网址
    embed: z.string(),
    cover: z.string().optional(),
  }),
});

const lectures = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/lectures' }),
  schema: z.object({ ...base }),
});

const experiments = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/experiments' }),
  schema: z.object({
    ...base,
    // 视频 / GIF 地址（public 相对路径或外链），可留空
    video: z.string().optional(),
    cover: z.string().optional(),
  }),
});

const downloads = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/downloads' }),
  schema: z.object({
    ...base,
    // 资源文件地址（public 相对路径或外链）
    file: z.string().optional(),
    format: z.string().optional(),
    size: z.string().optional(),
  }),
});

export const collections = { animations, lectures, experiments, downloads };
