# Agent Reach — Installation Guide

## For Humans

Copy this to your AI Agent:

```
Install Agent Reach: https://raw.githubusercontent.com/Panniantong/agent-reach/main/docs/install.md
```

> 🛡️ **Safe by default:** `agent-reach install` only checks the machine and lists missing dependencies:
> ```
> Safely check and install Agent Reach: https://raw.githubusercontent.com/Panniantong/agent-reach/main/docs/install.md
> ```
> Only use `--system` after the user explicitly approves system-level installs and configuration writes.

---

## For AI Agents

### Goal

Install Agent Reach and all upstream tools so your user's agent has full internet access. After installation, you'll use the upstream tools directly (OpenCLI, twitter-cli, rdt-cli, yt-dlp, mcporter, gh CLI, etc.) — Agent Reach is the selector, installer, health checker and router, never a wrapper.

### ⚠️ Boundaries

When fixing issues, stay within these limits:

- **DO NOT** run commands with `sudo` unless the user explicitly approved
- **DO NOT** modify system files outside `~/.agent-reach/`
- **DO NOT** install packages not listed in this guide
- **DO NOT** disable firewalls, security settings, or system protections
- **DO NOT** clone repos, create files, or run commands inside the agent workspace / working directory
- If something requires elevated permissions, **tell the user** what's needed and let them decide

### 📁 Directory Rules

All Agent Reach files go in dedicated directories — **never in the agent workspace**:

| Purpose | Directory | Example |
|---------|-----------|---------|
| Config & tokens | `~/.agent-reach/` | `~/.agent-reach/config.yaml` |
| Upstream tool files | `~/.agent-reach/tools/` | `~/.agent-reach/tools/` |
| Temporary files | `/tmp/` | `/tmp/yt-dlp-output/` |
| Skills | `~/.openclaw/skills/agent-reach/` | SKILL.md |

**Why?** If you clone repos or create files in the workspace, it pollutes the user's project directory and can break their agent over time. Keep the workspace clean.

### Step 1: Install the basics

```bash
# Recommended: pipx (least hassle)
pipx install https://github.com/Panniantong/agent-reach/archive/main.zip
agent-reach install --env=auto               # Read-only check (default)
# After the user explicitly approves system changes:
agent-reach install --env=auto --system

# If your Python comes from Homebrew / you hit PEP 668 (externally-managed-environment),
# install into a virtual environment:
python3 -m venv ~/.agent-reach-venv
source ~/.agent-reach-venv/bin/activate
pip install https://github.com/Panniantong/agent-reach/archive/main.zip
agent-reach install --env=auto               # Read-only check (default)
# After the user explicitly approves system changes:
agent-reach install --env=auto --system
```

> 💡 **Windows / Microsoft Store Python alias?**
> If `python3 --version` opens the Microsoft Store, or `where python3` points to
> `...\AppData\Local\Microsoft\WindowsApps\python3.exe`, then `python3` is the
> Windows Store alias, not a usable Python install. Use the Python Launcher
> `py -3` instead, or the `python.exe` in the actual install directory.
>
> PowerShell example:
> ```powershell
> py -3 -m venv $env:USERPROFILE\.agent-reach-venv
> $env:USERPROFILE\.agent-reach-venv\Scripts\Activate.ps1
> python -m pip install https://github.com/Panniantong/agent-reach/archive/main.zip
> agent-reach install --env=auto
> ```

The default command checks core infrastructure (gh CLI, Node.js, mcporter, Exa search, yt-dlp config) without changing the host. With explicit `--system` approval it installs/configures the missing pieces and activates these zero-config channels:

- Web (Jina Reader), YouTube, GitHub, RSS, Exa Search

> 💡 **macOS / Homebrew Python reports `externally-managed-environment`?**
> That is PEP 668 protection, not an Agent Reach problem. Prefer `pipx install ...`, or create a `venv` first and install into it.

**Install modes:**

```bash
agent-reach install --env=auto             # Check only; safe default
agent-reach install --env=auto --safe      # Same check-only behavior (compatibility)
agent-reach install --env=auto --system    # Explicitly allow external/system installs
agent-reach install --env=auto --dry-run   # Preview what --system would do
```

### Step 2: Ask the user which optional channels they want

After installing the basics, **ask the user** which additional channels they need. Present this list:

> The basic channels are ready! You can now ask me to search the web, watch YouTube, read GitHub and more.
>
> These optional channels are also available. Which ones do you want?
>
> - 🌟 **OpenCLI** (recommended on desktop) — one install covers Reddit/Facebook/Instagram and a Twitter fallback; it only uses an existing Chrome session that you explicitly control
> - 🐦 **Twitter/X** — search tweets, browse timelines (needs login cookies)
> - 📖 **Reddit** — search and read posts (login required: desktop OpenCLI, or rdt-cli + cookie)
> - 📘 **Facebook** — search, profiles, feed, groups list (desktop OpenCLI, reuses your Chrome session)
> - 📷 **Instagram** — user search, profiles, recent posts, Explore (desktop OpenCLI, reuses your Chrome session)
> - 💼 **LinkedIn** — profiles, job search
> - 🎙️ **Audio transcription** — transcribe videos/podcasts without subtitles (needs a free Groq key)
>
> Tell me which ones, e.g. "install Twitter and Reddit" or "install Facebook and Instagram". Or say "install everything".

Based on the user's choice, run:

```bash
agent-reach install --env=auto --system --channels=opencli,reddit         # Desktop user chose Reddit
agent-reach install --env=auto --system --channels=facebook,instagram    # Desktop Meta channels
agent-reach install --env=auto --system --channels=all                   # User approved everything
```

Supported channel names: `opencli`, `twitter`, `reddit`, `facebook`, `instagram`, `linkedin`, `all`

### Step 3: Configure things that need user input

Some channels need credentials only the user can provide. Based on the doctor output, ask for what's missing:

> 🔒 **Security tip:** For platforms that need cookies or browser sessions (Twitter, Reddit, Facebook, Instagram), we recommend using a **dedicated/secondary account** rather than your main account. Cookie/browser-session auth carries two risks:
> 1. **Account ban** — platforms may detect non-browser API calls and restrict or ban the account
> 2. **Credential exposure** — cookies grant full account access; using a secondary account limits the blast radius if credentials are ever compromised

> 🍪 **Cookies / login sessions:**
>
> For traditional CLIs that need cookies (Twitter), **import with Cookie-Editor** — it is the simplest and most reliable way:
> 1. The user logs in to the platform in their own browser
> 2. Install the [Cookie-Editor](https://chromewebstore.google.com/detail/cookie-editor/hlkenndednhfkekhgcdicdfddnkalmdm) Chrome extension
> 3. Click the extension → Export → Header String
> 4. Send the exported string to the Agent
>
> Twitter only accepts values the user explicitly exports with Cookie-Editor. Agent Reach never logs the user in and never reads browser cookie stores. OpenCLI only uses an existing Chrome session that the user explicitly controls.

**Twitter search & posting:**
> "To unlock Twitter search, I need your Twitter cookies. Install the Cookie-Editor Chrome extension, go to x.com/twitter.com, click the extension → Export → Header String, and paste it to me."

```bash
agent-reach configure twitter-cookies
```

This saves `twitter_auth_token` and `twitter_ct0` for Agent Reach's own
`doctor` config check. `doctor` does not run upstream `twitter status` live and
does not modify the current shell. Before running `twitter search/read/...`
directly, set these explicitly in that process's environment:

```bash
export TWITTER_AUTH_TOKEN="..."
export TWITTER_CT0="..."
twitter search "query" -n 10
```

> **Proxy note (networks that block Twitter/Reddit):**
>
> twitter-cli and rdt-cli are Python tools; on networks that need a proxy, configure it through environment variables.
>
> **What you (the Agent) do:**
> 1. Make sure the user saved a proxy: `agent-reach configure proxy` (hidden input)
> 2. Set the environment variables: `export HTTP_PROXY="..." HTTPS_PROXY="..."`
> 3. Agent Reach handles the rest; the user needs to do nothing else
>
> If the user reports "fetch failed", see [troubleshooting.md](troubleshooting.md)

**Reddit (login is mandatory — no zero-config path):**
> Reddit's anonymous endpoints are blocked and the official API needs manual approval. Desktop users should prefer OpenCLI (works once logged in to reddit.com in the browser); server/existing users use rdt-cli:

```bash
# PyPI lags behind; install from GitHub (same pinned version as _RDT_GIT_SOURCE in the code)
pipx install 'git+https://github.com/public-clis/rdt-cli.git@5e4fb3720d5c174e976cd425ccc3b879d52cac66'
rdt login   # extracts browser cookies itself; on a server without a browser, write the cookie manually per the doctor hint
```

> Some networks need a proxy to reach Reddit; if a server IP gets throttled, use a residential proxy (e.g. https://webshare.io, about $1/month):
> ```bash
> agent-reach configure proxy
> ```

**Facebook / Instagram (desktop OpenCLI):**
> Both platforms use OpenCLI: it reuses the user's own Chrome session, stores no username or password, and skips the Meta Graph API approval process. Servers/headless environments are not recommended.

```bash
agent-reach install --system --channels facebook,instagram
```

> After installing, guide the user through the one manual step (Chrome security rules make it impossible to do for them):
> 1. Open https://chromewebstore.google.com/detail/opencli/ildkmabpimmkaediidaifkhjpohdnifk
> 2. Click "Add to Chrome"
> 3. Run `opencli doctor` to verify (it should show Extension: connected)
>
> Then:
> 1. Log in to facebook.com / instagram.com in Chrome
> 2. The Agent calls OpenCLI directly:
>    ```bash
>    opencli facebook search "query" -f yaml
>    opencli facebook profile zuck -f yaml
>    opencli facebook groups -f yaml
>    opencli instagram search "query" -f yaml     # user search
>    opencli instagram profile nasa -f yaml
>    opencli instagram user nasa -f yaml          # recent posts from one user
>    ```
>
> On AUTH_REQUIRED, never log in on the user's behalf; ask them to log in in Chrome themselves.
>
> Facebook Groups currently only covers the group list/recent activity visible to the logged-in user; arbitrary group posts and comments are not supported. Instagram's search is a user search, not a site-wide keyword search over posts; on 429/login errors, have the user log in again in Chrome and slow down.

**Audio transcription (Groq Whisper):**
> "Transcription for videos and podcasts without subtitles is built in; it only needs a free Groq API key."

```bash
agent-reach configure groq-key
```

> **Get a Groq API key (free, no credit card, 30 seconds):**
> 1. Open https://console.groq.com
> 2. Sign in (or sign up) with a Google/GitHub account
> 3. Left menu → API Keys → Create API Key
> 4. Copy the key (starts with `gsk_`) and send it to the Agent
>
> **Usage:**
> When the user sends a video or podcast link without subtitles, the Agent runs:
> ```bash
> agent-reach transcribe "https://example.com/episode.mp3"
> ```
>
> **Free quota and limits:**
> - About 2 hours of audio per hour (7200 seconds); after that, wait about 15 minutes for it to reset
> - Plenty for a few podcast episodes a day
> - High transcription quality (Whisper large-v3), but no speaker separation
> - Split recordings longer than 2 hours into batches

**LinkedIn (optional — mcp-server-linkedin):**
> "Basic LinkedIn content can be read through Jina Reader. Full features (profile details, people and job search) need mcp-server-linkedin."

> **Setup (stdio recommended):**
> First install `uv` (which also provides `uvx`) following the official instructions:
> https://docs.astral.sh/uv/getting-started/installation/
>
> ```bash
> mcporter config add linkedin --command uvx --arg mcp-server-linkedin@latest --env UV_HTTP_TIMEOUT=300 --scope home
> ```
>
> `uvx` fetches and starts the latest server on demand; no separate Python package or long-running HTTP service is needed.
>
> **First login (needs a browser window):**
> ```bash
> uvx mcp-server-linkedin@latest --login
> ```
> Log in to LinkedIn manually when the browser opens; the session is saved to `~/.linkedin-mcp/profile/`. On a headless server, run the same login command inside a visible desktop such as VNC.
>
> Details: https://github.com/stickerdaniel/linkedin-mcp-server

### Step 4: Fix what's broken and do a final check

Run `agent-reach doctor` and check the output.

Try to get as many channels to ✅ as possible. If something failed during install or shows as [X]/[!] in doctor, diagnose the problem and try to fix it — but stay within the boundaries above. If a fix requires elevated permissions or system changes, ask the user first.

Only ask the user when you genuinely need their input (credentials, permissions, etc.). When you're done, run `agent-reach doctor` one final time and report the results to your user.

### Step 5: Set up daily monitoring (OpenClaw only)

If you are running inside **OpenClaw**, ask your user:

> "Agent Reach is installed. Want me to set up a daily automatic check? It keeps an eye on whether these channels still work and whether there's a new version. It only notifies you when something is wrong."

If the user agrees, create a **cron job** (daily, `sessionTarget: "isolated"`, `delivery: "announce"`) with this task:

```
Run the agent-reach watch command.
If the output contains "all good", do not notify the user; finish silently.
If the output lists problems ([X] or [!]) or "New version available", send the full report to the user with suggested fixes.
If a new version is available, ask the user whether to upgrade (sending this one line to the user's Agent performs a full update: Update Agent Reach for me: https://raw.githubusercontent.com/Panniantong/agent-reach/main/docs/update.md).
```

If the user wants a different agent to handle it, let them choose.

---

## Quick Reference

| Command | What it does |
|---------|-------------|
| `agent-reach install --env=auto` | Read-only dependency and channel check (default) |
| `agent-reach install --env=auto --system` | Explicitly install/configure core external tools |
| `agent-reach install --env=auto --system --channels=twitter,reddit` | Install approved optional channels |
| `agent-reach install --env=auto --system --channels=all` | Install everything after explicit approval |
| `agent-reach install --env=auto --safe` | Compatibility alias for the safe default |
| `agent-reach install --env=auto --dry-run` | Preview what would be done |
| `agent-reach doctor` | Show channel status |
| `agent-reach watch` | Quick health + update check (for scheduled tasks) |
| `agent-reach check-update` | Check for new versions |
| `agent-reach configure twitter-cookies` | Save Twitter cookies via hidden input; direct calls still need explicit env vars |
| `agent-reach configure proxy` | Save a proxy address via hidden input; not an automatic unlock switch |
| `agent-reach configure groq-key` | Save the Groq transcription key via hidden input |
| `agent-reach transcribe URL` | Transcribe audio/video without subtitles |

After installation, use upstream tools directly. See SKILL.md for the full command reference:

| Platform | Upstream Tool | Example |
|----------|--------------|---------|
| Twitter/X | `twitter` (fallback `opencli`) | Set `TWITTER_AUTH_TOKEN` / `TWITTER_CT0`, then run `twitter search "query" -n 10` |
| YouTube | `yt-dlp` | `yt-dlp --dump-json URL` |
| Reddit | `opencli` (fallback `rdt`) | `opencli reddit search "query" -f yaml` / `rdt read POST_ID` |
| Facebook | `opencli` | `opencli facebook search "query" -f yaml` |
| Instagram | `opencli` | `opencli instagram user nasa -f yaml` |
| GitHub | `gh` | `gh search repos "query"` |
| Web | `curl` + Jina | `curl -s "https://r.jina.ai/URL"` |
| Exa Search | `mcporter` | `mcporter call exa.web_search_exa query="..." numResults=5` |
| LinkedIn | `mcporter` | `mcporter call linkedin.get_person_profile linkedin_username="..."` |
| RSS | `feedparser` | `python3 -c "import feedparser; ..."` |
| Audio without subtitles | `agent-reach transcribe` | `agent-reach transcribe URL` |

> For multi-backend platforms, `active_backend` in `agent-reach doctor --json` is the source of truth.
