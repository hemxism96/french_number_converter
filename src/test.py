import unittest

from french_converter import NumberToFrenchConverter


class TestNumberToFrenchConverter(unittest.TestCase):

    def setUp(self):
        self.converter = NumberToFrenchConverter()

    def test_convert_unit(self):
        self.assertEqual(self.converter.convert_unit(0), "zéro")
        self.assertEqual(self.converter.convert_unit(5), "cinq")
        self.assertEqual(self.converter.convert_unit(9), "neuf")

    def test_convert_tens(self):
        self.assertEqual(self.converter.convert_tens(10), "dix")
        self.assertEqual(self.converter.convert_tens(21), "vingt-et-un")
        self.assertEqual(self.converter.convert_tens(34), "trente-quatre")
        self.assertEqual(self.converter.convert_tens(70), "soixante-dix")
        self.assertEqual(self.converter.convert_tens(81), "quatre-vingt-un")

    def test_convert_hundreds(self):
        self.assertEqual(self.converter.convert_hundreds(100), "cent")
        self.assertEqual(self.converter.convert_hundreds(201), "deux-cent-un")
        self.assertEqual(self.converter.convert_hundreds(345), "trois-cent-quarante-cinq")
        self.assertEqual(self.converter.convert_hundreds(999), "neuf-cent-quatre-vingt-dix-neuf")

    def test_convert_thousands(self):
        self.assertEqual(self.converter.convert_thousands(1000), "mille")
        self.assertEqual(self.converter.convert_thousands(2001), "deux-mille-un")
        self.assertEqual(self.converter.convert_thousands(3456), "trois-mille-quatre-cent-cinquante-six")
        self.assertEqual(self.converter.convert_thousands(9999), "neuf-mille-neuf-cent-quatre-vingt-dix-neuf")

    def test_convert_number(self):
        self.assertEqual(self.converter.convert_number(7), "sept")
        self.assertEqual(self.converter.convert_number(25), "vingt-cinq")
        self.assertEqual(self.converter.convert_number(456), "quatre-cent-cinquante-six")
        self.assertEqual(self.converter.convert_number(7890), "sept-mille-huit-cent-quatre-vingt-dix")

    def test_call(self):
        self.assertEqual(self.converter([0, 10, 100, 1000]), ["zéro", "dix", "cent", "mille"])
        self.assertEqual(self.converter([345, 567, 7890, 1234]), ["trois-cent-quarante-cinq", "cinq-cent-soixante-sept", "sept-mille-huit-cent-quatre-vingt-dix", "mille-deux-cent-trente-quatre"])


if __name__ == '__main__':
    unittest.main()