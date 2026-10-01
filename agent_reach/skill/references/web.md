# Web reading

General web pages and RSS.

## General web pages (Jina Reader)

```bash
# Read any web page
curl -s "https://r.jina.ai/URL"

# Example
curl -s "https://r.jina.ai/https://example.com/article"
```

**When to use**: most web pages can be read directly with Jina Reader.

## Web Reader (MCP)

```bash
# Read a page (Markdown)
mcporter call web-reader.webReader url="https://example.com"

# Keep images
mcporter call web-reader.webReader url="https://example.com" retain_images=true

# Plain text
mcporter call web-reader.webReader url="https://example.com" return_format="text"
```

**When to use**: when you need finer control over the output format.

## RSS (feedparser)

```python
python3 -c "
import feedparser
for e in feedparser.parse('FEED_URL').entries[:5]:
    print(f'{e.title} — {e.link}')
"
```

**When to use**: following blogs, news feeds, podcasts and other RSS feeds.

## Choosing a tool

| Scenario | Recommended tool |
|-----|---------|
| General web page | Jina Reader (`curl r.jina.ai`) |
| Need images/format control | web-reader MCP |
| RSS feeds | feedparser |
