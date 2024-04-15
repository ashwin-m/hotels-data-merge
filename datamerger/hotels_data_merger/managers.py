from .suppliers.acme import AcmeSupplier
from .suppliers.patagonia import PatagoniaSupplier
from .suppliers.paperflies import PaperfliesSupplier


class HotelsSearchManager:

    def __init__(self):
        self.suppliers = [AcmeSupplier(), PatagoniaSupplier(), PaperfliesSupplier()]

    def get_data_from_suppliers(self):
        data = []
        for supplier in self.suppliers:
            hotels_data = supplier.get_hotels()
            data.extend(hotels_data)
        return data

    def get_by_ids(self, hotel_ids):
        hotels_by_id = dict()
        data = self.get_data_from_suppliers()
        for datum in data:
            hotel_id = datum.id
            if hotel_id in hotel_ids:
                if hotels_by_id.get(hotel_id, None):
                    hotels_by_id[hotel_id].merge(datum)
                else:
                    hotels_by_id[hotel_id] = datum

        return [hotel.to_string() for hotel in hotels_by_id.values()]

    def get_hotels_by_destination_id(self, destination_id):
        hotels_by_id = dict()
        data = self.get_data_from_suppliers()
        for datum in data:
            hotel_id = datum.id
            hotel_destination_id = datum.destination_id
            if hotel_destination_id == destination_id:
                if hotels_by_id.get(hotel_id):
                    hotels_by_id[hotel_id].merge(datum)
                else:
                    hotels_by_id[hotel_id] = datum

        return [hotel.to_string() for hotel in hotels_by_id.values()]
