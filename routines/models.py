from django.db import models
import uuid
from core.models import Task, Robot

# Create your models here.

class AtualizacaoBaseClientesHubSoft(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_tarefa = models.ForeignKey(Task, on_delete=models.PROTECT, null=True, blank=True)
    id_robo = models.ForeignKey(Robot, on_delete=models.PROTECT, null=True, blank=True)
    data_inicio = models.DateTimeField(null=True, blank=True)
    data_fim = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=50, null=True, blank=True)
    detalhes = models.TextField(null=True, blank=True)