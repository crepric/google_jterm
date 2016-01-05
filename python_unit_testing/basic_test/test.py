import unittest
import code

class CodeTester(unittest.TestCase):
  
  def setUp(self):
    # This is called before each test, we don't need
    # setup though, so it's empty
    pass

  def TearDown(self):
    # This is called after each test, we don't need
    # closure, so it's empty
    pass
  
  def testReturnNoneNeverReturnsSomethingElse(self):
    res = code.returnNone()
    self.assertIsNone(res)

  def testReturnArgumentWorksForInts(self):
    # Test Positive Numbers
    res = code.returnArgument(132)
    self.assertEqual(132, res)
    # Test Negative Numbers
    res = code.returnArgument(-112)
    self.assertEqual(-112, res)
    # Test Zero
    res = code.returnArgument(0)
    self.assertEqual(0, res)
  
  def testReturnArgumentWorksForFloats(self):
    # Test Positive Numbers
    res = code.returnArgument(5.34)
    # Floats are always approximated in computers,
    # so a very small difference would be acceptable,
    # assertAlmostEqual is more tolerant than assertEqual
    self.assertAlmostEqual(5.34, res)
   
  def testReturnArgumentWorksForNone(self):
    # Test Positive Numbers
    res = code.returnArgument(None)
    self.assertIsNone(res)
 
  def testReturnArgumentWorksForList(self):
    # Test Positive Numbers
    mylist = [1, 5, 8, 'a', 'foo']
    res = code.returnArgument(mylist)
    self.assertSequenceEqual(res, mylist)
 
 
if __name__ == "__main__":
  unittest.main()
