import unittest
try:
    from grammar import capitalize
except ImportError as e:
    print("Could not import a function called 'capitalize' from 'grammar.py'")

class StretchExerciseTest(unittest.TestCase):
    def test_cipher(self):
        try:
            self.assertEqual(capitalize("hello world"), "Hello World") 
            self.assertEqual(capitalize("Hello World"), "Hello World")
        except NameError as e:
            self.fail("The function 'decode' is not defined")