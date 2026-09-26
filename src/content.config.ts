import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

// 两个内容集合：新知动画 / 教学讲义
// （板块显示名：2026-09-26 由「交互动画」改为「新知动画」，目录名 animations 不变）
// （原「实验演示 / 资源下载」两个集合已于 2026-09-26 按用户要求移除，恢复方法见
//   D:\WorkBuddy\2026-09-26-09-04-18\移除备份-演示实验与其它资源\如何恢复.md）
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

export const collections = { animations, lectures };
