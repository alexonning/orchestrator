from rest_framework import routers
from django.urls import path, include
from .viewsets import (
    AutomationViewSet, RobotViewSet, RobotHasAutomationViewSet,
    SystemViewSet, AutomationHasSystemViewSet, ScheduleRestrictionViewSet,
    ScheduleViewSet, AgendaViewSet, TaskViewSet
)

router = routers.DefaultRouter()
router.register(r'automations', AutomationViewSet)
router.register(r'robots', RobotViewSet)
router.register(r'robot-automations', RobotHasAutomationViewSet)
router.register(r'systems', SystemViewSet)
router.register(r'automation-systems', AutomationHasSystemViewSet)
router.register(r'schedule-restrictions', ScheduleRestrictionViewSet)
router.register(r'schedules', ScheduleViewSet)
router.register(r'agendas', AgendaViewSet)
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
