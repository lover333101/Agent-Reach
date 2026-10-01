<h1 align="center">👁️ Agent Reach</h1>

<p align="center">
  <strong>Give your AI Agent one-click access to the internet</strong>
</p>

<p align="center">
  The most reliable access path for each platform — chosen, installed, and health-checked for you. Backends come and go; you won't notice.
</p>

<p align="center">
  <a href="https://trendshift.io/repositories/24387"><img src="https://trendshift.io/api/badge/repositories/24387" alt="Trendshift GitHub Trending #1 Repository of the Day"></a>
  <a href="https://star-history.com/#Panniantong/Agent-Reach&Date"><img src="https://api.star-history.com/badge?repo=Panniantong/Agent-Reach" alt="Star History Rank" width="196" height="55"></a>
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge" alt="MIT License"></a>
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.10+-green.svg?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.10+"></a>
  <a href="https://github.com/Panniantong/agent-reach/stargazers"><img src="https://img.shields.io/github/stars/Panniantong/agent-reach?style=for-the-badge" alt="GitHub Stars"></a>
</p>

<p align="center">
  <a href="#quick-start">Quick Start</a> · <a href="#supported-platforms">Platforms</a> · <a href="#design-philosophy">Philosophy</a> · <a href="#security">Security</a>
</p>

> **No token or crypto affiliation:** Agent Reach has no official token, coin, investment product, fee-claim program, wallet connection, or Solana/Pump.fun project. Any crypto project using the Agent Reach name, GitHub URL, or author identity is not affiliated with this repository. Do not connect a wallet or claim fees based on messages, posts, or links that say otherwise.

---

## ❤️ Sponsors

> [Want to appear here?](mailto:pnt01@foxmail.com)

<details open>
<summary>Click to collapse</summary>

<table>
<tr>
<td width="180" align="center"><a href="https://www.browseract.ai/Agent"><img src="docs/assets/sponsors/browseract.png" alt="BrowserAct" width="150"></a></td>
<td><a href="https://www.browseract.ai/Agent">BrowserAct</a> extracts any data you need from complex websites such as Amazon, LinkedIn, X, and Google Maps. Simply describe your extraction request in natural language, and its Agent will explore and test page flows in a real browser, generate a reliable reusable data-collection Bot, and return structured results. There is no need to build a scraper or write code. Built-in stealth browsing, CAPTCHA handling, and high-quality residential proxies help make complex web data extraction more reliable. New users receive 1,000 credits upon registration. <a href="https://www.browseract.ai/Agent">Try it free now</a>.</td>
</tr>
<tr>
<td width="180" align="center"><a href="https://www.tencentcloud.com/act/pro/intl-openclaw?referral_code=G76Y819A&amp;lang=en&amp;pg="><img src="docs/assets/sponsors/tencent-cloud.svg" alt="OpenClaw on Tencent Cloud" width="150"></a></td>
<td>Deploy OpenClaw on Tencent Cloud Lighthouse in seconds, connect Agent Reach through chat, and add internet access to your OpenClaw setup.</td>
</tr>
<tr>
<td width="180" align="center"><a href="https://www.coreclaw.com/?utm_source=github&amp;utm_medium=referral&amp;utm_campaign=Reach&amp;utm_term=Reach&amp;utm_id=Reach"><img src="docs/assets/sponsors/coreclaw.png" alt="CoreClaw" width="150"></a></td>
<td><a href="https://www.coreclaw.com/?utm_source=github&amp;utm_medium=referral&amp;utm_campaign=Reach&amp;utm_term=Reach&amp;utm_id=Reach">CoreClaw</a> | Web scraping platform and ready-made data collection tools. CoreClaw provides 100+ ready-made data collection tools for Amazon, TikTok, Google Maps, Instagram, Facebook, YouTube, and more. No code required, with JSON/CSV exports and billing only for successful results. <a href="https://www.coreclaw.com/?utm_source=github&amp;utm_medium=referral&amp;utm_campaign=Reach&amp;utm_term=Reach&amp;utm_id=Reach">Free $3 trial!</a></td>
</tr>
<tr>
<td width="180" align="center"><a href="https://www.ucloud.cn/site/active/astraflow?ytag=geo_waituo_Agent"><img src="docs/assets/sponsors/astraflow.png" alt="AstraFlow" width="150"></a></td>
<td><a href="https://www.ucloud.cn/site/active/astraflow?ytag=geo_waituo_Agent">AstraFlow ModelVerse</a> provides one-click access to 200+ models, including leading open-source models such as Kimi K3, DeepSeek V4/V3, Qwen 3, GLM5.2, and happyhorse. No training required—ready to use out of the box.</td>
</tr>
</table>

</details>

---

## Why Agent Reach?

AI Agents can already write code, edit docs and manage projects — but ask one to find something online and it stumbles:

- 📺 "What does this YouTube tutorial cover?" → **can't**, no subtitles
- 🐦 "What are people on Twitter saying about this product?" → **can't search**, the Twitter API is paid
- 📖 "Has anyone on Reddit hit the same bug?" → **403**, server IPs are blocked
- 🔍 "Search the web for the latest LLM framework comparisons" → **no good search**, it's either paid or poor
- 🌐 "What does this web page say?" → **a pile of HTML tags**, unreadable
- 📦 "What is this GitHub repo for? What do the issues say?" → works, but auth setup is a chore
- 📡 "Subscribe to these RSS feeds and tell me what's new" → install a library and write code yourself

**None of this is hard, but every platform needs its own setup.** Paid APIs, blocks to route around, logins, data to clean. You'd have to find tools, install dependencies and debug configs one platform at a time.

**Agent Reach turns this into one sentence:**

```
Install Agent Reach: https://raw.githubusercontent.com/Panniantong/agent-reach/main/docs/install.md
```

Copy that to your Agent. A few minutes later, it can read tweets, search Reddit and pull YouTube transcripts.

**Already installed? Update in one sentence:**

```
Update Agent Reach: https://raw.githubusercontent.com/Panniantong/agent-reach/main/docs/update.md
```

### ✅ Before you start, you might want to know

| | |
|---|---|
| 💰 **Completely free** | All tools are open source, all APIs are free. The only possible cost is a server proxy ($1/month) — local computers don't need one |
| 🔒 **Privacy safe** | Cookies stay local. Never uploaded. Fully open source — audit anytime |
| 🔄 **Kept up to date** | Every platform routes through a primary + fallback backend list. When an access path dies, we switch to the next — you won't notice |
| 🤖 **Works with any Agent** | Claude Code, OpenClaw, Cursor, Windsurf… any Agent that can run commands |
| 🩺 **Built-in diagnostics** | `agent-reach doctor` — one command shows what works, what doesn't, and how to fix it |

---

## Supported Platforms

| Platform | Works out of the box | Unlocked after setup | How to set up |
|----------|---------------------|----------------------|---------------|
| 🌐 **Web** | Read any web page | — | No setup ([Jina Reader](https://github.com/jina-ai/reader)) |
| 📺 **YouTube** | Subtitles + video search | Audio transcription for videos without subtitles | No setup ([yt-dlp](https://github.com/yt-dlp/yt-dlp)); free Groq key for transcription |
| 📡 **RSS** | Read any RSS/Atom feed | — | No setup ([feedparser](https://github.com/kurtmckee/feedparser)) |
| 🔍 **Web search** | — | Semantic web search | Auto-configured, free, no API key ([Exa](https://exa.ai) via [mcporter](https://github.com/nicobailon/mcporter)) |
| 📦 **GitHub** | Read public repos + search | Private repos, issues/PRs, forks | Tell your Agent "log me in to GitHub" ([gh CLI](https://cli.github.com)) |
| 🐦 **Twitter/X** | — | Search, timelines, tweets, articles | Tell your Agent "set up Twitter for me" ([twitter-cli](https://github.com/public-clis/twitter-cli)) |
| 📖 **Reddit** | — (no zero-config path: anonymous endpoints are blocked) | Search + read posts and comments | Desktop: [OpenCLI](https://github.com/jackwener/opencli) browser session; or [rdt-cli](https://github.com/public-clis/rdt-cli) + cookie |
| 📘 **Facebook** | — | Search, profiles, feed, groups list | Desktop: OpenCLI (reuses your Chrome session) |
| 📷 **Instagram** | — | User search, profiles, recent posts, Explore | Desktop: OpenCLI (reuses your Chrome session) |
| 💼 **LinkedIn** | Public pages via Jina Reader | Full profiles, companies, job search | Tell your Agent "set up LinkedIn for me" |

> **Not sure how to set something up? No need to read docs.** Tell your Agent "set up XXX for me" — it knows what's needed and walks you through it.
>
> 🍪 Twitter only accepts values the user exports manually with Cookie-Editor. OpenCLI uses only an existing Chrome session the user explicitly controls; Agent Reach never logs the user in or reads browser cookies.
>
> After saving Twitter cookies, they are used only by `agent-reach doctor` to check whether credentials are complete. Before running upstream `twitter` commands directly, you still need `TWITTER_AUTH_TOKEN` and `TWITTER_CT0` set explicitly in that process's environment.
>
> 💻 Local computers don't need a proxy. A proxy is only needed on servers or restricted networks (~$1/month).

---

## Quick Start

> ⚠️ **OpenClaw users: enable `exec` permission first**
>
> Agent Reach relies on the Agent running shell commands (`pip install`, `mcporter`, `twitter`, etc.). If your OpenClaw uses the default `messaging` tool profile, the Agent won't be able to run them. **Enable `exec` before installing:**
>
> ```bash
> openclaw config set tools.profile "coding"
> ```
> Or set `"tools": { "profile": "coding" }` in `~/.openclaw/openclaw.json`. After changing it, restart the Gateway (`openclaw gateway restart`) and start a new conversation. Other platforms (Claude Code, Cursor, Windsurf, etc.) are not affected.

Copy this to your AI Agent (Claude Code, OpenClaw, Cursor, etc.):

```
Install Agent Reach: https://raw.githubusercontent.com/Panniantong/agent-reach/main/docs/install.md
```

That's it. The Agent handles the rest.

> 🔄 **Already installed?** Update in one sentence:
> ```
> Update Agent Reach: https://raw.githubusercontent.com/Panniantong/agent-reach/main/docs/update.md
> ```

> 🛡️ **Safe by default:** `agent-reach install` checks the machine without installing system packages or writing configuration:
> ```
> Safely check and install Agent Reach: https://raw.githubusercontent.com/Panniantong/agent-reach/main/docs/install.md
> ```
> Use `agent-reach install --system` only after explicitly approving system changes.

<details>
<summary>What does it do? (click to expand)</summary>

1. **Install the CLI** — installs the `agent-reach` command from this repository (bundles yt-dlp and feedparser; do not install the same-named PyPI package, which is a different project)
2. **Check system basics** — checks Node.js, gh CLI and mcporter, and shows how to install anything missing
3. **Install and configure with permission** — installs dependencies and connects Exa over MCP only when `--system` is passed explicitly
4. **Detect the environment** — local computer or server, with matching advice
5. **Register SKILL.md with permission** — writes to your Agent's skills directory only with an explicit `--system`; the default check changes no files
6. **Ask if you want more** — only the 5 zero-config channels are active by default; for login-backed ones (Twitter, Reddit, Facebook, Instagram, LinkedIn) the Agent shows a menu and installs only what you name

After installing, `agent-reach doctor` shows each channel's status and which path it currently uses.
</details>

<details>
<summary>Manual install</summary>

```bash
pip install https://github.com/Panniantong/agent-reach/archive/main.zip
agent-reach install --env=auto
```
</details>

<details>
<summary>Install as a Skill (Claude Code / OpenClaw / any agent with Skills support)</summary>

```bash
npx skills add Panniantong/Agent-Reach@agent-reach
```

After the Skill is installed, the Agent will auto-detect whether the `agent-reach` CLI is available and install it if needed.

> If you explicitly install external tools with `agent-reach install --system`, the skill is registered automatically. The default read-only check leaves existing files unchanged.
</details>

---

## Works Out of the Box

No configuration needed — just tell your Agent:

- "Read this link" → `curl https://r.jina.ai/URL` for any web page
- "What's this GitHub repo about?" → `gh repo view owner/repo`
- "What does this YouTube video cover?" → `yt-dlp` extracts subtitles
- "Search the web for LLM framework comparisons" → Exa semantic search
- "Subscribe to this RSS feed" → `feedparser` parses it
- "Search GitHub for LLM frameworks" → `gh search repos "LLM framework"`

**No commands to remember.** The Agent reads SKILL.md and knows what to call. For login-backed platforms (Twitter, Reddit, Facebook, Instagram), tell your Agent "set up XXX for me".

---

## Unlock on Demand

Don't use it? Don't configure it. Every step is optional.

### 🍪 Cookies — Free, 2 minutes

Tell your Agent "help me configure Twitter cookies" — it'll guide you through a
manual Cookie-Editor export. Agent Reach saves the values for `doctor` to check
whether credentials are present; `doctor` does not run `twitter status`.
Direct `twitter` commands still require `TWITTER_AUTH_TOKEN` and `TWITTER_CT0`
in their process environment.

### 🌐 Proxy — $1/month, restricted networks only

Most users need no proxy. If your network blocks Reddit/Twitter, get one ([Webshare](https://webshare.io) recommended, $1/month) and send the address to your Agent — it saves it and exports HTTP(S)_PROXY when calling those tools.

> Reddit needs a logged-in session either way — OpenCLI rides your browser session, or rdt-cli after `rdt login`.

---

## Status at a Glance

```
$ agent-reach doctor

Agent Reach Status
========================================
Legend: ✅ available  [!] installed, needs setup/login  [X] not installed

✅ Ready out of the box:
  [!]  GitHub repos and code — gh CLI runs, but no explicit auth config was found...
  ✅ YouTube videos and subtitles — Can extract video info and subtitles
  ✅ RSS/Atom feeds — Can read RSS/Atom feeds
  [!]  Web-wide semantic search — Exa is in the mcporter config, but Doctor does not start the remote service...
  ✅ Any web page — Reads any web page via Jina Reader (curl https://r.jina.ai/URL)

Status: 3/10 channels available
5 more optional channels can be unlocked (Twitter/X posts; Reddit posts and comments; ...).
```

`[!]` on a login-backed channel is often deliberate: Doctor never runs commands such as `twitter status` or `gh auth status` that would read browser cookies or write files, so it reports those as "not live-verified" instead of ✅.

---

## Design Philosophy

**Agent Reach is a capability layer, not yet another tool.**

It sits one level above any specific implementation — it handles **selection, installation, health checks, and routing**, not the reading itself. Reading is done by your Agent calling upstream tools directly; there is no wrapper layer.

Every time you set up a new Agent, you spend time finding tools, installing deps, and debugging configs — what reads Twitter? How do you log into Reddit? What replaces a CLI that went unmaintained? Every time, you redo the same work. Agent Reach does one simple thing: **the most reliable access path for each platform, chosen, installed, and health-checked for you. Access paths come and go (in March 2026 a batch of single-platform CLIs went unmaintained — we re-routed), so you don't have to care.**

### 🔌 Every platform = an ordered backend list (primary + fallbacks)

Switching access paths means reordering the list, not rewriting code. `agent-reach doctor` tells you **which backend each platform is currently using**.

```
channels/
├── web.py          → Jina Reader
├── twitter.py      → twitter-cli ▸ OpenCLI ▸ bird
├── youtube.py      → yt-dlp
├── github.py       → gh CLI
├── reddit.py       → OpenCLI ▸ rdt-cli (no zero-config path, login required)
├── facebook.py     → OpenCLI (desktop browser session)
├── instagram.py    → OpenCLI (desktop browser session)
├── linkedin.py     → mcp-server-linkedin ▸ Jina Reader
├── rss.py          → feedparser
├── exa_search.py   → Exa via mcporter
└── __init__.py     → Channel registry (for doctor checks)
```

Each channel file **actually probes** its candidate backends in order (not just checking that a command exists) — the first fully working one becomes the active backend, and broken ones come with a fix prescription. The actual reading and searching is done by the Agent calling the upstream tools directly.

### Current Tool Choices

| Scenario | Primary | Fallback | Why |
|----------|---------|----------|-----|
| Read web pages | [Jina Reader](https://github.com/jina-ai/reader) | — | Free, no API key needed |
| Read tweets | [twitter-cli](https://github.com/public-clis/twitter-cli) | [OpenCLI](https://github.com/jackwener/opencli) | Reliable search in real-world tests; OpenCLI falls back on your browser session |
| Reddit | [OpenCLI](https://github.com/jackwener/opencli) (desktop) | [rdt-cli](https://github.com/public-clis/rdt-cli) | Anonymous endpoints blocked, official API gated — logged-in sessions are the only route left |
| Facebook | [OpenCLI](https://github.com/jackwener/opencli) (desktop) | — | Graph/Groups API access is heavily restricted; browser sessions are the practical route |
| Instagram | [OpenCLI](https://github.com/jackwener/opencli) (desktop) | Official Graph API (Business/Creator + review) | Instaloader-style paths are unstable; OpenCLI reuses the real browser session |
| YouTube subtitles + search | [yt-dlp](https://github.com/yt-dlp/yt-dlp) | — | 154K stars, still the best for YouTube |
| Search the web | [Exa](https://exa.ai) via [mcporter](https://github.com/nicobailon/mcporter) | — | AI semantic search, MCP integration, no API key |
| GitHub | [gh CLI](https://cli.github.com) | — | Official tool, full API after auth |
| Read RSS | [feedparser](https://github.com/kurtmckee/feedparser) | — | Python ecosystem standard |
| LinkedIn | [mcp-server-linkedin](https://github.com/stickerdaniel/linkedin-mcp-server) | Jina Reader | MCP server, browser automation |

> 📌 These are the *current* choices, re-verified regularly on real machines. When a path dies we switch to the next — `agent-reach doctor` always tells you which one is active.

---

## Security

Agent Reach is designed with security in mind:

| Measure | Details |
|------|------|
| 🔒 **Local credentials** | Cookies and tokens live only in `~/.agent-reach/config.yaml` on your machine, with 600 permissions (owner read/write only). Never uploaded |
| 🛡️ **Safe by default** | `agent-reach install` changes nothing by default; only an explicit `--system` installs external tools and writes config |
| 👀 **Fully open source** | Transparent code, audit anytime. Every dependency is open source too |
| 🔍 **Dry run** | `agent-reach install --dry-run` previews every action without changing anything |
| 🧩 **Pluggable architecture** | Don't trust a component? Swap out its channel file; nothing else is affected |

### 🍪 Cookie safety

> ⚠️ **Account ban risk:** on cookie-based platforms (Twitter, etc.), scripted/API calls **can be detected and get the account banned**. Always use a **dedicated secondary account**, never your main one.

Platforms that need cookies or a logged-in session (Twitter, Reddit, Facebook, Instagram, etc.) should use a **dedicated secondary account**. Two reasons:
1. **Ban risk** — the platform may detect non-browser API calls and limit or ban the account
2. **Security risk** — a cookie is a full login; a secondary account limits the damage if credentials leak

### 📦 Install modes

| Mode | Command | When |
|------|------|---------|
| Default safe check | `agent-reach install --env=auto` | Any environment; read-only check that lists what's missing |
| Explicit system install | `agent-reach install --env=auto --system` | When you explicitly allow changes to this machine |
| Compatibility safe flag | `agent-reach install --env=auto --safe` | Same as the default |
| Preview only | `agent-reach install --env=auto --dry-run` | See what would happen first |

### 🗑️ Uninstall

```bash
agent-reach uninstall
```

Removes `~/.agent-reach/` (including all tokens/cookies) and every Agent's skill files. mcporter entries are kept unless they can be proven to be managed by Agent Reach.

```bash
# Preview only, delete nothing
agent-reach uninstall --dry-run

# Remove skill files only, keep tokens (for reinstalling)
agent-reach uninstall --keep-config
```

Remove the Python package itself: `pip uninstall agent-reach`

---

## Credits

[OpenCLI](https://github.com/jackwener/opencli) · [twitter-cli](https://github.com/public-clis/twitter-cli) · [rdt-cli](https://github.com/public-clis/rdt-cli) · [yt-dlp](https://github.com/yt-dlp/yt-dlp) · [Jina Reader](https://github.com/jina-ai/reader) · [Exa](https://exa.ai) · [mcporter](https://github.com/nicobailon/mcporter) · [feedparser](https://github.com/kurtmckee/feedparser) · [mcp-server-linkedin](https://github.com/stickerdaniel/linkedin-mcp-server)

## Contact

- 📧 **Email:** pnt01@foxmail.com
- 🐦 **Twitter/X:** [@Neo_Reidlab](https://x.com/Neo_Reidlab)

For collaboration or questions, add me on WeChat — I'll invite you to the community group:

<p align="center">
  <img src="docs/wechat-group-qr.jpg" width="280" alt="WeChat QR">
</p>

> For bug reports and feature requests, please use [GitHub Issues](https://github.com/Panniantong/Agent-Reach/issues) — easier to track.

## License

[MIT](LICENSE)

## Friends

[Agent Skills Hub](https://agentskillshub.top/) — Find Claude skills & MCP servers without guessing what's safe. Every one of 133,000+ entries is security-graded, quality-scored, and refreshed every 8 hours.

[AtomGit mirror](https://atomgit.com/qq_51337814/Agent-Reach) — Synchronized AtomGit mirror for Agent Reach.

## Star History

<a href="https://www.star-history.com/?type=date&repos=Panniantong%2FAgent-Reach"><picture><source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=Panniantong/Agent-Reach&type=date&theme=dark&legend=top-left&sealed_token=K3_u-LJQTVURYu-38Tqa_VWJOSqMf_HbAw-QKSdGwEq6seqznugdIpXdSeztEdOutT40IBXwVxTmg8wS_OSygb5UWf1x8e-Fai6aygrjq6QH8vU09EcqQCN7atp-76HmxX-j9fnZ9NiSrLDNzK98TnXBFJ_Wb_y80I0nWr3O8DdGnLXFhAJgoNK3Jz8D" /><source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=Panniantong/Agent-Reach&type=date&legend=top-left&sealed_token=P2746KOq7grpS8Q-nrqEzci1-Z0-dOw-M3KEqju-l3TyF24NMyRDR7TnxdReJWlXyomoT4mjjqC28-2-c2G6CnzmS1hgYdEDiGPmLkmEqKP5tgjORXshdrUFxoSxTqmIKEMFFmGZUX1v3ec-q_XMyftTVWzluiQH7CvKoZ1uDKU3PJN05mO22u7qlLeG" /><img alt="Star History Chart" src="https://api.star-history.com/chart?repos=Panniantong/Agent-Reach&type=date&legend=top-left&sealed_token=P2746KOq7grpS8Q-nrqEzci1-Z0-dOw-M3KEqju-l3TyF24NMyRDR7TnxdReJWlXyomoT4mjjqC28-2-c2G6CnzmS1hgYdEDiGPmLkmEqKP5tgjORXshdrUFxoSxTqmIKEMFFmGZUX1v3ec-q_XMyftTVWzluiQH7CvKoZ1uDKU3PJN05mO22u7qlLeG" /></picture></a>
