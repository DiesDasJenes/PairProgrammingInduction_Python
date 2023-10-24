from unittest import TestCase

import roman_letter_converter


class Test(TestCase):

    def test_that_roman_letter_converter_can_convert_one(self):
        result = roman_letter_converter.convert_roman_letter(1)
        assert result == "I"
