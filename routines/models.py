from django.db import models
import uuid
from core.models import Task, Robot
import pgtrigger
from django.utils import timezone

trigger_update_column_task = pgtrigger.Trigger(
        name="update_task_counters",
        operation=pgtrigger.Insert | pgtrigger.Update | pgtrigger.Delete,
        when=pgtrigger.After,
        func="""
            DECLARE
                tarefa_uuid UUID;
            BEGIN
                -- Captura o ID da tarefa alterada
                tarefa_uuid := COALESCE(NEW.id_tarefa_id, OLD.id_tarefa_id);

                -- Atualiza os contadores na tabela core_task
                UPDATE core_task AS t
                SET
                    total_rotinas = COALESCE(sub.total, 0),
                    rotinas_pendentes = COALESCE(sub.pending, 0),
                    rotinas_processando = COALESCE(sub.in_progress, 0),
                    rotinas_erros = COALESCE(sub.failed, 0),
                    rotinas_outros = COALESCE(sub.others, 0)
                FROM (
                    SELECT
                        id_tarefa_id,
                        COUNT(*) AS total,
                        COUNT(*) FILTER (WHERE status = 'pending') AS pending,
                        COUNT(*) FILTER (WHERE status = 'in_progress') AS in_progress,
                        COUNT(*) FILTER (WHERE status = 'failed') AS failed,
                        COUNT(*) FILTER (WHERE status NOT IN ('pending','in_progress','failed')) AS others
                    FROM routines_atualizacaobaseclienteshubsoft
                    GROUP BY id_tarefa_id
                ) AS sub
                WHERE t.id = tarefa_uuid
                  AND t.id = sub.id_tarefa_id;

                RETURN NULL;
            END;
        """,
    )

# Create your models here.
@pgtrigger.register(trigger_update_column_task)
class AtualizacaoBaseClientesHubSoft(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_tarefa = models.ForeignKey(Task, on_delete=models.PROTECT, null=True, blank=True)
    id_robo = models.ForeignKey(Robot, on_delete=models.PROTECT, null=True, blank=True)
    attempts = models.IntegerField(default=0, verbose_name="Tentativas")
    data_inicio = models.DateTimeField(null=True, blank=True)
    data_fim = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=25, choices=[('pending', 'Pendente'), ('in_progress', 'Em Progresso'), ('completed', 'Concluído'), ('failed', 'Falhou')], default='pending', verbose_name="Status")
    observation = models.TextField(blank=True, verbose_name="Observação")
    execute_after = models.DateTimeField(default=timezone.now, null=True, blank=True, verbose_name="Executar Após")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Data de Atualização")

    class Meta:
        verbose_name = "Atualização Base Clientes HubSoft"
        verbose_name_plural = "Atualizações Base Clientes HubSoft"
        
    def __str__(self):
        return f"AtualizaçãoBaseClientesHubSoft {self.id} - Status: {self.status}"