import io
from contextlib import redirect_stdout
import unittest
from unittest.mock import patch

try:
    from game import play
except ImportError as e:
    print("Could not import a function called 'play' from 'game.py'")

try:
    from calculator import calculator
except ImportError as e:
    print("Could not import a function called 'calculator' from 'calculator.py'")


class FunctionsTest(unittest.TestCase):
    @patch("builtins.input", side_effect=["4", "6", "bob", "5"])
    def test_game(self, input):
        output = io.StringIO()   
        with redirect_stdout(output):
            try:
                play(5)
            except NameError as e:
                self.fail("The function 'play' is not defined")
        assert output.getvalue().split("\n") == ["Too Low!", "Too High!", "Invalid Input!", "You Win!", ""]

    def test_calculator(self):
        try:
            self.assertEqual(calculator(5, 5, "+"), 10) 
            self.assertEqual(calculator(5, 3, "-"), 2)
            self.assertEqual(calculator(5, 5, "*"), 25)
            self.assertEqual(calculator(10, 5, "/"), 2)
            output = io.StringIO()
            with redirect_stdout(output):
                calculator(10, 3, "^")
            self.assertEqual(output.getvalue().rstrip("\n"), "Invalid Operator")
        except NameError as e:
            self.fail("The function 'calculator' is not defined")
        
if __name__ == "__main__":
    unittest.main()