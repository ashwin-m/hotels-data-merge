from . import Supplier, SupplierResponse, SupplierImages, Image


class PatagoniaResponse(SupplierResponse):
    def __init__(self, json_response):
        super().__init__()
        self.id = json_response["id"]
        self.destination_id = json_response["destination"]
        self.name = json_response["name"].trim()
        self.latitude = json_response["lat"]
        self.longitude = json_response["lng"]
        self.address = json_response["address"].trim()
        self.description = json_response["info"].trim()
        self.facilities = json_response["amenities"]

        images_resp = json_response["images"]

        room_images = []
        room_images_resp = images_resp["rooms"]
        for room in room_images_resp:
            image = Image(room["url"], room["description"])
            room_images.append(image)

        amenities_images = []
        amenities_images_resp = images_resp["amenities"]
        for amenities in amenities_images_resp:
            image = Image(amenities["url"], amenities["description"])
            amenities_images.append(image)

        self.images = SupplierImages(room_images, [], amenities_images)


class PatagoniaSupplier(Supplier):

    URL = "https://5f2be0b4ffc88500167b85a0.mockapi.io/suppliers/patagonia"

    def __init__(self):
        super().__init__(self.URL, PatagoniaResponse.__class__)
