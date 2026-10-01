# Exa Search Setup Guide

## What it does
Exa is an AI semantic search engine. It connects over MCP and is **free, with no API key**. Once set up it unlocks:
- Web-wide semantic search
- Reddit search (via site:reddit.com)
- Twitter search (via site:x.com)

## Steps the Agent can do automatically

After the user explicitly approves, `agent-reach install --env=auto --system` performs these steps.
The default command without `--system` only does a read-only check.

### 1. Install mcporter
```bash
npm install -g mcporter
```

### 2. Register the Exa MCP server
```bash
mcporter config add exa https://mcp.exa.ai/mcp --scope home
```

### 3. Verify
```bash
agent-reach doctor | grep "search"
mcporter call exa.web_search_exa query="test" numResults=1
```

## Steps the user must do manually

**None.** Exa connects over MCP; it's free with no sign-up and no API key.

If `agent-reach install --system` could not configure Exa because of a network problem, run the two commands above manually.

## FAQ

**Q: Is there a search limit?**
A: The MCP endpoint is provided by Exa itself (mcp.exa.ai) and is currently free without limits. If that changes, agent-reach updates will adapt.

**Q: What is mcporter?**
A: A command-line bridge for the MCP protocol, used to call MCP servers. Agent Reach uses it to connect to Exa and LinkedIn.
