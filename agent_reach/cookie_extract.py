# -*- coding: utf-8 -*-
"""Legacy Twitter credential sync for older upstream tools.

`agent-reach configure twitter-cookies --sync-legacy-twitter` copies the
Cookie-Editor credentials into the files xfetch and bird read. Agent Reach
never reads browser cookie stores itself.
"""

from pathlib import Path

_MAX_XFETCH_SESSION_BYTES = 64 * 1024


def _read_xfetch_session(path: Path) -> dict:
    """Read a small regular legacy session file without following symlinks."""
    import json

    from agent_reach.utils.paths import read_small_text_no_follow

    payload = read_small_text_no_follow(
        path,
        max_bytes=_MAX_XFETCH_SESSION_BYTES,
    )
    if payload is None:
        return {}
    loaded = json.loads(payload)
    if not isinstance(loaded, dict):
        raise ValueError("xfetch session file must be a JSON object")
    return loaded


def _sync_xfetch_session(auth_token: str, ct0: str) -> bool:
    """Sync Twitter credentials to ~/.config/xfetch/session.json (legacy xreach compat)."""
    import json

    try:
        from agent_reach.utils.paths import (
            atomic_write_private_text,
            home_dir,
            make_private_dir,
        )

        xfetch_dir = home_dir() / ".config" / "xfetch"
        make_private_dir(xfetch_dir)
        session_path = Path(xfetch_dir) / "session.json"
        session_data = _read_xfetch_session(session_path)
        session_data["authToken"] = auth_token
        session_data["ct0"] = ct0
        atomic_write_private_text(
            session_path,
            json.dumps(session_data, indent=2),
        )
        return True
    except Exception:
        # Non-fatal: agent-reach config is the source of truth, xfetch sync is best-effort
        return False


def _sync_bird_env(auth_token: str, ct0: str) -> bool:
    """Write Twitter credentials to ~/.config/bird/credentials.env for bird CLI.

    bird reads AUTH_TOKEN and CT0 from environment variables. This writes a
    shell-sourceable file so users can `source ~/.config/bird/credentials.env`.
    Values are passed through shlex.quote so a token containing a quote, $, or
    backtick cannot break out into shell syntax when the file is sourced.
    """
    import shlex

    try:
        from agent_reach.utils.paths import (
            atomic_write_private_text,
            home_dir,
            make_private_dir,
        )

        bird_dir = home_dir() / ".config" / "bird"
        make_private_dir(bird_dir)
        env_path = bird_dir / "credentials.env"
        atomic_write_private_text(
            env_path,
            f"AUTH_TOKEN={shlex.quote(auth_token)}\n"
            f"CT0={shlex.quote(ct0)}\n",
        )
        return True
    except Exception:
        # Non-fatal: agent-reach config is the source of truth, bird env sync is best-effort
        return False


# Alias for callers expecting the name _sync_bird_credentials
_sync_bird_credentials = _sync_bird_env
