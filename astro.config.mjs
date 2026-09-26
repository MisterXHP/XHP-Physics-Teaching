// @ts-check
import { defineConfig } from 'astro/config';
import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';

// 站点部署在 GitHub Pages 的项目子路径下：https://misterxhp.github.io/XHP-Physics-Teaching/
export default defineConfig({
  site: 'https://misterxhp.github.io',
  base: '/XHP-Physics-Teaching/',
  trailingSlash: 'ignore',
  build: {
    format: 'directory',
  },
  markdown: {
    remarkPlugins: [remarkMath],
    rehypePlugins: [[rehypeKatex, { strict: false, throwOnError: false, output: 'html' }]],
  },
});
