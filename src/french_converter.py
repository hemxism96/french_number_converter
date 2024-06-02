import sys


class NumberToFrenchConverter:

    def __init__(self):
        self.units = ["zéro", "un", "deux", "trois", "quatre", "cinq", "six", "sept", "huit", "neuf", "dix", "onze", "douze", "treize", "quatorze", "quinze", "seize"]
        self.tens = ["", "dix", "vingt", "trente", "quarante", "cinquante", "soixante", "soixante-dix", "quatre-vingt", "quatre-vingt-dix"]
        self.special_numbers = {
            70: "soixante-dix",
            71: "soixante-et-onze",
            80: "quatre-vingts",
            81: "quatre-vingt-un",
            90: "quatre-vingt-dix",
            91: "quatre-vingt-onze"
        }
    
    def validate_input(self, input):
        if not all(isinstance(number, int) and number >= 0 for number in input):
            raise ValueError("Please check input numbers are all non-negative integer.")

    def convert_unit(self, number):
        return self.units[number]

    def convert_tens(self, number):
        if number in self.special_numbers.keys():
            return self.special_numbers.get(number)
        else:
            ten, remainder = divmod(number, 10)
            if remainder == 1:
                return f"{self.tens[ten]}-et-un"
            elif ten < 7 or ten == 8:
                return f"{self.tens[ten]}{'-' + self.units[remainder] if remainder!=0 else ''}"
            else:
                return f"{self.tens[ten-1]}{'-' + self.convert_number(number-10*(ten-1))}"

    def convert_hundreds(self, number):
        hundred, remainder = divmod(number, 100)
        if hundred == 1:
            return f"cent{'-' + self.convert_number(remainder) if remainder!=0 else ''}"
        else:
            return f"{self.units[hundred]}-cent{'-' + self.convert_number(remainder) if remainder!=0 else 's'}"

    def check_plural(self, number):
        if number[-1] == "s" and not number.endswith('trois'):
            return number[:-1]
        else:
            return number

    def convert_thousands(self, number):
        thousand, remainder = divmod(number, 1000)
        if thousand == 1:
            return f"mille{'-' + self.convert_number(remainder) if remainder!=0 else ''}"
        else:
            new_thousand = self.check_plural(self.convert_number(thousand))
            return f"{new_thousand}-mille{'-' + self.convert_number(remainder) if remainder!=0 else 's'}"


    def convert_number(self, number):
        if number < 17:
            res = self.convert_unit(number)
        elif number < 100:
            res = self.convert_tens(number)
        elif number < 1000:
            res = self.convert_hundreds(number)
        else:
            res = self.convert_thousands(number)
        return res

    def __call__(self, input: list):
        self.validate_input(input)
        return list(map(self.convert_number, input))


if __name__ == "__main__" :
    input_list = list(map(int, sys.argv[1:]))
    fc = NumberToFrenchConverter()
    print(fc(input_list))
