# Search

The Exa AI search engine.

## Exa AI search

A high-quality AI search engine, good for finding technical docs, official
examples and related pages.

```bash
mcporter call exa.web_search_exa query="query" numResults=5
mcporter call exa.web_search_exa query="library API code example" numResults=5
```

### When to use

| Scenario | Arguments |
|-----|------|
| Web search | `web_search_exa(query: "...", numResults: 5)` |
| Technical/code material | `web_search_exa(query: "framework API example", numResults: 5)` |

> Exa MCP's `get_code_context_exa` is deprecated and not registered by default.
> Use `web_search_exa` for code questions too; to search repository contents
> precisely, use the GitHub search in `dev.md`.

### Strengths

- Strong on English content and technical documentation
- Query wording can target official docs and code examples
- High result quality

## Compared with other search tools

| Tool | Source | Best for |
|-----|------|---------|
| Exa | agent-reach | English/technical/code search |
| GitHub search | agent-reach (dev.md) | Repository/code search |
