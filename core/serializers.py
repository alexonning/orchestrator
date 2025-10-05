from rest_framework import serializers
from .models import Automation, Robot, RobotHasAutomation, System, AutomationHasSystem, ScheduleRestriction, Schedule

class AutomationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Automation
        fields = '__all__'

class RobotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Robot
        fields = '__all__'

class RobotHasAutomationSerializer(serializers.ModelSerializer):
    class Meta:
        model = RobotHasAutomation
        fields = '__all__'

class SystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = System
        fields = '__all__'

class AutomationHasSystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = AutomationHasSystem
        fields = '__all__'

class ScheduleRestrictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScheduleRestriction
        fields = '__all__'

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'
