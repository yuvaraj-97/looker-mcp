from mcp.server.fastmcp import FastMCP
from looker_tools import register_looker_tools, get_sdk

# Initialize FastMCP server
mcp = FastMCP("Looker")

@mcp.resource("looker://me")
def get_me() -> str:
    """Get the current Looker user information."""
    sdk = get_sdk()
    if sdk is None:
        return "Looker SDK not initialized"
    me = sdk.me()
    return str(me)

@mcp.prompt("analyze_dashboard")
def analyze_dashboard(dashboard_identifier: str) -> str:
    """Start a session to analyze a specific Looker dashboard."""
    return (
        f"I am working with the Looker dashboard identified by: '{dashboard_identifier}'. "
        "Please use the Looker MCP tools to locate this dashboard, retrieve its layout and underlying queries, "
        "and help me analyze the data."
    )

register_looker_tools(mcp)

def main():
    mcp.run(transport='stdio')

if __name__ == "__main__":
    main()
