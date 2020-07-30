from dahuffman import load_shakespeare


class Controller(object):
    def __init__(self):
        self._codec = load_shakespeare()

    def square_numbers(self, numbers):
        return self._square_odd(numbers)

    def _square_odd(self, numbers):
        return [i ** 2 for i in numbers if i % 2 != 0]

    def compress_strings(self, strings):
        compress_dict = {}

        for string in strings:
            compress_dict.setdefault(string, self._codec.encode(string).decode('cp1250'))
        return compress_dict

    def decode_string(self, string):
        return self._codec.decode(string.encode('cp1250'))
