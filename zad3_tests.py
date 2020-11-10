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

    def assertRaisesWithMessage(self, exception):
        return self.assertRaisesRegex(exception, r".+")

    def tearDown(self):
        self.invoice = None


if __name__ == '__main__':
    unittest.main()
