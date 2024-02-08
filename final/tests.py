import unittest
from without_GUI import sort_sequence, validate_input, is_valid_input

class TestSortingFunctions(unittest.TestCase):

    def test_is_valid_input_positive(self):
        input_str = "1, 2, 3, 4, 5"
        self.assertTrue(is_valid_input(input_str))
        with open("test_results.txt", "a") as file:
            file.write("Positive Test for is_valid_input:\n")
            file.write(f"Input: {input_str}\n")
            file.write("Result: Valid\n\n")

    def test_is_valid_input_negative(self):
        input_str = "1, 2, 3, a, 5"
        self.assertFalse(is_valid_input(input_str))
        with open("test_results.txt", "a") as file:
            file.write("Negative Test for is_valid_input:\n")
            file.write(f"Input: {input_str}\n")
            file.write("Result: Invalid\n\n")

    def test_validate_input_positive(self):
        new_value = "1, 2, 3, 4, 5"
        self.assertTrue(validate_input(new_value))
        with open("test_results.txt", "a") as file:
            file.write("Positive Test for validate_input:\n")
            file.write(f"Input: {new_value}\n")
            file.write("Result: Valid\n\n")

    def test_validate_input_negative(self):
        new_value = "1, 2, 3, a, 5"
        self.assertFalse(validate_input(new_value))
        with open("test_results.txt", "a") as file:
            file.write("Negative Test for validate_input:\n")
            file.write(f"Input: {new_value}\n")
            file.write("Result: Invalid\n\n")

    def test_sort_sequence(self):
        sequence = "1, 3, 2, 5, 4"
        sorting_order = "ascending"
        result, time_taken = sort_sequence(sequence, sorting_order)
        with open("test_results.txt", "a") as file:
            file.write("Sort Sequence Test:\n")
            file.write(f"Input Sequence: {sequence}\n")
            file.write(f"Sorting Order: {sorting_order}\n")
            file.write("Sorted Result: " + result + "\n")
            file.write("Time Taken: " + str(time_taken) + " seconds\n")

if __name__ == '__main__':
    with open("test_results.txt", "w") as file:
        file.write("Test Results:\n")

    unittest.main()
