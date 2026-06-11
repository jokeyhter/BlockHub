# test_blockhub.py
"""
Tests for BlockHub module.
"""

import unittest
from blockhub import BlockHub

class TestBlockHub(unittest.TestCase):
    """Test cases for BlockHub class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BlockHub()
        self.assertIsInstance(instance, BlockHub)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BlockHub()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
