import itertools
import json

from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.views import View

from hypernews.settings import NEWS_JSON_PATH

# Перенесети работу с файлов вне класса


class ComingSoonView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Coming soon")


class MainPageView(View):
    def get(self, request, *args, **kwargs):

        with open(NEWS_JSON_PATH, 'r') as file:
            data = json.load(file)

        # Group by news by date:
        #
        # data_from_json = json.load(file)
        # sorted_news = sorted(data_from_json, key=lambda i: i['created'], reverse=True)
        # groupped_news = itertools.groupby(sorted_news, lambda i: i['created'][:10])
        # obj = []
        # for k, v in groupped_news:

        context = []

        for el in data:
            context.append({'title': el['title'], 'created': el['created'], 'text': el['text'], 'link': el['link']})

        return render(request, 'news/index.html', {'context': context})

        # return HttpResponse(status=404)


class WorkWithJSON(View):
    def get(self, request, link, *args, **kwargs):

        with open(NEWS_JSON_PATH, 'r') as file:
            data = json.load(file)

        for el in data:
            if el['link'] == int(link):
                context = {'title': el['title'], 'created': el['created'], 'text': el['text']}

                return render(request, 'news/news.html', context=context)

        return HttpResponse(status=404)
