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

    @swagger_auto_schema(tags=["Automation"])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(tags=["Automation"])
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(tags=["Automation"])
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(tags=["Automation"])
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(tags=["Automation"])
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(tags=["Automation"])
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

class RobotViewSet(BaseModelViewSet):
    queryset = Robot.objects.all()
    serializer_class = RobotSerializer
    search_fields = ['name', 'host_ip']
    ordering_fields = '__all__'

    @swagger_auto_schema(tags=["Robot"])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(tags=["Robot"])
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(tags=["Robot"])
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(tags=["Robot"])
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(tags=["Robot"])
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(tags=["Robot"])
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

class RobotHasAutomationViewSet(BaseModelViewSet):
    queryset = RobotHasAutomation.objects.all()
    serializer_class = RobotHasAutomationSerializer
    ordering_fields = '__all__'

    @swagger_auto_schema(tags=["RobotHasAutomation"])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(tags=["RobotHasAutomation"])
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(tags=["RobotHasAutomation"])
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(tags=["RobotHasAutomation"])
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(tags=["RobotHasAutomation"])
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(tags=["RobotHasAutomation"])
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

class SystemViewSet(BaseModelViewSet):
    queryset = System.objects.all()
    serializer_class = SystemSerializer
    search_fields = ['name']
    ordering_fields = '__all__'

    @swagger_auto_schema(tags=["System"])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(tags=["System"])
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(tags=["System"])
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(tags=["System"])
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(tags=["System"])
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(tags=["System"])
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

class AutomationHasSystemViewSet(BaseModelViewSet):
    queryset = AutomationHasSystem.objects.all()
    serializer_class = AutomationHasSystemSerializer
    ordering_fields = '__all__'

    @swagger_auto_schema(tags=["AutomationHasSystem"])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(tags=["AutomationHasSystem"])
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(tags=["AutomationHasSystem"])
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(tags=["AutomationHasSystem"])
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(tags=["AutomationHasSystem"])
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(tags=["AutomationHasSystem"])
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

class ScheduleRestrictionViewSet(BaseModelViewSet):
    queryset = ScheduleRestriction.objects.all()
    serializer_class = ScheduleRestrictionSerializer
    ordering_fields = '__all__'

    @swagger_auto_schema(tags=["ScheduleRestriction"])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(tags=["ScheduleRestriction"])
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(tags=["ScheduleRestriction"])
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(tags=["ScheduleRestriction"])
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(tags=["ScheduleRestriction"])
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(tags=["ScheduleRestriction"])
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

class ScheduleViewSet(BaseModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    search_fields = ['days_of_week']
    ordering_fields = '__all__'

    @swagger_auto_schema(tags=["Schedule"])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(tags=["Schedule"])
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(tags=["Schedule"])
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(tags=["Schedule"])
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(tags=["Schedule"])
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(tags=["Schedule"])
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class AgendaViewSet(BaseModelViewSet):
    queryset = Agenda.objects.all()
    serializer_class = AgendaSerializer
    search_fields = ['automation__project_name']
    ordering_fields = '__all__'

    @swagger_auto_schema(tags=["Agenda"])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(tags=["Agenda"])
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(tags=["Agenda"])
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(tags=["Agenda"])
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(tags=["Agenda"])
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(tags=["Agenda"])
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class TaskViewSet(BaseModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    search_fields = ['automation__project_name', 'status']
    ordering_fields = '__all__'

    @swagger_auto_schema(tags=["Task"])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(tags=["Task"])
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(tags=["Task"])
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(tags=["Task"])
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(tags=["Task"])
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(tags=["Task"])
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
