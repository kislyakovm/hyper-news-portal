from django.urls import path
from news.views import WorkWithJSON


urlpatterns = [

    path('', WorkWithJSON.as_view()),
]
