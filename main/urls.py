from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('character/<int:pk>', views.character_detail, name='detail'),
]