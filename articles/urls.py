from django.urls import path
from .views import PyscriptHandlerView#파이스크립트
from . import views

app_name='articles'

urlpatterns = [
    path("", PyscriptHandlerView.as_view(), name="index" ),#파이스크립트/클래스 형 뷰
    path("test/", views.test1, name="test1"),
    path('create/', views.create, name='create'),
    path('<int:article_pk>/', views.detail, name='detail'),
    path('<int:article_pk>/comments/', views.comment_create, name='comment_create'),
    path('<int:article_pk>/comments/<int:comment_pk>/delete/', views.comments_delete, name='comments_delete'),
]