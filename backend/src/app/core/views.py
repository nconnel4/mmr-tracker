from django.http import JsonResponse


def ping(request):
    """Ping running api."""
    data = {"ping": "pong!"}
    return JsonResponse(data)
