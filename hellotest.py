import unittest
from hello import *

class MyTests(unittest.TestCase):
   ##your playground starts
   def test_hello(self):
       self.assertEqual(hello('John'), 'Happy testing! John')
   ##your playground ends

if __name__=="__main__":
   unittest.main()
