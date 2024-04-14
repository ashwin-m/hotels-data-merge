import requests


class Image:
    def __init__(self, image_url, caption):
        self.image_url = image_url
        self.caption = caption


class SupplierImages:

    def __init__(self, room_images, site_images, amenities_images):
        self.rooms = room_images
        self.sites = site_images
        self.amenities = amenities_images


class SupplierResponse:

    def __init__(self):
        self.id = ""
        self.destination_id = 0
        self.name = ""
        self.latitude = 0
        self.longitude = 0
        self.address = ""
        self.city = ""
        self.country = ""
        self.description = ""
        self.facilities = []
        self.images = None


class Supplier:

    def __init__(self, url, clazz):
        self.url = url
        self.clazz = clazz

    def get_hotels(self):
        resp = requests.get(self.url)
        resp_json = resp.json()
        return self.clazz(resp_json).to_supplier_response()
