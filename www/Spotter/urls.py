from django.urls import path

from Spotter.views import Index

urlpatterns = [
    path('', Index.as_view(), name='index'),
]