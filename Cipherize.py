from Cipher_Types import *


class Cipherize:
    def __init__(self):
        self.cipher = None
        self.cipher_name = None
        self.cipher_char_list = None
        self.cipher_algorithm = None
        self.cipher_input = None
        self.cipherize_log = None
        self.cipher_output = None

    def cipherize(self):
        self.choose_cipher()
        self.cipher_input1()
        self.cipher_output = self.cipher.use_cipher(self.cipher_char_list)
        print("Utilizing " + self.cipher_name + " with input \"" +
              self.cipher_input + "\" outputs \"" + self.cipher_output + "\"")
        self.add_cipher_to_log()
        self.show_cipherize_log()

    def add_cipher_to_log(self):
        self.cipherize_log[self.cipher_name] = (self.cipher_input, self.cipher_output)

    def choose_cipher(self):
        self.line_break()
        chosen_cipher = input("To begin, pick a cipher to use:"
                              "\n-Atbash"
                              "\n-ROT13"
                              "\n-Caesar"
                              "\n-Affine"
                              "\n-Rail-fence"
                              "\n")

        if chosen_cipher == "Atbash":
            self.cipher = Atbash()
        elif chosen_cipher == "ROT13":
            self.cipher = ROT13()
        elif chosen_cipher == "Caesar":
            self.cipher = Caesar()
        # elif chosen_cipher == "Affine":
        #     self.cipher = Affine()
        # elif chosen_cipher == "Rail-fence":
        #     self.cipher = Rail-fence()

        self.cipher_algorithm = self.cipher.cipher_algorithm
        self.cipher_name = self.cipher.cipher_name

        self.line_break()
        print("You are utilizing " + self.cipher_name + " cipher.")
        self.line_break()

    def cipher_input1(self):
        self.cipher_input = input("Please type your <<<<CIPHERIZING>>>> input:\n").lower()
        self.cipher_char_list = list(self.cipher_input)
        self.line_break()

    def line_break(self):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    def show_cipherize_log(self):
        self.line_break()
        view_cipherize_log = str(input("Would you like to view all your cipherize log? (\"y\"/\"n\")\n"))
        if view_cipherize_log == "y":
            print("Here is a log of all inputs/outputs used in this cipherize session.")
            for k, v in self.cipherize_log.items():
                print("Cipher:" + k + " | Input: " + v)


cipherize = Cipherize()

















