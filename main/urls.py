from django.urls import path
from .views import ClientListAPIView, ClientCreateAPIView, \
    ClientRUDAPIView, ScheduleCreateAPIView, ScheduleUpdateView


urlpatterns = [
    path('list/', ClientListAPIView.as_view()),
    path('create/', ClientCreateAPIView.as_view()),
    path('client/detail/<int:telegram_id>/', ClientRUDAPIView.as_view()),
    path('schedule/create/', ScheduleCreateAPIView.as_view()),
    path('schedule/update/', ScheduleUpdateView.as_view()),
]