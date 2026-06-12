# Looker MCP Server

A Model Context Protocol (MCP) server for Looker, utilizing the official [Looker Python SDK](https://github.com/looker-open-source/sdk-codegen/tree/main/python).

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Configure Looker Authentication. Set the following environment variables, or create a `looker.ini` file in the working directory:
   - `LOOKER_BASE_URL`: The URL of your Looker instance (e.g. `https://mycompany.looker.com:19999`)
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

## Running

Run the MCP server via standard IO:
```bash
python server.py
```
