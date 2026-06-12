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

register_looker_tools(mcp)

if __name__ == "__main__":
    mcp.run(transport='stdio')
