# Changelog

All notable changes to this project will be documented in this file.

---

## [Unreleased]

### 💥 Breaking Changes

#### 🌍 English-only build with China-only platforms removed

- Removed the XiaoHongShu, Bilibili, Boss Zhipin, Xueqiu, V2EX and Xiaoyuzhou
  channels, their installers, the `xhs-cookies` configure key, the xhs-only
  `format` command and the Xiaoyuzhou transcription script. 10 channels remain:
  Web, Twitter/X, YouTube, GitHub, Reddit, Facebook, Instagram, LinkedIn, RSS
  and Exa search. (The unreleased Boss Zhipin channel work was dropped with it.)
- Removed `agent-reach configure --from-browser`: every remaining login
  platform is Cookie-Editor-only, so browser cookie-store extraction (and the
  `cookies` extra / browser-cookie3) is gone. The Twitter legacy credential
  sync (`--sync-legacy-twitter`) is unchanged.
- All CLI output, doctor messages, docs, guides and the agent skill are now
  in English. `agent-reach skill --install` always installs the single
  English `SKILL.md`; the `SKILL_en.md` variant and `AGENT_REACH_LANG`
  switch are removed. The Japanese and Korean READMEs are removed.

## [1.3.1] - 2026-03-27

### 🐛 Bug Fixes

#### 📈 Xueqiu — full fix

- **Fixed the root cause of the 400 errors:** `_ensure_cookies()` only visited the homepage, which yields just `acw_tc` (an anti-DDoS token); `xq_a_token` is generated dynamically by Xueqiu's front-end JS and cannot be obtained with plain HTTP requests. Added a three-level cookie loading strategy: ① read the config file (saved by `--from-browser`) → ② extract automatically from the local Chrome browser (requires browser-cookie3) → ③ homepage fallback
- **Fixed the User-Agent:** `"agent-reach/1.0"` was recognized and rejected by Xueqiu's anti-scraping system; switched to a real Chrome UA
- **Fixed the missing `Referer` header:** every API request now sends `Referer: https://xueqiu.com/`
- **Fixed the `get_hot_posts()` endpoint:** the old `/statuses/hot/listV3.json` endpoint was deprecated (empty body); switched to `/v4/statuses/public_timeline_by_category.json` and correctly parse the `item.data` JSON string for author/likes/text
- **Fixed `urllib.request.quote` → `urllib.parse.quote`:** use the correct module explicitly
- **Fixed `configure --from-browser` not extracting Xueqiu cookies:** added Xueqiu to `PLATFORM_SPECS` and only save when `xq_a_token` is present
- **Corrected misleading docs:** "no setup needed" / "public API, no login required" in README/SKILL.md → accurately describe that a browser cookie is required
- **Better error messages:** a failing `check()` now suggests `configure --from-browser chrome` instead of "may need a proxy"

---

## [1.3.0] - 2026-03-12

### 🆕 New Channels

#### 💻 V2EX
- Hot topics, node topics, topic detail + replies, user profile via public JSON API
- Zero config — no auth, no proxy, no API key required
- `get_hot_topics(limit)`, `get_node_topics(node_name, limit)`, `get_topic(id)`, `get_user(username)`

### 📈 Improvements

- Channel count: 14 → 15

---

## [1.1.0] - 2025-02-25

### 🆕 New Channels

#### ~~📷 Instagram~~ (removed — upstream blocked)
- ~~Read public posts and profiles via [instaloader](https://github.com/instaloader/instaloader)~~
- **Removed:** Instagram's aggressive anti-scraping measures broke all available open-source tools (instaloader, etc.). See [instaloader#2585](https://github.com/instaloader/instaloader/issues/2585). Will re-add when upstream recovers.

#### 💼 LinkedIn
- Read person profiles, company pages, and job details via [linkedin-scraper-mcp](https://github.com/stickerdaniel/linkedin-mcp-server)
- Search people and jobs via MCP, with Exa fallback
- Fallback to Jina Reader when MCP is not configured

#### 🏢 Boss Zhipin
- Job search and recruiter greeting via [mcp-bosszp](https://github.com/mucsbr/mcp-bosszp) over MCP
- Fallback to Jina Reader for reading job pages

### 📈 Improvements

- Channel count: 9 → 12
- `agent-reach doctor` now detects all 12 channels
- CLI: added `search-linkedin`, `search-bosszhipin` subcommands
- Updated install guide with setup instructions for new channels

---

## [1.0.0] - 2025-02-24

### 🎉 Initial Release

- 9 channels: Web, Twitter/X, YouTube, Bilibili, GitHub, Reddit, XiaoHongShu, RSS, Exa Search
- CLI with `read`, `search`, `doctor`, `install` commands
- Unified channel interface — each platform is a single pluggable Python file
- Auto-detection of local vs server environments
- Built-in diagnostics via `agent-reach doctor`
- Skill registration for Claude Code / OpenClaw / Cursor
