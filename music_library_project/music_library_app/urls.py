from django.urls import path
from . import views



urlpatterns = [
    path('music_library_app/', views.SongList.as_view()),
    path('details/<int:pk>/', views.DetailClass.as_view())
]