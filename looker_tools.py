import inspect
import json
from typing import Any, Dict
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
    def dispatch(endpoint_name, arguments):
        sdk = get_sdk()
        if sdk is None:
            return "Looker SDK not initialized. Please configure credentials."
        method = getattr(sdk, endpoint_name, None)
        if not method: return f"Error: Endpoint {endpoint_name} not found."
        try:
            result = method(**arguments)
            if hasattr(result, '__dict__'): return str(result.__dict__)
            elif isinstance(result, list): return str([r.__dict__ if hasattr(r, '__dict__') else str(r) for r in result])
            return str(result)
        except Exception as e:
            return f"Looker API Error: {str(e)}"

    @mcp.tool(name="looker_dashboards")
    def looker_dashboards(endpoint_name: str, arguments: dict) -> str:
        """Call a Looker API endpoint in the Dashboards category.
        Available endpoints: all_dashboards, copy_dashboard, create_dashboard, create_dashboard_element, create_dashboard_element_render_task, create_dashboard_filter, create_dashboard_filter_state, create_dashboard_from_lookml, create_dashboard_layout, create_dashboard_render_task, dashboard, dashboard_aggregate_table_lookml, dashboard_dashboard_elements, dashboard_dashboard_filters, dashboard_dashboard_layouts, dashboard_element, dashboard_filter, dashboard_filter_state, dashboard_layout, dashboard_layout_component, dashboard_layout_dashboard_layout_components, dashboard_lookml, delete_dashboard, delete_dashboard_element, delete_dashboard_filter, delete_dashboard_layout, folder_dashboards, import_dashboard_from_lookml, import_lookml_dashboard, move_dashboard, scheduled_plans_for_dashboard, scheduled_plans_for_lookml_dashboard, search_dashboard_elements, search_dashboards, search_lookml_dashboards, sync_lookml_dashboard, update_dashboard, update_dashboard_certification, update_dashboard_element, update_dashboard_filter, update_dashboard_layout, update_dashboard_layout_component
        Arguments must be a valid dict matching the endpoint schema.
        """
        if endpoint_name not in ['all_dashboards', 'copy_dashboard', 'create_dashboard', 'create_dashboard_element', 'create_dashboard_element_render_task', 'create_dashboard_filter', 'create_dashboard_filter_state', 'create_dashboard_from_lookml', 'create_dashboard_layout', 'create_dashboard_render_task', 'dashboard', 'dashboard_aggregate_table_lookml', 'dashboard_dashboard_elements', 'dashboard_dashboard_filters', 'dashboard_dashboard_layouts', 'dashboard_element', 'dashboard_filter', 'dashboard_filter_state', 'dashboard_layout', 'dashboard_layout_component', 'dashboard_layout_dashboard_layout_components', 'dashboard_lookml', 'delete_dashboard', 'delete_dashboard_element', 'delete_dashboard_filter', 'delete_dashboard_layout', 'folder_dashboards', 'import_dashboard_from_lookml', 'import_lookml_dashboard', 'move_dashboard', 'scheduled_plans_for_dashboard', 'scheduled_plans_for_lookml_dashboard', 'search_dashboard_elements', 'search_dashboards', 'search_lookml_dashboards', 'sync_lookml_dashboard', 'update_dashboard', 'update_dashboard_certification', 'update_dashboard_element', 'update_dashboard_filter', 'update_dashboard_layout', 'update_dashboard_layout_component']:
            return "Error: Invalid endpoint for this category."
        return dispatch(endpoint_name, arguments)

    @mcp.tool(name="looker_looks")
    def looker_looks(endpoint_name: str, arguments: dict) -> str:
        """Call a Looker API endpoint in the Looks category.
        Available endpoints: all_lookml_models, all_lookml_tests, all_looks, copy_look, create_look, create_look_render_task, create_lookml_model, delete_look, delete_lookml_model, delete_user_credentials_looker_openid, folder_looks, look, lookml_model, lookml_model_explore, move_look, run_look, run_lookml_test, scheduled_plans_for_look, search_looks, update_look, update_look_certification, update_lookml_certification, update_lookml_model, user_credentials_looker_openid
        Arguments must be a valid dict matching the endpoint schema.
        """
        if endpoint_name not in ['all_lookml_models', 'all_lookml_tests', 'all_looks', 'copy_look', 'create_look', 'create_look_render_task', 'create_lookml_model', 'delete_look', 'delete_lookml_model', 'delete_user_credentials_looker_openid', 'folder_looks', 'look', 'lookml_model', 'lookml_model_explore', 'move_look', 'run_look', 'run_lookml_test', 'scheduled_plans_for_look', 'search_looks', 'update_look', 'update_look_certification', 'update_lookml_certification', 'update_lookml_model', 'user_credentials_looker_openid']:
            return "Error: Invalid endpoint for this category."
        return dispatch(endpoint_name, arguments)

    @mcp.tool(name="looker_queries")
    def looker_queries(endpoint_name: str, arguments: dict) -> str:
        """Call a Looker API endpoint in the Queries category.
        Available endpoints: create_golden_query, create_merge_query, create_query, create_query_render_task, create_query_task, create_sql_interface_query, create_sql_query, delete_golden_query, kill_query, merge_query, query, query_for_slug, query_task, query_task_multi_results, query_task_results, run_inline_query, run_query, run_sql_interface_query, run_sql_query, run_url_encoded_query, sql_interface_metadata, sql_query, update_golden_query
        Arguments must be a valid dict matching the endpoint schema.
        """
        if endpoint_name not in ['create_golden_query', 'create_merge_query', 'create_query', 'create_query_render_task', 'create_query_task', 'create_sql_interface_query', 'create_sql_query', 'delete_golden_query', 'kill_query', 'merge_query', 'query', 'query_for_slug', 'query_task', 'query_task_multi_results', 'query_task_results', 'run_inline_query', 'run_query', 'run_sql_interface_query', 'run_sql_query', 'run_url_encoded_query', 'sql_interface_metadata', 'sql_query', 'update_golden_query']:
            return "Error: Invalid endpoint for this category."
        return dispatch(endpoint_name, arguments)

    @mcp.tool(name="looker_users_and_authentication")
    def looker_users_and_authentication(endpoint_name: str, arguments: dict) -> str:
        """Call a Looker API endpoint in the Users_and_Authentication category.
        Available endpoints: acquire_embed_cookieless_session, activate_app_user, add_group_user, all_external_oauth_applications, all_group_users, all_oauth_client_apps, all_user_attribute_group_values, all_user_attributes, all_user_credentials_api3s, all_user_credentials_embeds, all_user_login_lockouts, all_user_sessions, all_users, create_embed_user, create_external_oauth_application, create_oauth_application_user_state, create_user, create_user_attribute, create_user_credentials_api3, create_user_credentials_email, create_user_credentials_email_password_reset, create_user_credentials_totp, deactivate_app_user, delete_embed_cookieless_session, delete_external_oauth_application, delete_group_user, delete_oauth_client_app, delete_repository_credential, delete_user, delete_user_attribute, delete_user_attribute_group_value, delete_user_attribute_user_value, delete_user_credentials_api3, delete_user_credentials_email, delete_user_credentials_embed, delete_user_credentials_google, delete_user_credentials_ldap, delete_user_credentials_oidc, delete_user_credentials_saml, delete_user_credentials_totp, delete_user_login_lockout, delete_user_session, force_password_reset_at_next_login_for_all_users, generate_tokens_for_cookieless_session, get_all_repository_credentials, login_user, me, oauth_client_app, register_oauth_client_app, role_users, search_credentials_email, search_roles_with_user_count, search_user_login_lockouts, search_users, search_users_names, send_user_credentials_email_password_reset, session, session_config, set_role_users, set_user_attribute_group_values, set_user_attribute_user_value, set_user_roles, test_ldap_config_auth, test_ldap_config_user_auth, test_ldap_config_user_info, update_external_oauth_application, update_oauth_client_app, update_repository_credential, update_session, update_session_config, update_user, update_user_attribute, update_user_attribute_group_value, update_user_credentials_api3, update_user_credentials_email, user, user_attribute, user_attribute_user_values, user_credentials_api3, user_credentials_email, user_credentials_embed, user_credentials_google, user_credentials_ldap, user_credentials_oidc, user_credentials_saml, user_credentials_totp, user_for_credential, user_roles, user_session, wipeout_user_emails
        Arguments must be a valid dict matching the endpoint schema.
        """
        if endpoint_name not in ['acquire_embed_cookieless_session', 'activate_app_user', 'add_group_user', 'all_external_oauth_applications', 'all_group_users', 'all_oauth_client_apps', 'all_user_attribute_group_values', 'all_user_attributes', 'all_user_credentials_api3s', 'all_user_credentials_embeds', 'all_user_login_lockouts', 'all_user_sessions', 'all_users', 'create_embed_user', 'create_external_oauth_application', 'create_oauth_application_user_state', 'create_user', 'create_user_attribute', 'create_user_credentials_api3', 'create_user_credentials_email', 'create_user_credentials_email_password_reset', 'create_user_credentials_totp', 'deactivate_app_user', 'delete_embed_cookieless_session', 'delete_external_oauth_application', 'delete_group_user', 'delete_oauth_client_app', 'delete_repository_credential', 'delete_user', 'delete_user_attribute', 'delete_user_attribute_group_value', 'delete_user_attribute_user_value', 'delete_user_credentials_api3', 'delete_user_credentials_email', 'delete_user_credentials_embed', 'delete_user_credentials_google', 'delete_user_credentials_ldap', 'delete_user_credentials_oidc', 'delete_user_credentials_saml', 'delete_user_credentials_totp', 'delete_user_login_lockout', 'delete_user_session', 'force_password_reset_at_next_login_for_all_users', 'generate_tokens_for_cookieless_session', 'get_all_repository_credentials', 'login_user', 'me', 'oauth_client_app', 'register_oauth_client_app', 'role_users', 'search_credentials_email', 'search_roles_with_user_count', 'search_user_login_lockouts', 'search_users', 'search_users_names', 'send_user_credentials_email_password_reset', 'session', 'session_config', 'set_role_users', 'set_user_attribute_group_values', 'set_user_attribute_user_value', 'set_user_roles', 'test_ldap_config_auth', 'test_ldap_config_user_auth', 'test_ldap_config_user_info', 'update_external_oauth_application', 'update_oauth_client_app', 'update_repository_credential', 'update_session', 'update_session_config', 'update_user', 'update_user_attribute', 'update_user_attribute_group_value', 'update_user_credentials_api3', 'update_user_credentials_email', 'user', 'user_attribute', 'user_attribute_user_values', 'user_credentials_api3', 'user_credentials_email', 'user_credentials_embed', 'user_credentials_google', 'user_credentials_ldap', 'user_credentials_oidc', 'user_credentials_saml', 'user_credentials_totp', 'user_for_credential', 'user_roles', 'user_session', 'wipeout_user_emails']:
            return "Error: Invalid endpoint for this category."
        return dispatch(endpoint_name, arguments)

    @mcp.tool(name="looker_groups_and_roles")
    def looker_groups_and_roles(endpoint_name: str, arguments: dict) -> str:
        """Call a Looker API endpoint in the Groups_and_Roles category.
        Available endpoints: add_group_group, all_datagroups, all_group_groups, all_groups, all_permission_sets, all_permissions, all_roles, create_group, create_permission_set, create_role, datagroup, delete_group, delete_group_from_group, delete_permission_set, delete_role, group, permission_set, role, role_groups, search_groups, search_groups_with_hierarchy, search_groups_with_roles, search_permission_sets, search_roles, set_role_groups, update_datagroup, update_group, update_permission_set, update_role
        Arguments must be a valid dict matching the endpoint schema.
        """
        if endpoint_name not in ['add_group_group', 'all_datagroups', 'all_group_groups', 'all_groups', 'all_permission_sets', 'all_permissions', 'all_roles', 'create_group', 'create_permission_set', 'create_role', 'datagroup', 'delete_group', 'delete_group_from_group', 'delete_permission_set', 'delete_role', 'group', 'permission_set', 'role', 'role_groups', 'search_groups', 'search_groups_with_hierarchy', 'search_groups_with_roles', 'search_permission_sets', 'search_roles', 'set_role_groups', 'update_datagroup', 'update_group', 'update_permission_set', 'update_role']:
            return "Error: Invalid endpoint for this category."
        return dispatch(endpoint_name, arguments)

    @mcp.tool(name="looker_projects_and_workspaces")
    def looker_projects_and_workspaces(endpoint_name: str, arguments: dict) -> str:
        """Call a Looker API endpoint in the Projects_and_Workspaces category.
        Available endpoints: all_git_branches, all_git_connection_tests, all_project_files, all_projects, all_workspaces, create_git_branch, create_git_deploy_key, create_project, delete_git_branch, find_git_branch, git_branch, git_deploy_key, project, project_file, project_validation_results, project_workspace, reset_project_to_production, reset_project_to_remote, run_git_connection_test, update_git_branch, update_project, validate_project, workspace
        Arguments must be a valid dict matching the endpoint schema.
        """
        if endpoint_name not in ['all_git_branches', 'all_git_connection_tests', 'all_project_files', 'all_projects', 'all_workspaces', 'create_git_branch', 'create_git_deploy_key', 'create_project', 'delete_git_branch', 'find_git_branch', 'git_branch', 'git_deploy_key', 'project', 'project_file', 'project_validation_results', 'project_workspace', 'reset_project_to_production', 'reset_project_to_remote', 'run_git_connection_test', 'update_git_branch', 'update_project', 'validate_project', 'workspace']:
            return "Error: Invalid endpoint for this category."
        return dispatch(endpoint_name, arguments)

    @mcp.tool(name="looker_folders_and_spaces")
    def looker_folders_and_spaces(endpoint_name: str, arguments: dict) -> str:
        """Call a Looker API endpoint in the Folders_and_Spaces category.
        Available endpoints: all_folders, artifact_namespaces, create_folder, delete_folder, folder, folder_ancestors, folder_children, folder_children_search, folder_parent, scheduled_plans_for_space, search_folders, update_folder
        Arguments must be a valid dict matching the endpoint schema.
        """
        if endpoint_name not in ['all_folders', 'artifact_namespaces', 'create_folder', 'delete_folder', 'folder', 'folder_ancestors', 'folder_children', 'folder_children_search', 'folder_parent', 'scheduled_plans_for_space', 'search_folders', 'update_folder']:
            return "Error: Invalid endpoint for this category."
        return dispatch(endpoint_name, arguments)

    @mcp.tool(name="looker_connections_and_databases")
    def looker_connections_and_databases(endpoint_name: str, arguments: dict) -> str:
        """Call a Looker API endpoint in the Connections_and_Databases category.
        Available endpoints: all_connections, all_dialect_infos, connection, connection_columns, connection_cost_estimate, connection_databases, connection_features, connection_schemas, connection_search_columns, connection_tables, create_connection, delete_connection, delete_connection_override, get_self_service_model_allowed_connections, test_connection, test_connection_config, test_ldap_config_connection, update_connection
        Arguments must be a valid dict matching the endpoint schema.
        """
        if endpoint_name not in ['all_connections', 'all_dialect_infos', 'connection', 'connection_columns', 'connection_cost_estimate', 'connection_databases', 'connection_features', 'connection_schemas', 'connection_search_columns', 'connection_tables', 'create_connection', 'delete_connection', 'delete_connection_override', 'get_self_service_model_allowed_connections', 'test_connection', 'test_connection_config', 'test_ldap_config_connection', 'update_connection']:
            return "Error: Invalid endpoint for this category."
        return dispatch(endpoint_name, arguments)

    @mcp.tool(name="looker_models_and_explores")
    def looker_models_and_explores(endpoint_name: str, arguments: dict) -> str:
        """Call a Looker API endpoint in the Models_and_Explores category.
        Available endpoints: active_themes, all_color_collections, all_model_sets, all_themes, color_collection, color_collections_custom, color_collections_standard, create_color_collection, create_model_set, create_theme, default_color_collection, default_theme, delete_color_collection, delete_model_set, delete_theme, get_model, graph_derived_tables_for_model, graph_derived_tables_for_view, model_fieldname_suggestions, model_set, search_content_views, search_model_sets, search_themes, set_default_color_collection, set_default_theme, theme, theme_or_default, update_color_collection, update_model_set, update_self_service_explore_certification, update_theme, validate_theme
        Arguments must be a valid dict matching the endpoint schema.
        """
        if endpoint_name not in ['active_themes', 'all_color_collections', 'all_model_sets', 'all_themes', 'color_collection', 'color_collections_custom', 'color_collections_standard', 'create_color_collection', 'create_model_set', 'create_theme', 'default_color_collection', 'default_theme', 'delete_color_collection', 'delete_model_set', 'delete_theme', 'get_model', 'graph_derived_tables_for_model', 'graph_derived_tables_for_view', 'model_fieldname_suggestions', 'model_set', 'search_content_views', 'search_model_sets', 'search_themes', 'set_default_color_collection', 'set_default_theme', 'theme', 'theme_or_default', 'update_color_collection', 'update_model_set', 'update_self_service_explore_certification', 'update_theme', 'validate_theme']:
            return "Error: Invalid endpoint for this category."
        return dispatch(endpoint_name, arguments)

    @mcp.tool(name="looker_boards")
    def looker_boards(endpoint_name: str, arguments: dict) -> str:
        """Call a Looker API endpoint in the Boards category.
        Available endpoints: all_board_items, all_board_sections, all_boards, all_primary_homepage_sections, board, board_item, board_section, create_board, create_board_item, create_board_section, delete_board, delete_board_item, delete_board_section, search_boards, update_board, update_board_item, update_board_section
        Arguments must be a valid dict matching the endpoint schema.
        """
        if endpoint_name not in ['all_board_items', 'all_board_sections', 'all_boards', 'all_primary_homepage_sections', 'board', 'board_item', 'board_section', 'create_board', 'create_board_item', 'create_board_section', 'delete_board', 'delete_board_item', 'delete_board_section', 'search_boards', 'update_board', 'update_board_item', 'update_board_section']:
            return "Error: Invalid endpoint for this category."
        return dispatch(endpoint_name, arguments)

    @mcp.tool(name="looker_alerts_and_schedules")
    def looker_alerts_and_schedules(endpoint_name: str, arguments: dict) -> str:
        """Call a Looker API endpoint in the Alerts_and_Schedules category.
        Available endpoints: alert_notifications, all_scheduled_plans, create_alert, create_scheduled_plan, delete_alert, delete_scheduled_plan, enqueue_alert, follow_alert, get_alert, read_alert_notification, scheduled_plan, scheduled_plan_run_once, scheduled_plan_run_once_by_id, search_alerts, search_scheduled_plans, unfollow_alert, update_alert, update_alert_field, update_scheduled_plan
        Arguments must be a valid dict matching the endpoint schema.
        """
        if endpoint_name not in ['alert_notifications', 'all_scheduled_plans', 'create_alert', 'create_scheduled_plan', 'delete_alert', 'delete_scheduled_plan', 'enqueue_alert', 'follow_alert', 'get_alert', 'read_alert_notification', 'scheduled_plan', 'scheduled_plan_run_once', 'scheduled_plan_run_once_by_id', 'search_alerts', 'search_scheduled_plans', 'unfollow_alert', 'update_alert', 'update_alert_field', 'update_scheduled_plan']:
            return "Error: Invalid endpoint for this category."
        return dispatch(endpoint_name, arguments)

    @mcp.tool(name="looker_system_and_misc")
    def looker_system_and_misc(endpoint_name: str, arguments: dict) -> str:
        """Call a Looker API endpoint in the System_and_Misc category.
        Available endpoints: accept_integration_hub_legal_agreement, add_support_access_allowlist_entries, all_content_metadata_accesses, all_content_metadatas, all_conversation_messages, all_integration_hubs, all_integrations, all_legacy_features, all_locales, all_running_queries, all_ssh_servers, all_ssh_tunnels, all_timezones, api_spec, artifact, artifact_usage, artifact_value, async_deploy_ref_to_production, async_deploy_status, check_pdt_build, cloud_storage_configuration, content_favorite, content_metadata, content_summary, content_thumbnail, content_validation, conversational_analytics_chat, create_agent, create_ci_run, create_content_favorite, create_content_metadata_access, create_continuous_integration_run, create_conversation, create_conversation_message, create_digest_email_send, create_embed_secret, create_embed_url_as_me, create_integration_hub, create_oidc_test_config, create_saml_test_config, create_service_account, create_ssh_server, create_ssh_tunnel, create_sso_embed_url, custom_welcome_email, delete, delete_agent, delete_artifact, delete_content_favorite, delete_content_metadata_access, delete_conversation, delete_conversation_message, delete_embed_secret, delete_integration_hub, delete_oidc_test_config, delete_saml_test_config, delete_service_account, delete_ssh_server, delete_ssh_tunnel, delete_support_access_allowlist_entry, deploy_ref_to_production, deploy_to_production, deregister_mobile_device, digest_emails_enabled, disable_support_access, enable_support_access, encode_path_param, fetch_and_parse_saml_idp_metadata, fetch_integration_form, fetch_remote_data_action_form, get, get_agent, get_ci_run, get_continuous_integration_run, get_conversation, get_conversation_message, get_integration_hub_health, get_setting, get_support_access_allowlist_entries, integration, integration_hub, internal_help_resources, internal_help_resources_content, invalidate_tokens, ldap_config, legacy_feature, lock_all, login, logout, manifest, mobile_settings, oidc_config, oidc_test_config, parse_saml_idp_metadata, password_config, patch, perform_data_action, post, public_egress_ip_addresses, purge_artifacts, put, register_mobile_device, render_task, render_task_results, run_key_driver_analysis, saml_config, saml_test_config, search_agents, search_artifacts, search_content, search_content_favorites, search_conversations, search_reports, set_setting, set_smtp_settings, smtp_status, ssh_public_key, ssh_server, ssh_tunnel, start_pdt_build, stop_pdt_build, support_access_status, tag_ref, test_integration, test_ssh_server, test_ssh_tunnel, update_agent, update_artifacts, update_cloud_storage_configuration, update_content_metadata, update_content_metadata_access, update_conversation, update_conversation_message, update_custom_welcome_email, update_custom_welcome_email_test, update_digest_emails_enabled, update_integration, update_integration_hub, update_internal_help_resources, update_internal_help_resources_content, update_ldap_config, update_legacy_feature, update_mobile_device_registration, update_oidc_config, update_password_config, update_saml_config, update_service_account, update_ssh_server, update_ssh_tunnel, update_whitelabel_configuration, validate_embed_url, vector_thumbnail, versions, whitelabel_configuration
        Arguments must be a valid dict matching the endpoint schema.
        """
        if endpoint_name not in ['accept_integration_hub_legal_agreement', 'add_support_access_allowlist_entries', 'all_content_metadata_accesses', 'all_content_metadatas', 'all_conversation_messages', 'all_integration_hubs', 'all_integrations', 'all_legacy_features', 'all_locales', 'all_running_queries', 'all_ssh_servers', 'all_ssh_tunnels', 'all_timezones', 'api_spec', 'artifact', 'artifact_usage', 'artifact_value', 'async_deploy_ref_to_production', 'async_deploy_status', 'check_pdt_build', 'cloud_storage_configuration', 'content_favorite', 'content_metadata', 'content_summary', 'content_thumbnail', 'content_validation', 'conversational_analytics_chat', 'create_agent', 'create_ci_run', 'create_content_favorite', 'create_content_metadata_access', 'create_continuous_integration_run', 'create_conversation', 'create_conversation_message', 'create_digest_email_send', 'create_embed_secret', 'create_embed_url_as_me', 'create_integration_hub', 'create_oidc_test_config', 'create_saml_test_config', 'create_service_account', 'create_ssh_server', 'create_ssh_tunnel', 'create_sso_embed_url', 'custom_welcome_email', 'delete', 'delete_agent', 'delete_artifact', 'delete_content_favorite', 'delete_content_metadata_access', 'delete_conversation', 'delete_conversation_message', 'delete_embed_secret', 'delete_integration_hub', 'delete_oidc_test_config', 'delete_saml_test_config', 'delete_service_account', 'delete_ssh_server', 'delete_ssh_tunnel', 'delete_support_access_allowlist_entry', 'deploy_ref_to_production', 'deploy_to_production', 'deregister_mobile_device', 'digest_emails_enabled', 'disable_support_access', 'enable_support_access', 'encode_path_param', 'fetch_and_parse_saml_idp_metadata', 'fetch_integration_form', 'fetch_remote_data_action_form', 'get', 'get_agent', 'get_ci_run', 'get_continuous_integration_run', 'get_conversation', 'get_conversation_message', 'get_integration_hub_health', 'get_setting', 'get_support_access_allowlist_entries', 'integration', 'integration_hub', 'internal_help_resources', 'internal_help_resources_content', 'invalidate_tokens', 'ldap_config', 'legacy_feature', 'lock_all', 'login', 'logout', 'manifest', 'mobile_settings', 'oidc_config', 'oidc_test_config', 'parse_saml_idp_metadata', 'password_config', 'patch', 'perform_data_action', 'post', 'public_egress_ip_addresses', 'purge_artifacts', 'put', 'register_mobile_device', 'render_task', 'render_task_results', 'run_key_driver_analysis', 'saml_config', 'saml_test_config', 'search_agents', 'search_artifacts', 'search_content', 'search_content_favorites', 'search_conversations', 'search_reports', 'set_setting', 'set_smtp_settings', 'smtp_status', 'ssh_public_key', 'ssh_server', 'ssh_tunnel', 'start_pdt_build', 'stop_pdt_build', 'support_access_status', 'tag_ref', 'test_integration', 'test_ssh_server', 'test_ssh_tunnel', 'update_agent', 'update_artifacts', 'update_cloud_storage_configuration', 'update_content_metadata', 'update_content_metadata_access', 'update_conversation', 'update_conversation_message', 'update_custom_welcome_email', 'update_custom_welcome_email_test', 'update_digest_emails_enabled', 'update_integration', 'update_integration_hub', 'update_internal_help_resources', 'update_internal_help_resources_content', 'update_ldap_config', 'update_legacy_feature', 'update_mobile_device_registration', 'update_oidc_config', 'update_password_config', 'update_saml_config', 'update_service_account', 'update_ssh_server', 'update_ssh_tunnel', 'update_whitelabel_configuration', 'validate_embed_url', 'vector_thumbnail', 'versions', 'whitelabel_configuration']:
            return "Error: Invalid endpoint for this category."
        return dispatch(endpoint_name, arguments)
