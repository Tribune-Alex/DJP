from django.conf import settings
from django.http import HttpResponse


class MaintenanceModeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        
        if not getattr(settings, "MAINTENANCE_MODE", False):
            return self.get_response(request)

        
        if request.path.startswith("/admin/"):
            return self.get_response(request)

        
        return HttpResponse(
            "Site is under maintenance",
            status=503
        )
