from django.urls import path

from . import views

urlpatterns = [
    path('pull-request/', views.pull_request)
]

