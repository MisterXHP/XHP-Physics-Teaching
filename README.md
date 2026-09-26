# 大熊印象 · 物理星河（XHP-Physics-Teaching）

熊和平（大熊印象）的中学物理教学资源站「大熊印象 · 物理星河」。基于 **Astro** 的纯静态站点，包含两个内容板块：

- **新知动画**：可动手操作的物理模拟（独立 html，用 iframe 隔离嵌入）
- **教学讲义**：Markdown 撰写，支持 TeX 公式（构建时用 KaTeX 渲染）

> 「实验演示」与「资源下载」两个板块已于 2026-09-26 按需求暂时移除。将来要恢复，见
> `D:\WorkBuddy\2026-09-26-09-04-18\移除备份-演示实验与其它资源\如何恢复.md`（或在 GitHub 上回退对应提交）。

站内还有 17 个物理主题分类、全站搜索（Pagefind）、深浅主题切换。

---

## 一、本地开发与构建

需要 Node.js 18+（推荐 22）。

```bash
npm install        # 首次安装依赖
npm run dev        # 本地预览，默认 http://localhost:4321/XHP-Physics-Teaching/
npm run build      # 构建静态文件到 dist/（同时生成搜索索引）
npm run preview    # 预览构建结果
```

> 注意：站点的部署路径是子目录 `/XHP-Physics-Teaching/`，本地预览地址也带这个前缀。

---

## 二、以后怎么添加内容（日常操作）

**推荐方式：用后台（无需代码）**

1. 打开 `https://misterxhp.github.io/XHP-Physics-Teaching/admin/`
2. 用 GitHub 账号登录，选择板块（新知动画 / 教学讲义）
3. 点「新建」，填标题、选主题分类、写正文（讲义里直接用 `$...$` 写公式）
4. 点「发布」，系统自动提交到仓库并触发重新部署，几分钟后网站更新

**添加新动画**：先把 html 文件放到 `public/animations/` 目录（可在后台用「媒体」上传，或直接拖进仓库），然后在后台新建新知动画条目，「嵌入地址」填 `animations/你的文件名.html`。

---

## 三、页面结构

| 路径 | 说明 |
|------|------|
| `/` | 首页：站点简介 + 精选动画 + 最新讲义 |
| `/animations/` | 新知动画列表 |
| `/lectures/` | 教学讲义列表 |
| `/topics/<主题>/` | 按物理主题汇总的内容页 |
| `/search/` | 全站搜索 |
| `/admin/` | 内容管理后台 |

---

## 四、增删主题分类

主题列表定义在 **两处**，增删时请同步修改：

1. `src/data/topics.ts` —— 决定网站的分类页与导航
2. `public/admin/config.yml` 里的 `x-topics` —— 决定后台下拉选项

改完后提交，网站会自动重新生成分类页。

---

## 五、部署到 GitHub Pages

1. 在 GitHub 新建仓库 `XHP-Physics-Teaching`（属主 `misterxhp`）
2. 把本项目推送上去（分支 `main`）
3. 仓库 **Settings → Pages → Build and deployment → Source** 选择 **GitHub Actions**
4. 之后每次 push 到 `main`，`.github/workflows/deploy.yml` 会自动构建并发布
5. 访问 `https://misterxhp.github.io/XHP-Physics-Teaching/`

---

## 六、后台（Decap CMS）首次配置

Decap CMS 的 GitHub 登录需要一个 OAuth 代理（免费，一次性配置）。任选其一：

- **GitHub OAuth App + 免费代理服务**（如 Cloudflare Worker 部署的开源 OAuth 代理）
- 或参考 Decap 官方文档：[https://decapcms.org/docs/github-backend/](https://decapcms.org/docs/github-backend/)

配置完成后，把代理地址填入 `public/admin/config.yml` 的 `base_url` 字段即可。

---

## 七、隐私（不被搜索引擎收录）

站点已加入 `public/robots.txt`（`Disallow: /`）和全站 `<meta name="robots" content="noindex, nofollow">`。

> 说明：这只是"请求"爬虫不要收录，主流搜索引擎会遵守，但不构成 100% 保证。若需更强隐私，可改用自定义域名并进一步限制访问。

---

## 八、目录结构

```
XHP-Physics-Teaching/
├─ public/
│  ├─ animations/        动画 html 文件（iframe 嵌入源）
│  ├─ uploads/           后台媒体上传目录
│  ├─ admin/             Decap CMS 后台
│  ├─ robots.txt         防收录
│  └─ favicon.svg
├─ src/
│  ├─ content/
│  │  ├─ animations/     新知动画条目（.md）
│  │  └─ lectures/       教学讲义条目（.md）
│  ├─ content.config.ts  内容模型定义
│  ├─ data/topics.ts     17 个主题分类
│  ├─ layouts/           页面布局
│  ├─ components/        组件
│  ├─ pages/             页面路由
│  └─ styles/global.css  全局样式与主题变量
└─ .github/workflows/deploy.yml  自动部署
```

---

## 九、迁移到其它环境

本站是纯静态项目，代码和内容都在 Git 仓库里，**不依赖任何服务器**：

- 换电脑：安装 Node + Git，`git clone` 本仓库，`npm install && npm run dev` 即可继续开发
- 换托管：`npm run build` 生成的 `dist/` 可放到任意静态托管（国内 CDN、对象存储等），无需改代码
