from rest_framework import viewsets, permissions, filters as rest_framework_filters
from drf_yasg.utils import swagger_auto_schema
from .models import Automation, Robot, RobotHasAutomation, System, AutomationHasSystem, ScheduleRestriction, Schedule
from .serializers import (
    AutomationSerializer, RobotSerializer, RobotHasAutomationSerializer,
    SystemSerializer, AutomationHasSystemSerializer, ScheduleRestrictionSerializer,
    ScheduleSerializer
)
from .filters import DynamicFilterBackend

class BaseModelViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [
        DynamicFilterBackend,
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
