import inspect
import json
from typing import Any, Dict
import looker_sdk
from looker_sdk.sdk.api40.methods import Looker40SDK

sdk_instance = None

def get_sdk():
    global sdk_instance
    if sdk_instance is None:
        try:
            sdk_instance = looker_sdk.init40()
        except Exception as e:
            print("Warning: Looker SDK init failed:", e)
    return sdk_instance

def get_all_methods():
    return [m for m in inspect.getmembers(Looker40SDK, predicate=inspect.isfunction) if not m[0].startswith('_')]

def get_groups():
    groups = {
        "Dashboards": [],
        "Looks": [],
        "Queries": [],
        "Users_and_Authentication": [],
        "Groups_and_Roles": [],
        "Projects_and_Workspaces": [],
        "Folders_and_Spaces": [],
        "Connections_and_Databases": [],
        "Models_and_Explores": [],
        "Boards": [],
        "Alerts_and_Schedules": [],
        "System_and_Misc": []
    }
    
    for name, method in get_all_methods():
        if 'dashboard' in name: groups["Dashboards"].append((name, method))
        elif 'look' in name: groups["Looks"].append((name, method))
        elif 'query' in name or 'sql' in name: groups["Queries"].append((name, method))
        elif 'user' in name or 'session' in name or 'auth' in name or 'credential' in name or name == 'me': groups["Users_and_Authentication"].append((name, method))
        elif 'group' in name or 'role' in name or 'permission' in name: groups["Groups_and_Roles"].append((name, method))
        elif 'project' in name or 'workspace' in name or 'git' in name or 'branch' in name: groups["Projects_and_Workspaces"].append((name, method))
        elif 'folder' in name or 'space' in name: groups["Folders_and_Spaces"].append((name, method))
        elif 'connection' in name or 'datagroup' in name or 'dialect' in name: groups["Connections_and_Databases"].append((name, method))
        elif 'model' in name or 'explore' in name or 'view' in name or 'theme' in name or 'color_collection' in name or 'custom_measure' in name: groups["Models_and_Explores"].append((name, method))
        elif 'board' in name or 'homepage' in name: groups["Boards"].append((name, method))
        elif 'alert' in name or 'schedule' in name: groups["Alerts_and_Schedules"].append((name, method))
        else: groups["System_and_Misc"].append((name, method))
    return groups

def register_looker_tools(mcp):
    groups = get_groups()
    
    @mcp.tool(name="list_looker_groups")
    def list_looker_groups() -> str:
        """Returns the list of available Looker API endpoint categories/groups. Use this to find which group to explore."""
        return json.dumps(list(groups.keys()), indent=2)

    @mcp.tool(name="list_group_endpoints")
    def list_group_endpoints(group_name: str) -> str:
        """Returns the list of endpoints and their parameter schemas for a specific Looker API group."""
        if group_name not in groups:
            return f"Group not found. Available groups: {list(groups.keys())}"
        
        endpoints_info = {}
        for name, method in groups[group_name]:
            sig = inspect.signature(method)
            params = []
            for p_name, param in sig.parameters.items():
                if p_name == 'self': continue
                p_info = p_name
                if param.default != inspect.Parameter.empty:
                    p_info += f" (optional, default: {param.default})"
                params.append(p_info)
            doc = inspect.getdoc(method) or "No description"
            endpoints_info[name] = {
                "description": doc.split('\n')[0], # just first line to save tokens
                "parameters": params
            }
        return json.dumps(endpoints_info, indent=2)

    @mcp.tool(name="call_looker_endpoint")
    def call_looker_endpoint(endpoint_name: str, arguments: dict) -> str:
        """Calls a specific Looker API endpoint with the provided JSON arguments. 
        Example arguments: {"title": "Sales", "limit": 10}
        """
        sdk = get_sdk()
        if sdk is None:
            return "Looker SDK not initialized. Please configure credentials."
        
        method = getattr(sdk, endpoint_name, None)
        if not method:
            return f"Error: Endpoint {endpoint_name} not found."
        
        try:
            result = method(**arguments)
            # Basic serialization effort for complex objects
            if hasattr(result, '__dict__'):
                return str(result.__dict__)
            elif isinstance(result, list):
                return str([r.__dict__ if hasattr(r, '__dict__') else str(r) for r in result])
            return str(result)
        except Exception as e:
            return f"Looker API Error: {str(e)}"
