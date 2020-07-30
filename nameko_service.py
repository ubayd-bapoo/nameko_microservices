from nameko.rpc import rpc

from controller import Controller

class NamekoService:
    name = "nameko_service"

    def __init__(self):
        self._cntrl = Controller()

    @rpc
    def square_list(self, numbers):
        return self._cntrl.square_numbers(numbers)

    @rpc
    def compress_string(self, strings):
        return self._cntrl.compress_strings(strings)

    @rpc
    def decode_string(self, string):
        return self._cntrl.decode_string(string)
