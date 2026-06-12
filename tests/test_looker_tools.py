import json
import os
import pytest
from unittest.mock import patch, MagicMock
from mcp.server.fastmcp import FastMCP
from looker_tools import register_looker_tools, serialize_result
from server import analyze_dashboard, mcp

@pytest.fixture
def mock_sdk():
    with patch('looker_tools.looker_sdk.init40') as mock_init:
        mock_instance = MagicMock()
        mock_init.return_value = mock_instance
        
        # mock all_dashboards
        mock_instance.all_dashboards.return_value = [{"id": "1", "title": "Test Dashboard"}]
        
        yield mock_instance

@pytest.fixture
def registered_mcp():
    test_mcp = FastMCP("Test")
    register_looker_tools(test_mcp)
    return test_mcp

def test_analyze_dashboard_prompt_empty():
    result = analyze_dashboard("")
    assert "I want to analyze a Looker dashboard, but I don't know the exact name or ID" in result

def test_analyze_dashboard_prompt_with_id():
    result = analyze_dashboard("123")
    assert "identified by: '123'" in result

def test_invalid_endpoint_call(registered_mcp):
    # Retrieve the registered tool for dashboards
    tool_func = None
    for t in registered_mcp._tool_manager.list_tools():
        if t.name == "looker_dashboards":
            tool_func = t.fn
            break
            
    assert tool_func is not None
    result = tool_func(action="call", endpoint="invalid_endpoint", body={})
    assert "Error: Invalid endpoint for this category" in result

@patch('looker_tools.get_sdk')
def test_valid_endpoint_call(mock_get_sdk, registered_mcp, mock_sdk):
    mock_get_sdk.return_value = mock_sdk
    
    tool_func = None
    for t in registered_mcp._tool_manager.list_tools():
        if t.name == "looker_dashboards":
            tool_func = t.fn
            break
            
    result = tool_func(action="call", endpoint="all_dashboards", body={"limit": 10})
    
    mock_sdk.all_dashboards.assert_called_once_with(limit=10)
    assert "Test Dashboard" in result

def test_initialize_looker_credentials(registered_mcp, mock_sdk):
    tool_func = None
    for t in registered_mcp._tool_manager.list_tools():
        if t.name == "initialize_looker_credentials":
            tool_func = t.fn
            break
            
    result = tool_func("https://test.looker.com", "client123", "secret123")
    # The Looker SDK reads LOOKERSDK_*-prefixed env vars.
    assert os.environ["LOOKERSDK_BASE_URL"] == "https://test.looker.com"
    assert os.environ["LOOKERSDK_CLIENT_ID"] == "client123"
    assert os.environ["LOOKERSDK_CLIENT_SECRET"] == "secret123"
    assert "Successfully initialized Looker SDK" in result


def _get_tool(registered_mcp, name):
    for t in registered_mcp._tool_manager.list_tools():
        if t.name == name:
            return t.fn
    return None


def test_serialize_result_model_to_json():
    from looker_sdk.sdk.api40 import models
    d = models.Dashboard(
        id="1", title="Sales",
        dashboard_elements=[models.DashboardElement(id="e1", title="Tile")],
    )
    out = serialize_result(d)
    parsed = json.loads(out)  # must be valid JSON
    assert parsed["id"] == "1"
    assert parsed["dashboard_elements"][0]["id"] == "e1"
    # null fields are omitted to keep output compact
    assert "content_favorite_id" not in parsed


def test_serialize_result_passthrough_and_bytes():
    # raw JSON/CSV strings (e.g. from run_query) are returned unchanged
    assert serialize_result('{"rows":[]}') == '{"rows":[]}'
    # binary payloads are summarized, not mangled
    assert serialize_result(b"\x89PNG\x00") == "<binary payload: 5 bytes>"


@patch('looker_tools.get_sdk')
def test_dispatch_accepts_json_string_arguments(mock_get_sdk, registered_mcp, mock_sdk):
    mock_get_sdk.return_value = mock_sdk
    tool_func = _get_tool(registered_mcp, "looker_dashboards")
    # client passes arguments as a JSON string instead of a dict
    tool_func(action="call", endpoint="all_dashboards", body='{"limit": 5}')
    mock_sdk.all_dashboards.assert_called_once_with(limit=5)


@patch('looker_tools.get_sdk')
def test_dispatch_rejects_malformed_arguments(mock_get_sdk, registered_mcp, mock_sdk):
    mock_get_sdk.return_value = mock_sdk
    tool_func = _get_tool(registered_mcp, "looker_dashboards")
    result = tool_func(action="call", endpoint="all_dashboards", body="not-json")
    assert "must be a JSON object" in result


def test_describe_action(registered_mcp):
    tool_func = _get_tool(registered_mcp, "looker_dashboards")
    assert tool_func is not None
    result = tool_func(action="describe")
    parsed = json.loads(result)
    assert isinstance(parsed, list)
    all_dashboards_info = next(item for item in parsed if item["name"] == "all_dashboards")
    assert "params" in all_dashboards_info
