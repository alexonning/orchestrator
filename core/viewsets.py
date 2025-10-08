from rest_framework import viewsets, permissions, filters as rest_framework_filters
from drf_yasg.utils import swagger_auto_schema
from .models import Automation, Robot, RobotHasAutomation, System, AutomationHasSystem, ScheduleRestriction, Schedule, Agenda, Task
from .serializers import (
    AutomationSerializer, RobotSerializer, RobotHasAutomationSerializer,
    SystemSerializer, AutomationHasSystemSerializer, ScheduleRestrictionSerializer,
    ScheduleSerializer, AgendaSerializer, TaskSerializer
)
from .filters import DynamicFilterBackend, JQLFilterBackend

class BaseModelViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [
        DynamicFilterBackend,
        JQLFilterBackend,
        rest_framework_filters.SearchFilter,
        rest_framework_filters.OrderingFilter,
    ]

class AutomationViewSet(BaseModelViewSet):
    queryset = Automation.objects.all()
    serializer_class = AutomationSerializer
    search_fields = ['name']
    ordering_fields = '__all__'

class RobotViewSet(BaseModelViewSet):
    queryset = Robot.objects.all()
    serializer_class = RobotSerializer
    search_fields = ['name', 'host_ip']
    ordering_fields = '__all__'

class RobotHasAutomationViewSet(BaseModelViewSet):
    queryset = RobotHasAutomation.objects.all()
    serializer_class = RobotHasAutomationSerializer
    ordering_fields = '__all__'

class SystemViewSet(BaseModelViewSet):
    queryset = System.objects.all()
    serializer_class = SystemSerializer
    search_fields = ['name']
    ordering_fields = '__all__'

class AutomationHasSystemViewSet(BaseModelViewSet):
    queryset = AutomationHasSystem.objects.all()
    serializer_class = AutomationHasSystemSerializer
    ordering_fields = '__all__'

class ScheduleRestrictionViewSet(BaseModelViewSet):
    queryset = ScheduleRestriction.objects.all()
    serializer_class = ScheduleRestrictionSerializer
    ordering_fields = '__all__'

class ScheduleViewSet(BaseModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    search_fields = ['days_of_week']
    ordering_fields = '__all__'


class AgendaViewSet(BaseModelViewSet):
    queryset = Agenda.objects.all()
    serializer_class = AgendaSerializer
    search_fields = ['automation__project_name']
    ordering_fields = '__all__'


class TaskViewSet(BaseModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    search_fields = ['automation__project_name', 'status']
    ordering_fields = '__all__'
