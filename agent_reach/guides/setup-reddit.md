# Reddit Setup Guide

## What it does

Reddit blocks almost all non-browser direct access (including data-center and ISP proxy IPs); the JSON API returns 403.

On desktop, Agent Reach prefers **OpenCLI**, which reuses your logged-in Chrome session. On servers or existing installs it uses **rdt-cli** for Reddit search and reading:
- **Search**: `rdt search "keywords"`
- **Read a full post + comments**: `rdt read POST_ID`

Free, with no API key. A logged-in session is required (`rdt login` extracts cookies from the browser itself; on a server, write the cookie manually per the doctor hint).

## Steps the Agent can do automatically

1. Check whether rdt-cli is available:
```bash
which rdt && echo "installed" || echo "not installed"
```

2. If it isn't, install it (the PyPI release lags behind; install the latest from GitHub):
```bash
pipx install 'git+https://github.com/public-clis/rdt-cli.git'
```

Or use the one-step installer (desktop installs OpenCLI, servers install rdt-cli):
```bash
agent-reach install --env=auto --system --channels=reddit
```

## Usage

Search Reddit:
```bash
rdt search "python best practices" -n 5
```

Read a full post with comments:
```bash
rdt read POST_ID
```

## Steps the user must do manually

Log in to reddit.com (in Chrome for OpenCLI, or via `rdt login` / a Cookie-Editor export for rdt-cli). After the user explicitly approves, the tools themselves are installed by
`agent-reach install --env=auto --system --channels=reddit`.

## Fallback: Exa search

If Exa is configured (through mcporter), you can also search Reddit content with Exa:

```bash
mcporter call exa.web_search_exa query="site:reddit.com python best practices" numResults=5
```
