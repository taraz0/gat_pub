from django.urls import path
from .views import index, page_a, features_page

urlpatterns = [
    path('', index, name='index'),
    path('a/', page_a, name='page_a'),
    path('features/', features_page, name='features_page'),
]
