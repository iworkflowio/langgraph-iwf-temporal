"""
Basic tests for the langgraph-iwf-temporal library.
"""

import saf


def test_version():
    """Test that version is available."""
    assert saf.__version__ == "0.1.0"


def test_author():
    """Test that author information is available."""
    assert saf.__author__ == "Indeed"


def test_email():
    """Test that email information is available."""
    assert saf.__email__ == "opensource@indeed.com"


def test_import():
    """Test that the package can be imported."""
    import saf
    assert saf is not None