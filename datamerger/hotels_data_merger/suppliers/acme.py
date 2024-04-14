from . import Supplier


class AcmeSupplier(Supplier):

    URL = "https://5f2be0b4ffc88500167b85a0.mockapi.io/suppliers/acme"

    def __init__(self):
        super().__init__(self.URL)

    def get_hotels(self):
        pass
