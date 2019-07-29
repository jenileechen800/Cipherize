from Cipherize import Cipherize

class Use_Cipherize:
    def __init__(self):
        self.introduction()
        self.cipherize_log = None

    def introduction(self):
        self.line_break()
        print("Welcome to <<<CIPHERIZE>>> spymaster!\nHere you can create cool codes"
              " out of simple\nwords or sentences using famous ciphers.")
        self.line_break()
        self.cipherize_loop()

    def cipherize_loop(self):
        # self.show_cipherize_log()

        cipher_again = input("Would you like to cipher? (\"y\"/\"n\")\n")

        while str(cipher_again) == "y":
            cipher = Cipherize()
            cipher.cipherize()
            # cipher.add_cipher_to_log(self.cipherize_log)

    def line_break(self):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

user_cipherize = Use_Cipherize()
