from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import AtualizacaoBaseClientesHubSoft

@admin.register(AtualizacaoBaseClientesHubSoft)
class AtualizacaoBaseClientesHubSoftAdmin(ModelAdmin):
    fieldsets = (
        (
            "Informações Gerais",
            {
                "fields": [
                    'id_tarefa', 'id_robo', 'attempts', 'data_inicio', 'data_fim', 'status', 'observation', 'execute_after'
                ],
            },
        ),
        (
            "Datas de Registro",
            {
                "fields": [
                    'created_at', 'updated_at'
                ],
                "classes": ["collapse"],
            },
        ),
    )
    list_display = ('id', 'id_robo__name', 'status', 'attempts', 'data_inicio', 'data_fim', 'execute_after')
    list_filter = ('id_robo__name', 'status', 'data_inicio', 'data_fim')
    ordering = ('id_robo__name', 'status', 'data_inicio', 'data_fim')

    readonly_fields = ('created_at', 'updated_at')