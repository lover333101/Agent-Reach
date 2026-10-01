# Twitter Advanced Setup Guide (twitter-cli)

Basic Twitter reading works for free through Jina Reader with no setup.

Advanced features need twitter-cli (@public-clis/twitter-cli):

- Search tweets (`twitter search`)
- Read full tweets and conversation threads (`twitter tweet`, `twitter thread`)
- User timelines (`twitter timeline`)
- Long-form articles (`twitter article`)

twitter-cli is a free open-source tool (installed with pipx), but it needs your Twitter account cookies.

## Quick setup

1. Check whether twitter-cli is installed:

```bash
which twitter && echo "installed" || echo "not installed"
```

2. Install twitter-cli:

```bash
pipx install twitter-cli
```

3. Confirm the command is installed (no auth request is made at this point):

```bash
twitter --help
```

## Getting the cookies (Cookie-Editor, recommended)

1. Install the [Cookie-Editor](https://cookie-editor.com/) browser extension
2. Log in to x.com
3. Click the Cookie-Editor icon → Export → Header String
4. Run the configure command:

```bash
agent-reach configure twitter-cookies
```

This extracts `auth_token` and `ct0` and saves them securely to
`~/.agent-reach/config.yaml`, so `agent-reach doctor` can check whether explicit
credentials are complete. Doctor will not run `twitter status`: it does not
live-verify the account and does not modify the current shell.

By default it only writes `~/.agent-reach/config.yaml`. Only when the user
explicitly agrees to copy the credentials and adds `--sync-legacy-twitter`
does it also write:

- `~/.config/xfetch/session.json`
- `~/.config/bird/credentials.env`

```bash
agent-reach configure twitter-cookies --sync-legacy-twitter
```

`agent-reach uninstall` only warns about these legacy copies; it never deletes
them automatically. To clean them up, confirm with the user first, then delete
those two files by hand.

`twitter` is a separate upstream command and does not read Agent Reach's
config file. When running `twitter status/search/read/...` directly, set
`TWITTER_AUTH_TOKEN` and `TWITTER_CT0` explicitly in the current shell or
child-process environment, as in the next section. Do not rely on automatic
browser cookie reads.

## Setting the cookies manually

If you already know `auth_token` and `ct0`:

1. Install twitter-cli (if needed): `pipx install twitter-cli`

2. Set the environment variables:

```bash
export TWITTER_AUTH_TOKEN="your_auth_token"
export TWITTER_CT0="your_ct0"
```

3. Test:

```bash
twitter search "test" -n 1
```

## Proxy setup

> twitter-cli supports proxies through environment variables:

```bash
export HTTP_PROXY="http://user:pass@host:port"
export HTTPS_PROXY="http://user:pass@host:port"
twitter search "test" -n 1
```

You can also use a system-wide proxy tool:

```bash
proxychains twitter search "test" -n 1
```

## Fallback: bird CLI

If you already have [bird CLI](https://www.npmjs.com/package/@steipete/bird) installed (`npm install -g @steipete/bird`), it works too. Agent Reach detects and uses an installed bird automatically. The two are similar; twitter-cli is the current recommendation.
