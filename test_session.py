from Session import Session
import unittest


class SessionTest(unittest.TestCase):
    def setUp(self):
        self.session = Session()

    def test_password_not_empty(self):
        self.assertEqual(self.session.validate_password(""), False)

    def test_password_longer_than_eight(self):
        self.assertEqual(self.session.validate_password("mojehaslohaslo"), False)

    def test_password_shorter_than_eight(self):
        self.assertEqual(self.session.validate_password("moje"), False)

    def test_password_at_least_one_capital_letter(self):
        self.assertEqual(self.session.validate_password("mojeHaslo2020"), False)

    def test_password_at_least_one_capital_letter_false(self):
        self.assertEqual(self.session.validate_password("mojemalehaslo"), False)

    def test_password_at_least_one_capital_letter_and_one_digit_true(self):
        self.assertEqual(self.session.validate_password("haslo3Wielkie"), False)

    def test_password_at_least_one_capital_letter_digit_and_symbol(self):
        self.assertEqual(self.session.validate_password("MojeWielkie20!"), True)

    def test_password_at_least_one_capital_letter_digit_and_symbol_2(self):
        self.assertEqual(self.session.validate_password("Duze?has201hm"), True)

    def test_password_at_least_one_capital_letter_digit_and_symbol_3(self):
        self.assertEqual(self.session.validate_password("2134Haslomm*m"), True)

    def test_password_no_capital_letter(self):
        self.assertEqual(self.session.validate_password("2134aslomm*m"), False)

    def test_password_not_enough_letters(self):
        self.assertEqual(self.session.validate_password("2134abcdE?"), False)

    def test_password_only_capital_letters(self):
        self.assertEqual(self.session.validate_password("2134EBASDFGG?"), True)

    def test_password_contains_a_space(self):
        with self.assertRaisesWithMessage(ValueError):
            self.session.validate_password("Pogodaladna 2020$")

    def test_password_not_a_str(self):
        with self.assertRaisesWithMessage(ValueError):
            self.session.validate_password(15)

    def assertRaisesWithMessage(self, exception):
        return self.assertRaisesRegex(exception, r".+")

    def tearDown(self):
        self.hamming = None


if __name__ == '__main__':
    unittest.main()
