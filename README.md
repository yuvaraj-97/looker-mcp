# Looker MCP Server

A Model Context Protocol (MCP) server for Looker, utilizing the official [Looker Python SDK](https://github.com/looker-open-source/sdk-codegen/tree/main/python).

This server dynamically provides **all 483 Looker API methods** as tools for your favorite MCP client!

## Quick Start (Automatic Setup)

If you are using an MCP client (like Claude Desktop, Cursor, or Cline), you can run this server directly from GitHub without any manual setup! The client will automatically fetch and install everything.

Add the following to your client's `mcp_servers.json` (or equivalent configuration):

```json
{
  "mcpServers": {
    "looker": {
      "command": "uvx",
      "args": [
        "--from",
        "git+https://github.com/yuvaraj-97/looker-mcp.git",
        "looker-mcp"
      ],
      "env": {
        "LOOKER_BASE_URL": "https://mycompany.looker.com:19999",
        "LOOKER_CLIENT_ID": "your_client_id",
        "LOOKER_CLIENT_SECRET": "your_client_secret"
      }
    }
  }
}
```

*Note: Ensure you have [`uv`](https://docs.astral.sh/uv/) installed on your machine so `uvx` can automatically run the git repository.*

## Manual Setup (Local Development)

If you'd like to run it locally or contribute:

1. Clone the repository and install dependencies:
   ```bash
   git clone https://github.com/yuvaraj-97/looker-mcp.git
   cd looker-mcp
   pip install .
   ```

2. Configure Looker Authentication. Set the following environment variables, or create a `looker.ini` file in the working directory:
   - `LOOKER_BASE_URL`: The URL of your Looker instance
   - `LOOKER_CLIENT_ID`: Your Looker API Client ID
   - `LOOKER_CLIENT_SECRET`: Your Looker API Client Secret

   If using `looker.ini`, format it as follows:
   ```ini
   [Looker]
   base_url=https://your_looker_endpoint:19999
   client_id=your_client_id
   client_secret=your_client_secret
   verify_ssl=True
   ```

3. Run the MCP server via standard IO:
   ```bash
   looker-mcp
   ```
