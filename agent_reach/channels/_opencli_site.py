# -*- coding: utf-8 -*-
"""Shared channel helper for OpenCLI browser-session-only platforms."""

from agent_reach.utils.url import host_matches

from .base import Channel


class OpenCLISiteChannel(Channel):
    """A platform served directly by OpenCLI.

    These channels are intentionally thin: Agent Reach only installs,
    health-checks, and routes. Agents call `opencli <site> ...` directly.
    """

    site: str = ""
    domains: tuple[str, ...] = ()
    usage: str = ""
    login_hint: str = ""

    backends = ["OpenCLI"]
    tier = 1

    def can_handle(self, url: str) -> bool:
        return host_matches(url, *self.domains)

    def check(self, config=None):
        from agent_reach.backends import opencli_status

        self.active_backend = None
        st = opencli_status()
        if not st.installed:
            return "off", (
                f"No backend installed for {self.description}. Install:\n"
                "  agent-reach install --system --channels opencli\n"
                f"Then log in to {self.login_hint} in Chrome"
            )
        if st.broken:
            return "error", st.hint

        if st.ready:
            return "warn", (
                f"OpenCLI bridge is connected, but the {self.login_hint} login and "
                "real commands are not live-verified; Doctor does not run platform "
                "commands, so this is not marked available. "
                f"When needed, log in to {self.login_hint} in Chrome first"
            )
        return "warn", st.hint
