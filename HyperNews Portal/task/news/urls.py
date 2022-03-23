from django.urls import path
from news.views import MainPageView, WorkWithJSON

urlpatterns = [
    path('', WorkWithJSON.as_view()),
    # path('/news', MainPageView.as_view()),
]
