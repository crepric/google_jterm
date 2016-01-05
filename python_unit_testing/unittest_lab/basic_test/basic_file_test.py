import unittest
import basic_file

class SimpleUnitTest(unittest.TestCase):

    # Simply forget to name this class "test" and you will
    # have the test always "PASSING", actually never running.
    # This is why it is crucial to write tests firs.
    def testFirstTest(self):
        my_val = basic_file.function()
        self.assertIsNotNone(my_val)


if __name__ == "__main__":
    unittest.main()
