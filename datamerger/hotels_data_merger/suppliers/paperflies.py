from . import Supplier, SupplierResponse, SupplierImages, Image


class PaperfliesResponse(SupplierResponse):
    def __init__(self, json_response):
        super().__init__()
        self.id = json_response["hotel_id"]
        self.destination_id = json_response["destination_id"]
        self.name = json_response["hotel_name"].trim()
        self.address = json_response["location"]["address"].trim()
        self.country = json_response["location"]["country"].trim()
        self.description = json_response["details"].trim()
        amenities = json_response["amenities"]["general"]
        amenities.extend(json_response["amenities"]["room"])
        self.facilities = amenities

        room_images = []
        room_images_resp = json_response["images"]["rooms"]
        for room in room_images_resp:
            image = Image(room["link"].trim(), room["caption"].trim())
            room_images.append(image)

        site_images = []
        site_images_resp = json_response["images"]["site"]
        for site in site_images_resp:
            image = Image(site["link"].trim(), site["caption"].trim())
            site_images.append(image)

        self.images = SupplierImages(room_images, site_images, [])


class PaperfliesSupplier(Supplier):

    URL = "https://5f2be0b4ffc88500167b85a0.mockapi.io/suppliers/paperflies"

    def __init__(self):
        super().__init__(self.URL, PaperfliesResponse.__class__)
