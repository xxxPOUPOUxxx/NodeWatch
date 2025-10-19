# test_nodewatch.py
"""
Tests for NodeWatch module.
"""

import unittest
from nodewatch import NodeWatch

class TestNodeWatch(unittest.TestCase):
    """Test cases for NodeWatch class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NodeWatch()
        self.assertIsInstance(instance, NodeWatch)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NodeWatch()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
