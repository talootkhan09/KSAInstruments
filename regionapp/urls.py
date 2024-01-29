from django.urls import path
from .views import RegionList, RegionDetail, generate_mcqs

urlpatterns = [
    path('regions/', RegionList.as_view(), name='region-list'),
    path('regions/<int:pk>/', RegionDetail.as_view(), name='region-detail'),
    path('regions/generate-mcqs/<str:topic>/', generate_mcqs, name='generate_mcqs'),    
]