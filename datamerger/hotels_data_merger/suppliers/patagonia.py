from . import Supplier, SupplierResponse, SupplierImages, Image


class PatagoniaResponse(SupplierResponse):

    def parse(self, json_response):
        self.id = json_response["id"]
        self.destination_id = json_response["destination"]
        self.name = json_response["name"].strip() if json_response["name"] is not None else ""
        self.latitude = json_response["lat"]
        self.longitude = json_response["lng"]
        self.address = json_response["address"].strip() if json_response["address"] is not None else ""
        self.description = json_response["info"].strip() if json_response["info"] is not None else ""
        facilities = json_response["amenities"] if json_response["amenities"] is not None else []
        for facility in facilities:
            self.facilities.add(facility.strip().capitalize())

        images_resp = json_response["images"]
        if images_resp is not None:
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
        super().__init__(self.URL, PatagoniaResponse, 1)
