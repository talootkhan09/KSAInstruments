from django.urls import path
from .views import RegionList, RegionDetail

urlpatterns = [
    path('regions/', RegionList.as_view(), name='region-list'),
    path('regions/<int:pk>/', RegionDetail.as_view(), name='region-detail'),
]