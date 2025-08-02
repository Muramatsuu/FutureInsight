# test_futureinsight.py
"""
Tests for FutureInsight module.
"""

import unittest
from futureinsight import FutureInsight

class TestFutureInsight(unittest.TestCase):
    """Test cases for FutureInsight class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = FutureInsight()
        self.assertIsInstance(instance, FutureInsight)
        
    def test_run_method(self):
        """Test the run method."""
        instance = FutureInsight()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
