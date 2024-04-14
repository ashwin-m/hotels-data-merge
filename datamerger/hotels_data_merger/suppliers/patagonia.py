from . import Supplier


class PatagoniaSupplier(Supplier):

    URL = "https://5f2be0b4ffc88500167b85a0.mockapi.io/suppliers/patagonia"

    def __init__(self):
        super().__init__(self.URL)

    def get_hotels(self):
        pass
