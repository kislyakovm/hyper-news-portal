from django.urls import include, path, re_path
from news.views import MainPageView, ComingSoonView

urlpatterns = [
    # path('news/', include('news.urls')),
    path('news/', MainPageView.as_view()),
    re_path('news/(?P<link>[^/]*)/?', include('news.urls')),
    path('', ComingSoonView.as_view()),
    # path('news/', WorkWithJSON.as_view()),
]