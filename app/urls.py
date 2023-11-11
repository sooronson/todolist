from django.urls import path

from .views import *

urlpatterns = [
    path('', TaskListCreateAPIView.as_view()),
    path("<int:pk>/", TaskDetail.as_view())
]