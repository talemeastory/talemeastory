from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'stories', views.StoryViewSet)
router.register(r'excerpts', views.ExcerptViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', views.index),
]

urlpatterns += router.urls
