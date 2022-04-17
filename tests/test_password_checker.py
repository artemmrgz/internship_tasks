import unittest
from password_checker import checker, contains, has_digit, has_punctuation, has_upper_lower, has_proper_length


class TestChecker(unittest.TestCase):
    weak_psw = 'qwerty'

    def test_contains(self):
        self.assertTrue(contains('123', 'qwerty1'))
        self.assertFalse(contains('123', self.weak_psw))

    def test_has_upper_lower(self):
        self.assertTrue(has_upper_lower('Qwerty'))
        self.assertFalse(has_upper_lower(self.weak_psw))

    def test_has_digit(self):
        self.assertTrue(has_digit('qwerty1'))
        self.assertFalse(has_digit(self.weak_psw))

    def test_has_punctuation(self):
        self.assertTrue(has_punctuation('qwerty$'))
        self.assertFalse(has_punctuation(self.weak_psw))

    def test_has_proper_length(self):
        self.assertTrue(has_proper_length('qwerty1234qwerty'))
        self.assertFalse(has_proper_length(self.weak_psw))

    def test_checker(self):
        errors = checker('Jdk$12kdew_sDl')
        self.assertEqual(len(errors), 0)

        errors = checker(self.weak_psw)
        self.assertEqual(len(errors), 4)


if __name__ == '__main__':
    unittest.main()
