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

    def merge(self, image):
        if len(image.rooms) > 0:
            self.rooms.extend(image.rooms)
        if len(image.sites) > 0:
            self.sites.extend(image.sites)
        if len(image.amenities) > 0:
            self.amenities.extend(image.amenities)


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
        self.facilities = set()
        self.images = None
        self.booking_conditions = set()

    def merge(self, data):
        if self.destination_id != data.destination_id:
            self.merge_destination_id(data.destination_id)
        if self.name.strip().lower() != data.name.strip().lower():
            self.merge_name(data.name)
        if self.latitude != data.latitude:
            self.merge_latitude(data.latitude)
        if self.longitude != data.longitude:
            self.merge_longitude(data.longitude)
        if self.address.strip().lower() != data.address.strip().lower():
            self.merge_address(data.address)
        if self.city.strip().lower() != data.city.strip().lower():
            self.merge_city(data.city)
        if self.country.strip().lower() != data.country.strip().lower():
            self.merge_country(data.country)
        if self.description.strip() != data.description.strip():
            self.merge_description(data.description)
        if self.facilities != data.facilities:
            self.merge_facilities(data.facilities)
        if self.images != data.images:
            self.merge_images(data.images)
        if self.booking_conditions != data.booking_conditions:
            self.merge_booking_conditions(data.booking_conditions)

    def merge_destination_id(self, destination_id):
        if self.destination_id == 0:
            self.destination_id = destination_id

    def merge_name(self, name):
        if self.name == "":
            self.name = name
            return
        if len(self.name) < len(name):
            self.name = name

    def merge_latitude(self, latitude):
        if self.latitude == 0:
            self.latitude = latitude
            return
        if len(str(self.latitude)) < len(str(latitude)):
            self.latitude = latitude

    def merge_longitude(self, longitude):
        if self.longitude == 0:
            self.longitude = longitude
            return
        if len(str(self.longitude)) < len(str(longitude)):
            self.longitude = longitude

    def merge_address(self, address):
        if self.address == "":
            self.address = address
            return
        if len(self.address) < len(address):
            self.address = address

    def merge_city(self, city):
        if self.city == "":
            self.city = city
            return
        if len(self.city) < len(city):
            self.city = city

    def merge_country(self, country):
        if self.country == "":
            self.country = country
            return
        if len(self.country) < len(country):
            self.country = country

    def merge_description(self, description):
        if self.description == "":
            self.description = description
            return
        self.country = f"{self.country} {description}"

    def merge_facilities(self, facilities):
        if not self.facilities:
            self.facilities = facilities
            return
        for facility in facilities:
            if facility not in self.facilities:
                self.facilities.add(facility)

    def merge_images(self, images):
        if not self.images:
            self.images = images
            return
        self.images.merge(images)

    def merge_booking_conditions(self, booking_conditions):
        if not self.booking_conditions:
            self.booking_conditions = booking_conditions
            return
        for booking_condition in booking_conditions:
            if booking_condition not in self.booking_conditions:
                self.booking_conditions.add(booking_conditions)


class Supplier:

    def __init__(self, url, clazz):
        self.url = url
        self.clazz = clazz

    def get_hotels(self):
        resp = requests.get(self.url)
        resp_json = resp.json()
        return self.clazz(resp_json)
