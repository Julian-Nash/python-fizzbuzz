import unittest
from fizz_buzz import fizz_buzz_v1, fizz_buzz_v2


class TestFizzBuzz(unittest.TestCase):

    # Testing fizz_buzz_v1 (if, elif, else)
    def test_fizz_buzz_v1(self):
        start = 1
        end = 5
        expected_result = "1,2,Fizz,4,Buzz"
        self.assertEqual(fizz_buzz_v1(start=start, end=end), expected_result)

    def test_fizz_buzz_v1_2(self):
        start = 1
        end = 15
        expected_result = "1,2,Fizz,4,Buzz,Fizz,7,8,Fizz,Buzz,11,Fizz,13,14,FizzBuzz"
        self.assertEqual(fizz_buzz_v1(start=start, end=end), expected_result)

    def test_fizz_buzz_v1_3(self):
        start = 1
        end = 999
        with open("fizz_buzz.txt", "r") as results:
            expected_result = results.read()
        self.assertEqual(fizz_buzz_v1(start=start, end=end), expected_result)

    # Testing fizz_buzz_v2 (List comprehension)
    def test_fizz_buzz_v2(self):
        start = 1
        end = 5
        expected_result = "1,2,Fizz,4,Buzz"
        self.assertEqual(fizz_buzz_v2(start=start, end=end), expected_result)

    def test_fizz_buzz_v2_2(self):
        start = 1
        end = 15
        expected_result = "1,2,Fizz,4,Buzz,Fizz,7,8,Fizz,Buzz,11,Fizz,13,14,FizzBuzz"
        self.assertEqual(fizz_buzz_v2(start=start, end=end), expected_result)

    def test_fizz_buzz_v2_3(self):
        start = 1
        end = 999
        with open("fizz_buzz.txt", "r") as results:
            expected_result = results.read()
        self.assertEqual(fizz_buzz_v2(start=start, end=end), expected_result)


if __name__ == "__main__":
    unittest.main()
