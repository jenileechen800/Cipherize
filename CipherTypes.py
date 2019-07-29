import string


class Atbash:
    def __init__(self):
        self.cipher_name = "Atbash"
        self.cipher_algorithm = {"a": "z", "b": "y", "c": "x",
                                 "d": "w", "e": "v", "f": "u",
                                 "g": "t", "h": "s", "i": "r",
                                 "j": "q", "k": "p", "l": "o",
                                 "m": "n", "n": "m", "o": "l",
                                 "p": "k", "q": "j", "r": "i",
                                 "s": "h", "t": "g", "u": "f",
                                 "v": "e", "w": "d", "x": "c",
                                 "y": "b", "z": "a", " ": " "}

    def cipher_algorithm(self):
        return self.cipher_algorithm()

    def use_cipher(self, cipher_char_list):
        cipher_output = ""

        for char in cipher_char_list:
            cipher_output += str(self.cipher_algorithm.get(char))

        return cipher_output


class ROT13:
    def __init__(self):
        self.cipher_name = "ROT13"
        self.cipher_algorithm = {"a": "n", "b": "o", "c": "p",
                                 "d": "q", "e": "r", "f": "s",
                                 "g": "t", "h": "u", "i": "v",
                                 "j": "w", "k": "x", "l": "y",
                                 "m": "z", "n": "a", "o": "b",
                                 "p": "c", "q": "d", "r": "e",
                                 "s": "f", "t": "g", "u": "h",
                                 "v": "i", "w": "j", "x": "k",
                                 "y": "l", "z": "m", " ": " "}

    def cipher_algorithm(self):
        return self.cipher_algorithm()

    def use_cipher(self, cipher_char_list):
        cipher_output = ""

        for char in cipher_char_list:
            cipher_output += str(self.cipher_algorithm.get(char))

        return cipher_output

class Caesar:
    def __init__(self):
        self.cipher_name = "Caesar"
        self.cipher_algorithm = self.cipher_algorithm()

    def cipher_algorithm(self):

        alphabet = [a for a in string.ascii_lowercase]
        counter = 0
        dict = {}

        for letter in alphabet:
            dict[letter] = counter
            counter += 1

        return dict

    def use_cipher(self, cipher_char_list):
        self.input_to_numbers(cipher_char_list)
        self.apply_cipher_formula()
        self.numbers_to_output()
        print(self.numbers_to_output())

    def input_to_numbers(self, cipher_char_list):
        global number_input
        number_input = []

        for char in cipher_char_list:
            number_input.append(self.cipher_algorithm.get(char))

        print(number_input)

    def apply_cipher_formula(self):
        user_shift = int(input("How much shift would you like the cipher to utilize? (Integer)\n"))

        for number in number_input:
            if number is None:
                pass
            number = (number + user_shift) % 26

    def numbers_to_output(self):
        cipher_output = ""

        for num_input in number_input:
            for num_algorithm in self.cipher_algorithm:
                if num_input == num_algorithm:
                    cipher_output += self.cipher_algorithm()
        print(cipher_output)
        return cipher_output









