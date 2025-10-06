from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import (
    Automation, Robot, RobotHasAutomation, System, AutomationHasSystem, 
    ScheduleRestriction, Schedule, DAYS_OF_WEEK_CHOICES, DAYS_OF_MONTH_CHOICES,
    Agenda, Task
)
from django.utils.translation import gettext_lazy as _
from.forms import ScheduleForm


@admin.register(Automation)
class AutomationAdmin(ModelAdmin):
    fieldsets = (
        (
            ("Informações principais"),
            {
                "classes": ['collapse', 'extrapretty'],
                "fields": [
                    'name', 'description', 'status', 'priority', 'business_day_only', 'executor_time', 'average_executor_cost', 'limit_attempts', 'system_restriction', 'project_type', 'git_project_url', 'project_name', 'project_version',
                ],
            },
        ),
        (
            _("Configurações do Banco de Dados"),
            {
                "classes": ['collapse', 'extrapretty'],
                "fields": [
                    'project_file_start', 'table_name_schema', 'table_name', 'by_pass'
                ],
                'description': "Configurações relacionadas ao banco de dados.",
            },
        ),
    )
    
    list_display = ('project_name', 'status', 'priority', 'system_restriction', 'project_version', 'created_at')
    search_fields = ('name', 'status', 'project_type', 'git_project_url', 'project_name', 'project_version', 'table_name_schema', 'table_name')
    list_filter = ('status', 'priority', 'business_day_only', 'system_restriction', 'project_type', 'by_pass', 'created_at', 'updated_at')
    ordering = ('-created_at', 'name')
    compressed_fields = True
    warn_unsaved_form = True

    readonly_preprocess_fields = {
        "id": "html.unescape",
        "name": lambda content: content.strip(),
    }

    list_filter_submit = False

     # Display changelist in fullwidth
    list_fullwidth = False

    # Set to False, to enable filter as "sidebar"
    list_filter_sheet = True

    # Position horizontal scrollbar in changelist at the top
    list_horizontal_scrollbar_top = False

    # Dsable select all action in changelist
    list_disable_select_all = False

    # Custom actions
    actions_list = []  # Displayed above the results list
    actions_row = []  # Displayed in a table row in results list
    actions_detail = []  # Displayed at the top of for in object detail
    actions_submit_line = []  # Displayed near save in object detail

    # Display cancel button in submit line in changeform
    change_form_show_cancel_button = True # show/hide cancel button in changeform, default: False

@admin.register(Robot)
class RobotAdmin(ModelAdmin):
    related_modal_active = True 
    fieldsets = (
        (
            ("Informações principais"),
            {
                "fields": [
                    'name', 'automation', 'type', 'host_name', 'host_ip', 'status', 'active'
                ],
            },
        ),
    )
    
    list_display = ('name', 'automation', 'host_name', 'host_ip', 'status', 'active')
    search_fields = ('name', 'automation__name', 'type', 'host_name', 'host_ip', 'status')
    list_filter = ('type', 'status', 'active', 'created_at', 'updated_at')
    ordering = ('-created_at', 'name')
    compressed_fields = True
    warn_unsaved_form = True


    list_filter_submit = False

     # Display changelist in fullwidth
    list_fullwidth = False


    # Set to False, to enable filter as "sidebar"
    list_filter_sheet = True

    # Position horizontal scrollbar in changelist at the top
    list_horizontal_scrollbar_top = False

    # Dsable select all action in changelist
    list_disable_select_all = False

    # Custom actions
    actions_list = []  # Displayed above the results list
    actions_row = []  # Displayed in a table row in results list
    actions_detail = []  # Displayed at the top of for in object detail
    actions_submit_line = []  # Displayed near save in object detail

    # Display cancel button in submit line in changeform
    change_form_show_cancel_button = True # show/hide cancel button in changeform, default: False

@admin.register(RobotHasAutomation)
class RobotHasAutomationAdmin(ModelAdmin):
    related_modal_active = True 
    fieldsets = (
        (
            ("Informações principais"),
            {
                "fields": [
                    'robot', 'automation'
                ],
            },
        ),
    )
    
    list_display = ('robot', 'automation', 'updated_at', 'created_at')
    search_fields = ('robot__name', 'automation__project_name')
    list_filter = ('created_at', 'updated_at')
    ordering = ('-created_at', 'robot__name')
    compressed_fields = True
    warn_unsaved_form = True


    list_filter_submit = False

     # Display changelist in fullwidth
    list_fullwidth = False


    # Set to False, to enable filter as "sidebar"
    list_filter_sheet = True

    # Position horizontal scrollbar in changelist at the top
    list_horizontal_scrollbar_top = False

    # Dsable select all action in changelist
    list_disable_select_all = False

    # Custom actions
    actions_list = []  # Displayed above the results list
    actions_row = []  # Displayed in a table row in results list
    actions_detail = []  # Displayed at the top of for in object detail
    actions_submit_line = []  # Displayed near save in object detail

    # Display cancel button in submit line in changeform
    change_form_show_cancel_button = True # show/hide cancel button in changeform, default: False3

@admin.register(System)
class SystemAdmin(ModelAdmin):
    fieldsets = (
        (
            ("Informações principais"),
            {
                "fields": [
                    'name', 'description', 'restriction'
                ],
            },
        ),
    )
    
    list_display = ('name', 'restriction', 'updated_at', 'created_at')
    search_fields = ('name', 'description')
    list_filter = ('restriction', 'created_at', 'updated_at')
    ordering = ('-created_at', 'name')
    compressed_fields = True
    warn_unsaved_form = True


    list_filter_submit = False

     # Display changelist in fullwidth
    list_fullwidth = False


    # Set to False, to enable filter as "sidebar"
    list_filter_sheet = True

    # Position horizontal scrollbar in changelist at the top
    list_horizontal_scrollbar_top = False

    # Dsable select all action in changelist
    list_disable_select_all = False

    # Custom actions
    actions_list = []  # Displayed above the results list
    actions_row = []  # Displayed in a table row in results list
    actions_detail = []  # Displayed at the top of for in object detail
    actions_submit_line = []  # Displayed near save in object detail

    # Display cancel button in submit line in changeform
    change_form_show_cancel_button = True # show/hide cancel button in changeform, default: False

@admin.register(AutomationHasSystem)
class AutomationHasSystemAdmin(ModelAdmin):
    related_modal_active = True 
    fieldsets = (
        (
            ("Informações principais"),
            {
                "fields": [
                    'automation', 'system'
                ],
            },
        ),
    )
    
    list_display = ('automation', 'system', 'updated_at', 'created_at')
    search_fields = ('automation__project_name', 'system__name')
    list_filter = ('created_at', 'updated_at')
    ordering = ('-created_at', 'automation__project_name')
    compressed_fields = True
    warn_unsaved_form = True


    list_filter_submit = False

     # Display changelist in fullwidth
    list_fullwidth = False


    # Set to False, to enable filter as "sidebar"
    list_filter_sheet = True

    # Position horizontal scrollbar in changelist at the top
    list_horizontal_scrollbar_top = False

    # Dsable select all action in changelist
    list_disable_select_all = False

    # Custom actions
    actions_list = []  # Displayed above the results list
    actions_row = []  # Displayed in a table row in results list
    actions_detail = []  # Displayed at the top of for in object detail
    actions_submit_line = []  # Displayed near save in object detail

    # Display cancel button in submit line in changeform
    change_form_show_cancel_button = True # show/hide cancel button in changeform, default: False
    
@admin.register(ScheduleRestriction)
class ScheduleRestrictionAdmin(ModelAdmin):
    fieldsets = (
        (
            ("Informações principais"),
            {
                "fields": [
                    'automation', 'start_time', 'end_time', 'active'
                ],
            },
        ),
    )
    
    list_display = ('automation', 'start_time', 'end_time', 'active')
    search_fields = ['automation__project_name']
    list_filter = ('created_at', 'updated_at', 'active')
    ordering = ('-created_at', 'automation__project_name')
    compressed_fields = True
    warn_unsaved_form = True


    list_filter_submit = False

     # Display changelist in fullwidth
    list_fullwidth = False


    # Set to False, to enable filter as "sidebar"
    list_filter_sheet = True

    # Position horizontal scrollbar in changelist at the top
    list_horizontal_scrollbar_top = False

    # Dsable select all action in changelist
    list_disable_select_all = False

    # Custom actions
    actions_list = []  # Displayed above the results list
    actions_row = []  # Displayed in a table row in results list
    actions_detail = []  # Displayed at the top of for in object detail
    actions_submit_line = []  # Displayed near save in object detail

    # Display cancel button in submit line in changeform
    change_form_show_cancel_button = True # show/hide cancel button in changeform, default: False

@admin.register(Schedule)
class ScheduleAdmin(ModelAdmin):
    form = ScheduleForm
    related_modal_active = True
    fieldsets = (
        (
            ("Informações principais"),
            {
                "fields": [
                    'automation', 'days_of_week', 'months', 'active', 'action', 'business_day', 'hours', 'minutes'
                ],
                "description": "Marque os dias da semana e meses desejados."
            },
        ),
    )
    
    list_display = ['automation', 'get_days_of_week', 'get_months', 'active', 'business_day']
    search_fields = ['automation__project_name']
    list_filter = ('active', 'business_day', 'days_of_week', 'months')
    ordering = ('automation__project_name',)
    compressed_fields = True
    warn_unsaved_form = True

    def get_days_of_week(self, obj):
        return ", ".join([dict(DAYS_OF_WEEK_CHOICES).get(day) for day in obj.days_of_week])
    get_days_of_week.short_description = "Dias da Semana"

    def get_months(self, obj):
        return ", ".join([dict(DAYS_OF_MONTH_CHOICES).get(month) for month in obj.months])
    get_months.short_description = "Meses"


    list_filter_submit = False

     # Display changelist in fullwidth
    list_fullwidth = False


    # Set to False, to enable filter as "sidebar"
    list_filter_sheet = True

    # Position horizontal scrollbar in changelist at the top
    list_horizontal_scrollbar_top = False

    # Dsable select all action in changelist
    list_disable_select_all = False

    # Custom actions
    actions_list = []  # Displayed above the results list
    actions_row = []  # Displayed in a table row in results list
    actions_detail = []  # Displayed at the top of for in object detail
    actions_submit_line = []  # Displayed near save in object detail

    # Display cancel button in submit line in changeform
    change_form_show_cancel_button = True # show/hide cancel button in changeform, default: False

@admin.register(Agenda)
class AgendaAdmin(ModelAdmin):
    fieldsets = (
        (
            ("Informações principais"),
            {
                "fields": [
                    'automation', 'date_execution', 'created_task', 'created_at'
                ],
            },
        ),
    )

    list_display = ('automation', 'date_execution', 'created_task', 'created_at')
    search_fields = ['automation__project_name']
    list_filter = ['created_at']
    ordering = ('-created_at', 'automation__project_name')

    compressed_fields = True
    warn_unsaved_form = True


    list_filter_submit = False

     # Display changelist in fullwidth
    list_fullwidth = False


    # Set to False, to enable filter as "sidebar"
    list_filter_sheet = True

    # Position horizontal scrollbar in changelist at the top
    list_horizontal_scrollbar_top = False

    # Dsable select all action in changelist
    list_disable_select_all = False

    # Custom actions
    actions_list = []  # Displayed above the results list
    actions_row = []  # Displayed in a table row in results list
    actions_detail = []  # Displayed at the top of for in object detail
    actions_submit_line = []  # Displayed near save in object detail

    # Display cancel button in submit line in changeform
    change_form_show_cancel_button = True # show/hide cancel button in changeform, default: False

@admin.register(Task)
class TaskAdmin(ModelAdmin):
    fieldsets = (
        (
            ("Informações principais"),
            {
                "fields": [
                    'automation', 'robot', 'agenda', 'start_time', 'end_time', 'status'
                ],
            },
        ),
    )

    list_display = ('automation', 'robot', 'start_time', 'end_time', 'status')
    search_fields = ['automation__project_name', 'status']
    list_filter = ['created_at']
    ordering = ('-created_at', 'automation__project_name')

    compressed_fields = True
    warn_unsaved_form = True


    list_filter_submit = False

     # Display changelist in fullwidth
    list_fullwidth = False


    # Set to False, to enable filter as "sidebar"
    list_filter_sheet = True

    # Position horizontal scrollbar in changelist at the top
    list_horizontal_scrollbar_top = False

    # Dsable select all action in changelist
    list_disable_select_all = False

    # Custom actions
    actions_list = []  # Displayed above the results list
    actions_row = []  # Displayed in a table row in results list
    actions_detail = []  # Displayed at the top of for in object detail
    actions_submit_line = []  # Displayed near save in object detail

    # Display cancel button in submit line in changeform
    change_form_show_cancel_button = True # show/hide cancel button in changeform, default: False

