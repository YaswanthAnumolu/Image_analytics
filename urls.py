from django.urls import path
from .views import home_view, image_recognition_view

urlpatterns = [
    path('', home_view, name='analytics.home'),  # Home page route
    path('image-recognition/', image_recognition_view, name='image_recognition'),  # Image recognition page
]
