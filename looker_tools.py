from typing import Any, List, Dict, Optional, Sequence
import looker_sdk

sdk_instance = None
def get_sdk():
    global sdk_instance
    if sdk_instance is None:
        try:
            sdk_instance = looker_sdk.init40()
        except Exception as e:
            print("Warning: Looker SDK init failed:", e)
    return sdk_instance

def register_looker_tools(mcp):
    @mcp.tool(name="accept_integration_hub_legal_agreement")
    def tool_accept_integration_hub_legal_agreement(integration_hub_id: str, transport_options: dict = None) -> str:
        """Accept Integration Hub Legal Agreement"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.accept_integration_hub_legal_agreement(integration_hub_id=integration_hub_id, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="acquire_embed_cookieless_session")
    def tool_acquire_embed_cookieless_session(body: dict, transport_options: dict = None) -> str:
        """Create Acquire cookieless embed session"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.acquire_embed_cookieless_session(body=body, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="activate_app_user")
    def tool_activate_app_user(client_guid: str, user_id: str, fields: str | None = None, transport_options: dict = None) -> str:
        """Activate OAuth App User"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.activate_app_user(client_guid=client_guid, user_id=user_id, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="active_themes")
    def tool_active_themes(name: str | None = None, ts: Any = None, fields: str | None = None, transport_options: dict = None) -> str:
        """Get Active Themes"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.active_themes(name=name, ts=ts, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="add_group_group")
    def tool_add_group_group(group_id: str, body: dict, transport_options: dict = None) -> str:
        """Add a Group to Group"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.add_group_group(group_id=group_id, body=body, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="add_group_user")
    def tool_add_group_user(group_id: str, body: dict, transport_options: dict = None) -> str:
        """Add a User to Group"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.add_group_user(group_id=group_id, body=body, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="add_support_access_allowlist_entries")
    def tool_add_support_access_allowlist_entries(body: dict, transport_options: dict = None) -> str:
        """Add Support Access Allowlist Users"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.add_support_access_allowlist_entries(body=body, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="alert_notifications")
    def tool_alert_notifications(limit: int | None = None, offset: int | None = None, transport_options: dict = None) -> str:
        """Alert Notifications"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.alert_notifications(limit=limit, offset=offset, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="all_board_items")
    def tool_all_board_items(fields: str | None = None, sorts: str | None = None, board_section_id: str | None = None, transport_options: dict = None) -> str:
        """Get All Board Items"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.all_board_items(fields=fields, sorts=sorts, board_section_id=board_section_id, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="all_board_sections")
    def tool_all_board_sections(fields: str | None = None, sorts: str | None = None, transport_options: dict = None) -> str:
        """Get All Board sections"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.all_board_sections(fields=fields, sorts=sorts, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="all_boards")
    def tool_all_boards(fields: str | None = None, transport_options: dict = None) -> str:
        """Get All Boards"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.all_boards(fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="all_color_collections")
    def tool_all_color_collections(fields: str | None = None, transport_options: dict = None) -> str:
        """Get all Color Collections"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.all_color_collections(fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="all_connections")
    def tool_all_connections(fields: str | None = None, transport_options: dict = None) -> str:
        """Get All Connections"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.all_connections(fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="all_content_metadata_accesses")
    def tool_all_content_metadata_accesses(content_metadata_id: str, fields: str | None = None, transport_options: dict = None) -> str:
        """Get All Content Metadata Accesses"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.all_content_metadata_accesses(content_metadata_id=content_metadata_id, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="all_content_metadatas")
    def tool_all_content_metadatas(parent_id: str, fields: str | None = None, transport_options: dict = None) -> str:
        """Get All Content Metadatas"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.all_content_metadatas(parent_id=parent_id, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="all_conversation_messages")
    def tool_all_conversation_messages(conversation_id: str, fields: str | None = None, transport_options: dict = None) -> str:
        """Get All Conversation Messages"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.all_conversation_messages(conversation_id=conversation_id, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="all_dashboards")
    def tool_all_dashboards(fields: str | None = None, transport_options: dict = None) -> str:
        """Get All Dashboards"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.all_dashboards(fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="all_datagroups")
    def tool_all_datagroups(transport_options: dict = None) -> str:
        """Get All Datagroups"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.all_datagroups(transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="all_dialect_infos")
    def tool_all_dialect_infos(fields: str | None = None, transport_options: dict = None) -> str:
        """Get All Dialect Infos"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.all_dialect_infos(fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="all_external_oauth_applications")
    def tool_all_external_oauth_applications(name: str | None = None, client_id: str | None = None, transport_options: dict = None) -> str:
        """Get All External OAuth Applications"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.all_external_oauth_applications(name=name, client_id=client_id, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="all_folders")
    def tool_all_folders(fields: str | None = None, transport_options: dict = None) -> str:
        """Get All Folders"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.all_folders(fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="all_git_branches")
    def tool_all_git_branches(project_id: str, transport_options: dict = None) -> str:
        """Get All Git Branches"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.all_git_branches(project_id=project_id, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="all_git_connection_tests")
    def tool_all_git_connection_tests(project_id: str, remote_url: str | None = None, transport_options: dict = None) -> str:
        """Get All Git Connection Tests"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.all_git_connection_tests(project_id=project_id, remote_url=remote_url, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="all_group_groups")
    def tool_all_group_groups(group_id: str, fields: str | None = None, transport_options: dict = None) -> str:
        """Get All Groups in Group"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.all_group_groups(group_id=group_id, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="all_group_users")
    def tool_all_group_users(group_id: str, fields: str | None = None, page: int | None = None, per_page: int | None = None, limit: int | None = None, offset: int | None = None, sorts: str | None = None, transport_options: dict = None) -> str:
        """Get All Users in Group"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.all_group_users(group_id=group_id, fields=fields, page=page, per_page=per_page, limit=limit, offset=offset, sorts=sorts, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="all_groups")
    def tool_all_groups(fields: str | None = None, page: int | None = None, per_page: int | None = None, limit: int | None = None, offset: int | None = None, sorts: str | None = None, ids: list = None, content_metadata_id: str | None = None, can_add_to_content_metadata: bool | None = None, transport_options: dict = None) -> str:
        """Get All Groups"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.all_groups(fields=fields, page=page, per_page=per_page, limit=limit, offset=offset, sorts=sorts, ids=ids, content_metadata_id=content_metadata_id, can_add_to_content_metadata=can_add_to_content_metadata, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="all_integration_hubs")
    def tool_all_integration_hubs(fields: str | None = None, transport_options: dict = None) -> str:
        """Get All Integration Hubs"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.all_integration_hubs(fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="all_integrations")
    def tool_all_integrations(fields: str | None = None, integration_hub_id: str | None = None, transport_options: dict = None) -> str:
        """Get All Integrations"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.all_integrations(fields=fields, integration_hub_id=integration_hub_id, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="all_legacy_features")
    def tool_all_legacy_features(transport_options: dict = None) -> str:
        """Get All Legacy Features"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.all_legacy_features(transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="all_locales")
    def tool_all_locales(transport_options: dict = None) -> str:
        """Get All Locales"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.all_locales(transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="all_lookml_models")
    def tool_all_lookml_models(fields: str | None = None, limit: int | None = None, offset: int | None = None, exclude_empty: bool | None = None, exclude_hidden: bool | None = None, include_internal: bool | None = None, include_self_service: bool | None = None, transport_options: dict = None) -> str:
        """Get All LookML Models"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.all_lookml_models(fields=fields, limit=limit, offset=offset, exclude_empty=exclude_empty, exclude_hidden=exclude_hidden, include_internal=include_internal, include_self_service=include_self_service, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="all_lookml_tests")
    def tool_all_lookml_tests(project_id: str, file_id: str | None = None, transport_options: dict = None) -> str:
        """Get All LookML Tests"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.all_lookml_tests(project_id=project_id, file_id=file_id, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="all_looks")
    def tool_all_looks(fields: str | None = None, transport_options: dict = None) -> str:
        """Get All Looks"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.all_looks(fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="all_model_sets")
    def tool_all_model_sets(fields: str | None = None, transport_options: dict = None) -> str:
        """Get All Model Sets"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.all_model_sets(fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="all_oauth_client_apps")
    def tool_all_oauth_client_apps(fields: str | None = None, transport_options: dict = None) -> str:
        """Get All OAuth Client Apps"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.all_oauth_client_apps(fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="all_permission_sets")
    def tool_all_permission_sets(fields: str | None = None, transport_options: dict = None) -> str:
        """Get All Permission Sets"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.all_permission_sets(fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="all_permissions")
    def tool_all_permissions(transport_options: dict = None) -> str:
        """Get All Permissions"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.all_permissions(transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="all_primary_homepage_sections")
    def tool_all_primary_homepage_sections(fields: str | None = None, transport_options: dict = None) -> str:
        """Get All Primary homepage sections"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.all_primary_homepage_sections(fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="all_project_files")
    def tool_all_project_files(project_id: str, fields: str | None = None, transport_options: dict = None) -> str:
        """Get All Project Files"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.all_project_files(project_id=project_id, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="all_projects")
    def tool_all_projects(fields: str | None = None, transport_options: dict = None) -> str:
        """Get All Projects"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.all_projects(fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="all_roles")
    def tool_all_roles(fields: str | None = None, ids: list = None, get_all_support_roles: bool | None = None, transport_options: dict = None) -> str:
        """Get All Roles"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.all_roles(fields=fields, ids=ids, get_all_support_roles=get_all_support_roles, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="all_running_queries")
    def tool_all_running_queries(transport_options: dict = None) -> str:
        """Get All Running Queries"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.all_running_queries(transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="all_scheduled_plans")
    def tool_all_scheduled_plans(user_id: str | None = None, fields: str | None = None, all_users: bool | None = None, transport_options: dict = None) -> str:
        """Get All Scheduled Plans"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.all_scheduled_plans(user_id=user_id, fields=fields, all_users=all_users, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="all_ssh_servers")
    def tool_all_ssh_servers(fields: str | None = None, transport_options: dict = None) -> str:
        """Get All SSH Servers"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.all_ssh_servers(fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="all_ssh_tunnels")
    def tool_all_ssh_tunnels(fields: str | None = None, transport_options: dict = None) -> str:
        """Get All SSH Tunnels"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.all_ssh_tunnels(fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="all_themes")
    def tool_all_themes(fields: str | None = None, transport_options: dict = None) -> str:
        """Get All Themes"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.all_themes(fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="all_timezones")
    def tool_all_timezones(transport_options: dict = None) -> str:
        """Get All Timezones"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.all_timezones(transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="all_user_attribute_group_values")
    def tool_all_user_attribute_group_values(user_attribute_id: str, fields: str | None = None, transport_options: dict = None) -> str:
        """Get User Attribute Group Values"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.all_user_attribute_group_values(user_attribute_id=user_attribute_id, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="all_user_attributes")
    def tool_all_user_attributes(fields: str | None = None, sorts: str | None = None, transport_options: dict = None) -> str:
        """Get All User Attributes"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.all_user_attributes(fields=fields, sorts=sorts, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="all_user_credentials_api3s")
    def tool_all_user_credentials_api3s(user_id: str, fields: str | None = None, transport_options: dict = None) -> str:
        """Get All API Credentials"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.all_user_credentials_api3s(user_id=user_id, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="all_user_credentials_embeds")
    def tool_all_user_credentials_embeds(user_id: str, fields: str | None = None, transport_options: dict = None) -> str:
        """Get All Embedding Credentials"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.all_user_credentials_embeds(user_id=user_id, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="all_user_login_lockouts")
    def tool_all_user_login_lockouts(fields: str | None = None, transport_options: dict = None) -> str:
        """Get All User Login Lockouts"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.all_user_login_lockouts(fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="all_user_sessions")
    def tool_all_user_sessions(user_id: str, fields: str | None = None, transport_options: dict = None) -> str:
        """Get All Web Login Sessions"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.all_user_sessions(user_id=user_id, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="all_users")
    def tool_all_users(fields: str | None = None, page: int | None = None, per_page: int | None = None, limit: int | None = None, offset: int | None = None, sorts: str | None = None, ids: list = None, transport_options: dict = None) -> str:
        """Get All Users"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.all_users(fields=fields, page=page, per_page=per_page, limit=limit, offset=offset, sorts=sorts, ids=ids, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="all_workspaces")
    def tool_all_workspaces(transport_options: dict = None) -> str:
        """Get All Workspaces"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.all_workspaces(transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="api_spec")
    def tool_api_spec(api_version: str, specification: str, transport_options: dict = None) -> str:
        """Get an API specification"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.api_spec(api_version=api_version, specification=specification, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="artifact")
    def tool_artifact(namespace: str, key: str, fields: str | None = None, limit: int | None = None, offset: int | None = None, tally: bool | None = None, transport_options: dict = None) -> str:
        """Get one or more artifacts"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.artifact(namespace=namespace, key=key, fields=fields, limit=limit, offset=offset, tally=tally, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="artifact_namespaces")
    def tool_artifact_namespaces(fields: str | None = None, limit: int | None = None, offset: int | None = None, transport_options: dict = None) -> str:
        """Get namespaces and counts"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.artifact_namespaces(fields=fields, limit=limit, offset=offset, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="artifact_usage")
    def tool_artifact_usage(fields: str | None = None, transport_options: dict = None) -> str:
        """Artifact store usage"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.artifact_usage(fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="artifact_value")
    def tool_artifact_value(namespace: str, key: str | None = None, transport_options: dict = None) -> str:
        """Get an artifact value"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.artifact_value(namespace=namespace, key=key, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="async_deploy_ref_to_production")
    def tool_async_deploy_ref_to_production(project_id: str, branch: str | None = None, ref: str | None = None, transport_options: dict = None) -> str:
        """Asynchronously Deploy Remote Branch or Ref to Production"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.async_deploy_ref_to_production(project_id=project_id, branch=branch, ref=ref, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="async_deploy_status")
    def tool_async_deploy_status(project_id: str, deployment_id: int, transport_options: dict = None) -> str:
        """Check Async Deploy Status"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.async_deploy_status(project_id=project_id, deployment_id=deployment_id, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="board")
    def tool_board(board_id: str, fields: str | None = None, transport_options: dict = None) -> str:
        """Get Board"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.board(board_id=board_id, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="board_item")
    def tool_board_item(board_item_id: str, fields: str | None = None, transport_options: dict = None) -> str:
        """Get Board Item"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.board_item(board_item_id=board_item_id, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="board_section")
    def tool_board_section(board_section_id: str, fields: str | None = None, transport_options: dict = None) -> str:
        """Get Board section"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.board_section(board_section_id=board_section_id, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="check_pdt_build")
    def tool_check_pdt_build(materialization_id: str, transport_options: dict = None) -> str:
        """Check status of a PDT materialization"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.check_pdt_build(materialization_id=materialization_id, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="cloud_storage_configuration")
    def tool_cloud_storage_configuration(transport_options: dict = None) -> str:
        """Get Cloud Storage"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.cloud_storage_configuration(transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="color_collection")
    def tool_color_collection(collection_id: str, fields: str | None = None, transport_options: dict = None) -> str:
        """Get Color Collection by ID"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.color_collection(collection_id=collection_id, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="color_collections_custom")
    def tool_color_collections_custom(fields: str | None = None, transport_options: dict = None) -> str:
        """Get all Custom Color Collections"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.color_collections_custom(fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="color_collections_standard")
    def tool_color_collections_standard(fields: str | None = None, transport_options: dict = None) -> str:
        """Get all Standard Color Collections"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.color_collections_standard(fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="connection")
    def tool_connection(connection_name: str, fields: str | None = None, transport_options: dict = None) -> str:
        """Get Connection"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.connection(connection_name=connection_name, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="connection_columns")
    def tool_connection_columns(connection_name: str, database: str | None = None, schema_name: str | None = None, cache: bool | None = None, table_limit: int | None = None, table_names: str | None = None, fields: str | None = None, transport_options: dict = None) -> str:
        """Get columns for a connection"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.connection_columns(connection_name=connection_name, database=database, schema_name=schema_name, cache=cache, table_limit=table_limit, table_names=table_names, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="connection_cost_estimate")
    def tool_connection_cost_estimate(connection_name: str, body: dict, fields: str | None = None, transport_options: dict = None) -> str:
        """Estimate costs for a connection"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.connection_cost_estimate(connection_name=connection_name, body=body, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="connection_databases")
    def tool_connection_databases(connection_name: str, transport_options: dict = None) -> str:
        """List accessible databases to this connection"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.connection_databases(connection_name=connection_name, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="connection_features")
    def tool_connection_features(connection_name: str, fields: str | None = None, transport_options: dict = None) -> str:
        """Metadata features supported by this connection"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.connection_features(connection_name=connection_name, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="connection_schemas")
    def tool_connection_schemas(connection_name: str, database: str | None = None, cache: bool | None = None, fields: str | None = None, transport_options: dict = None) -> str:
        """Get schemas for a connection"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.connection_schemas(connection_name=connection_name, database=database, cache=cache, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="connection_search_columns")
    def tool_connection_search_columns(connection_name: str, column_name: str | None = None, fields: str | None = None, transport_options: dict = None) -> str:
        """Search a connection for columns"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.connection_search_columns(connection_name=connection_name, column_name=column_name, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="connection_tables")
    def tool_connection_tables(connection_name: str, database: str | None = None, schema_name: str | None = None, cache: bool | None = None, fields: str | None = None, table_filter: str | None = None, table_limit: int | None = None, transport_options: dict = None) -> str:
        """Get tables for a connection"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.connection_tables(connection_name=connection_name, database=database, schema_name=schema_name, cache=cache, fields=fields, table_filter=table_filter, table_limit=table_limit, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="content_favorite")
    def tool_content_favorite(content_favorite_id: str, fields: str | None = None, transport_options: dict = None) -> str:
        """Get Favorite Content"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.content_favorite(content_favorite_id=content_favorite_id, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="content_metadata")
    def tool_content_metadata(content_metadata_id: str, fields: str | None = None, transport_options: dict = None) -> str:
        """Get Content Metadata"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.content_metadata(content_metadata_id=content_metadata_id, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="content_summary")
    def tool_content_summary(fields: str | None = None, limit: int | None = None, offset: int | None = None, target_group_id: str | None = None, target_user_id: str | None = None, target_content_type: str | None = None, sorts: str | None = None, transport_options: dict = None) -> str:
        """Search Content Summaries"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.content_summary(fields=fields, limit=limit, offset=offset, target_group_id=target_group_id, target_user_id=target_user_id, target_content_type=target_content_type, sorts=sorts, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="content_thumbnail")
    def tool_content_thumbnail(type: str, resource_id: str, reload: str | None = None, theme: str | None = None, format: str | None = None, width: int | None = None, height: int | None = None, transport_options: dict = None) -> str:
        """Get Content Thumbnail"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.content_thumbnail(type=type, resource_id=resource_id, reload=reload, theme=theme, format=format, width=width, height=height, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="content_validation")
    def tool_content_validation(fields: str | None = None, project_names: list = None, space_ids: list = None, transport_options: dict = None) -> str:
        """Validate Content"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.content_validation(fields=fields, project_names=project_names, space_ids=space_ids, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="conversational_analytics_chat")
    def tool_conversational_analytics_chat(body: dict, transport_options: dict = None) -> str:
        """Chat"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.conversational_analytics_chat(body=body, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="copy_dashboard")
    def tool_copy_dashboard(dashboard_id: str, folder_id: str | None = None, transport_options: dict = None) -> str:
        """Copy Dashboard"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.copy_dashboard(dashboard_id=dashboard_id, folder_id=folder_id, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="copy_look")
    def tool_copy_look(look_id: str, folder_id: str | None = None, transport_options: dict = None) -> str:
        """Copy Look"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.copy_look(look_id=look_id, folder_id=folder_id, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="create_agent")
    def tool_create_agent(body: dict, fields: str | None = None, transport_options: dict = None) -> str:
        """Create Agent"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.create_agent(body=body, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="create_alert")
    def tool_create_alert(body: dict, transport_options: dict = None) -> str:
        """Create an alert"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.create_alert(body=body, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="create_board")
    def tool_create_board(body: dict, fields: str | None = None, transport_options: dict = None) -> str:
        """Create Board"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.create_board(body=body, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="create_board_item")
    def tool_create_board_item(body: dict, fields: str | None = None, transport_options: dict = None) -> str:
        """Create Board Item"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.create_board_item(body=body, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="create_board_section")
    def tool_create_board_section(body: dict, fields: str | None = None, transport_options: dict = None) -> str:
        """Create Board section"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.create_board_section(body=body, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="create_ci_run")
    def tool_create_ci_run(project_id: str, body: dict, fields: str | None = None, transport_options: dict = None) -> str:
        """Create a Continuous Integration run"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.create_ci_run(project_id=project_id, body=body, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="create_color_collection")
    def tool_create_color_collection(body: dict, transport_options: dict = None) -> str:
        """Create ColorCollection"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.create_color_collection(body=body, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="create_connection")
    def tool_create_connection(body: dict, transport_options: dict = None) -> str:
        """Create Connection"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.create_connection(body=body, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="create_content_favorite")
    def tool_create_content_favorite(body: dict, transport_options: dict = None) -> str:
        """Create Favorite Content"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.create_content_favorite(body=body, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="create_content_metadata_access")
    def tool_create_content_metadata_access(body: dict, send_boards_notification_email: bool | None = None, transport_options: dict = None) -> str:
        """Create Content Metadata Access"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.create_content_metadata_access(body=body, send_boards_notification_email=send_boards_notification_email, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="create_continuous_integration_run")
    def tool_create_continuous_integration_run(project_id: str, body: dict, fields: str | None = None, transport_options: dict = None) -> str:
        """Create and queue a Continuous Integration run"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.create_continuous_integration_run(project_id=project_id, body=body, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="create_conversation")
    def tool_create_conversation(body: dict, fields: str | None = None, transport_options: dict = None) -> str:
        """Create Conversation"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.create_conversation(body=body, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="create_conversation_message")
    def tool_create_conversation_message(conversation_id: str, body: dict, fields: str | None = None, transport_options: dict = None) -> str:
        """Create Conversation Message"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.create_conversation_message(conversation_id=conversation_id, body=body, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="create_dashboard")
    def tool_create_dashboard(body: dict, transport_options: dict = None) -> str:
        """Create Dashboard"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.create_dashboard(body=body, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="create_dashboard_element")
    def tool_create_dashboard_element(body: dict, fields: str | None = None, apply_filters: bool | None = None, transport_options: dict = None) -> str:
        """Create DashboardElement"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.create_dashboard_element(body=body, fields=fields, apply_filters=apply_filters, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="create_dashboard_element_render_task")
    def tool_create_dashboard_element_render_task(dashboard_element_id: str, result_format: str, width: int, height: int, fields: str | None = None, transport_options: dict = None) -> str:
        """Create Dashboard Element Render Task"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.create_dashboard_element_render_task(dashboard_element_id=dashboard_element_id, result_format=result_format, width=width, height=height, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="create_dashboard_filter")
    def tool_create_dashboard_filter(body: dict, fields: str | None = None, transport_options: dict = None) -> str:
        """Create Dashboard Filter"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.create_dashboard_filter(body=body, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="create_dashboard_filter_state")
    def tool_create_dashboard_filter_state(body: str, transport_options: dict = None) -> str:
        """Create Dashboard Filter State"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.create_dashboard_filter_state(body=body, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="create_dashboard_from_lookml")
    def tool_create_dashboard_from_lookml(body: dict, transport_options: dict = None) -> str:
        """Create Dashboard from LookML"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.create_dashboard_from_lookml(body=body, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="create_dashboard_layout")
    def tool_create_dashboard_layout(body: dict, fields: str | None = None, transport_options: dict = None) -> str:
        """Create DashboardLayout"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.create_dashboard_layout(body=body, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="create_dashboard_render_task")
    def tool_create_dashboard_render_task(dashboard_id: str, result_format: str, body: dict, width: int, height: int, fields: str | None = None, pdf_paper_size: str | None = None, pdf_landscape: bool | None = None, long_tables: bool | None = None, theme: str | None = None, transport_options: dict = None) -> str:
        """Create Dashboard Render Task"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.create_dashboard_render_task(dashboard_id=dashboard_id, result_format=result_format, body=body, width=width, height=height, fields=fields, pdf_paper_size=pdf_paper_size, pdf_landscape=pdf_landscape, long_tables=long_tables, theme=theme, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="create_digest_email_send")
    def tool_create_digest_email_send(transport_options: dict = None) -> str:
        """Deliver digest email contents"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.create_digest_email_send(transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="create_embed_secret")
    def tool_create_embed_secret(body: dict = None, transport_options: dict = None) -> str:
        """Create Embed Secret"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.create_embed_secret(body=body, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="create_embed_url_as_me")
    def tool_create_embed_url_as_me(body: dict, transport_options: dict = None) -> str:
        """Create Embed URL"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.create_embed_url_as_me(body=body, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="create_embed_user")
    def tool_create_embed_user(body: dict, transport_options: dict = None) -> str:
        """Create an embed user from an external user ID"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.create_embed_user(body=body, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="create_external_oauth_application")
    def tool_create_external_oauth_application(body: dict, transport_options: dict = None) -> str:
        """Create External OAuth Application"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.create_external_oauth_application(body=body, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="create_folder")
    def tool_create_folder(body: dict, transport_options: dict = None) -> str:
        """Create Folder"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.create_folder(body=body, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="create_git_branch")
    def tool_create_git_branch(project_id: str, body: dict, transport_options: dict = None) -> str:
        """Checkout New Git Branch"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.create_git_branch(project_id=project_id, body=body, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="create_git_deploy_key")
    def tool_create_git_deploy_key(project_id: str, transport_options: dict = None) -> str:
        """Create Deploy Key"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.create_git_deploy_key(project_id=project_id, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="create_golden_query")
    def tool_create_golden_query(body: dict, transport_options: dict = None) -> str:
        """Create Golden Query"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.create_golden_query(body=body, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="create_group")
    def tool_create_group(body: dict, fields: str | None = None, transport_options: dict = None) -> str:
        """Create Group"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.create_group(body=body, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="create_integration_hub")
    def tool_create_integration_hub(body: dict, fields: str | None = None, transport_options: dict = None) -> str:
        """Create Integration Hub"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.create_integration_hub(body=body, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="create_look")
    def tool_create_look(body: dict, fields: str | None = None, transport_options: dict = None) -> str:
        """Create Look"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.create_look(body=body, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="create_look_render_task")
    def tool_create_look_render_task(look_id: str, result_format: str, width: int, height: int, fields: str | None = None, transport_options: dict = None) -> str:
        """Create Look Render Task"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.create_look_render_task(look_id=look_id, result_format=result_format, width=width, height=height, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="create_lookml_model")
    def tool_create_lookml_model(body: dict, transport_options: dict = None) -> str:
        """Create LookML Model"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.create_lookml_model(body=body, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="create_merge_query")
    def tool_create_merge_query(body: dict = None, fields: str | None = None, transport_options: dict = None) -> str:
        """Create Merge Query"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.create_merge_query(body=body, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="create_model_set")
    def tool_create_model_set(body: dict, transport_options: dict = None) -> str:
        """Create Model Set"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.create_model_set(body=body, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="create_oauth_application_user_state")
    def tool_create_oauth_application_user_state(body: dict, transport_options: dict = None) -> str:
        """Create Create OAuth user state."""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.create_oauth_application_user_state(body=body, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="create_oidc_test_config")
    def tool_create_oidc_test_config(body: dict, transport_options: dict = None) -> str:
        """Create OIDC Test Configuration"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.create_oidc_test_config(body=body, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="create_permission_set")
    def tool_create_permission_set(body: dict, transport_options: dict = None) -> str:
        """Create Permission Set"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.create_permission_set(body=body, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="create_project")
    def tool_create_project(body: dict, transport_options: dict = None) -> str:
        """Create Project"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.create_project(body=body, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="create_query")
    def tool_create_query(body: dict, fields: str | None = None, transport_options: dict = None) -> str:
        """Create Query"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.create_query(body=body, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="create_query_render_task")
    def tool_create_query_render_task(query_id: str, result_format: str, width: int, height: int, fields: str | None = None, transport_options: dict = None) -> str:
        """Create Query Render Task"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.create_query_render_task(query_id=query_id, result_format=result_format, width=width, height=height, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="create_query_task")
    def tool_create_query_task(body: dict, limit: int | None = None, apply_formatting: bool | None = None, apply_vis: bool | None = None, cache: bool | None = None, generate_drill_links: bool | None = None, force_production: bool | None = None, cache_only: bool | None = None, path_prefix: str | None = None, rebuild_pdts: bool | None = None, server_table_calcs: bool | None = None, fields: str | None = None, transport_options: dict = None) -> str:
        """Run Query Async"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.create_query_task(body=body, limit=limit, apply_formatting=apply_formatting, apply_vis=apply_vis, cache=cache, generate_drill_links=generate_drill_links, force_production=force_production, cache_only=cache_only, path_prefix=path_prefix, rebuild_pdts=rebuild_pdts, server_table_calcs=server_table_calcs, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="create_role")
    def tool_create_role(body: dict, transport_options: dict = None) -> str:
        """Create Role"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.create_role(body=body, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="create_saml_test_config")
    def tool_create_saml_test_config(body: dict, transport_options: dict = None) -> str:
        """Create SAML Test Configuration"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.create_saml_test_config(body=body, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="create_scheduled_plan")
    def tool_create_scheduled_plan(body: dict, transport_options: dict = None) -> str:
        """Create Scheduled Plan"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.create_scheduled_plan(body=body, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="create_service_account")
    def tool_create_service_account(body: dict, fields: str | None = None, transport_options: dict = None) -> str:
        """Create Service Account"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.create_service_account(body=body, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="create_sql_interface_query")
    def tool_create_sql_interface_query(body: dict, transport_options: dict = None) -> str:
        """Create SQL Interface Query"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.create_sql_interface_query(body=body, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="create_sql_query")
    def tool_create_sql_query(body: dict, transport_options: dict = None) -> str:
        """Create SQL Runner Query"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.create_sql_query(body=body, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="create_ssh_server")
    def tool_create_ssh_server(body: dict, transport_options: dict = None) -> str:
        """Create SSH Server"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.create_ssh_server(body=body, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="create_ssh_tunnel")
    def tool_create_ssh_tunnel(body: dict, transport_options: dict = None) -> str:
        """Create SSH Tunnel"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.create_ssh_tunnel(body=body, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="create_sso_embed_url")
    def tool_create_sso_embed_url(body: dict, transport_options: dict = None) -> str:
        """Create Signed Embed Url"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.create_sso_embed_url(body=body, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="create_theme")
    def tool_create_theme(body: dict, transport_options: dict = None) -> str:
        """Create Theme"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.create_theme(body=body, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="create_user")
    def tool_create_user(body: dict = None, fields: str | None = None, transport_options: dict = None) -> str:
        """Create User"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.create_user(body=body, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="create_user_attribute")
    def tool_create_user_attribute(body: dict, fields: str | None = None, transport_options: dict = None) -> str:
        """Create User Attribute"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.create_user_attribute(body=body, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="create_user_credentials_api3")
    def tool_create_user_credentials_api3(user_id: str, fields: str | None = None, transport_options: dict = None) -> str:
        """Create API Credential"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.create_user_credentials_api3(user_id=user_id, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="create_user_credentials_email")
    def tool_create_user_credentials_email(user_id: str, body: dict, fields: str | None = None, transport_options: dict = None) -> str:
        """Create Email/Password Credential"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.create_user_credentials_email(user_id=user_id, body=body, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="create_user_credentials_email_password_reset")
    def tool_create_user_credentials_email_password_reset(user_id: str, expires: bool | None = None, fields: str | None = None, transport_options: dict = None) -> str:
        """Create Password Reset Token"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.create_user_credentials_email_password_reset(user_id=user_id, expires=expires, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="create_user_credentials_totp")
    def tool_create_user_credentials_totp(user_id: str, body: dict = None, fields: str | None = None, transport_options: dict = None) -> str:
        """Create Two-Factor Credential"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.create_user_credentials_totp(user_id=user_id, body=body, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="custom_welcome_email")
    def tool_custom_welcome_email(transport_options: dict = None) -> str:
        """Get Custom Welcome Email"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.custom_welcome_email(transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="dashboard")
    def tool_dashboard(dashboard_id: str, fields: str | None = None, transport_options: dict = None) -> str:
        """Get Dashboard"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.dashboard(dashboard_id=dashboard_id, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="dashboard_aggregate_table_lookml")
    def tool_dashboard_aggregate_table_lookml(dashboard_id: str, transport_options: dict = None) -> str:
        """Get Aggregate Table LookML for a dashboard"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.dashboard_aggregate_table_lookml(dashboard_id=dashboard_id, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="dashboard_dashboard_elements")
    def tool_dashboard_dashboard_elements(dashboard_id: str, fields: str | None = None, transport_options: dict = None) -> str:
        """Get All DashboardElements"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.dashboard_dashboard_elements(dashboard_id=dashboard_id, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="dashboard_dashboard_filters")
    def tool_dashboard_dashboard_filters(dashboard_id: str, fields: str | None = None, transport_options: dict = None) -> str:
        """Get All Dashboard Filters"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.dashboard_dashboard_filters(dashboard_id=dashboard_id, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="dashboard_dashboard_layouts")
    def tool_dashboard_dashboard_layouts(dashboard_id: str, fields: str | None = None, transport_options: dict = None) -> str:
        """Get All DashboardLayouts"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.dashboard_dashboard_layouts(dashboard_id=dashboard_id, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="dashboard_element")
    def tool_dashboard_element(dashboard_element_id: str, fields: str | None = None, transport_options: dict = None) -> str:
        """Get DashboardElement"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.dashboard_element(dashboard_element_id=dashboard_element_id, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="dashboard_filter")
    def tool_dashboard_filter(dashboard_filter_id: str, fields: str | None = None, transport_options: dict = None) -> str:
        """Get Dashboard Filter"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.dashboard_filter(dashboard_filter_id=dashboard_filter_id, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="dashboard_filter_state")
    def tool_dashboard_filter_state(guid: str, transport_options: dict = None) -> str:
        """Get Dashboard Filter State"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.dashboard_filter_state(guid=guid, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="dashboard_layout")
    def tool_dashboard_layout(dashboard_layout_id: str, fields: str | None = None, transport_options: dict = None) -> str:
        """Get DashboardLayout"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.dashboard_layout(dashboard_layout_id=dashboard_layout_id, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="dashboard_layout_component")
    def tool_dashboard_layout_component(dashboard_layout_component_id: str, fields: str | None = None, transport_options: dict = None) -> str:
        """Get DashboardLayoutComponent"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.dashboard_layout_component(dashboard_layout_component_id=dashboard_layout_component_id, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="dashboard_layout_dashboard_layout_components")
    def tool_dashboard_layout_dashboard_layout_components(dashboard_layout_id: str, fields: str | None = None, transport_options: dict = None) -> str:
        """Get All DashboardLayoutComponents"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.dashboard_layout_dashboard_layout_components(dashboard_layout_id=dashboard_layout_id, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="dashboard_lookml")
    def tool_dashboard_lookml(dashboard_id: str, transport_options: dict = None) -> str:
        """Get lookml of a UDD"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.dashboard_lookml(dashboard_id=dashboard_id, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="datagroup")
    def tool_datagroup(datagroup_id: str, transport_options: dict = None) -> str:
        """Get Datagroup"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.datagroup(datagroup_id=datagroup_id, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="deactivate_app_user")
    def tool_deactivate_app_user(client_guid: str, user_id: str, fields: str | None = None, transport_options: dict = None) -> str:
        """Deactivate OAuth App User"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.deactivate_app_user(client_guid=client_guid, user_id=user_id, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="default_color_collection")
    def tool_default_color_collection(transport_options: dict = None) -> str:
        """Get Default Color Collection"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.default_color_collection(transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="default_theme")
    def tool_default_theme(ts: Any = None, transport_options: dict = None) -> str:
        """Get Default Theme"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.default_theme(ts=ts, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="delete")
    def tool_delete(path: str, structure: list = None, query_params: Any = None, transport_options: dict = None) -> str:
        """DELETE method"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.delete(path=path, structure=structure, query_params=query_params, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="delete_agent")
    def tool_delete_agent(id: str, fields: str | None = None, transport_options: dict = None) -> str:
        """Delete Agent"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.delete_agent(id=id, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="delete_alert")
    def tool_delete_alert(alert_id: str, transport_options: dict = None) -> str:
        """Delete an alert"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.delete_alert(alert_id=alert_id, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="delete_artifact")
    def tool_delete_artifact(namespace: str, key: str, transport_options: dict = None) -> str:
        """Delete one or more artifacts"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.delete_artifact(namespace=namespace, key=key, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="delete_board")
    def tool_delete_board(board_id: str, transport_options: dict = None) -> str:
        """Delete Board"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.delete_board(board_id=board_id, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="delete_board_item")
    def tool_delete_board_item(board_item_id: str, transport_options: dict = None) -> str:
        """Delete Board Item"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.delete_board_item(board_item_id=board_item_id, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="delete_board_section")
    def tool_delete_board_section(board_section_id: str, transport_options: dict = None) -> str:
        """Delete Board section"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.delete_board_section(board_section_id=board_section_id, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="delete_color_collection")
    def tool_delete_color_collection(collection_id: str, transport_options: dict = None) -> str:
        """Delete ColorCollection"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.delete_color_collection(collection_id=collection_id, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="delete_connection")
    def tool_delete_connection(connection_name: str, transport_options: dict = None) -> str:
        """Delete Connection"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.delete_connection(connection_name=connection_name, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="delete_connection_override")
    def tool_delete_connection_override(connection_name: str, override_context: str, transport_options: dict = None) -> str:
        """Delete Connection Override"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.delete_connection_override(connection_name=connection_name, override_context=override_context, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="delete_content_favorite")
    def tool_delete_content_favorite(content_favorite_id: str, transport_options: dict = None) -> str:
        """Delete Favorite Content"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.delete_content_favorite(content_favorite_id=content_favorite_id, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="delete_content_metadata_access")
    def tool_delete_content_metadata_access(content_metadata_access_id: str, transport_options: dict = None) -> str:
        """Delete Content Metadata Access"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.delete_content_metadata_access(content_metadata_access_id=content_metadata_access_id, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="delete_conversation")
    def tool_delete_conversation(id: str, fields: str | None = None, transport_options: dict = None) -> str:
        """Delete Conversation"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.delete_conversation(id=id, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="delete_conversation_message")
    def tool_delete_conversation_message(conversation_id: str, id: str, fields: str | None = None, transport_options: dict = None) -> str:
        """Delete Conversation Message"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.delete_conversation_message(conversation_id=conversation_id, id=id, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="delete_dashboard")
    def tool_delete_dashboard(dashboard_id: str, transport_options: dict = None) -> str:
        """Delete Dashboard"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.delete_dashboard(dashboard_id=dashboard_id, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="delete_dashboard_element")
    def tool_delete_dashboard_element(dashboard_element_id: str, transport_options: dict = None) -> str:
        """Delete DashboardElement"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.delete_dashboard_element(dashboard_element_id=dashboard_element_id, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="delete_dashboard_filter")
    def tool_delete_dashboard_filter(dashboard_filter_id: str, transport_options: dict = None) -> str:
        """Delete Dashboard Filter"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.delete_dashboard_filter(dashboard_filter_id=dashboard_filter_id, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="delete_dashboard_layout")
    def tool_delete_dashboard_layout(dashboard_layout_id: str, transport_options: dict = None) -> str:
        """Delete DashboardLayout"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.delete_dashboard_layout(dashboard_layout_id=dashboard_layout_id, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="delete_embed_cookieless_session")
    def tool_delete_embed_cookieless_session(session_reference_token: str, transport_options: dict = None) -> str:
        """Delete cookieless embed session"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.delete_embed_cookieless_session(session_reference_token=session_reference_token, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="delete_embed_secret")
    def tool_delete_embed_secret(embed_secret_id: str, transport_options: dict = None) -> str:
        """Delete Embed Secret"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.delete_embed_secret(embed_secret_id=embed_secret_id, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="delete_external_oauth_application")
    def tool_delete_external_oauth_application(client_id: str, transport_options: dict = None) -> str:
        """Delete External OAuth Application"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.delete_external_oauth_application(client_id=client_id, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="delete_folder")
    def tool_delete_folder(folder_id: str, transport_options: dict = None) -> str:
        """Delete Folder"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.delete_folder(folder_id=folder_id, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="delete_git_branch")
    def tool_delete_git_branch(project_id: str, branch_name: str, transport_options: dict = None) -> str:
        """Delete a Git Branch"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.delete_git_branch(project_id=project_id, branch_name=branch_name, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="delete_golden_query")
    def tool_delete_golden_query(golden_query_id: int, transport_options: dict = None) -> str:
        """Delete Golden Query"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.delete_golden_query(golden_query_id=golden_query_id, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="delete_group")
    def tool_delete_group(group_id: str, transport_options: dict = None) -> str:
        """Delete Group"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.delete_group(group_id=group_id, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="delete_group_from_group")
    def tool_delete_group_from_group(group_id: str, deleting_group_id: str, transport_options: dict = None) -> str:
        """Deletes a Group from Group"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.delete_group_from_group(group_id=group_id, deleting_group_id=deleting_group_id, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="delete_group_user")
    def tool_delete_group_user(group_id: str, user_id: str, transport_options: dict = None) -> str:
        """Remove a User from Group"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.delete_group_user(group_id=group_id, user_id=user_id, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="delete_integration_hub")
    def tool_delete_integration_hub(integration_hub_id: str, transport_options: dict = None) -> str:
        """Delete Integration Hub"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.delete_integration_hub(integration_hub_id=integration_hub_id, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="delete_look")
    def tool_delete_look(look_id: str, transport_options: dict = None) -> str:
        """Delete Look"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.delete_look(look_id=look_id, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="delete_lookml_model")
    def tool_delete_lookml_model(lookml_model_name: str, transport_options: dict = None) -> str:
        """Delete LookML Model"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.delete_lookml_model(lookml_model_name=lookml_model_name, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="delete_model_set")
    def tool_delete_model_set(model_set_id: str, transport_options: dict = None) -> str:
        """Delete Model Set"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.delete_model_set(model_set_id=model_set_id, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="delete_oauth_client_app")
    def tool_delete_oauth_client_app(client_guid: str, transport_options: dict = None) -> str:
        """Delete OAuth Client App"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.delete_oauth_client_app(client_guid=client_guid, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="delete_oidc_test_config")
    def tool_delete_oidc_test_config(test_slug: str, transport_options: dict = None) -> str:
        """Delete OIDC Test Configuration"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.delete_oidc_test_config(test_slug=test_slug, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="delete_permission_set")
    def tool_delete_permission_set(permission_set_id: str, transport_options: dict = None) -> str:
        """Delete Permission Set"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.delete_permission_set(permission_set_id=permission_set_id, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="delete_repository_credential")
    def tool_delete_repository_credential(root_project_id: str, credential_id: str, transport_options: dict = None) -> str:
        """Delete Repository Credential"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.delete_repository_credential(root_project_id=root_project_id, credential_id=credential_id, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="delete_role")
    def tool_delete_role(role_id: str, transport_options: dict = None) -> str:
        """Delete Role"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.delete_role(role_id=role_id, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="delete_saml_test_config")
    def tool_delete_saml_test_config(test_slug: str, transport_options: dict = None) -> str:
        """Delete SAML Test Configuration"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.delete_saml_test_config(test_slug=test_slug, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="delete_scheduled_plan")
    def tool_delete_scheduled_plan(scheduled_plan_id: str, transport_options: dict = None) -> str:
        """Delete Scheduled Plan"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.delete_scheduled_plan(scheduled_plan_id=scheduled_plan_id, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="delete_service_account")
    def tool_delete_service_account(user_id: str, transport_options: dict = None) -> str:
        """Delete Service Account"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.delete_service_account(user_id=user_id, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="delete_ssh_server")
    def tool_delete_ssh_server(ssh_server_id: str, transport_options: dict = None) -> str:
        """Delete SSH Server"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.delete_ssh_server(ssh_server_id=ssh_server_id, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="delete_ssh_tunnel")
    def tool_delete_ssh_tunnel(ssh_tunnel_id: str, transport_options: dict = None) -> str:
        """Delete SSH Tunnel"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.delete_ssh_tunnel(ssh_tunnel_id=ssh_tunnel_id, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="delete_support_access_allowlist_entry")
    def tool_delete_support_access_allowlist_entry(entry_id: str, transport_options: dict = None) -> str:
        """Delete Support Access Allowlist Entry"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.delete_support_access_allowlist_entry(entry_id=entry_id, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="delete_theme")
    def tool_delete_theme(theme_id: str, transport_options: dict = None) -> str:
        """Delete Theme"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.delete_theme(theme_id=theme_id, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="delete_user")
    def tool_delete_user(user_id: str, transport_options: dict = None) -> str:
        """Delete User"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.delete_user(user_id=user_id, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="delete_user_attribute")
    def tool_delete_user_attribute(user_attribute_id: str, transport_options: dict = None) -> str:
        """Delete User Attribute"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.delete_user_attribute(user_attribute_id=user_attribute_id, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="delete_user_attribute_group_value")
    def tool_delete_user_attribute_group_value(group_id: str, user_attribute_id: str, transport_options: dict = None) -> str:
        """Delete User Attribute Group Value"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.delete_user_attribute_group_value(group_id=group_id, user_attribute_id=user_attribute_id, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="delete_user_attribute_user_value")
    def tool_delete_user_attribute_user_value(user_id: str, user_attribute_id: str, transport_options: dict = None) -> str:
        """Delete User Attribute User Value"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.delete_user_attribute_user_value(user_id=user_id, user_attribute_id=user_attribute_id, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="delete_user_credentials_api3")
    def tool_delete_user_credentials_api3(user_id: str, credentials_api3_id: str, transport_options: dict = None) -> str:
        """Delete API Credential"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.delete_user_credentials_api3(user_id=user_id, credentials_api3_id=credentials_api3_id, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="delete_user_credentials_email")
    def tool_delete_user_credentials_email(user_id: str, transport_options: dict = None) -> str:
        """Delete Email/Password Credential"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.delete_user_credentials_email(user_id=user_id, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="delete_user_credentials_embed")
    def tool_delete_user_credentials_embed(user_id: str, credentials_embed_id: str, transport_options: dict = None) -> str:
        """Delete Embedding Credential"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.delete_user_credentials_embed(user_id=user_id, credentials_embed_id=credentials_embed_id, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="delete_user_credentials_google")
    def tool_delete_user_credentials_google(user_id: str, transport_options: dict = None) -> str:
        """Delete Google Auth Credential"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.delete_user_credentials_google(user_id=user_id, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="delete_user_credentials_ldap")
    def tool_delete_user_credentials_ldap(user_id: str, transport_options: dict = None) -> str:
        """Delete LDAP Credential"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.delete_user_credentials_ldap(user_id=user_id, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="delete_user_credentials_looker_openid")
    def tool_delete_user_credentials_looker_openid(user_id: str, transport_options: dict = None) -> str:
        """Delete Looker OpenId Credential"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.delete_user_credentials_looker_openid(user_id=user_id, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="delete_user_credentials_oidc")
    def tool_delete_user_credentials_oidc(user_id: str, transport_options: dict = None) -> str:
        """Delete OIDC Auth Credential"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.delete_user_credentials_oidc(user_id=user_id, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="delete_user_credentials_saml")
    def tool_delete_user_credentials_saml(user_id: str, transport_options: dict = None) -> str:
        """Delete Saml Auth Credential"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.delete_user_credentials_saml(user_id=user_id, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="delete_user_credentials_totp")
    def tool_delete_user_credentials_totp(user_id: str, transport_options: dict = None) -> str:
        """Delete Two-Factor Credential"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.delete_user_credentials_totp(user_id=user_id, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="delete_user_login_lockout")
    def tool_delete_user_login_lockout(key: str, transport_options: dict = None) -> str:
        """Delete User Login Lockout"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.delete_user_login_lockout(key=key, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="delete_user_session")
    def tool_delete_user_session(user_id: str, session_id: str, transport_options: dict = None) -> str:
        """Delete Web Login Session"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.delete_user_session(user_id=user_id, session_id=session_id, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="deploy_ref_to_production")
    def tool_deploy_ref_to_production(project_id: str, branch: str | None = None, ref: str | None = None, transport_options: dict = None) -> str:
        """Deploy Remote Branch or Ref to Production"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.deploy_ref_to_production(project_id=project_id, branch=branch, ref=ref, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="deploy_to_production")
    def tool_deploy_to_production(project_id: str, transport_options: dict = None) -> str:
        """Deploy To Production"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.deploy_to_production(project_id=project_id, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="deregister_mobile_device")
    def tool_deregister_mobile_device(device_id: str, transport_options: dict = None) -> str:
        """Deregister Mobile Device"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.deregister_mobile_device(device_id=device_id, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="digest_emails_enabled")
    def tool_digest_emails_enabled(transport_options: dict = None) -> str:
        """Get Digest_emails"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.digest_emails_enabled(transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="disable_support_access")
    def tool_disable_support_access(transport_options: dict = None) -> str:
        """Disable Support Access"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.disable_support_access(transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="enable_support_access")
    def tool_enable_support_access(body: dict, transport_options: dict = None) -> str:
        """Enable Support Access"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.enable_support_access(body=body, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="encode_path_param")
    def tool_encode_path_param(value: str) -> str:
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.encode_path_param(value=value)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="enqueue_alert")
    def tool_enqueue_alert(alert_id: str, force: bool | None = None, transport_options: dict = None) -> str:
        """Enqueue an alert"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.enqueue_alert(alert_id=alert_id, force=force, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="fetch_and_parse_saml_idp_metadata")
    def tool_fetch_and_parse_saml_idp_metadata(body: str, transport_options: dict = None) -> str:
        """Parse SAML IdP Url"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.fetch_and_parse_saml_idp_metadata(body=body, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="fetch_integration_form")
    def tool_fetch_integration_form(integration_id: str, body: Any = None, transport_options: dict = None) -> str:
        """Fetch Remote Integration Form"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.fetch_integration_form(integration_id=integration_id, body=body, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="fetch_remote_data_action_form")
    def tool_fetch_remote_data_action_form(body: Any, transport_options: dict = None) -> str:
        """Fetch Remote Data Action Form"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.fetch_remote_data_action_form(body=body, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="find_git_branch")
    def tool_find_git_branch(project_id: str, branch_name: str, transport_options: dict = None) -> str:
        """Find a Git Branch"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.find_git_branch(project_id=project_id, branch_name=branch_name, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="folder")
    def tool_folder(folder_id: str, fields: str | None = None, transport_options: dict = None) -> str:
        """Get Folder"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.folder(folder_id=folder_id, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="folder_ancestors")
    def tool_folder_ancestors(folder_id: str, fields: str | None = None, transport_options: dict = None) -> str:
        """Get Folder Ancestors"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.folder_ancestors(folder_id=folder_id, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="folder_children")
    def tool_folder_children(folder_id: str, fields: str | None = None, page: int | None = None, per_page: int | None = None, limit: int | None = None, offset: int | None = None, sorts: str | None = None, transport_options: dict = None) -> str:
        """Get Folder Children"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.folder_children(folder_id=folder_id, fields=fields, page=page, per_page=per_page, limit=limit, offset=offset, sorts=sorts, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="folder_children_search")
    def tool_folder_children_search(folder_id: str, fields: str | None = None, sorts: str | None = None, name: str | None = None, transport_options: dict = None) -> str:
        """Search Folder Children"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.folder_children_search(folder_id=folder_id, fields=fields, sorts=sorts, name=name, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="folder_dashboards")
    def tool_folder_dashboards(folder_id: str, fields: str | None = None, transport_options: dict = None) -> str:
        """Get Folder Dashboards"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.folder_dashboards(folder_id=folder_id, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="folder_looks")
    def tool_folder_looks(folder_id: str, fields: str | None = None, transport_options: dict = None) -> str:
        """Get Folder Looks"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.folder_looks(folder_id=folder_id, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="folder_parent")
    def tool_folder_parent(folder_id: str, fields: str | None = None, transport_options: dict = None) -> str:
        """Get Folder Parent"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.folder_parent(folder_id=folder_id, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="follow_alert")
    def tool_follow_alert(alert_id: str, transport_options: dict = None) -> str:
        """Follow an alert"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.follow_alert(alert_id=alert_id, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="force_password_reset_at_next_login_for_all_users")
    def tool_force_password_reset_at_next_login_for_all_users(transport_options: dict = None) -> str:
        """Force password reset"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.force_password_reset_at_next_login_for_all_users(transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="generate_tokens_for_cookieless_session")
    def tool_generate_tokens_for_cookieless_session(body: dict, transport_options: dict = None) -> str:
        """Generate tokens for cookieless embed session"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.generate_tokens_for_cookieless_session(body=body, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="get")
    def tool_get(path: str, structure: list, query_params: Any = None, transport_options: dict = None) -> str:
        """GET method"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.get(path=path, structure=structure, query_params=query_params, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="get_agent")
    def tool_get_agent(agent_id: str, fields: str | None = None, transport_options: dict = None) -> str:
        """Get Agent"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.get_agent(agent_id=agent_id, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="get_alert")
    def tool_get_alert(alert_id: str, transport_options: dict = None) -> str:
        """Get an alert"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.get_alert(alert_id=alert_id, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="get_all_repository_credentials")
    def tool_get_all_repository_credentials(root_project_id: str, transport_options: dict = None) -> str:
        """Get All Repository Credentials"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.get_all_repository_credentials(root_project_id=root_project_id, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="get_ci_run")
    def tool_get_ci_run(project_id: str, run_id: str, fields: str | None = None, transport_options: dict = None) -> str:
        """Fetch Continuous Integration run"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.get_ci_run(project_id=project_id, run_id=run_id, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="get_continuous_integration_run")
    def tool_get_continuous_integration_run(project_id: str, run_id: str, fields: str | None = None, transport_options: dict = None) -> str:
        """Get a Continuous Integration run"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.get_continuous_integration_run(project_id=project_id, run_id=run_id, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="get_conversation")
    def tool_get_conversation(conversation_id: str, fields: str | None = None, transport_options: dict = None) -> str:
        """Get Conversation"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.get_conversation(conversation_id=conversation_id, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="get_conversation_message")
    def tool_get_conversation_message(conversation_id: str, message_id: str, fields: str | None = None, transport_options: dict = None) -> str:
        """Get Conversation Message"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.get_conversation_message(conversation_id=conversation_id, message_id=message_id, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="get_integration_hub_health")
    def tool_get_integration_hub_health(integration_hub_id: str, fields: str | None = None, transport_options: dict = None) -> str:
        """Check the health of Integration Hub"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.get_integration_hub_health(integration_hub_id=integration_hub_id, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="get_model")
    def tool_get_model(model_name: str, transport_options: dict = None) -> str:
        """Get a single model"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.get_model(model_name=model_name, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="get_self_service_model_allowed_connections")
    def tool_get_self_service_model_allowed_connections(google_sheets: bool | None = None, transport_options: dict = None) -> str:
        """Get self service allowed connections"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.get_self_service_model_allowed_connections(google_sheets=google_sheets, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="get_setting")
    def tool_get_setting(fields: str | None = None, transport_options: dict = None) -> str:
        """Get Setting"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.get_setting(fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="get_support_access_allowlist_entries")
    def tool_get_support_access_allowlist_entries(fields: str | None = None, transport_options: dict = None) -> str:
        """Get Support Access Allowlist Users"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.get_support_access_allowlist_entries(fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="git_branch")
    def tool_git_branch(project_id: str, transport_options: dict = None) -> str:
        """Get Active Git Branch"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.git_branch(project_id=project_id, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="git_deploy_key")
    def tool_git_deploy_key(project_id: str, transport_options: dict = None) -> str:
        """Git Deploy Key"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.git_deploy_key(project_id=project_id, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="graph_derived_tables_for_model")
    def tool_graph_derived_tables_for_model(model: str, format: str | None = None, color: str | None = None, transport_options: dict = None) -> str:
        """Get Derived Table graph for model"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.graph_derived_tables_for_model(model=model, format=format, color=color, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="graph_derived_tables_for_view")
    def tool_graph_derived_tables_for_view(view: str, models: str | None = None, workspace: str | None = None, transport_options: dict = None) -> str:
        """Get subgraph of derived table and dependencies"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.graph_derived_tables_for_view(view=view, models=models, workspace=workspace, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="group")
    def tool_group(group_id: str, fields: str | None = None, transport_options: dict = None) -> str:
        """Get Group"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.group(group_id=group_id, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="import_dashboard_from_lookml")
    def tool_import_dashboard_from_lookml(body: dict, transport_options: dict = None) -> str:
        """Import Dashboard from LookML"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.import_dashboard_from_lookml(body=body, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="import_lookml_dashboard")
    def tool_import_lookml_dashboard(lookml_dashboard_id: str, space_id: str, body: dict = None, raw_locale: bool | None = None, transport_options: dict = None) -> str:
        """Import LookML Dashboard"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.import_lookml_dashboard(lookml_dashboard_id=lookml_dashboard_id, space_id=space_id, body=body, raw_locale=raw_locale, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="integration")
    def tool_integration(integration_id: str, fields: str | None = None, transport_options: dict = None) -> str:
        """Get Integration"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.integration(integration_id=integration_id, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="integration_hub")
    def tool_integration_hub(integration_hub_id: str, fields: str | None = None, transport_options: dict = None) -> str:
        """Get Integration Hub"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.integration_hub(integration_hub_id=integration_hub_id, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="internal_help_resources")
    def tool_internal_help_resources(transport_options: dict = None) -> str:
        """Get Internal Help Resources"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.internal_help_resources(transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="internal_help_resources_content")
    def tool_internal_help_resources_content(transport_options: dict = None) -> str:
        """Get Internal Help Resources Content"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.internal_help_resources_content(transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="invalidate_tokens")
    def tool_invalidate_tokens(client_guid: str, transport_options: dict = None) -> str:
        """Invalidate Tokens"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.invalidate_tokens(client_guid=client_guid, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="kill_query")
    def tool_kill_query(query_task_id: str, transport_options: dict = None) -> str:
        """Kill Running Query"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.kill_query(query_task_id=query_task_id, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="ldap_config")
    def tool_ldap_config(transport_options: dict = None) -> str:
        """Get LDAP Configuration"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.ldap_config(transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="legacy_feature")
    def tool_legacy_feature(legacy_feature_id: str, transport_options: dict = None) -> str:
        """Get Legacy Feature"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.legacy_feature(legacy_feature_id=legacy_feature_id, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="lock_all")
    def tool_lock_all(project_id: str, fields: str | None = None, transport_options: dict = None) -> str:
        """Lock All"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.lock_all(project_id=project_id, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="login")
    def tool_login(client_id: str | None = None, client_secret: str | None = None, transport_options: dict = None) -> str:
        """Login"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.login(client_id=client_id, client_secret=client_secret, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="login_user")
    def tool_login_user(user_id: str, transport_options: dict = None) -> str:
        """Login user"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.login_user(user_id=user_id, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="logout")
    def tool_logout(transport_options: dict = None) -> str:
        """Logout"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.logout(transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="look")
    def tool_look(look_id: str, fields: str | None = None, transport_options: dict = None) -> str:
        """Get Look"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.look(look_id=look_id, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="lookml_model")
    def tool_lookml_model(lookml_model_name: str, fields: str | None = None, transport_options: dict = None) -> str:
        """Get LookML Model"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.lookml_model(lookml_model_name=lookml_model_name, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="lookml_model_explore")
    def tool_lookml_model_explore(lookml_model_name: str, explore_name: str, fields: str | None = None, add_drills_metadata: bool | None = None, transport_options: dict = None) -> str:
        """Get LookML Model Explore"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.lookml_model_explore(lookml_model_name=lookml_model_name, explore_name=explore_name, fields=fields, add_drills_metadata=add_drills_metadata, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="manifest")
    def tool_manifest(project_id: str, transport_options: dict = None) -> str:
        """Get Manifest"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.manifest(project_id=project_id, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="me")
    def tool_me(fields: str | None = None, transport_options: dict = None) -> str:
        """Get Current User"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.me(fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="merge_query")
    def tool_merge_query(merge_query_id: str, fields: str | None = None, transport_options: dict = None) -> str:
        """Get Merge Query"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.merge_query(merge_query_id=merge_query_id, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="mobile_settings")
    def tool_mobile_settings(transport_options: dict = None) -> str:
        """Get Mobile_Settings"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.mobile_settings(transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="model_fieldname_suggestions")
    def tool_model_fieldname_suggestions(model_name: str, view_name: str, field_name: str, term: str | None = None, filters: str | None = None, transport_options: dict = None) -> str:
        """Model field name suggestions"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.model_fieldname_suggestions(model_name=model_name, view_name=view_name, field_name=field_name, term=term, filters=filters, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="model_set")
    def tool_model_set(model_set_id: str, fields: str | None = None, transport_options: dict = None) -> str:
        """Get Model Set"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.model_set(model_set_id=model_set_id, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="move_dashboard")
    def tool_move_dashboard(dashboard_id: str, folder_id: str, transport_options: dict = None) -> str:
        """Move Dashboard"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.move_dashboard(dashboard_id=dashboard_id, folder_id=folder_id, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="move_look")
    def tool_move_look(look_id: str, folder_id: str, transport_options: dict = None) -> str:
        """Move Look"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.move_look(look_id=look_id, folder_id=folder_id, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="oauth_client_app")
    def tool_oauth_client_app(client_guid: str, fields: str | None = None, transport_options: dict = None) -> str:
        """Get OAuth Client App"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.oauth_client_app(client_guid=client_guid, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="oidc_config")
    def tool_oidc_config(transport_options: dict = None) -> str:
        """Get OIDC Configuration"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.oidc_config(transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="oidc_test_config")
    def tool_oidc_test_config(test_slug: str, transport_options: dict = None) -> str:
        """Get OIDC Test Configuration"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.oidc_test_config(test_slug=test_slug, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="parse_saml_idp_metadata")
    def tool_parse_saml_idp_metadata(body: str, transport_options: dict = None) -> str:
        """Parse SAML IdP XML"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.parse_saml_idp_metadata(body=body, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="password_config")
    def tool_password_config(transport_options: dict = None) -> str:
        """Get Password Config"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.password_config(transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="patch")
    def tool_patch(path: str, structure: list, query_params: Any = None, body: list = None, transport_options: dict = None) -> str:
        """PATCH method"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.patch(path=path, structure=structure, query_params=query_params, body=body, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="perform_data_action")
    def tool_perform_data_action(body: dict, transport_options: dict = None) -> str:
        """Send a Data Action"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.perform_data_action(body=body, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="permission_set")
    def tool_permission_set(permission_set_id: str, fields: str | None = None, transport_options: dict = None) -> str:
        """Get Permission Set"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.permission_set(permission_set_id=permission_set_id, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="post")
    def tool_post(path: str, structure: list, query_params: Any = None, body: list = None, transport_options: dict = None) -> str:
        """POST method"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.post(path=path, structure=structure, query_params=query_params, body=body, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="project")
    def tool_project(project_id: str, fields: str | None = None, transport_options: dict = None) -> str:
        """Get Project"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.project(project_id=project_id, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="project_file")
    def tool_project_file(project_id: str, file_id: str, fields: str | None = None, transport_options: dict = None) -> str:
        """Get Project File"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.project_file(project_id=project_id, file_id=file_id, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="project_validation_results")
    def tool_project_validation_results(project_id: str, fields: str | None = None, transport_options: dict = None) -> str:
        """Cached Project Validation Results"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.project_validation_results(project_id=project_id, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="project_workspace")
    def tool_project_workspace(project_id: str, fields: str | None = None, transport_options: dict = None) -> str:
        """Get Project Workspace"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.project_workspace(project_id=project_id, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="public_egress_ip_addresses")
    def tool_public_egress_ip_addresses(transport_options: dict = None) -> str:
        """Public Egress IP Addresses"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.public_egress_ip_addresses(transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="purge_artifacts")
    def tool_purge_artifacts(namespace: str, transport_options: dict = None) -> str:
        """Purge artifacts"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.purge_artifacts(namespace=namespace, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="put")
    def tool_put(path: str, structure: list = None, query_params: Any = None, body: list = None, transport_options: dict = None) -> str:
        """PUT method"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.put(path=path, structure=structure, query_params=query_params, body=body, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="query")
    def tool_query(query_id: str, fields: str | None = None, transport_options: dict = None) -> str:
        """Get Query"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.query(query_id=query_id, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="query_for_slug")
    def tool_query_for_slug(slug: str, fields: str | None = None, transport_options: dict = None) -> str:
        """Get Query for Slug"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.query_for_slug(slug=slug, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="query_task")
    def tool_query_task(query_task_id: str, fields: str | None = None, transport_options: dict = None) -> str:
        """Get Async Query Info"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.query_task(query_task_id=query_task_id, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="query_task_multi_results")
    def tool_query_task_multi_results(query_task_ids: list, transport_options: dict = None) -> str:
        """Get Multiple Async Query Results"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.query_task_multi_results(query_task_ids=query_task_ids, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="query_task_results")
    def tool_query_task_results(query_task_id: str, transport_options: dict = None) -> str:
        """Get Async Query Results"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.query_task_results(query_task_id=query_task_id, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="read_alert_notification")
    def tool_read_alert_notification(alert_notification_id: str, transport_options: dict = None) -> str:
        """Read a Notification"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.read_alert_notification(alert_notification_id=alert_notification_id, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="register_mobile_device")
    def tool_register_mobile_device(body: dict, transport_options: dict = None) -> str:
        """Register Mobile Device"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.register_mobile_device(body=body, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="register_oauth_client_app")
    def tool_register_oauth_client_app(client_guid: str, body: dict, fields: str | None = None, transport_options: dict = None) -> str:
        """Register OAuth App"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.register_oauth_client_app(client_guid=client_guid, body=body, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="render_task")
    def tool_render_task(render_task_id: str, fields: str | None = None, transport_options: dict = None) -> str:
        """Get Render Task"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.render_task(render_task_id=render_task_id, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="render_task_results")
    def tool_render_task_results(render_task_id: str, transport_options: dict = None) -> str:
        """Render Task Results"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.render_task_results(render_task_id=render_task_id, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="reset_project_to_production")
    def tool_reset_project_to_production(project_id: str, transport_options: dict = None) -> str:
        """Reset To Production"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.reset_project_to_production(project_id=project_id, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="reset_project_to_remote")
    def tool_reset_project_to_remote(project_id: str, transport_options: dict = None) -> str:
        """Reset To Remote"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.reset_project_to_remote(project_id=project_id, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="role")
    def tool_role(role_id: str, transport_options: dict = None) -> str:
        """Get Role"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.role(role_id=role_id, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="role_groups")
    def tool_role_groups(role_id: str, fields: str | None = None, transport_options: dict = None) -> str:
        """Get Role Groups"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.role_groups(role_id=role_id, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="role_users")
    def tool_role_users(role_id: str, fields: str | None = None, direct_association_only: bool | None = None, transport_options: dict = None) -> str:
        """Get Role Users"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.role_users(role_id=role_id, fields=fields, direct_association_only=direct_association_only, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="run_git_connection_test")
    def tool_run_git_connection_test(project_id: str, test_id: str, remote_url: str | None = None, use_production: str | None = None, transport_options: dict = None) -> str:
        """Run Git Connection Test"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.run_git_connection_test(project_id=project_id, test_id=test_id, remote_url=remote_url, use_production=use_production, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="run_inline_query")
    def tool_run_inline_query(result_format: str, body: dict, limit: int | None = None, apply_formatting: bool | None = None, apply_vis: bool | None = None, cache: bool | None = None, image_width: int | None = None, image_height: int | None = None, generate_drill_links: bool | None = None, force_production: bool | None = None, cache_only: bool | None = None, path_prefix: str | None = None, rebuild_pdts: bool | None = None, server_table_calcs: bool | None = None, transport_options: dict = None) -> str:
        """Run Inline Query"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.run_inline_query(result_format=result_format, body=body, limit=limit, apply_formatting=apply_formatting, apply_vis=apply_vis, cache=cache, image_width=image_width, image_height=image_height, generate_drill_links=generate_drill_links, force_production=force_production, cache_only=cache_only, path_prefix=path_prefix, rebuild_pdts=rebuild_pdts, server_table_calcs=server_table_calcs, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="run_key_driver_analysis")
    def tool_run_key_driver_analysis(body: dict, transport_options: dict = None) -> str:
        """Analyze Key Drivers"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.run_key_driver_analysis(body=body, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="run_look")
    def tool_run_look(look_id: str, result_format: str, limit: int | None = None, apply_formatting: bool | None = None, apply_vis: bool | None = None, cache: bool | None = None, image_width: int | None = None, image_height: int | None = None, generate_drill_links: bool | None = None, force_production: bool | None = None, cache_only: bool | None = None, path_prefix: str | None = None, rebuild_pdts: bool | None = None, server_table_calcs: bool | None = None, transport_options: dict = None) -> str:
        """Run Look"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.run_look(look_id=look_id, result_format=result_format, limit=limit, apply_formatting=apply_formatting, apply_vis=apply_vis, cache=cache, image_width=image_width, image_height=image_height, generate_drill_links=generate_drill_links, force_production=force_production, cache_only=cache_only, path_prefix=path_prefix, rebuild_pdts=rebuild_pdts, server_table_calcs=server_table_calcs, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="run_lookml_test")
    def tool_run_lookml_test(project_id: str, file_id: str | None = None, test: str | None = None, model: str | None = None, transport_options: dict = None) -> str:
        """Run LookML Test"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.run_lookml_test(project_id=project_id, file_id=file_id, test=test, model=model, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="run_query")
    def tool_run_query(query_id: str, result_format: str, limit: int | None = None, apply_formatting: bool | None = None, apply_vis: bool | None = None, cache: bool | None = None, image_width: int | None = None, image_height: int | None = None, generate_drill_links: bool | None = None, force_production: bool | None = None, cache_only: bool | None = None, path_prefix: str | None = None, rebuild_pdts: bool | None = None, server_table_calcs: bool | None = None, transport_options: dict = None) -> str:
        """Run Query"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.run_query(query_id=query_id, result_format=result_format, limit=limit, apply_formatting=apply_formatting, apply_vis=apply_vis, cache=cache, image_width=image_width, image_height=image_height, generate_drill_links=generate_drill_links, force_production=force_production, cache_only=cache_only, path_prefix=path_prefix, rebuild_pdts=rebuild_pdts, server_table_calcs=server_table_calcs, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="run_sql_interface_query")
    def tool_run_sql_interface_query(query_id: int, result_format: str, transport_options: dict = None) -> str:
        """Run SQL Interface Query"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.run_sql_interface_query(query_id=query_id, result_format=result_format, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="run_sql_query")
    def tool_run_sql_query(slug: str, result_format: str, download: str | None = None, transport_options: dict = None) -> str:
        """Run SQL Runner Query"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.run_sql_query(slug=slug, result_format=result_format, download=download, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="run_url_encoded_query")
    def tool_run_url_encoded_query(model_name: str, view_name: str, result_format: str, transport_options: dict = None) -> str:
        """Run Url Encoded Query"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.run_url_encoded_query(model_name=model_name, view_name=view_name, result_format=result_format, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="saml_config")
    def tool_saml_config(transport_options: dict = None) -> str:
        """Get SAML Configuration"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.saml_config(transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="saml_test_config")
    def tool_saml_test_config(test_slug: str, transport_options: dict = None) -> str:
        """Get SAML Test Configuration"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.saml_test_config(test_slug=test_slug, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="scheduled_plan")
    def tool_scheduled_plan(scheduled_plan_id: str, fields: str | None = None, transport_options: dict = None) -> str:
        """Get Scheduled Plan"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.scheduled_plan(scheduled_plan_id=scheduled_plan_id, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="scheduled_plan_run_once")
    def tool_scheduled_plan_run_once(body: dict, transport_options: dict = None) -> str:
        """Run Scheduled Plan Once"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.scheduled_plan_run_once(body=body, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="scheduled_plan_run_once_by_id")
    def tool_scheduled_plan_run_once_by_id(scheduled_plan_id: str, body: dict = None, transport_options: dict = None) -> str:
        """Run Scheduled Plan Once by Id"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.scheduled_plan_run_once_by_id(scheduled_plan_id=scheduled_plan_id, body=body, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="scheduled_plans_for_dashboard")
    def tool_scheduled_plans_for_dashboard(dashboard_id: str, user_id: str | None = None, all_users: bool | None = None, fields: str | None = None, transport_options: dict = None) -> str:
        """Scheduled Plans for Dashboard"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.scheduled_plans_for_dashboard(dashboard_id=dashboard_id, user_id=user_id, all_users=all_users, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="scheduled_plans_for_look")
    def tool_scheduled_plans_for_look(look_id: str, user_id: str | None = None, fields: str | None = None, all_users: bool | None = None, transport_options: dict = None) -> str:
        """Scheduled Plans for Look"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.scheduled_plans_for_look(look_id=look_id, user_id=user_id, fields=fields, all_users=all_users, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="scheduled_plans_for_lookml_dashboard")
    def tool_scheduled_plans_for_lookml_dashboard(lookml_dashboard_id: str, user_id: str | None = None, fields: str | None = None, all_users: bool | None = None, transport_options: dict = None) -> str:
        """Scheduled Plans for LookML Dashboard"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.scheduled_plans_for_lookml_dashboard(lookml_dashboard_id=lookml_dashboard_id, user_id=user_id, fields=fields, all_users=all_users, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="scheduled_plans_for_space")
    def tool_scheduled_plans_for_space(space_id: str, fields: str | None = None, transport_options: dict = None) -> str:
        """Scheduled Plans for Space"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.scheduled_plans_for_space(space_id=space_id, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="search_agents")
    def tool_search_agents(id: str | None = None, name: str | None = None, description: str | None = None, created_by_user_id: str | None = None, fields: str | None = None, limit: int | None = None, category: str | None = None, offset: int | None = None, sorts: str | None = None, filter_or: bool | None = None, not_owned_by: bool | None = None, deleted: bool | None = None, primary_agent_id: str | None = None, transport_options: dict = None) -> str:
        """Search Agents"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.search_agents(id=id, name=name, description=description, created_by_user_id=created_by_user_id, fields=fields, limit=limit, category=category, offset=offset, sorts=sorts, filter_or=filter_or, not_owned_by=not_owned_by, deleted=deleted, primary_agent_id=primary_agent_id, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="search_alerts")
    def tool_search_alerts(limit: int | None = None, offset: int | None = None, group_by: str | None = None, fields: str | None = None, disabled: bool | None = None, frequency: str | None = None, condition_met: bool | None = None, last_run_start: str | None = None, last_run_end: str | None = None, all_owners: bool | None = None, transport_options: dict = None) -> str:
        """Search Alerts"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.search_alerts(limit=limit, offset=offset, group_by=group_by, fields=fields, disabled=disabled, frequency=frequency, condition_met=condition_met, last_run_start=last_run_start, last_run_end=last_run_end, all_owners=all_owners, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="search_artifacts")
    def tool_search_artifacts(namespace: str, fields: str | None = None, key: str | None = None, user_ids: str | None = None, min_size: int | None = None, max_size: int | None = None, limit: int | None = None, offset: int | None = None, tally: bool | None = None, transport_options: dict = None) -> str:
        """Search artifacts"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.search_artifacts(namespace=namespace, fields=fields, key=key, user_ids=user_ids, min_size=min_size, max_size=max_size, limit=limit, offset=offset, tally=tally, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="search_boards")
    def tool_search_boards(title: str | None = None, created_at: str | None = None, first_name: str | None = None, last_name: str | None = None, fields: str | None = None, favorited: bool | None = None, creator_id: str | None = None, sorts: str | None = None, page: int | None = None, per_page: int | None = None, offset: int | None = None, limit: int | None = None, filter_or: bool | None = None, permission: str | None = None, transport_options: dict = None) -> str:
        """Search Boards"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.search_boards(title=title, created_at=created_at, first_name=first_name, last_name=last_name, fields=fields, favorited=favorited, creator_id=creator_id, sorts=sorts, page=page, per_page=per_page, offset=offset, limit=limit, filter_or=filter_or, permission=permission, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="search_content")
    def tool_search_content(terms: str, fields: str | None = None, types: str | None = None, limit: int | None = None, offset: int | None = None, page: int | None = None, per_page: int | None = None, transport_options: dict = None) -> str:
        """Search Content"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.search_content(terms=terms, fields=fields, types=types, limit=limit, offset=offset, page=page, per_page=per_page, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="search_content_favorites")
    def tool_search_content_favorites(id: str | None = None, user_id: str | None = None, content_metadata_id: str | None = None, dashboard_id: str | None = None, look_id: str | None = None, board_id: str | None = None, lookml_dashboard_id: str | None = None, include_board_items: bool | None = None, limit: int | None = None, offset: int | None = None, sorts: str | None = None, fields: str | None = None, filter_or: bool | None = None, transport_options: dict = None) -> str:
        """Search Favorite Contents"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.search_content_favorites(id=id, user_id=user_id, content_metadata_id=content_metadata_id, dashboard_id=dashboard_id, look_id=look_id, board_id=board_id, lookml_dashboard_id=lookml_dashboard_id, include_board_items=include_board_items, limit=limit, offset=offset, sorts=sorts, fields=fields, filter_or=filter_or, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="search_content_views")
    def tool_search_content_views(view_count: str | None = None, group_id: str | None = None, look_id: str | None = None, dashboard_id: str | None = None, content_metadata_id: str | None = None, start_of_week_date: str | None = None, all_time: bool | None = None, user_id: str | None = None, fields: str | None = None, limit: int | None = None, offset: int | None = None, sorts: str | None = None, filter_or: bool | None = None, transport_options: dict = None) -> str:
        """Search Content Views"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.search_content_views(view_count=view_count, group_id=group_id, look_id=look_id, dashboard_id=dashboard_id, content_metadata_id=content_metadata_id, start_of_week_date=start_of_week_date, all_time=all_time, user_id=user_id, fields=fields, limit=limit, offset=offset, sorts=sorts, filter_or=filter_or, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="search_conversations")
    def tool_search_conversations(id: str | None = None, name: str | None = None, agent_id: str | None = None, fields: str | None = None, limit: int | None = None, offset: int | None = None, sorts: str | None = None, filter_or: bool | None = None, category: str | None = None, deleted: bool | None = None, transport_options: dict = None) -> str:
        """Search Conversations"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.search_conversations(id=id, name=name, agent_id=agent_id, fields=fields, limit=limit, offset=offset, sorts=sorts, filter_or=filter_or, category=category, deleted=deleted, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="search_credentials_email")
    def tool_search_credentials_email(fields: str | None = None, limit: int | None = None, offset: int | None = None, sorts: str | None = None, id: str | None = None, email: str | None = None, emails: str | None = None, filter_or: bool | None = None, transport_options: dict = None) -> str:
        """Search CredentialsEmail"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.search_credentials_email(fields=fields, limit=limit, offset=offset, sorts=sorts, id=id, email=email, emails=emails, filter_or=filter_or, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="search_dashboard_elements")
    def tool_search_dashboard_elements(dashboard_id: str | None = None, look_id: str | None = None, title: str | None = None, deleted: bool | None = None, fields: str | None = None, filter_or: bool | None = None, sorts: str | None = None, transport_options: dict = None) -> str:
        """Search Dashboard Elements"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.search_dashboard_elements(dashboard_id=dashboard_id, look_id=look_id, title=title, deleted=deleted, fields=fields, filter_or=filter_or, sorts=sorts, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="search_dashboards")
    def tool_search_dashboards(id: str | None = None, slug: str | None = None, title: str | None = None, description: str | None = None, content_favorite_id: str | None = None, folder_id: str | None = None, deleted: str | None = None, user_id: str | None = None, view_count: str | None = None, content_metadata_id: str | None = None, curate: bool | None = None, last_viewed_at: str | None = None, fields: str | None = None, page: int | None = None, per_page: int | None = None, limit: int | None = None, offset: int | None = None, sorts: str | None = None, filter_or: bool | None = None, not_owned_by: bool | None = None, transport_options: dict = None) -> str:
        """Search Dashboards"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.search_dashboards(id=id, slug=slug, title=title, description=description, content_favorite_id=content_favorite_id, folder_id=folder_id, deleted=deleted, user_id=user_id, view_count=view_count, content_metadata_id=content_metadata_id, curate=curate, last_viewed_at=last_viewed_at, fields=fields, page=page, per_page=per_page, limit=limit, offset=offset, sorts=sorts, filter_or=filter_or, not_owned_by=not_owned_by, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="search_folders")
    def tool_search_folders(fields: str | None = None, page: int | None = None, per_page: int | None = None, limit: int | None = None, offset: int | None = None, sorts: str | None = None, name: str | None = None, id: str | None = None, parent_id: str | None = None, creator_id: str | None = None, filter_or: bool | None = None, is_shared_root: bool | None = None, is_users_root: bool | None = None, transport_options: dict = None) -> str:
        """Search Folders"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.search_folders(fields=fields, page=page, per_page=per_page, limit=limit, offset=offset, sorts=sorts, name=name, id=id, parent_id=parent_id, creator_id=creator_id, filter_or=filter_or, is_shared_root=is_shared_root, is_users_root=is_users_root, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="search_groups")
    def tool_search_groups(fields: str | None = None, limit: int | None = None, offset: int | None = None, sorts: str | None = None, filter_or: bool | None = None, id: str | None = None, name: str | None = None, external_group_id: str | None = None, externally_managed: bool | None = None, externally_orphaned: bool | None = None, transport_options: dict = None) -> str:
        """Search Groups"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.search_groups(fields=fields, limit=limit, offset=offset, sorts=sorts, filter_or=filter_or, id=id, name=name, external_group_id=external_group_id, externally_managed=externally_managed, externally_orphaned=externally_orphaned, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="search_groups_with_hierarchy")
    def tool_search_groups_with_hierarchy(fields: str | None = None, limit: int | None = None, offset: int | None = None, sorts: str | None = None, filter_or: bool | None = None, id: str | None = None, name: str | None = None, external_group_id: str | None = None, externally_managed: bool | None = None, externally_orphaned: bool | None = None, transport_options: dict = None) -> str:
        """Search Groups with Hierarchy"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.search_groups_with_hierarchy(fields=fields, limit=limit, offset=offset, sorts=sorts, filter_or=filter_or, id=id, name=name, external_group_id=external_group_id, externally_managed=externally_managed, externally_orphaned=externally_orphaned, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="search_groups_with_roles")
    def tool_search_groups_with_roles(fields: str | None = None, limit: int | None = None, offset: int | None = None, sorts: str | None = None, filter_or: bool | None = None, id: str | None = None, name: str | None = None, external_group_id: str | None = None, externally_managed: bool | None = None, externally_orphaned: bool | None = None, transport_options: dict = None) -> str:
        """Search Groups with Roles"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.search_groups_with_roles(fields=fields, limit=limit, offset=offset, sorts=sorts, filter_or=filter_or, id=id, name=name, external_group_id=external_group_id, externally_managed=externally_managed, externally_orphaned=externally_orphaned, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="search_lookml_dashboards")
    def tool_search_lookml_dashboards(folder_id: str | None = None, title: str | None = None, content_favorite_id: str | None = None, fields: str | None = None, limit: int | None = None, offset: int | None = None, sorts: str | None = None, transport_options: dict = None) -> str:
        """Search LookML Dashboards"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.search_lookml_dashboards(folder_id=folder_id, title=title, content_favorite_id=content_favorite_id, fields=fields, limit=limit, offset=offset, sorts=sorts, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="search_looks")
    def tool_search_looks(id: str | None = None, title: str | None = None, description: str | None = None, content_favorite_id: str | None = None, folder_id: str | None = None, user_id: str | None = None, view_count: str | None = None, deleted: bool | None = None, query_id: str | None = None, curate: bool | None = None, last_viewed_at: str | None = None, fields: str | None = None, page: int | None = None, per_page: int | None = None, limit: int | None = None, offset: int | None = None, sorts: str | None = None, filter_or: bool | None = None, transport_options: dict = None) -> str:
        """Search Looks"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.search_looks(id=id, title=title, description=description, content_favorite_id=content_favorite_id, folder_id=folder_id, user_id=user_id, view_count=view_count, deleted=deleted, query_id=query_id, curate=curate, last_viewed_at=last_viewed_at, fields=fields, page=page, per_page=per_page, limit=limit, offset=offset, sorts=sorts, filter_or=filter_or, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="search_model_sets")
    def tool_search_model_sets(fields: str | None = None, limit: int | None = None, offset: int | None = None, sorts: str | None = None, id: str | None = None, name: str | None = None, all_access: bool | None = None, built_in: bool | None = None, filter_or: bool | None = None, models: str | None = None, transport_options: dict = None) -> str:
        """Search Model Sets"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.search_model_sets(fields=fields, limit=limit, offset=offset, sorts=sorts, id=id, name=name, all_access=all_access, built_in=built_in, filter_or=filter_or, models=models, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="search_permission_sets")
    def tool_search_permission_sets(fields: str | None = None, limit: int | None = None, offset: int | None = None, sorts: str | None = None, id: str | None = None, name: str | None = None, all_access: bool | None = None, built_in: bool | None = None, filter_or: bool | None = None, permissions: str | None = None, transport_options: dict = None) -> str:
        """Search Permission Sets"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.search_permission_sets(fields=fields, limit=limit, offset=offset, sorts=sorts, id=id, name=name, all_access=all_access, built_in=built_in, filter_or=filter_or, permissions=permissions, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="search_reports")
    def tool_search_reports(folder_id: str | None = None, favorite: bool | None = None, recent: bool | None = None, id: str | None = None, title: str | None = None, sorts: str | None = None, limit: int | None = None, fields: str | None = None, next_page_token: str | None = None, transport_options: dict = None) -> str:
        """Search Reports"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.search_reports(folder_id=folder_id, favorite=favorite, recent=recent, id=id, title=title, sorts=sorts, limit=limit, fields=fields, next_page_token=next_page_token, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="search_roles")
    def tool_search_roles(fields: str | None = None, limit: int | None = None, offset: int | None = None, sorts: str | None = None, id: str | None = None, model_set_ids: str | None = None, permission_set_ids: str | None = None, name: str | None = None, built_in: bool | None = None, filter_or: bool | None = None, transport_options: dict = None) -> str:
        """Search Roles"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.search_roles(fields=fields, limit=limit, offset=offset, sorts=sorts, id=id, model_set_ids=model_set_ids, permission_set_ids=permission_set_ids, name=name, built_in=built_in, filter_or=filter_or, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="search_roles_with_user_count")
    def tool_search_roles_with_user_count(fields: str | None = None, limit: int | None = None, offset: int | None = None, sorts: str | None = None, id: str | None = None, name: str | None = None, built_in: bool | None = None, filter_or: bool | None = None, transport_options: dict = None) -> str:
        """Search Roles with User Count"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.search_roles_with_user_count(fields=fields, limit=limit, offset=offset, sorts=sorts, id=id, name=name, built_in=built_in, filter_or=filter_or, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="search_scheduled_plans")
    def tool_search_scheduled_plans(user_id: str | None = None, fields: str | None = None, all_users: bool | None = None, limit: int | None = None, offset: int | None = None, sorts: str | None = None, name: str | None = None, user_first_name: str | None = None, user_last_name: str | None = None, dashboard_id: str | None = None, look_id: str | None = None, lookml_dashboard_id: str | None = None, recipient: str | None = None, destination_type: str | None = None, delivery_format: str | None = None, filter_or: bool | None = None, transport_options: dict = None) -> str:
        """Search Scheduled Plans"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.search_scheduled_plans(user_id=user_id, fields=fields, all_users=all_users, limit=limit, offset=offset, sorts=sorts, name=name, user_first_name=user_first_name, user_last_name=user_last_name, dashboard_id=dashboard_id, look_id=look_id, lookml_dashboard_id=lookml_dashboard_id, recipient=recipient, destination_type=destination_type, delivery_format=delivery_format, filter_or=filter_or, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="search_themes")
    def tool_search_themes(id: str | None = None, name: str | None = None, begin_at: Any = None, end_at: Any = None, limit: int | None = None, offset: int | None = None, sorts: str | None = None, fields: str | None = None, filter_or: bool | None = None, theme_type: str | None = None, transport_options: dict = None) -> str:
        """Search Themes"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.search_themes(id=id, name=name, begin_at=begin_at, end_at=end_at, limit=limit, offset=offset, sorts=sorts, fields=fields, filter_or=filter_or, theme_type=theme_type, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="search_user_login_lockouts")
    def tool_search_user_login_lockouts(fields: str | None = None, page: int | None = None, per_page: int | None = None, limit: int | None = None, offset: int | None = None, sorts: str | None = None, auth_type: str | None = None, full_name: str | None = None, email: str | None = None, remote_id: str | None = None, filter_or: bool | None = None, transport_options: dict = None) -> str:
        """Search User Login Lockouts"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.search_user_login_lockouts(fields=fields, page=page, per_page=per_page, limit=limit, offset=offset, sorts=sorts, auth_type=auth_type, full_name=full_name, email=email, remote_id=remote_id, filter_or=filter_or, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="search_users")
    def tool_search_users(fields: str | None = None, page: int | None = None, per_page: int | None = None, limit: int | None = None, offset: int | None = None, sorts: str | None = None, id: str | None = None, first_name: str | None = None, last_name: str | None = None, full_name: str | None = None, verified_looker_employee: bool | None = None, embed_user: bool | None = None, email: str | None = None, is_disabled: bool | None = None, filter_or: bool | None = None, content_metadata_id: str | None = None, group_id: str | None = None, can_manage_api3_creds: bool | None = None, is_service_account: bool | None = None, transport_options: dict = None) -> str:
        """Search Users"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.search_users(fields=fields, page=page, per_page=per_page, limit=limit, offset=offset, sorts=sorts, id=id, first_name=first_name, last_name=last_name, full_name=full_name, verified_looker_employee=verified_looker_employee, embed_user=embed_user, email=email, is_disabled=is_disabled, filter_or=filter_or, content_metadata_id=content_metadata_id, group_id=group_id, can_manage_api3_creds=can_manage_api3_creds, is_service_account=is_service_account, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="search_users_names")
    def tool_search_users_names(pattern: str, fields: str | None = None, page: int | None = None, per_page: int | None = None, limit: int | None = None, offset: int | None = None, sorts: str | None = None, id: str | None = None, first_name: str | None = None, last_name: str | None = None, verified_looker_employee: bool | None = None, email: str | None = None, is_disabled: bool | None = None, transport_options: dict = None) -> str:
        """Search User Names"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.search_users_names(pattern=pattern, fields=fields, page=page, per_page=per_page, limit=limit, offset=offset, sorts=sorts, id=id, first_name=first_name, last_name=last_name, verified_looker_employee=verified_looker_employee, email=email, is_disabled=is_disabled, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="send_user_credentials_email_password_reset")
    def tool_send_user_credentials_email_password_reset(user_id: str, fields: str | None = None, transport_options: dict = None) -> str:
        """Send Password Reset Token"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.send_user_credentials_email_password_reset(user_id=user_id, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="session")
    def tool_session(transport_options: dict = None) -> str:
        """Get Auth"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.session(transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="session_config")
    def tool_session_config(transport_options: dict = None) -> str:
        """Get Session Config"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.session_config(transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="set_default_color_collection")
    def tool_set_default_color_collection(collection_id: str, transport_options: dict = None) -> str:
        """Set Default Color Collection"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.set_default_color_collection(collection_id=collection_id, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="set_default_theme")
    def tool_set_default_theme(name: str, transport_options: dict = None) -> str:
        """Set Default Theme"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.set_default_theme(name=name, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="set_role_groups")
    def tool_set_role_groups(role_id: str, body: Any, transport_options: dict = None) -> str:
        """Update Role Groups"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.set_role_groups(role_id=role_id, body=body, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="set_role_users")
    def tool_set_role_users(role_id: str, body: Any, transport_options: dict = None) -> str:
        """Update Role Users"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.set_role_users(role_id=role_id, body=body, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="set_setting")
    def tool_set_setting(body: dict, fields: str | None = None, transport_options: dict = None) -> str:
        """Set Setting"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.set_setting(body=body, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="set_smtp_settings")
    def tool_set_smtp_settings(body: dict, transport_options: dict = None) -> str:
        """Set SMTP Setting"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.set_smtp_settings(body=body, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="set_user_attribute_group_values")
    def tool_set_user_attribute_group_values(user_attribute_id: str, body: list, transport_options: dict = None) -> str:
        """Set User Attribute Group Values"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.set_user_attribute_group_values(user_attribute_id=user_attribute_id, body=body, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="set_user_attribute_user_value")
    def tool_set_user_attribute_user_value(user_id: str, user_attribute_id: str, body: dict, transport_options: dict = None) -> str:
        """Set User Attribute User Value"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.set_user_attribute_user_value(user_id=user_id, user_attribute_id=user_attribute_id, body=body, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="set_user_roles")
    def tool_set_user_roles(user_id: str, body: Any, fields: str | None = None, transport_options: dict = None) -> str:
        """Set User Roles"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.set_user_roles(user_id=user_id, body=body, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="smtp_status")
    def tool_smtp_status(fields: str | None = None, transport_options: dict = None) -> str:
        """Get SMTP Status"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.smtp_status(fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="sql_interface_metadata")
    def tool_sql_interface_metadata(avatica_request: str | None = None, transport_options: dict = None) -> str:
        """Get SQL Interface Query Metadata"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.sql_interface_metadata(avatica_request=avatica_request, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="sql_query")
    def tool_sql_query(slug: str, transport_options: dict = None) -> str:
        """Get SQL Runner Query"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.sql_query(slug=slug, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="ssh_public_key")
    def tool_ssh_public_key(transport_options: dict = None) -> str:
        """Get SSH Public Key"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.ssh_public_key(transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="ssh_server")
    def tool_ssh_server(ssh_server_id: str, transport_options: dict = None) -> str:
        """Get SSH Server"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.ssh_server(ssh_server_id=ssh_server_id, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="ssh_tunnel")
    def tool_ssh_tunnel(ssh_tunnel_id: str, transport_options: dict = None) -> str:
        """Get SSH Tunnel"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.ssh_tunnel(ssh_tunnel_id=ssh_tunnel_id, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="start_pdt_build")
    def tool_start_pdt_build(model_name: str, view_name: str, force_rebuild: str | None = None, force_full_incremental: str | None = None, workspace: str | None = None, source: str | None = None, transport_options: dict = None) -> str:
        """Start a PDT materialization"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.start_pdt_build(model_name=model_name, view_name=view_name, force_rebuild=force_rebuild, force_full_incremental=force_full_incremental, workspace=workspace, source=source, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="stop_pdt_build")
    def tool_stop_pdt_build(materialization_id: str, source: str | None = None, transport_options: dict = None) -> str:
        """Stop a PDT materialization"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.stop_pdt_build(materialization_id=materialization_id, source=source, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="support_access_status")
    def tool_support_access_status(transport_options: dict = None) -> str:
        """Support Access Status"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.support_access_status(transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="sync_lookml_dashboard")
    def tool_sync_lookml_dashboard(lookml_dashboard_id: str, raw_locale: bool | None = None, dashboard_ids: list = None, transport_options: dict = None) -> str:
        """Sync LookML Dashboard"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.sync_lookml_dashboard(lookml_dashboard_id=lookml_dashboard_id, raw_locale=raw_locale, dashboard_ids=dashboard_ids, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="tag_ref")
    def tool_tag_ref(project_id: str, body: dict, commit_sha: str | None = None, tag_name: str | None = None, tag_message: str | None = None, transport_options: dict = None) -> str:
        """Tag Ref"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.tag_ref(project_id=project_id, body=body, commit_sha=commit_sha, tag_name=tag_name, tag_message=tag_message, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="test_connection")
    def tool_test_connection(connection_name: str, tests: list = None, transport_options: dict = None) -> str:
        """Test Connection"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.test_connection(connection_name=connection_name, tests=tests, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="test_connection_config")
    def tool_test_connection_config(body: dict, tests: list = None, transport_options: dict = None) -> str:
        """Test Connection Configuration"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.test_connection_config(body=body, tests=tests, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="test_integration")
    def tool_test_integration(integration_id: str, transport_options: dict = None) -> str:
        """Test integration"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.test_integration(integration_id=integration_id, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="test_ldap_config_auth")
    def tool_test_ldap_config_auth(body: dict, transport_options: dict = None) -> str:
        """Test LDAP Auth"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.test_ldap_config_auth(body=body, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="test_ldap_config_connection")
    def tool_test_ldap_config_connection(body: dict, transport_options: dict = None) -> str:
        """Test LDAP Connection"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.test_ldap_config_connection(body=body, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="test_ldap_config_user_auth")
    def tool_test_ldap_config_user_auth(body: dict, transport_options: dict = None) -> str:
        """Test LDAP User Auth"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.test_ldap_config_user_auth(body=body, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="test_ldap_config_user_info")
    def tool_test_ldap_config_user_info(body: dict, transport_options: dict = None) -> str:
        """Test LDAP User Info"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.test_ldap_config_user_info(body=body, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="test_ssh_server")
    def tool_test_ssh_server(ssh_server_id: str, transport_options: dict = None) -> str:
        """Test SSH Server"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.test_ssh_server(ssh_server_id=ssh_server_id, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="test_ssh_tunnel")
    def tool_test_ssh_tunnel(ssh_tunnel_id: str, transport_options: dict = None) -> str:
        """Test SSH Tunnel"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.test_ssh_tunnel(ssh_tunnel_id=ssh_tunnel_id, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="theme")
    def tool_theme(theme_id: str, fields: str | None = None, transport_options: dict = None) -> str:
        """Get Theme"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.theme(theme_id=theme_id, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="theme_or_default")
    def tool_theme_or_default(name: str, ts: Any = None, transport_options: dict = None) -> str:
        """Get Theme or Default"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.theme_or_default(name=name, ts=ts, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="unfollow_alert")
    def tool_unfollow_alert(alert_id: str, transport_options: dict = None) -> str:
        """Unfollow an alert"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.unfollow_alert(alert_id=alert_id, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="update_agent")
    def tool_update_agent(agent_id: str, body: dict, fields: str | None = None, transport_options: dict = None) -> str:
        """Update Agent"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.update_agent(agent_id=agent_id, body=body, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="update_alert")
    def tool_update_alert(alert_id: str, body: dict, transport_options: dict = None) -> str:
        """Update an alert"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.update_alert(alert_id=alert_id, body=body, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="update_alert_field")
    def tool_update_alert_field(alert_id: str, body: dict, transport_options: dict = None) -> str:
        """Update select fields on an alert"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.update_alert_field(alert_id=alert_id, body=body, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="update_artifacts")
    def tool_update_artifacts(namespace: str, body: list, fields: str | None = None, transport_options: dict = None) -> str:
        """Create or update artifacts"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.update_artifacts(namespace=namespace, body=body, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="update_board")
    def tool_update_board(board_id: str, body: dict, fields: str | None = None, transport_options: dict = None) -> str:
        """Update Board"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.update_board(board_id=board_id, body=body, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="update_board_item")
    def tool_update_board_item(board_item_id: str, body: dict, fields: str | None = None, transport_options: dict = None) -> str:
        """Update Board Item"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.update_board_item(board_item_id=board_item_id, body=body, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="update_board_section")
    def tool_update_board_section(board_section_id: str, body: dict, fields: str | None = None, transport_options: dict = None) -> str:
        """Update Board section"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.update_board_section(board_section_id=board_section_id, body=body, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="update_cloud_storage_configuration")
    def tool_update_cloud_storage_configuration(body: dict, transport_options: dict = None) -> str:
        """Update Cloud Storage"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.update_cloud_storage_configuration(body=body, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="update_color_collection")
    def tool_update_color_collection(collection_id: str, body: dict, transport_options: dict = None) -> str:
        """Update Custom Color collection"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.update_color_collection(collection_id=collection_id, body=body, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="update_connection")
    def tool_update_connection(connection_name: str, body: dict, transport_options: dict = None) -> str:
        """Update Connection"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.update_connection(connection_name=connection_name, body=body, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="update_content_metadata")
    def tool_update_content_metadata(content_metadata_id: str, body: dict, transport_options: dict = None) -> str:
        """Update Content Metadata"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.update_content_metadata(content_metadata_id=content_metadata_id, body=body, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="update_content_metadata_access")
    def tool_update_content_metadata_access(content_metadata_access_id: str, body: dict, transport_options: dict = None) -> str:
        """Update Content Metadata Access"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.update_content_metadata_access(content_metadata_access_id=content_metadata_access_id, body=body, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="update_conversation")
    def tool_update_conversation(conversation_id: str, body: dict, fields: str | None = None, transport_options: dict = None) -> str:
        """Update Conversation"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.update_conversation(conversation_id=conversation_id, body=body, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="update_conversation_message")
    def tool_update_conversation_message(conversation_id: str, message_id: str, body: dict, fields: str | None = None, transport_options: dict = None) -> str:
        """Update Conversation Message"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.update_conversation_message(conversation_id=conversation_id, message_id=message_id, body=body, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="update_custom_welcome_email")
    def tool_update_custom_welcome_email(body: dict, send_test_welcome_email: bool | None = None, transport_options: dict = None) -> str:
        """Update Custom Welcome Email Content"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.update_custom_welcome_email(body=body, send_test_welcome_email=send_test_welcome_email, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="update_custom_welcome_email_test")
    def tool_update_custom_welcome_email_test(body: dict, transport_options: dict = None) -> str:
        """Send a test welcome email to the currently logged in user with the supplied content"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.update_custom_welcome_email_test(body=body, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="update_dashboard")
    def tool_update_dashboard(dashboard_id: str, body: dict, transport_options: dict = None) -> str:
        """Update Dashboard"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.update_dashboard(dashboard_id=dashboard_id, body=body, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="update_dashboard_certification")
    def tool_update_dashboard_certification(dashboard_id: str, body: dict, transport_options: dict = None) -> str:
        """Update Dashboard Certification"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.update_dashboard_certification(dashboard_id=dashboard_id, body=body, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="update_dashboard_element")
    def tool_update_dashboard_element(dashboard_element_id: str, body: dict, fields: str | None = None, transport_options: dict = None) -> str:
        """Update DashboardElement"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.update_dashboard_element(dashboard_element_id=dashboard_element_id, body=body, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="update_dashboard_filter")
    def tool_update_dashboard_filter(dashboard_filter_id: str, body: dict, fields: str | None = None, transport_options: dict = None) -> str:
        """Update Dashboard Filter"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.update_dashboard_filter(dashboard_filter_id=dashboard_filter_id, body=body, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="update_dashboard_layout")
    def tool_update_dashboard_layout(dashboard_layout_id: str, body: dict, fields: str | None = None, transport_options: dict = None) -> str:
        """Update DashboardLayout"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.update_dashboard_layout(dashboard_layout_id=dashboard_layout_id, body=body, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="update_dashboard_layout_component")
    def tool_update_dashboard_layout_component(dashboard_layout_component_id: str, body: dict, fields: str | None = None, transport_options: dict = None) -> str:
        """Update DashboardLayoutComponent"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.update_dashboard_layout_component(dashboard_layout_component_id=dashboard_layout_component_id, body=body, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="update_datagroup")
    def tool_update_datagroup(datagroup_id: str, body: dict, transport_options: dict = None) -> str:
        """Update Datagroup"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.update_datagroup(datagroup_id=datagroup_id, body=body, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="update_digest_emails_enabled")
    def tool_update_digest_emails_enabled(body: dict, transport_options: dict = None) -> str:
        """Update Digest_emails"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.update_digest_emails_enabled(body=body, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="update_external_oauth_application")
    def tool_update_external_oauth_application(client_id: str, body: dict, transport_options: dict = None) -> str:
        """Update External OAuth Application"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.update_external_oauth_application(client_id=client_id, body=body, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="update_folder")
    def tool_update_folder(folder_id: str, body: dict, transport_options: dict = None) -> str:
        """Update Folder"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.update_folder(folder_id=folder_id, body=body, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="update_git_branch")
    def tool_update_git_branch(project_id: str, body: dict, transport_options: dict = None) -> str:
        """Update Project Git Branch"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.update_git_branch(project_id=project_id, body=body, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="update_golden_query")
    def tool_update_golden_query(golden_query_id: int, body: dict, transport_options: dict = None) -> str:
        """Update Golden Query"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.update_golden_query(golden_query_id=golden_query_id, body=body, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="update_group")
    def tool_update_group(group_id: str, body: dict, fields: str | None = None, transport_options: dict = None) -> str:
        """Update Group"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.update_group(group_id=group_id, body=body, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="update_integration")
    def tool_update_integration(integration_id: str, body: dict, fields: str | None = None, transport_options: dict = None) -> str:
        """Update Integration"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.update_integration(integration_id=integration_id, body=body, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="update_integration_hub")
    def tool_update_integration_hub(integration_hub_id: str, body: dict, fields: str | None = None, transport_options: dict = None) -> str:
        """Update Integration Hub"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.update_integration_hub(integration_hub_id=integration_hub_id, body=body, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="update_internal_help_resources")
    def tool_update_internal_help_resources(body: dict, transport_options: dict = None) -> str:
        """Update internal help resources configuration"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.update_internal_help_resources(body=body, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="update_internal_help_resources_content")
    def tool_update_internal_help_resources_content(body: dict, transport_options: dict = None) -> str:
        """Update internal help resources content"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.update_internal_help_resources_content(body=body, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="update_ldap_config")
    def tool_update_ldap_config(body: dict, transport_options: dict = None) -> str:
        """Update LDAP Configuration"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.update_ldap_config(body=body, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="update_legacy_feature")
    def tool_update_legacy_feature(legacy_feature_id: str, body: dict, transport_options: dict = None) -> str:
        """Update Legacy Feature"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.update_legacy_feature(legacy_feature_id=legacy_feature_id, body=body, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="update_look")
    def tool_update_look(look_id: str, body: dict, fields: str | None = None, transport_options: dict = None) -> str:
        """Update Look"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.update_look(look_id=look_id, body=body, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="update_look_certification")
    def tool_update_look_certification(look_id: str, body: dict, transport_options: dict = None) -> str:
        """Update Look Certification"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.update_look_certification(look_id=look_id, body=body, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="update_lookml_certification")
    def tool_update_lookml_certification(dashboard_id: str, body: dict, transport_options: dict = None) -> str:
        """Update LookML Dashboard Certification"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.update_lookml_certification(dashboard_id=dashboard_id, body=body, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="update_lookml_model")
    def tool_update_lookml_model(lookml_model_name: str, body: dict, transport_options: dict = None) -> str:
        """Update LookML Model"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.update_lookml_model(lookml_model_name=lookml_model_name, body=body, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="update_mobile_device_registration")
    def tool_update_mobile_device_registration(device_id: str, transport_options: dict = None) -> str:
        """Update Mobile Device Registration"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.update_mobile_device_registration(device_id=device_id, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="update_model_set")
    def tool_update_model_set(model_set_id: str, body: dict, transport_options: dict = None) -> str:
        """Update Model Set"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.update_model_set(model_set_id=model_set_id, body=body, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="update_oauth_client_app")
    def tool_update_oauth_client_app(client_guid: str, body: dict, fields: str | None = None, transport_options: dict = None) -> str:
        """Update OAuth App"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.update_oauth_client_app(client_guid=client_guid, body=body, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="update_oidc_config")
    def tool_update_oidc_config(body: dict, transport_options: dict = None) -> str:
        """Update OIDC Configuration"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.update_oidc_config(body=body, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="update_password_config")
    def tool_update_password_config(body: dict, transport_options: dict = None) -> str:
        """Update Password Config"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.update_password_config(body=body, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="update_permission_set")
    def tool_update_permission_set(permission_set_id: str, body: dict, transport_options: dict = None) -> str:
        """Update Permission Set"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.update_permission_set(permission_set_id=permission_set_id, body=body, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="update_project")
    def tool_update_project(project_id: str, body: dict, fields: str | None = None, transport_options: dict = None) -> str:
        """Update Project"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.update_project(project_id=project_id, body=body, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="update_repository_credential")
    def tool_update_repository_credential(root_project_id: str, credential_id: str, body: dict, transport_options: dict = None) -> str:
        """Create Repository Credential"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.update_repository_credential(root_project_id=root_project_id, credential_id=credential_id, body=body, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="update_role")
    def tool_update_role(role_id: str, body: dict, transport_options: dict = None) -> str:
        """Update Role"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.update_role(role_id=role_id, body=body, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="update_saml_config")
    def tool_update_saml_config(body: dict, transport_options: dict = None) -> str:
        """Update SAML Configuration"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.update_saml_config(body=body, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="update_scheduled_plan")
    def tool_update_scheduled_plan(scheduled_plan_id: str, body: dict, transport_options: dict = None) -> str:
        """Update Scheduled Plan"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.update_scheduled_plan(scheduled_plan_id=scheduled_plan_id, body=body, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="update_self_service_explore_certification")
    def tool_update_self_service_explore_certification(model_name: str, body: dict, transport_options: dict = None) -> str:
        """Update certification for a Self Service Explore"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.update_self_service_explore_certification(model_name=model_name, body=body, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="update_service_account")
    def tool_update_service_account(user_id: str, body: dict, fields: str | None = None, transport_options: dict = None) -> str:
        """Update Service Account"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.update_service_account(user_id=user_id, body=body, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="update_session")
    def tool_update_session(body: dict, transport_options: dict = None) -> str:
        """Update Auth"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.update_session(body=body, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="update_session_config")
    def tool_update_session_config(body: dict, transport_options: dict = None) -> str:
        """Update Session Config"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.update_session_config(body=body, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="update_ssh_server")
    def tool_update_ssh_server(ssh_server_id: str, body: dict, transport_options: dict = None) -> str:
        """Update SSH Server"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.update_ssh_server(ssh_server_id=ssh_server_id, body=body, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="update_ssh_tunnel")
    def tool_update_ssh_tunnel(ssh_tunnel_id: str, body: dict, transport_options: dict = None) -> str:
        """Update SSH Tunnel"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.update_ssh_tunnel(ssh_tunnel_id=ssh_tunnel_id, body=body, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="update_theme")
    def tool_update_theme(theme_id: str, body: dict, transport_options: dict = None) -> str:
        """Update Theme"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.update_theme(theme_id=theme_id, body=body, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="update_user")
    def tool_update_user(user_id: str, body: dict, fields: str | None = None, transport_options: dict = None) -> str:
        """Update User"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.update_user(user_id=user_id, body=body, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="update_user_attribute")
    def tool_update_user_attribute(user_attribute_id: str, body: dict, fields: str | None = None, transport_options: dict = None) -> str:
        """Update User Attribute"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.update_user_attribute(user_attribute_id=user_attribute_id, body=body, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="update_user_attribute_group_value")
    def tool_update_user_attribute_group_value(group_id: str, user_attribute_id: str, body: dict, transport_options: dict = None) -> str:
        """Set User Attribute Group Value"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.update_user_attribute_group_value(group_id=group_id, user_attribute_id=user_attribute_id, body=body, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="update_user_credentials_api3")
    def tool_update_user_credentials_api3(user_id: str, credentials_api3_id: str, body: dict, fields: str | None = None, transport_options: dict = None) -> str:
        """Update API Credential"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.update_user_credentials_api3(user_id=user_id, credentials_api3_id=credentials_api3_id, body=body, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="update_user_credentials_email")
    def tool_update_user_credentials_email(user_id: str, body: dict, fields: str | None = None, transport_options: dict = None) -> str:
        """Update Email/Password Credential"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.update_user_credentials_email(user_id=user_id, body=body, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="update_whitelabel_configuration")
    def tool_update_whitelabel_configuration(body: dict, transport_options: dict = None) -> str:
        """Update Private label configuration"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.update_whitelabel_configuration(body=body, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="user")
    def tool_user(user_id: str, fields: str | None = None, transport_options: dict = None) -> str:
        """Get User by Id"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.user(user_id=user_id, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="user_attribute")
    def tool_user_attribute(user_attribute_id: str, fields: str | None = None, transport_options: dict = None) -> str:
        """Get User Attribute"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.user_attribute(user_attribute_id=user_attribute_id, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="user_attribute_user_values")
    def tool_user_attribute_user_values(user_id: str, fields: str | None = None, user_attribute_ids: list = None, all_values: bool | None = None, include_unset: bool | None = None, transport_options: dict = None) -> str:
        """Get User Attribute Values"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.user_attribute_user_values(user_id=user_id, fields=fields, user_attribute_ids=user_attribute_ids, all_values=all_values, include_unset=include_unset, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="user_credentials_api3")
    def tool_user_credentials_api3(user_id: str, credentials_api3_id: str, fields: str | None = None, transport_options: dict = None) -> str:
        """Get API Credential"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.user_credentials_api3(user_id=user_id, credentials_api3_id=credentials_api3_id, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="user_credentials_email")
    def tool_user_credentials_email(user_id: str, fields: str | None = None, transport_options: dict = None) -> str:
        """Get Email/Password Credential"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.user_credentials_email(user_id=user_id, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="user_credentials_embed")
    def tool_user_credentials_embed(user_id: str, credentials_embed_id: str, fields: str | None = None, transport_options: dict = None) -> str:
        """Get Embedding Credential"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.user_credentials_embed(user_id=user_id, credentials_embed_id=credentials_embed_id, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="user_credentials_google")
    def tool_user_credentials_google(user_id: str, fields: str | None = None, transport_options: dict = None) -> str:
        """Get Google Auth Credential"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.user_credentials_google(user_id=user_id, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="user_credentials_ldap")
    def tool_user_credentials_ldap(user_id: str, fields: str | None = None, transport_options: dict = None) -> str:
        """Get LDAP Credential"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.user_credentials_ldap(user_id=user_id, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="user_credentials_looker_openid")
    def tool_user_credentials_looker_openid(user_id: str, fields: str | None = None, transport_options: dict = None) -> str:
        """Get Looker OpenId Credential"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.user_credentials_looker_openid(user_id=user_id, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="user_credentials_oidc")
    def tool_user_credentials_oidc(user_id: str, fields: str | None = None, transport_options: dict = None) -> str:
        """Get OIDC Auth Credential"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.user_credentials_oidc(user_id=user_id, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="user_credentials_saml")
    def tool_user_credentials_saml(user_id: str, fields: str | None = None, transport_options: dict = None) -> str:
        """Get Saml Auth Credential"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.user_credentials_saml(user_id=user_id, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="user_credentials_totp")
    def tool_user_credentials_totp(user_id: str, fields: str | None = None, transport_options: dict = None) -> str:
        """Get Two-Factor Credential"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.user_credentials_totp(user_id=user_id, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="user_for_credential")
    def tool_user_for_credential(credential_type: str, credential_id: str, fields: str | None = None, transport_options: dict = None) -> str:
        """Get User by Credential Id"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.user_for_credential(credential_type=credential_type, credential_id=credential_id, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="user_roles")
    def tool_user_roles(user_id: str, fields: str | None = None, direct_association_only: bool | None = None, transport_options: dict = None) -> str:
        """Get User Roles"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.user_roles(user_id=user_id, fields=fields, direct_association_only=direct_association_only, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="user_session")
    def tool_user_session(user_id: str, session_id: str, fields: str | None = None, transport_options: dict = None) -> str:
        """Get Web Login Session"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.user_session(user_id=user_id, session_id=session_id, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="validate_embed_url")
    def tool_validate_embed_url(url: str | None = None, transport_options: dict = None) -> str:
        """Get Embed URL Validation"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.validate_embed_url(url=url, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="validate_project")
    def tool_validate_project(project_id: str, fields: str | None = None, transport_options: dict = None) -> str:
        """Validate Project"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.validate_project(project_id=project_id, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="validate_theme")
    def tool_validate_theme(body: dict, transport_options: dict = None) -> str:
        """Validate Theme"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.validate_theme(body=body, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="vector_thumbnail")
    def tool_vector_thumbnail(type: str, resource_id: str, reload: str | None = None, transport_options: dict = None) -> str:
        """Get Vector Thumbnail"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.vector_thumbnail(type=type, resource_id=resource_id, reload=reload, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="versions")
    def tool_versions(fields: str | None = None, transport_options: dict = None) -> str:
        """Get ApiVersion"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.versions(fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="whitelabel_configuration")
    def tool_whitelabel_configuration(fields: str | None = None, transport_options: dict = None) -> str:
        """Get Private label configuration"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.whitelabel_configuration(fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="wipeout_user_emails")
    def tool_wipeout_user_emails(user_id: str, body: dict, fields: str | None = None, transport_options: dict = None) -> str:
        """Wipeout User Emails"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.wipeout_user_emails(user_id=user_id, body=body, fields=fields, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    @mcp.tool(name="workspace")
    def tool_workspace(workspace_id: str, transport_options: dict = None) -> str:
        """Get Workspace"""
        sdk = get_sdk()
        if sdk is None: return "Looker SDK not initialized"
        try:
            result = sdk.workspace(workspace_id=workspace_id, transport_options=transport_options)
            return str(result)
        except Exception as e:
            return f"Error: {e}"

