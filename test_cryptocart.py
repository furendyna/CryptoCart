# test_cryptocart.py
"""
Tests for CryptoCart module.
"""

import unittest
from cryptocart import CryptoCart

class TestCryptoCart(unittest.TestCase):
    """Test cases for CryptoCart class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CryptoCart()
        self.assertIsInstance(instance, CryptoCart)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CryptoCart()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
