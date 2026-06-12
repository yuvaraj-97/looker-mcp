import os
import looker_sdk
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("Looker")

# Initialize Looker SDK
# It relies on LOOKER_BASE_URL, LOOKER_CLIENT_ID, LOOKER_CLIENT_SECRET
# environment variables, or a looker.ini file.
try:
    sdk = looker_sdk.init40()
except Exception as e:
    # Will fail if env vars / ini not present. 
    # For MCP, we should probably initialize lazily or let it crash on startup if not configured.
    print(f"Warning: Failed to initialize Looker SDK: {e}")
    sdk = None

@mcp.resource("looker://me")
def get_me() -> str:
    """Get the current Looker user information."""
    if sdk is None:
        return "Looker SDK not initialized"
    me = sdk.me()
    return str(me)

@mcp.tool()
def search_dashboards(title: str) -> str:
    """Search for Looker dashboards by title."""
    if sdk is None:
        return "Looker SDK not initialized"
    dashboards = sdk.search_dashboards(title=title)
    return str([{"id": d.id, "title": d.title} for d in dashboards])

@mcp.tool()
def run_look(look_id: int, format: str = "json") -> str:
    """Run a specific Look by ID and get results."""
    if sdk is None:
        return "Looker SDK not initialized"
    result = sdk.run_look(look_id=look_id, result_format=format)
    return str(result)

if __name__ == "__main__":
    mcp.run(transport='stdio')
