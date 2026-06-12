import logging
import sys

from mcp.server.fastmcp import FastMCP
from looker_tools import register_looker_tools, get_sdk, serialize_result

# Initialize FastMCP server
mcp = FastMCP("Looker")

@mcp.resource("looker://me")
def get_me() -> str:
    """Get the current Looker user information."""
    sdk = get_sdk()
    if sdk is None:
        return "Looker SDK not initialized"
    return serialize_result(sdk.me())

@mcp.prompt("analyze_dashboard")
def analyze_dashboard(dashboard_identifier: str = "") -> str:
    """Start a session to analyze a Looker dashboard. If you leave the identifier blank, the AI will list available dashboards for you to choose from."""
    if dashboard_identifier:
        return (
            f"I am working with the Looker dashboard identified by: '{dashboard_identifier}'. "
            "Please use the Looker MCP tools to locate this dashboard, retrieve its layout and underlying queries, "
            "and help me analyze the data."
        )
    else:
        return (
            "I want to analyze a Looker dashboard, but I don't know the exact name or ID. "
            "Please use the Looker MCP tools to fetch a list of all available dashboards (their programmatic IDs and user-friendly titles). "
            "Present this list to me so I can select one. Once I reply with my selection, remember it for the duration of this session and proceed to analyze it."
        )

register_looker_tools(mcp)

def main():
    # Route all logging to stderr; stdout carries the MCP JSON-RPC stream.
    logging.basicConfig(level=logging.INFO, stream=sys.stderr)
    mcp.run(transport='stdio')

if __name__ == "__main__":
    main()
