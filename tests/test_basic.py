"""
Basic tests for the langgraph-iwf-temporal library.
"""

import langgraph_iwf_temporal


def test_version():
    """Test that version is available."""
    assert langgraph_iwf_temporal.__version__ == "0.1.0"


def test_author():
    """Test that author information is available."""
    assert langgraph_iwf_temporal.__author__ == "Indeed"


def test_email():
    """Test that email information is available."""
    assert langgraph_iwf_temporal.__email__ == "opensource@indeed.com"


def test_import():
    """Test that the package can be imported."""
    import langgraph_iwf_temporal
    assert langgraph_iwf_temporal is not None 