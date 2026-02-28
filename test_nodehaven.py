# test_nodehaven.py
"""
Tests for NodeHaven module.
"""

import unittest
from nodehaven import NodeHaven

class TestNodeHaven(unittest.TestCase):
    """Test cases for NodeHaven class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NodeHaven()
        self.assertIsInstance(instance, NodeHaven)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NodeHaven()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
