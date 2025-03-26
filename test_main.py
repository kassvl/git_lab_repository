import unittest
from main import main

class TestMain(unittest.TestCase):
    def test_main_runs(self):
        # This is a simple test to verify that main() runs without errors
        try:
            main()
            self.assertTrue(True)
        except Exception as e:
            self.fail(f"main() raised exception {e}")

if __name__ == '__main__':
    unittest.main()
