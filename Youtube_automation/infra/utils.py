import random
import string


class Utils:

    @staticmethod
    def generate_random_string():
        return random.choice(string.digits)

