from django.urls import path

from cars.views import (
    cars_list_view,
    car_detail_view,
    download_car_image
)

urlpatterns = [
    path('', cars_list_view, name='list'),
    path('<int:pk>/', car_detail_view, name='detail'),
    path('download/<int:pk>/', download_car_image, name='download'),
]
