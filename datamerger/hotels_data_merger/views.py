import json

from django.http import HttpResponse, JsonResponse
from http import HTTPStatus
from .managers import HotelsSearchManager


MAX_ALLOWED_SEARCH_IDS = 500


def index(request):
    return HttpResponse("Hello, world. You're at the hotels data merger index.")


def search(request):
    request_body = json.loads(request.body)

    # validation of requests
    is_valid, error = validate_search_request(request_body)
    if not is_valid:
        return JsonResponse({"resp": [], "error": error}, status=HTTPStatus.BAD_REQUEST)

    hotel_ids = request_body.get('hotel_ids')
    destination_id = request_body.get('destination_id')

    # todo add from and size

    search_manager = HotelsSearchManager()

    if hotel_ids:
        hotels = search_manager.get_by_ids(hotel_ids)
    else:
        hotels = search_manager.get_hotels_by_destination_id(destination_id)

    return JsonResponse({"resp": hotels, "error": ""})


def validate_search_request(request_body):
    hotel_ids = request_body.get('hotel_ids')
    destination_id = request_body.get('destination_id')

    if not hotel_ids and not destination_id:
        return False, "missing required parameters"

    if hotel_ids and len(hotel_ids) > MAX_ALLOWED_SEARCH_IDS:
        return False, f"only {MAX_ALLOWED_SEARCH_IDS} hotel ids allowed to be searched at a time"

    return True, ""
