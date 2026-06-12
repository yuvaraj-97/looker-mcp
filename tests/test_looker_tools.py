import os
import pytest
from unittest.mock import patch, MagicMock
from mcp.server.fastmcp import FastMCP
from looker_tools import register_looker_tools
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
    result = tool_func("invalid_endpoint", {})
    assert "Error: Invalid endpoint for this category" in result

@patch('looker_tools.get_sdk')
def test_valid_endpoint_call(mock_get_sdk, registered_mcp, mock_sdk):
    mock_get_sdk.return_value = mock_sdk
    
    tool_func = None
    for t in registered_mcp._tool_manager.list_tools():
        if t.name == "looker_dashboards":
            tool_func = t.fn
            break
            
    result = tool_func("all_dashboards", {"limit": 10})
    
    mock_sdk.all_dashboards.assert_called_once_with(limit=10)
    assert "Test Dashboard" in result

def test_initialize_looker_credentials(registered_mcp, mock_sdk):
    tool_func = None
    for t in registered_mcp._tool_manager.list_tools():
        if t.name == "initialize_looker_credentials":
            tool_func = t.fn
            break
            
    result = tool_func("https://test.looker.com", "client123", "secret123")
    assert os.environ["LOOKER_BASE_URL"] == "https://test.looker.com"
    assert os.environ["LOOKER_CLIENT_ID"] == "client123"
    assert "Successfully initialized Looker SDK" in result
