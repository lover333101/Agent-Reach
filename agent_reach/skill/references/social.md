# Social media & communities

Twitter/X, Reddit, Facebook, Instagram.

## Twitter/X (twitter-cli)

### Auth prerequisites

Cookies saved through the hidden prompt of `agent-reach configure twitter-cookies`
are used only by `agent-reach doctor` to check that explicit credentials are
complete. `doctor` does not run upstream `twitter status` and does not
configure the current shell. Before running any `twitter` command below, you
must explicitly provide these in the same shell or child-process environment:

```bash
export TWITTER_AUTH_TOKEN="..."
export TWITTER_CT0="..."
```

### Stable commands

```bash
# Home timeline (most stable)
twitter feed -n 20

# Read one tweet (with replies)
twitter tweet URL_OR_ID

# Read a long post / X Article
twitter article URL_OR_ID

# A user's timeline
twitter user-posts @username -n 20

# A user's profile
twitter user @username
```

### Commands that may be unstable

```bash
# Search tweets (Twitter changes GraphQL endpoints often; may 404)
twitter search "query" -n 10

# Likes (since 2024 you can only see your own; platform restriction)
twitter likes
```

### Retry chain when search fails (in order; stop on success)

1. Retry once as-is (sporadic failures are common): `twitter search "query" -n 10`
2. Upgrade and retry: `pipx upgrade twitter-cli && twitter search "query" -n 10`
3. Switch to the OpenCLI fallback (desktop, reuses the browser session): `opencli twitter search "query" -f yaml`
4. If nothing works, route around it with stable commands such as `twitter feed` / `twitter user-posts @somebody`

### Important notes

> **Install**: `pipx install twitter-cli` (make sure it is v0.8.5+)
>
> **Auth**: only export manually with Cookie-Editor, then explicitly set the
> environment variables `TWITTER_AUTH_TOKEN` + `TWITTER_CT0`; do not rely on
> automatic browser reads.
>
> **IP throttling**: do not call it heavily from VPS/data-center IPs, especially followers/following; accounts can get banned. Use a residential proxy or a local machine.
>
> **OpenCLI fallback**: if OpenCLI is installed on the desktop, the full `opencli twitter search/article/user-posts -f yaml` set works (browser session, no cookie env vars needed).
>
> **Output format**: prefer `--yaml` or `--json` for structured output that is easier for AI agents.

## Reddit (multi-backend, login required)

**Reddit has no zero-config path**: the anonymous `.json` endpoints are blocked (403), and since 2025-11 the official API needs manual approval that is rarely granted. Both backends rely on a logged-in session, so run `agent-reach doctor --json` first and check reddit's `active_backend`. Some networks need a proxy to reach Reddit.

### Backend A: OpenCLI (desktop first choice, reuses the browser session)

```bash
# Search posts
opencli reddit search "query" -f yaml

# Read a full post + comments
opencli reddit read POST_ID -f yaml

# Browse a subreddit / hot / popular
opencli reddit subreddit LocalLLaMA -f yaml
opencli reddit hot -f yaml
opencli reddit popular -f yaml

# Subreddit metadata (subscribers, description)
opencli reddit subreddit-info LocalLLaMA -f yaml
```

> Requires Chrome to be open and logged in to reddit.com.

### Backend B: rdt-cli (existing installs/server fallback; upstream unmaintained since 2026-03)

```bash
rdt search "query" --limit 10   # search posts
rdt read POST_ID                # read a full post + comments
rdt sub python --limit 20       # browse a subreddit
rdt popular --limit 10          # browse popular
rdt all --limit 10              # browse /r/all
```

> **Install**: `pipx install 'git+https://github.com/public-clis/rdt-cli.git'` (the PyPI release lags; install v0.4.2+ from GitHub). Run `rdt login` before searching or reading (on a server without a browser, write the cookie manually; see the doctor hint).
> Prefer `--yaml` output; it is easier for AI agents.

### Advanced: official API + PRAW (only for users who already have credentials)

Users who registered a Reddit script app before 2025-11 (and hold a client_id/client_secret) can use PRAW against the official API (100 QPM free). New applications need manual approval that personal projects rarely get, so **do not recommend this path to new users**.

## Facebook (OpenCLI, login required)

Facebook goes through OpenCLI, reusing the facebook.com session in the user's Chrome. Run `agent-reach doctor --json` first and check facebook's `active_backend`; it should normally be `OpenCLI`. Do not recommend Jina/Exa/Graph API as the default path.

```bash
# Search people / pages / posts
opencli facebook search "query" -f yaml

# Person or page info
opencli facebook profile zuck -f yaml

# The current account's News Feed
opencli facebook feed --limit 10 -f yaml

# Groups visible to the current account / recent activity
opencli facebook groups --limit 20 -f yaml
```

> Requires Chrome to be open with the OpenCLI extension installed and logged in to facebook.com. For Facebook Groups, only the group list/recent activity visible to the current account is supported; arbitrary group posts and comments are not.

## Instagram (OpenCLI, login required)

Instagram goes through OpenCLI, reusing the instagram.com session in the user's Chrome. Run `agent-reach doctor --json` first and check instagram's `active_backend`; it should normally be `OpenCLI`. Do not fall back to instaloader by default; historically its cookies/401/429 handling was unstable.

```bash
# Search users (not a site-wide keyword search over posts)
opencli instagram search "query" -f yaml

# A user's profile
opencli instagram profile nasa -f yaml

# A user's recent posts
opencli instagram user nasa --limit 12 -f yaml

# Explore / Discover
opencli instagram explore --limit 20 -f yaml

# The current account's saved posts
opencli instagram saved --limit 20 -f yaml
```

> Requires Chrome to be open with the OpenCLI extension installed and logged in to instagram.com. `instagram search` is a user search; to read posts, identify the username first, then use `instagram user USERNAME`. On 429 / login required, have the user log in again in Chrome and slow down.
