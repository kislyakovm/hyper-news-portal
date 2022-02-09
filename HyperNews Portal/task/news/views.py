from django.http import HttpResponse
from django.views import View


def ComingSoonView(View):
    # def get(self, request, *args, **kwargs):
    return HttpResponse("Coming soon")
