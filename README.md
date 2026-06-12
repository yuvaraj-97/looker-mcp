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

## ⚡ Middle-Ground Optimization

To prevent massive token bloat while remaining highly discoverable to LLMs, this MCP server uses a **Middle-Ground Categorization Pattern**. Rather than exposing all 483 endpoints as individual tools (which overwhelms context windows) or hiding them entirely, it exposes **12 Category Tools**:

Each tool (like `looker_dashboards` or `looker_users`) handles all endpoints for its category. The LLM can easily see the list of endpoints inside the tool's description!

## Available Tools (483 Total)

Here are the tools available, organized by category:

<details>
<summary><b>Dashboards (42 tools)</b></summary>

<p>`all_dashboards`, `copy_dashboard`, `create_dashboard`, `create_dashboard_element`, `create_dashboard_element_render_task`, `create_dashboard_filter`, `create_dashboard_filter_state`, `create_dashboard_from_lookml`, `create_dashboard_layout`, `create_dashboard_render_task`, `dashboard`, `dashboard_aggregate_table_lookml`, `dashboard_dashboard_elements`, `dashboard_dashboard_filters`, `dashboard_dashboard_layouts`, `dashboard_element`, `dashboard_filter`, `dashboard_filter_state`, `dashboard_layout`, `dashboard_layout_component`, `dashboard_layout_dashboard_layout_components`, `dashboard_lookml`, `delete_dashboard`, `delete_dashboard_element`, `delete_dashboard_filter`, `delete_dashboard_layout`, `folder_dashboards`, `import_dashboard_from_lookml`, `import_lookml_dashboard`, `move_dashboard`, `scheduled_plans_for_dashboard`, `scheduled_plans_for_lookml_dashboard`, `search_dashboard_elements`, `search_dashboards`, `search_lookml_dashboards`, `sync_lookml_dashboard`, `update_dashboard`, `update_dashboard_certification`, `update_dashboard_element`, `update_dashboard_filter`, `update_dashboard_layout`, `update_dashboard_layout_component`</p>

</details>

<details>
<summary><b>Looks (24 tools)</b></summary>

<p>`all_lookml_models`, `all_lookml_tests`, `all_looks`, `copy_look`, `create_look`, `create_look_render_task`, `create_lookml_model`, `delete_look`, `delete_lookml_model`, `delete_user_credentials_looker_openid`, `folder_looks`, `look`, `lookml_model`, `lookml_model_explore`, `move_look`, `run_look`, `run_lookml_test`, `scheduled_plans_for_look`, `search_looks`, `update_look`, `update_look_certification`, `update_lookml_certification`, `update_lookml_model`, `user_credentials_looker_openid`</p>

</details>

<details>
<summary><b>Queries (23 tools)</b></summary>

<p>`create_golden_query`, `create_merge_query`, `create_query`, `create_query_render_task`, `create_query_task`, `create_sql_interface_query`, `create_sql_query`, `delete_golden_query`, `kill_query`, `merge_query`, `query`, `query_for_slug`, `query_task`, `query_task_multi_results`, `query_task_results`, `run_inline_query`, `run_query`, `run_sql_interface_query`, `run_sql_query`, `run_url_encoded_query`, `sql_interface_metadata`, `sql_query`, `update_golden_query`</p>

</details>

<details>
<summary><b>Users and Authentication (90 tools)</b></summary>

<p>`acquire_embed_cookieless_session`, `activate_app_user`, `add_group_user`, `all_external_oauth_applications`, `all_group_users`, `all_oauth_client_apps`, `all_user_attribute_group_values`, `all_user_attributes`, `all_user_credentials_api3s`, `all_user_credentials_embeds`, `all_user_login_lockouts`, `all_user_sessions`, `all_users`, `create_embed_user`, `create_external_oauth_application`, `create_oauth_application_user_state`, `create_user`, `create_user_attribute`, `create_user_credentials_api3`, `create_user_credentials_email`, `create_user_credentials_email_password_reset`, `create_user_credentials_totp`, `deactivate_app_user`, `delete_embed_cookieless_session`, `delete_external_oauth_application`, `delete_group_user`, `delete_oauth_client_app`, `delete_repository_credential`, `delete_user`, `delete_user_attribute`, `delete_user_attribute_group_value`, `delete_user_attribute_user_value`, `delete_user_credentials_api3`, `delete_user_credentials_email`, `delete_user_credentials_embed`, `delete_user_credentials_google`, `delete_user_credentials_ldap`, `delete_user_credentials_oidc`, `delete_user_credentials_saml`, `delete_user_credentials_totp`, `delete_user_login_lockout`, `delete_user_session`, `force_password_reset_at_next_login_for_all_users`, `generate_tokens_for_cookieless_session`, `get_all_repository_credentials`, `login_user`, `me`, `oauth_client_app`, `register_oauth_client_app`, `role_users`, `search_credentials_email`, `search_roles_with_user_count`, `search_user_login_lockouts`, `search_users`, `search_users_names`, `send_user_credentials_email_password_reset`, `session`, `session_config`, `set_role_users`, `set_user_attribute_group_values`, `set_user_attribute_user_value`, `set_user_roles`, `test_ldap_config_auth`, `test_ldap_config_user_auth`, `test_ldap_config_user_info`, `update_external_oauth_application`, `update_oauth_client_app`, `update_repository_credential`, `update_session`, `update_session_config`, `update_user`, `update_user_attribute`, `update_user_attribute_group_value`, `update_user_credentials_api3`, `update_user_credentials_email`, `user`, `user_attribute`, `user_attribute_user_values`, `user_credentials_api3`, `user_credentials_email`, `user_credentials_embed`, `user_credentials_google`, `user_credentials_ldap`, `user_credentials_oidc`, `user_credentials_saml`, `user_credentials_totp`, `user_for_credential`, `user_roles`, `user_session`, `wipeout_user_emails`</p>

</details>

<details>
<summary><b>Groups and Roles (29 tools)</b></summary>

<p>`add_group_group`, `all_datagroups`, `all_group_groups`, `all_groups`, `all_permission_sets`, `all_permissions`, `all_roles`, `create_group`, `create_permission_set`, `create_role`, `datagroup`, `delete_group`, `delete_group_from_group`, `delete_permission_set`, `delete_role`, `group`, `permission_set`, `role`, `role_groups`, `search_groups`, `search_groups_with_hierarchy`, `search_groups_with_roles`, `search_permission_sets`, `search_roles`, `set_role_groups`, `update_datagroup`, `update_group`, `update_permission_set`, `update_role`</p>

</details>

<details>
<summary><b>Projects and Workspaces (23 tools)</b></summary>

<p>`all_git_branches`, `all_git_connection_tests`, `all_project_files`, `all_projects`, `all_workspaces`, `create_git_branch`, `create_git_deploy_key`, `create_project`, `delete_git_branch`, `find_git_branch`, `git_branch`, `git_deploy_key`, `project`, `project_file`, `project_validation_results`, `project_workspace`, `reset_project_to_production`, `reset_project_to_remote`, `run_git_connection_test`, `update_git_branch`, `update_project`, `validate_project`, `workspace`</p>

</details>

<details>
<summary><b>Folders and Spaces (12 tools)</b></summary>

<p>`all_folders`, `artifact_namespaces`, `create_folder`, `delete_folder`, `folder`, `folder_ancestors`, `folder_children`, `folder_children_search`, `folder_parent`, `scheduled_plans_for_space`, `search_folders`, `update_folder`</p>

</details>

<details>
<summary><b>Connections and Databases (18 tools)</b></summary>

<p>`all_connections`, `all_dialect_infos`, `connection`, `connection_columns`, `connection_cost_estimate`, `connection_databases`, `connection_features`, `connection_schemas`, `connection_search_columns`, `connection_tables`, `create_connection`, `delete_connection`, `delete_connection_override`, `get_self_service_model_allowed_connections`, `test_connection`, `test_connection_config`, `test_ldap_config_connection`, `update_connection`</p>

</details>

<details>
<summary><b>Models and Explores (32 tools)</b></summary>

<p>`active_themes`, `all_color_collections`, `all_model_sets`, `all_themes`, `color_collection`, `color_collections_custom`, `color_collections_standard`, `create_color_collection`, `create_model_set`, `create_theme`, `default_color_collection`, `default_theme`, `delete_color_collection`, `delete_model_set`, `delete_theme`, `get_model`, `graph_derived_tables_for_model`, `graph_derived_tables_for_view`, `model_fieldname_suggestions`, `model_set`, `search_content_views`, `search_model_sets`, `search_themes`, `set_default_color_collection`, `set_default_theme`, `theme`, `theme_or_default`, `update_color_collection`, `update_model_set`, `update_self_service_explore_certification`, `update_theme`, `validate_theme`</p>

</details>

<details>
<summary><b>Boards (17 tools)</b></summary>

<p>`all_board_items`, `all_board_sections`, `all_boards`, `all_primary_homepage_sections`, `board`, `board_item`, `board_section`, `create_board`, `create_board_item`, `create_board_section`, `delete_board`, `delete_board_item`, `delete_board_section`, `search_boards`, `update_board`, `update_board_item`, `update_board_section`</p>

</details>

<details>
<summary><b>Alerts and Schedules (19 tools)</b></summary>

<p>`alert_notifications`, `all_scheduled_plans`, `create_alert`, `create_scheduled_plan`, `delete_alert`, `delete_scheduled_plan`, `enqueue_alert`, `follow_alert`, `get_alert`, `read_alert_notification`, `scheduled_plan`, `scheduled_plan_run_once`, `scheduled_plan_run_once_by_id`, `search_alerts`, `search_scheduled_plans`, `unfollow_alert`, `update_alert`, `update_alert_field`, `update_scheduled_plan`</p>

</details>

<details>
<summary><b>System and Misc (154 tools)</b></summary>

<p>`accept_integration_hub_legal_agreement`, `add_support_access_allowlist_entries`, `all_content_metadata_accesses`, `all_content_metadatas`, `all_conversation_messages`, `all_integration_hubs`, `all_integrations`, `all_legacy_features`, `all_locales`, `all_running_queries`, `all_ssh_servers`, `all_ssh_tunnels`, `all_timezones`, `api_spec`, `artifact`, `artifact_usage`, `artifact_value`, `async_deploy_ref_to_production`, `async_deploy_status`, `check_pdt_build`, `cloud_storage_configuration`, `content_favorite`, `content_metadata`, `content_summary`, `content_thumbnail`, `content_validation`, `conversational_analytics_chat`, `create_agent`, `create_ci_run`, `create_content_favorite`, `create_content_metadata_access`, `create_continuous_integration_run`, `create_conversation`, `create_conversation_message`, `create_digest_email_send`, `create_embed_secret`, `create_embed_url_as_me`, `create_integration_hub`, `create_oidc_test_config`, `create_saml_test_config`, `create_service_account`, `create_ssh_server`, `create_ssh_tunnel`, `create_sso_embed_url`, `custom_welcome_email`, `delete`, `delete_agent`, `delete_artifact`, `delete_content_favorite`, `delete_content_metadata_access`, `delete_conversation`, `delete_conversation_message`, `delete_embed_secret`, `delete_integration_hub`, `delete_oidc_test_config`, `delete_saml_test_config`, `delete_service_account`, `delete_ssh_server`, `delete_ssh_tunnel`, `delete_support_access_allowlist_entry`, `deploy_ref_to_production`, `deploy_to_production`, `deregister_mobile_device`, `digest_emails_enabled`, `disable_support_access`, `enable_support_access`, `encode_path_param`, `fetch_and_parse_saml_idp_metadata`, `fetch_integration_form`, `fetch_remote_data_action_form`, `get`, `get_agent`, `get_ci_run`, `get_continuous_integration_run`, `get_conversation`, `get_conversation_message`, `get_integration_hub_health`, `get_setting`, `get_support_access_allowlist_entries`, `integration`, `integration_hub`, `internal_help_resources`, `internal_help_resources_content`, `invalidate_tokens`, `ldap_config`, `legacy_feature`, `lock_all`, `login`, `logout`, `manifest`, `mobile_settings`, `oidc_config`, `oidc_test_config`, `parse_saml_idp_metadata`, `password_config`, `patch`, `perform_data_action`, `post`, `public_egress_ip_addresses`, `purge_artifacts`, `put`, `register_mobile_device`, `render_task`, `render_task_results`, `run_key_driver_analysis`, `saml_config`, `saml_test_config`, `search_agents`, `search_artifacts`, `search_content`, `search_content_favorites`, `search_conversations`, `search_reports`, `set_setting`, `set_smtp_settings`, `smtp_status`, `ssh_public_key`, `ssh_server`, `ssh_tunnel`, `start_pdt_build`, `stop_pdt_build`, `support_access_status`, `tag_ref`, `test_integration`, `test_ssh_server`, `test_ssh_tunnel`, `update_agent`, `update_artifacts`, `update_cloud_storage_configuration`, `update_content_metadata`, `update_content_metadata_access`, `update_conversation`, `update_conversation_message`, `update_custom_welcome_email`, `update_custom_welcome_email_test`, `update_digest_emails_enabled`, `update_integration`, `update_integration_hub`, `update_internal_help_resources`, `update_internal_help_resources_content`, `update_ldap_config`, `update_legacy_feature`, `update_mobile_device_registration`, `update_oidc_config`, `update_password_config`, `update_saml_config`, `update_service_account`, `update_ssh_server`, `update_ssh_tunnel`, `update_whitelabel_configuration`, `validate_embed_url`, `vector_thumbnail`, `versions`, `whitelabel_configuration`</p>

</details>

