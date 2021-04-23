from django.urls import path
from . import views

app_name = "match"

urlpatterns = [
    path('', views.MatchList.as_view()),
    path('<int:pk>', views.MatchRetrieve.as_view()),
]