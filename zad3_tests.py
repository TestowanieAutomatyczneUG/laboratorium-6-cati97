import unittest
from zad3 import statement


class zad3Test(unittest.TestCase):

    def setUp(self):
        self.invoice = {
            "customer": "BigCo",
            "performances": [
                {
                    "playID": "hamlet",
                    "audience": 55
                },
                {
                    "playID": "as-like",
                    "audience": 35
                },
                {
                    "playID": "othello",
                    "audience": 40
                }
            ]
        }

    def test_exception_not_tragedy_nor_comedy(self):
        plays = {
            "hamlet": {"name": "Hamlet", "type": "document"},
            "as-like": {"name": "As You Like It", "type": "document"},
            "othello": {"name": "Othello", "type": "document"}
        }
        with self.assertRaisesWithMessage(ValueError):
            statement(self.invoice, plays)

    def test_first_line_of_result(self):
        plays = {
            "hamlet": {"name": "Hamlet", "type": "tragedy"},
            "as-like": {"name": "As You Like It", "type": "comedy"},
            "othello": {"name": "Othello", "type": "tragedy"}
        }
        result = statement(self.invoice, plays)
        first_line = result.split("\n")[0]
        self.assertEqual(first_line, "Statement for BigCo")


    def test_amount_owed(self):
        plays = {
            "hamlet": {"name": "Hamlet", "type": "tragedy"},
            "as-like": {"name": "As You Like It", "type": "tragedy"},
            "othello": {"name": "Othello", "type": "tragedy"}
        }
        result = statement(self.invoice, plays)
        fourth_line = result.split("\n")[4]
        self.assertEqual(fourth_line, "Amount owed is $1,600.00")


    def test_second_line_result(self):
        plays = {
            "hamlet": {"name": "Hamlet", "type": "tragedy"},
            "as-like": {"name": "As You Like It", "type": "tragedy"},
            "othello": {"name": "Othello", "type": "tragedy"}
        }
        result = statement(self.invoice, plays)
        second_line = result.split("\n")[1]
        self.assertEqual(second_line, " Hamlet: $650.00 (55 seats)")

    def test_third_line_result(self):
        plays = {
            "hamlet": {"name": "Hamlet", "type": "tragedy"},
            "as-like": {"name": "As You Like It", "type": "tragedy"},
            "othello": {"name": "Othello", "type": "tragedy"}
        }
        result = statement(self.invoice, plays)
        third_line = result.split("\n")[2]
        self.assertEqual(third_line, " As You Like It: $450.00 (35 seats)")


    def assertRaisesWithMessage(self, exception):
        return self.assertRaisesRegex(exception, r".+")

    def tearDown(self):
        self.invoice = None


if __name__ == '__main__':
    unittest.main()
