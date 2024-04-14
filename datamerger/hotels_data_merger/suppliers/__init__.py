class Supplier:

    def __init__(self, url):
        self.url = url

    def get_hotels(self):
        raise NotImplementedError
