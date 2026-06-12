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

## Example Usage Scenario

Once the Looker MCP server is connected to your AI assistant, you can ask the AI to perform complex data workflows naturally. Here are some examples of what you can say:

**Prompt 1: "Find the Q3 Sales dashboard and give me a summary of the data."**
1. The AI uses the `search_dashboards(title="Q3 Sales")` tool to get the dashboard ID.
2. The AI uses the `dashboard(dashboard_id="...")` tool to retrieve the dashboard details and underlying query IDs.
3. The AI runs `run_query(query_id="...", result_format="json")` to extract the raw data and then writes a natural language summary for you!

**Prompt 2: "Create a new user for John Doe and add them to the Marketing group."**
1. The AI calls `create_user(body={"first_name": "John", "last_name": "Doe"})`.
2. The AI searches for the Marketing group using `search_groups(name="Marketing")`.
3. The AI assigns the user using `add_group_user(group_id="...", body={"user_id": "..."})`.

**Prompt 3: "List all broken looks or queries that failed recently."**
1. The AI might query `all_looks()` and check their status, or look into the system activity queries to find recently failed query tasks using `all_query_tasks()`.

Because the AI has access to **every single endpoint** Looker provides, the possibilities are nearly limitless!

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
