"""
Unit and regression test for the cmiles_cloud package.
"""

# Import package, test suite, and other packages as needed
import cmiles_cloud
import pytest
import sys

def test_cmiles_cloud_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "cmiles_cloud" in sys.modules
