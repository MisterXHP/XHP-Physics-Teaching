# -*- coding: utf-8 -*-
"""把「带 KaTeX 的动画」导出为单文件 HTML。

用法:
  python bundle_animation.py "动画.html" --offline   # 内联 KaTeX，离线可用（文件大）
  python bundle_animation.py "动画.html" --online    # 本地优先 + CDN 回退（需联网，文件小）

可选参数:
  -o, --out <文件>        指定输出路径
  --katex-dir <目录>      指定 KaTeX 目录（默认：与动画同级的 katex/）
"""
import argparse
import base64
import os
import re
import sys

CDN = "https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/"
MIME = {"woff2": "font/woff2", "woff": "font/woff", "ttf": "font/ttf"}

LINK_TAG = '<link rel="stylesheet" href="katex/katex.min.css">'
JS_TAG = '<script defer src="katex/katex.min.js"></script>'
AR_TAG = '<script defer src="katex/contrib/auto-render.min.js"></script>'
RENDER_BLOCK_RE = re.compile(
    r"<script>\s*document\.addEventListener\('DOMContentLoaded'[\s\S]*?</script>\s*", re.M
)

SMART = """<script>
(function () {
  var LOCAL = 'katex/';
  var CDN = '%s';
  function boot(base) {
    var l = document.createElement('link');
    l.rel = 'stylesheet'; l.href = base + 'katex.min.css';
    document.head.appendChild(l);
    var k = document.createElement('script');
    k.src = base + 'katex.min.js';
    k.onload = function () {
      var a = document.createElement('script');
      a.src = base + 'contrib/auto-render.min.js';
      a.onload = function () {
        if (window.renderMathInElement)
          renderMathInElement(document.body, {
            delimiters: [
              { left: '$$', right: '$$', display: true },
              { left: '$', right: '$', display: false }
            ], throwOnError: false
          });
      };
      document.head.appendChild(a);
    };
    k.onerror = function () { if (base !== CDN) boot(CDN); };
    document.head.appendChild(k);
  }
  boot(LOCAL);
})();
</script>
""" % CDN


def read_text(p):
    with open(p, "r", encoding="utf-8") as f:
        return f.read()


def inline_css(css, katex_dir):
    def repl(m):
        rel = m.group(2).replace("\\", "/")
        fp = os.path.join(katex_dir, *rel.split("/"))
        if not os.path.isfile(fp):
            return m.group(0)
        with open(fp, "rb") as f:
            b64 = base64.b64encode(f.read()).decode("ascii")
        ext = rel.rsplit(".", 1)[-1].lower()
        return "url(data:%s;base64,%s)" % (MIME.get(ext, "application/octet-stream"), b64)

    return re.sub(r"url\((['\"]?)([^)'\"]+)\1\)", repl, css)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("input", help="动画 html 路径")
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--offline", action="store_true", help="内联 KaTeX（离线可用，文件大）")
    g.add_argument("--online", action="store_true", help="本地优先 + CDN 回退（需联网，文件小）")
    ap.add_argument("-o", "--out")
    ap.add_argument("--katex-dir")
    a = ap.parse_args()

    src = os.path.abspath(a.input)
    katex_dir = a.katex_dir or os.path.join(os.path.dirname(src), "katex")
    html = read_text(src)

    if LINK_TAG not in html:
        print("!! 该动画未包含 KaTeX 引用（可能不含公式），无需打包。", file=sys.stderr)
        sys.exit(2)

    if a.offline:
        css = inline_css(read_text(os.path.join(katex_dir, "katex.min.css")), katex_dir)
        kjs = read_text(os.path.join(katex_dir, "katex.min.js"))
        arjs = read_text(os.path.join(katex_dir, "contrib", "auto-render.min.js"))
        html = html.replace(LINK_TAG, "<style>\n%s\n</style>" % css)
        html = html.replace(JS_TAG, "<script>\n%s\n</script>" % kjs)
        html = html.replace(AR_TAG, "<script>\n%s\n</script>" % arjs)
        suffix = ".offline.html"
    else:
        html = html.replace(LINK_TAG, "")
        if JS_TAG + "\n" + AR_TAG in html:
            html = html.replace(JS_TAG + "\n" + AR_TAG, SMART)
        else:
            html = html.replace(JS_TAG, SMART)
            html = html.replace(AR_TAG, "")
        html = RENDER_BLOCK_RE.sub("", html)
        suffix = ".online.html"

    out = a.out or (os.path.splitext(src)[0] + suffix)
    with open(out, "w", encoding="utf-8") as f:
        f.write(html)
    print("已生成: %s  (%.0f KB)" % (out, os.path.getsize(out) / 1024.0))


if __name__ == "__main__":
    main()
