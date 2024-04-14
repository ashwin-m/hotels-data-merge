from . import Supplier, SupplierResponse


class AcmeResponse(SupplierResponse):

    COUNTRY_CODE_MAP = {
        "SG": "Singapore",
        "JP": "Japan"
    }

    def __init__(self, json_response):
        super().__init__()
        self.id = json_response["Id"]
        self.destination_id = json_response["DestinationId"]
        self.name = json_response["Name"].trim()
        self.latitude = json_response["Latitude"]
        self.longitude = json_response["Longitude"]
        address = json_response["Address"].trim()
        postal_code = json_response["PostalCode"].trim()
        self.address = f"{address}, {postal_code}"
        self.city = json_response["City"].trim()
        country = json_response["Country"].trim()
        self.country = self.COUNTRY_CODE_MAP.get(country, "")
        self.description = json_response["Description"].trim()
        self.facilities = json_response["Facilities"]


class AcmeSupplier(Supplier):

    URL = "https://5f2be0b4ffc88500167b85a0.mockapi.io/suppliers/acme"

    def __init__(self):
        super().__init__(self.URL, AcmeResponse.__class__)
