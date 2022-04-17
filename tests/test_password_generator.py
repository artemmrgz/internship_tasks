import unittest
from string import ascii_lowercase, ascii_uppercase, digits, punctuation
from password_generator import generate_password
from password_checker import contains


class TestGenerator(unittest.TestCase):
    def test_psw_generator(self):
        password = generate_password(10)
        self.assertEqual(len(password), 10)
        self.assertTrue(contains(ascii_lowercase, password))
        self.assertTrue(contains(ascii_uppercase, password))
        self.assertTrue(contains(punctuation, password))
        self.assertTrue(contains(digits, password))


if __name__ == '__main__':
    unittest.main()