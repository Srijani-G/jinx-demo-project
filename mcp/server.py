"""MCP server exposing internal developer tools to Copilot agents.

Registers a small set of tools (search_runbooks, trigger_deploy) over the
Model Context Protocol so agents can call internal tooling directly.
"""
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("internal-dev-tools")


@mcp.tool()
def search_runbooks(query: str) -> list[str]:
    """Search the internal runbook index."""
    return []


@mcp.tool()
def trigger_deploy(service: str, env: str) -> dict:
    """Kick off a deploy of `service` to `env`."""
    return {"service": service, "env": env, "status": "queued"}


if __name__ == "__main__":
    mcp.run()