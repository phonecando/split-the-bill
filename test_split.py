import unittest

from split import main, split


class SplitTest(unittest.TestCase):
    def test_no_tip(self):
        self.assertEqual(split(90, 3), 30.00)

    def test_rounds_to_cents(self):
        self.assertEqual(split(100, 3), 33.33)

    def test_tip_is_a_percent(self):
        self.assertEqual(split(80, 4, 20), 24.00)

    def test_tip_for_one(self):
        self.assertEqual(split(50, 1, 10), 55.00)

    def test_nobody_pays(self):
        with self.assertRaises(ValueError):
            split(50, 0)

    def test_command_line(self):
        self.assertEqual(main(["80", "4", "20"]), "Each pays $24.00")


if __name__ == "__main__":
    unittest.main()
