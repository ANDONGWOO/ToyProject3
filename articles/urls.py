from django.urls import path
from .views import PyscriptHandlerView#파이스크립트
from . import views
urlpatterns = [
    path("", PyscriptHandlerView.as_view()),#파이스크립트
    path("test/", views.test1, name="test1"),
]