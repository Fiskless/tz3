from django.urls import path
from . import views

app_name = "human"

urlpatterns = [
    path('human/', views.HumanList.as_view()),
    path('human/<int:pk>', views.HumanRetrieveUpdateDestroy.as_view()),
]