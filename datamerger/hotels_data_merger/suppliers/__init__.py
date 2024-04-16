import requests


class Image:
    def __init__(self, image_url, caption):
        self.image_url = image_url
        self.caption = caption

    def to_string(self):
        return dict(
            url=self.image_url,
            caption=self.caption,
        )


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

    def to_string(self):
        return dict(
            rooms=self.get_room_images_string(),
            sites=self.get_site_images_string(),
            amenities=self.get_amenities_images_string(),
        )

    def get_room_images_string(self):
        room_images = []
        if self.rooms is not None:
            for room in self.rooms:
                room_images.append(room.to_string())
        return room_images

    def get_site_images_string(self):
        site_images = []
        if self.sites is not None:
            for site in self.sites:
                site_images.append(site.to_string())
        return site_images

    def get_amenities_images_string(self):
        amenities_images = []
        if self.amenities is not None:
            for amenities in self.amenities:
                amenities_images.append(amenities.to_string())
        return amenities_images


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

    def parse(self, json_response):
        raise NotImplementedError

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
        self.description = f"{self.description} {description}"

    def merge_facilities(self, facilities):
        for facility in facilities:
            facility_without_space = facility.replace(" ", "")
            if facility_without_space.capitalize() in self.facilities:
                self.facilities.remove(facility_without_space.capitalize())
            if facility.strip().capitalize() not in self.facilities:
                self.facilities.add(facility.strip().capitalize())

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

    def to_string(self):
        string_value = dict(
            id=self.id,
            destination_id=self.destination_id,
            name=self.name,
            latitude=self.latitude,
            longitude=self.longitude,
            address=self.address,
            city=self.city,
            country=self.country,
            description=self.description,
        )
        if self.facilities is not None:
            string_value["facilities"] = list(self.facilities)
        if self.booking_conditions is not None:
            string_value["booking_conditions"] = list(self.booking_conditions)
        if self.images is not None:
            string_value["images"] = self.images.to_string()

        return string_value


class Supplier:

    def __init__(self, url, clazz, timeout=1):
        self.url = url
        self.clazz = clazz
        self.timeout = timeout

    def get_hotels(self):
        data = []
        resp = requests.get(self.url, timeout=self.timeout)
        resp_json = resp.json()
        for hotels_data in resp_json:
            parsed_resp_class = self.clazz()
            parsed_resp_class.parse(hotels_data)
            data.append(parsed_resp_class)
        return data
