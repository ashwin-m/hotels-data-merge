from . import Supplier, SupplierResponse


class AcmeResponse(SupplierResponse):

    COUNTRY_CODE_MAP = {
        "SG": "Singapore",
        "JP": "Japan"
    }

    def parse(self, json_response):
        self.id = json_response["Id"]
        self.destination_id = json_response["DestinationId"]
        self.name = json_response["Name"].strip() if json_response["Name"] is not None else ""
        self.latitude = json_response["Latitude"]
        self.longitude = json_response["Longitude"]
        address = json_response["Address"].strip() if json_response["Address"] is not None else ""
        postal_code = json_response["PostalCode"].strip() if json_response["PostalCode"] is not None else ""
        self.address = f"{address}, {postal_code}"
        self.city = json_response["City"].strip() if json_response["City"] is not None else ""
        country = json_response["Country"].strip() if json_response["Country"] is not None else ""
        self.country = self.COUNTRY_CODE_MAP.get(country, "")
        self.description = json_response["Description"].strip() if json_response["Description"] is not None else ""
        facilities = json_response["Facilities"] if json_response["Facilities"] is not None else []
        for facility in facilities:
            self.facilities.add(facility.strip().capitalize())


class AcmeSupplier(Supplier):

    URL = "https://5f2be0b4ffc88500167b85a0.mockapi.io/suppliers/acme"

    def __init__(self):
        super().__init__(self.URL, AcmeResponse)
