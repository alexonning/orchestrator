from django import forms
from.models import Schedule

class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = '__all__'
        widgets = {
            'days_of_week': forms.CheckboxSelectMultiple(),
            'months': forms.CheckboxSelectMultiple()
        }
