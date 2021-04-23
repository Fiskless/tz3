from django.urls import path
from . import views

app_name = "human"

urlpatterns = [
    path('', views.HumanList.as_view()),
    path('<int:pk>', views.HumanRetrieveUpdateDestroy.as_view()),
]