from rest_framework import generics
from .models import Client, Schedule
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ClientSerializer, ClientRUDSerializer, ScheduleSerializer


class ClientListAPIView(generics.ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ClientCreateAPIView(generics.CreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ClientRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientRUDSerializer
    lookup_field = 'telegram_id'


class ScheduleCreateAPIView(generics.ListCreateAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer


class ScheduleUpdateView(APIView):
    def put(self, request, *args, **kwargs):
        month = request.data.get('month')
        day = request.data.get('day')
        time = request.data.get('time')
        user_id = request.data.get('user_id')
        try:
            schedule = Schedule.objects.get(month=month, day=day, time=time)
            schedule.user_id = user_id
            schedule.save()
            serializer = ScheduleSerializer(schedule)
            return Response(serializer.data)
        except Schedule.DoesNotExist:
            return Response({'status': 'error', 'message': 'Schedule does not exist'})
