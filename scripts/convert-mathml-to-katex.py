# -*- coding: utf-8 -*-
"""把动画里的原生 MathML 公式转换为 KaTeX(TeX) 写法，并接入共享 KaTeX。"""
import io

path = r"D:\WorkBuddy\2026-09-25-19-39-52\交互动画 匀变速直线运动.html"

with io.open(path, "r", encoding="utf-8") as f:
    s = f.read()

pairs = [
    ("<math><msub><mi>x</mi><mn>0</mn></msub></math>", "$x_0$"),
    ("<math><msub><mi>v</mi><mn>0</mn></msub></math>", "$v_0$"),
    ("<math><mtext>m/s²</mtext></math>", "$\\text{m/s}^2$"),
    ("<math><mtext>m/s</mtext></math>", "$\\text{m/s}$"),
    ("<math><mtext>m</mtext></math>", "$\\text{m}$"),
    ("<math><mi>x</mi></math>", "$x$"),
    ("<math><mi>t</mi></math>", "$t$"),
    ("<math><mi>v</mi></math>", "$v$"),
    ("<math><mi>a</mi></math>", "$a$"),
]

total = 0
for a, b in pairs:
    n = s.count(a)
    s = s.replace(a, b)
    total += n
    print("replace %-52s x %d" % (a, n))

assert "<math" not in s, "still has MathML left!"

# 1) 在 <title> 后引入 KaTeX 样式
title = "<title>匀变速直线运动 · 交互演示</title>"
assert title in s
s = s.replace(title, title + '\n<link rel="stylesheet" href="../katex/katex.min.css">', 1)

# 2) 替换针对 MathML 的样式为 KaTeX 适配
old_css = 'math{font-size:1.2em;color:inherit}\nmath mtext{font-style:normal}\nmath{font-family:"Cambria Math","Times New Roman",Times,serif}'
assert old_css in s, "MathML css block not found"
s = s.replace(old_css, ".katex{font-size:1.08em}", 1)

# 3) 在 </body> 前插入 KaTeX 脚本 + 自动渲染
scripts = """<script defer src="../katex/katex.min.js"></script>
<script defer src="../katex/contrib/auto-render.min.js"></script>
<script>
document.addEventListener('DOMContentLoaded', function(){
  if (window.renderMathInElement){
    renderMathInElement(document.body, {
      delimiters: [
        {left: '$$', right: '$$', display: true},
        {left: '$', right: '$', display: false}
      ],
      throwOnError: false
    });
  }
});
</script>
</body>"""
assert s.count("</body>") == 1, "unexpected </body> count"
s = s.replace("</body>", scripts, 1)

with io.open(path, "w", encoding="utf-8") as f:
    f.write(s)

print("total formula replacements:", total)
print("DONE")
