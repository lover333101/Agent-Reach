# Troubleshooting

## Twitter/X: twitter-cli fails to connect

**Symptom:** `twitter search` or other commands return errors

**Cause:** twitter-cli needs the `TWITTER_AUTH_TOKEN` and `TWITTER_CT0`
environment variables to reach the Twitter API. The values saved by
`agent-reach configure twitter-cookies` are only used by doctor to check that
the config is complete; doctor does not run upstream authentication and does
not set the current shell. If your network needs a proxy to reach x.com, you
also need to configure one.

**Fixes:**

### Option 1: Set environment-variable proxies

```bash
export TWITTER_AUTH_TOKEN="..."
export TWITTER_CT0="..."
export HTTP_PROXY="http://user:pass@host:port"
export HTTPS_PROXY="http://user:pass@host:port"
twitter search "test" -n 1
```

### Option 2: Use a system-wide proxy tool

Let a proxy tool take over all network traffic so twitter-cli's requests go through it too:

```bash
# macOS — enable "enhanced mode" in ClashX / Surge
# Linux — proxychains or tun2socks
proxychains twitter search "test" -n 1
```

### Option 3: Skip twitter-cli and search with Exa instead

When twitter-cli is unavailable, search Twitter content through Exa:

```bash
mcporter call exa.web_search_exa query="site:x.com search terms" numResults=5
```

### Option 4: Check auth

```bash
twitter check
```

> If it returns "Missing credentials", set `TWITTER_AUTH_TOKEN` and
> `TWITTER_CT0` in the environment of the process that runs the command.
>
> **Fallback:** if you already have bird CLI installed (`npm install -g @steipete/bird`), it works too. Agent Reach detects installed tools automatically.

---

## Reddit: every backend reports a login problem

**Symptom:** `agent-reach doctor` shows Reddit as [!] or [X].

**Cause:** Reddit has no zero-config path. Anonymous `.json` endpoints return
403 and the official API needs manual approval, so a logged-in session is
required.

**Fixes:**

- Desktop: `agent-reach install --system --channels opencli`, install the
  OpenCLI Chrome extension, and log in to reddit.com in Chrome.
- Server: install rdt-cli and write the `reddit_session` cookie exported with
  Cookie-Editor, following the steps in the doctor message.
- If your network blocks Reddit, save a proxy with `agent-reach configure proxy`
  and export `HTTP_PROXY` / `HTTPS_PROXY` before calling `rdt`.
