import json

from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.views import View

from hypernews.settings import NEWS_JSON_PATH

# Перенесети работу с файлов вне класса

class ComingSoonView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Coming soon")


class WorkWithJSON(View):
    def get(self, request, link, *args, **kwargs):

        with open(NEWS_JSON_PATH, 'r') as file:
            data = json.load(file)

        for el in data:
            if el['link'] == int(link):
                context = {'title': el['title'], 'created': el['created'], 'text': el['text']}

                return render(request, 'news/index.html', context=context)

        return HttpResponse(status=404)
