from django.http import HttpResponse, JsonResponse
from http import HTTPStatus
from managers import HotelsSearchManager


MAX_ALLOWED_SEARCH_IDS = 500


def index(request):
    return HttpResponse("Hello, world. You're at the hotels data merger index.")


def search(request):
    # validation of requests
    is_valid, error = validate_search_request(request.POST)
    if not is_valid:
        return JsonResponse({"resp": [], "error": error}, status=HTTPStatus.BAD_REQUEST)

    hotel_ids = request.POST['hotel_ids']
    destination_id = request.POST['destination_id']

    # todo add from and size

    hotels = []
    search_manager = HotelsSearchManager()

    if hotel_ids:
        hotels = search_manager.get_by_ids(hotel_ids)
    else:
        hotels = search_manager.get_hotels_by_destination_id(destination_id)

    return JsonResponse({"resp": hotels, "error": ""})


def validate_search_request(request_post):
    hotel_ids = request_post['hotel_ids']
    destination_id = request_post['destination_id']

    if not hotel_ids or not destination_id:
        return False, "missing required parameters"

    if len(hotel_ids) > MAX_ALLOWED_SEARCH_IDS:
        return False, f"only {MAX_ALLOWED_SEARCH_IDS} hotel ids allowed to be searched at a time"

    return True, ""
