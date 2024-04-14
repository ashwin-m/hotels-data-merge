from . import Supplier


class PaperfliesSupplier(Supplier):

    URL = "https://5f2be0b4ffc88500167b85a0.mockapi.io/suppliers/paperflies"

    def __init__(self):
        super().__init__(self.URL)

    def get_hotels(self):
        pass
