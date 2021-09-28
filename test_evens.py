import unittest
from evens import even_number_of_evens


class TestEvens(unittest.TestCase):
    # Remember test names MUST start with the word test
    # Keep them related

    def test_throws_error_if_value_passed_in_is_not_list(self):
        # assertRaises is a method from TestCase and when ran will check if a
        # TypeError has been raised when the function is called with a value
        # of 4
        self.assertRaises(TypeError, even_number_of_evens, 4)

    def test_values_in_list(self):
        # Returns false if empty list is passed in
        self.assertEqual(even_number_of_evens([]), False)
        # Returns true if even number of evens is sent
        self.assertEqual(even_number_of_evens([2, 4]), True)
        # Fails when one even number is sent
        self.assertEqual(even_number_of_evens([2]), False)
        # Fails when no even numbers are sent
        self.assertEqual(even_number_of_evens([1, 3, 5]), False)


if __name__ == "__main__":
    unittest.main()
