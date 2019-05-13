"""
Unit and regression test for the hey package.
"""

# Import package, test suite, and other packages as needed
import hey
import pytest
import sys

def test_hey_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "hey" in sys.modules
