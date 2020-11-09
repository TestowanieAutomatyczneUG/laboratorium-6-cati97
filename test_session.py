from Session import Session
import unittest


class SessionTest(unittest.TestCase):
    def setUp(self):
        self.session = Session()
        try:
            self.assertRaisesRegex
        except AttributeError:
            self.assertRaisesRegex = self.assertRaisesRegexp

    def test_password_not_empty(self):
        self.assertEqual(self.session.validate_password(""), False)

    def test_password_longer_than_eight(self):
        self.assertEqual(self.session.validate_password("mojehaslo2020"), True)

    def test_password_shorter_than_eight(self):
        self.assertEqual(self.session.validate_password("moje"), False)

    def assertRaisesWithMessage(self, exception):
        return self.assertRaisesRegex(exception, r".+")

    def tearDown(self):
        self.hamming = None


if __name__ == '__main__':
    unittest.main()
