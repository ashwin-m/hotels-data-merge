from . import Supplier, SupplierResponse, SupplierImages, Image


class PaperfliesResponse(SupplierResponse):
    def __init__(self, json_response):
        super().__init__()
        self.id = json_response["hotel_id"]
        self.destination_id = json_response["destination_id"]
        self.name = json_response["hotel_name"].strip() if json_response["hotel_name"] is not None else ""
        if json_response["location"] is not None:
            location = json_response["location"]
            self.address = location["address"].strip() if json_response["location"]["address"] is not None else ""
            self.country = location["country"].strip() if json_response["location"]["country"] is not None else ""
        self.description = json_response["details"].strip() if json_response["details"] is not None else ""

        if json_response["amenities"] is not None:
            amenities = json_response["amenities"]["general"]
            amenities.extend(json_response["amenities"]["room"])
            self.facilities = set(amenities)

        room_images = []
        images_resp = json_response["images"]
        if images_resp is not None:
            room_images_resp = images_resp["rooms"]
            for room in room_images_resp:
                image = Image(room["link"].strip(), room["caption"].strip())
                room_images.append(image)

            site_images = []
            site_images_resp = images_resp["site"]
            for site in site_images_resp:
                image = Image(site["link"].strip(), site["caption"].strip())
                site_images.append(image)

            self.images = SupplierImages(room_images, site_images, [])
        booking_conditions = json_response["booking_conditions"]
        self.booking_conditions = set(booking_conditions) if booking_conditions is not None else set()


class PaperfliesSupplier(Supplier):

    URL = "https://5f2be0b4ffc88500167b85a0.mockapi.io/suppliers/paperflies"

    def __init__(self):
        super().__init__(self.URL, PaperfliesResponse.__class__)
