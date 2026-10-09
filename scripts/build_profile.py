"""Generate the bilingual profile and its three self-contained SVG themes."""

from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPO = "https://github.com/virtue192/virtue192"
RAW = "https://raw.githubusercontent.com/virtue192/virtue192/main"
WIKI = "https://moonspaceai.feishu.cn/wiki/QnwSwDygIiG7PUkklyicAjcQncg"
THEMES = {
    "purple": ("月光紫", "Moonlight", "#c4b5fd", "#a78bfa", "#211a3b"),
    "blue": ("天空蓝", "Sky", "#7dd3fc", "#38bdf8", "#102c40"),
    "mint": ("薄荷绿", "Mint", "#6ee7b7", "#34d399", "#10352e"),
}


def readme_path(lang, theme):
    return "README.md" if (lang, theme) == ("zh", "purple") else f"profiles/README.{lang}.{theme}.md"


def badge(label, color, filename, width=124):
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="32" viewBox="0 0 {width} 32" role="img" aria-label="{escape(label)}">
<rect x=".5" y=".5" width="{width-1}" height="31" rx="16" fill="#121827" stroke="#334155"/>
<circle cx="16" cy="16" r="4" fill="{color}"/>
<text x="{width / 2 + 7}" y="21" text-anchor="middle" font-family="system-ui, -apple-system, 'Segoe UI', 'Microsoft YaHei', sans-serif" font-size="12" font-weight="600" fill="#f1f5f9">{escape(label)}</text>
</svg>'''
    (ROOT / "assets" / filename).write_text(svg, encoding="utf-8")


def header(lang, theme):
    _, _, accent, secondary, tint = THEMES[theme]
    lines = (
        ["你好，我是慢慢。", "连接开发者、AI 产品与校园。", "让想法在真实协作中落地。"]
        if lang == "zh"
        else ["Hi, I'm Manman / Virtu.", "Connecting people, ideas and AI.", "Turning conversations into collaboration."]
    )
    title = "慢慢 · Virtu" if lang == "zh" else "Manman · Virtu"
    groups = []
    for index, line in enumerate(lines):
        # Each line types in, pauses, then disappears. All timelines share a 15s loop.
        start = index / 3
        glyph_widths = [24 if ord(char) > 127 else 14.4 for char in line]
        total_width = sum(glyph_widths)
        times = [0] + ([start] if index else [])
        sizes = [0] * len(times)
        width = 0
        for position, glyph_width in enumerate(glyph_widths, 1):
            width += glyph_width
            times.append(start + .18 * position / len(line))
            sizes.append(width)
        times.extend([start + .31, (index + 1) / 3])
        sizes.extend([total_width, 0])
        if index < 2:
            times.append(1)
            sizes.append(0)
        key_times = ";".join(f"{time:.6f}" for time in times)
        widths = ";".join(f"{size:.1f}" for size in sizes)
        cursor_positions = ";".join(f"{54 + size + 4:.1f}" for size in sizes)
        opacity_times = ["0;.333333;1", "0;.333333;.666667;1", "0;.666667;1"][index]
        opacity_values = ["1;0;0", "0;1;0;0", "0;1;1"][index]
        groups.append(f'''<clipPath id="typing-{index}"><rect x="54" y="147" width="660" height="42"><animate attributeName="width" values="{widths}" keyTimes="{key_times}" calcMode="discrete" dur="15s" repeatCount="indefinite"/></rect></clipPath>
<g opacity="{1 if index == 0 else 0}"><animate attributeName="opacity" values="{opacity_values}" keyTimes="{opacity_times}" calcMode="discrete" dur="15s" repeatCount="indefinite"/>
<text x="54" y="178" fill="{accent}" font-size="24" textLength="{total_width:.1f}" lengthAdjust="spacingAndGlyphs" font-family="ui-monospace, Consolas, 'Microsoft YaHei', monospace" clip-path="url(#typing-{index})">{escape(line)}</text>
<rect x="{58 + total_width:.1f}" y="154" width="2" height="28" fill="{accent}"><animate attributeName="x" values="{cursor_positions}" keyTimes="{key_times}" calcMode="discrete" dur="15s" repeatCount="indefinite"/><animate attributeName="opacity" values="1;0" dur=".8s" calcMode="discrete" repeatCount="indefinite"/></rect></g>''')
    subtitle = "让人相遇 · 让想法落地" if lang == "zh" else "Make connections. Build things together."
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="960" height="300" viewBox="0 0 960 300" role="img" aria-labelledby="title desc">
<title id="title">{escape(title)} — AI community, DevRel and campus collaboration</title>
<desc id="desc">{escape(' / '.join(lines))}</desc>
<style>.still{{display:none}}@media(prefers-reduced-motion:reduce){{.motion{{display:none}}.still{{display:block}}}}</style>
<defs>
<linearGradient id="bg" x2="1" y2="1"><stop stop-color="#0c1220"/><stop offset="1" stop-color="{tint}"/></linearGradient>
<radialGradient id="glow"><stop stop-color="{secondary}" stop-opacity=".16"/><stop offset="1" stop-color="{secondary}" stop-opacity="0"/></radialGradient>
<linearGradient id="moon" x2="1" y2="1"><stop stop-color="#f8fafc"/><stop offset="1" stop-color="{accent}"/></linearGradient>
</defs>
<rect x=".5" y=".5" width="959" height="299" rx="24" fill="url(#bg)" stroke="#334155"/>
<circle cx="808" cy="130" r="186" fill="url(#glow)"/>
<g fill="{accent}" opacity=".55"><circle cx="710" cy="52" r="2"/><circle cx="881" cy="59" r="2.5"/><circle cx="914" cy="153" r="1.5"/><circle cx="697" cy="217" r="1.5"/><circle cx="875" cy="250" r="2"/></g>
<g transform="translate(805 134)"><ellipse rx="99" ry="39" transform="rotate(-26)" fill="none" stroke="{accent}" stroke-opacity=".3"/>
<circle r="54" fill="url(#moon)"/><circle cx="22" cy="-14" r="49" fill="{tint}"/>
<circle cx="-76" cy="37" r="5" fill="{secondary}"/></g>
<g font-family="system-ui, -apple-system, 'Segoe UI', 'Microsoft YaHei', 'Noto Sans CJK SC', sans-serif">
<text x="54" y="53" fill="{accent}" font-size="12" font-weight="600" letter-spacing="3">PEOPLE · IDEAS · AI</text>
<text x="54" y="124" fill="#f8fafc" font-size="46" font-weight="700">{escape(title)}</text>
<g class="motion">{''.join(groups)}</g>
<text class="still" x="54" y="178" fill="{accent}" font-size="24">{escape(lines[0])}</text>
<path d="M54 211 H640" stroke="#475569" stroke-opacity=".5"/>
<text x="54" y="244" fill="#cbd5e1" font-size="13">MOONSPACE.AI  /  DEVREL  /  COMMUNITY</text>
<text x="54" y="275" fill="#94a3b8" font-size="12">{escape(subtitle)}</text>
</g></svg>'''
    (ROOT / "assets" / f"header-{lang}-{theme}.svg").write_text(svg, encoding="utf-8")


def navigation(lang, theme):
    items = []
    for target_lang, label in [("zh", "简体中文"), ("en", "English")]:
        url = f"{REPO}/blob/main/{readme_path(target_lang, theme)}"
        items.append(f'<a href="{url}"><img src="{RAW}/assets/lang-{target_lang}.svg" alt="{label}" height="32" /></a>')
    languages = " ".join(items)
    items = []
    for target_theme, data in THEMES.items():
        label = data[0 if lang == "zh" else 1]
        url = f"{REPO}/blob/main/{readme_path(lang, target_theme)}"
        items.append(f'<a href="{url}"><img src="{RAW}/assets/theme-{lang}-{target_theme}.svg" alt="{label}" height="32" /></a>')
    themes = " ".join(items)
    current = f"当前：简体中文 · {THEMES[theme][0]}" if lang == "zh" else f"Viewing: English · {THEMES[theme][1]}"
    return f'''<div align="center">

<p>{languages}</p>
<p>{themes}</p>
<p><sub>{current}</sub></p>

</div>'''


ZH = '''商科出身，正在 AI 行业探索**开发者关系与社区运营**。目前参与搭建 **MoonSpace.ai**，担任 **PMO & 运营负责人**，也是公众号 **「慢慢Virtu」** 的作者。

我喜欢让不同背景的人看见彼此，把一次对话、一个念头，变成能继续一起做的事。

### 我在做什么

| 方向 | 正在推进的事 |
| :--- | :--- |
| 🌙 **AI 社区 × DevRel** | 连接 AI 产品、开发者与学生，组织社区活动与黑客松，让合作在活动之后继续。 |
| 🖥️ **Life Ledger OS** | 迭代个人 Wiki 与知识桌面。本地版本已支持卡片拖拽与位置保存、搜索分类、知识摘要及飞书原文跳转；正在打磨移动端和阅读体验。 |
| 🤖 **Agent × AI 工作流** | 边学边试，探索 Agent、Harness 与飞书 AI 在知识整理、项目推进和日常协作中的用法。 |
| 🌱 **校园 AI 实践** | 为学生连接真实项目与共创机会，持续搭建西南地区的 AI 社区入口。 |

### 从这些地方认识我

| 入口 | 你会看到 |
| :--- | :--- |
| [📖 个人说明书](https://moonspaceai.feishu.cn/wiki/QnwSwDygIiG7PUkklyicAjcQncg) | 我的工作、实践与最近关注的事。 |
| [🧩 产品与项目](https://moonspaceai.feishu.cn/wiki/KIZqwmgVfivNnMkftaUcKRbsnIb) | 从想法到动手的尝试。 |
| [🤖 Agent 学习路线](https://moonspaceai.feishu.cn/wiki/TQY0w9NejiYe6Ekxf3CclxGInJd) | 学习线索与实践记录。 |
| [📚 阅读与思考](https://moonspaceai.feishu.cn/wiki/QYxYwiXkSiErkmkMKwFc9Q90nVf) | 读到的内容、留下的问题与自己的判断。 |
| [🌙 MoonSpace.ai](https://moonspaceai.feishu.cn/wiki/Km5QwCbEkiBg9HkSRajc2lDQn7x) | 我参与搭建的 AI 社区。 |

### 最近的代码实践

- [**牧空 Mukong**](https://github.com/virtue192/mukong) — 自托管、API 优先的个人信息收集与知识管理系统。
- [**JD Mirror**](https://github.com/virtue192/jd-mirror) — 对比官网与招聘平台的岗位描述，帮助文商科转 AI 产品运营的人判断机会。
- [**Vibe QR**](https://github.com/virtue192/vibe-qr) — 本地优先的 3D 艺术二维码实验，支持自定义中心卡片。

### 一起做点什么

欢迎聊 **AI 产品、开发者社区、校园活动、内容访谈**，或者从一个 **个人知识库 / AI 工作流** 的小问题开始共创。我参与过 Datawhale × 小浣熊活动成都站、成都创变者黑客松等活动的组织与落地。

也欢迎约一杯 Coffee chat。工作之外，我喜欢跑步、阅读，还有把看似无关的事联想在一起。

<div align="center">

**微信：`QBBai10086`**

扫码加我，备注「GitHub」就好。点击二维码可查看原图。

<a href="https://raw.githubusercontent.com/virtue192/virtue192/main/assets/wechat-qr.jpg"><img src="https://raw.githubusercontent.com/virtue192/virtue192/main/assets/wechat-qr.jpg" alt="慢慢的个人微信二维码，微信号 QBBai10086" width="260" /></a>

[即刻](https://web.okjike.com/u/d30556f9-e6a1-4c1c-ac23-223a8e3e3e49) · [小红书](https://xhslink.cn/o/9rTaagRLVLb) · [掘金](https://juejin.cn/user/2750331338887808) · 公众号 **慢慢Virtu**

</div>

---

> 在 AI 产品、开发者与校园之间，做一些让人相遇、让想法落地的事。

<sub>依据飞书个人说明书整理 · 2026-10-09 更新 · 最新动态以[飞书原文](https://moonspaceai.feishu.cn/wiki/QnwSwDygIiG7PUkklyicAjcQncg)为准。</sub>
'''

EN = '''I came to AI from a **business background** and am exploring **developer relations and community operations**. I help build **MoonSpace.ai** as its **PMO & Operations Lead**, and write the WeChat publication **慢慢Virtu**.

I enjoy connecting people from different backgrounds and turning a conversation or an idea into something we can keep building together.

### What I'm working on

| Focus | In progress |
| :--- | :--- |
| 🌙 **AI community × DevRel** | Connecting AI products, developers and students through community events and hackathons, with collaboration that continues afterward. |
| 🖥️ **Life Ledger OS** | A personal wiki and knowledge desktop. The local version supports draggable cards with saved positions, search and categories, knowledge summaries and links to Feishu originals. Mobile and reading experiences are still being refined. |
| 🤖 **Agents × AI workflows** | Learning by doing: exploring agents, harnesses and Feishu AI for knowledge organization, project coordination and everyday collaboration. |
| 🌱 **AI on campus** | Helping students participate in real projects and building community connections in Southwest China. |

### Explore my world

The linked Feishu resources are written in Chinese.

| Start here | What you'll find |
| :--- | :--- |
| [📖 About me](https://moonspaceai.feishu.cn/wiki/QnwSwDygIiG7PUkklyicAjcQncg) | My work, experiments and current interests. |
| [🧩 Products & projects](https://moonspaceai.feishu.cn/wiki/KIZqwmgVfivNnMkftaUcKRbsnIb) | Ideas I'm putting into practice. |
| [🤖 Agent learning roadmap](https://moonspaceai.feishu.cn/wiki/TQY0w9NejiYe6Ekxf3CclxGInJd) | Learning resources and hands-on exploration. |
| [📚 Reading & reflections](https://moonspaceai.feishu.cn/wiki/QYxYwiXkSiErkmkMKwFc9Q90nVf) | Notes, questions and my own takeaways. |
| [🌙 MoonSpace.ai](https://moonspaceai.feishu.cn/wiki/Km5QwCbEkiBg9HkSRajc2lDQn7x) | The AI community I'm helping build. |

### Recent coding experiments

- [**Mukong**](https://github.com/virtue192/mukong) — A self-hosted, API-first system for collecting information and managing personal knowledge.
- [**JD Mirror**](https://github.com/virtue192/jd-mirror) — Compares job descriptions across company sites and hiring platforms to help people with business or humanities backgrounds assess AI product operations roles.
- [**Vibe QR**](https://github.com/virtue192/vibe-qr) — A local-first 3D artistic QR code playground with customizable center cards.

### Let's build something together

I'd love to talk about **AI products, developer communities, campus events and interviews**, or collaborate on a small **personal knowledge / AI workflow** problem. I've helped organize and deliver events including the Chengdu stop of Datawhale × 小浣熊 and the Chengdu Changemakers Hackathon.

Coffee chats are welcome, too. Outside work, I enjoy running, reading and finding unexpected connections between ideas.

<div align="center">

**WeChat: `QBBai10086`**

Scan to connect and mention “GitHub”. Click the QR code for the original image.

<a href="https://raw.githubusercontent.com/virtue192/virtue192/main/assets/wechat-qr.jpg"><img src="https://raw.githubusercontent.com/virtue192/virtue192/main/assets/wechat-qr.jpg" alt="Manman's personal WeChat QR code, WeChat ID QBBai10086" width="260" /></a>

[Jike](https://web.okjike.com/u/d30556f9-e6a1-4c1c-ac23-223a8e3e3e49) · [Xiaohongshu](https://xhslink.cn/o/9rTaagRLVLb) · [Juejin](https://juejin.cn/user/2750331338887808) · WeChat publication **慢慢Virtu**

</div>

---

> Connecting AI products, developers and campuses — helping people meet and ideas take shape.

<sub>Adapted from my Feishu introduction · Updated 2026-10-09 · [Feishu](https://moonspaceai.feishu.cn/wiki/QnwSwDygIiG7PUkklyicAjcQncg) has the latest updates.</sub>
'''


def main():
    (ROOT / "assets").mkdir(exist_ok=True)
    (ROOT / "profiles").mkdir(exist_ok=True)
    badge("简体中文", "#c4b5fd", "lang-zh.svg", 110)
    badge("English", "#7dd3fc", "lang-en.svg", 104)
    for lang in ["zh", "en"]:
        for theme, data in THEMES.items():
            badge(data[0 if lang == "zh" else 1], data[2], f"theme-{lang}-{theme}.svg")
            header(lang, theme)
            alt = "慢慢 · Virtu：连接开发者、AI 产品与校园，打字机动画" if lang == "zh" else "Manman / Virtu: connecting people, ideas and AI, typing animation"
            content = f'''<!-- Generated by scripts/build_profile.py; edit the source and regenerate all variants together. -->
<div align="center">
<img src="{RAW}/assets/header-{lang}-{theme}.svg" alt="{alt}" width="960" />
</div>

{navigation(lang, theme)}

---

{ZH if lang == 'zh' else EN}'''
            (ROOT / readme_path(lang, theme)).write_text(content, encoding="utf-8")
    print("Generated 6 profile variants, 6 animated headers and 8 navigation badges.")


if __name__ == "__main__":
    main()
