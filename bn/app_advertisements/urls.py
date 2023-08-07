from django.urls import path
from .views import index, top_sellers

urlpatterns = [
    path('', index,name = 'main'),
    path('top-sellers.html/', top_sellers, name='top-sellers')


]