"""
Project 1
CPE 202
John Wright
"""
from stacks import *
import unittest

class TestCase(unittest.TestCase):


   def test_stackarray(self):
      stack = StackArray()
      for i in range(10):
         stack.push(i)
      self.assertEqual(stack.size(), 10)
      self.assertEqual(stack.peek(), 9)
      for i in range(10):
         val = stack.pop()
      self.assertRaises(IndexError, stack.pop)
      self.assertRaises(IndexError, stack.peek)
      self.assertEqual(stack.size(), 0)
      self.assertTrue(stack.is_empty())

   def test_stacklinked(self):
      stack = StackLinked()
      for i in range(10):
         stack.push(i)
      self.assertEqual(stack.size(), 10)
      self.assertEqual(stack.peek(), 9)
      for i in range(10):
         val = stack.pop()
      self.assertRaises(IndexError, stack.pop)
      self.assertRaises(IndexError, stack.peek)
      self.assertEqual(stack.size(), 0)
      self.assertTrue(stack.is_empty())



def main():
   # execute unit tests
   unittest.main()

if __name__ == '__main__':
   # execute main() function
   main()
