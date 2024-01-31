import unittest
import os
import io
from hw_21_task_1 import CustomOpen

class TestCustomOpen(unittest.TestCase):

    def test_writing_to_file(self):
        filename = 'test_file.txt'
        content = "Test content to write"

        with CustomOpen(filename, 'w') as file:
            file.write(content)

        self.assertTrue(os.path.exists(filename))
        with open(filename, 'r') as file:
            written_content = file.read()
        self.assertEqual(written_content, content)

        os.remove(filename)
    
    def test_incrementing_counter(self):
        filename = 'test_file.txt'
        initial_counter_value = CustomOpen('test_file.txt', 'r').get_counter()

        with CustomOpen(filename, 'w') as file:
            file.write("Test content to write")

        final_counter_value = CustomOpen('test_file.txt', 'r').get_counter()
        self.assertEqual(final_counter_value, initial_counter_value + 1)

        os.remove(filename)

    def test_handle_file_not_found_error(self):
        non_existing_file = 'non_existing_file.txt'
        initial_counter_value = CustomOpen('test_file.txt', 'r').get_counter()

        with self.assertRaises(FileNotFoundError):
            with CustomOpen(non_existing_file, 'r'):
                pass

        final_counter_value = CustomOpen('test_file.txt', 'r').get_counter()
        self.assertEqual(final_counter_value, initial_counter_value)

    def test_handle_runtime_error(self):
        filename = 'Lesson_21/counter.txt'
        initial_counter_value = CustomOpen(filename, 'r').get_counter()

        print("Initial Counter Value:", initial_counter_value)

        with self.assertRaises(io.UnsupportedOperation):
            with CustomOpen(filename, 'r') as file:
                file.write("This should raise a runtime error")

        final_counter_value = CustomOpen(filename, 'r').get_counter()
        print("Final Counter Value:", final_counter_value)

        self.assertEqual(final_counter_value, initial_counter_value + 1)


if __name__ == '__main__':
    unittest.main()