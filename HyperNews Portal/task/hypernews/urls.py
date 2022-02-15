from django.urls import include, path, re_path
from news.views import ComingSoonView


urlpatterns = [
    # path('news/', include('news.urls')),
    path('', ComingSoonView.as_view()),
    re_path('news/(?P<link>[^/]*)/?', include('news.urls')),
]