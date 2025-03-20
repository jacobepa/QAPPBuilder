from django.shortcuts import render


class UnauthorizedMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if response.status_code == 401:
            return render(request, '401.html', status=401)
        return response
