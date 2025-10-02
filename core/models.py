import uuid
from django.db import models

# Create your models here.
PRIORITY_CHOICES = [(i, str(i)) for i in range(0, 31)]

STATUS_AUTOMATION_CHOICES = [
    ('roadmap', 'Roadmap'),
    ('in_progress', 'In Progress'),
    ('development', 'Development'),
    ('homologation', 'Homologation'),
    ('production', 'Production'),
    ('discontinued', 'Discontinued'),
]

STATUS_ROBOT_CHOICES = [
    ('idle', 'Idle'),
    ('working', 'Working'),
    ('error', 'Error'),
    ('shutting_down_systems', 'Shutting Down Systems'),
]

DAYS_OF_WEEK_CHOICES = [
    ('mon', 'Segunda-feira'),
    ('tue', 'Terça-feira'),
    ('wed', 'Quarta-feira'),
    ('thu', 'Quinta-feira'),
    ('fri', 'Sexta-feira'),
    ('sat', 'Sábado'),
    ('sun', 'Domingo'),
]

DAYS_OF_MONTH_CHOICES = [
    (1, 'Janeiro'),
    (2, 'Fevereiro'),
    (3, 'Março'),
    (4, 'Abril'),
    (5, 'Maio'),
    (6, 'Junho'),
    (7, 'Julho'),
    (8, 'Agosto'),
    (9, 'Setembro'),
    (10, 'Outubro'),
    (11, 'Novembro'),
    (12, 'Dezembro'),
]

class Automation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, verbose_name="Nome")
    description = models.TextField(blank=True, verbose_name="Descrição")
    status = models.CharField(max_length=25, choices=STATUS_AUTOMATION_CHOICES, default='roadmap', verbose_name="Status")
    priority = models.IntegerField(default=0, verbose_name="Prioridade", choices=PRIORITY_CHOICES)
    business_day_only = models.BooleanField(default=False, verbose_name="Apenas Dias Úteis")
    executor_time = models.DurationField(blank=True, null=True, verbose_name="Tempo do Executor")
    average_executor_cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name="Custo Médio do Executor")
    limit_attempts = models.IntegerField(default=3, verbose_name="Limite de Tentativas")
    system_restriction = models.BooleanField(default=False, verbose_name="Restrição do Sistema")
    project_type = models.CharField(max_length=25, verbose_name="Tipo de Projeto", help_text="Informe o tipo de projeto. Ex: Python, Java")
    git_project_url = models.CharField(max_length=255, verbose_name="URL do Projeto Git", help_text="Informe a URL do repositório Git.")
    project_name = models.CharField(max_length=255, verbose_name="Nome do Projeto", help_text="Informe o nome do projeto.")
    project_version = models.CharField(max_length=50, verbose_name="Versão do Projeto", help_text="Informe a versão do projeto.")
    project_file_start = models.CharField(max_length=255, verbose_name="Arquivo de Início do Projeto", help_text="Informe o caminho do arquivo de início do projeto.")
    table_name_schema = models.CharField(max_length=255, verbose_name="Schema da Tabela", help_text="Informe o nome do schema da tabela no banco de dados.")
    table_name = models.CharField(max_length=255, verbose_name="Nome da Tabela", help_text="Informe o nome da tabela no banco de dados.")
    by_pass = models.BooleanField(default=False, verbose_name="Bypass")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Data de Atualização")

    def __str__(self):
        return self.name

class Robot(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, verbose_name="Nome")
    automation = models.ForeignKey(Automation, on_delete=models.CASCADE, related_name="robots")
    type = models.CharField(max_length=20, verbose_name="Tipo")
    host_name = models.CharField(max_length=255, verbose_name="Nome do Host")
    host_ip = models.GenericIPAddressField(verbose_name="IP do Host")
    status = models.CharField(max_length=25, choices=STATUS_ROBOT_CHOICES, default='idle', verbose_name="Status")
    active = models.BooleanField(default=True, verbose_name="Ativo")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Data de Atualização")

    def __str__(self):
        return self.name
    

class RobotHasAutomation(models.Model):
    robot = models.ForeignKey(Robot, on_delete=models.CASCADE, related_name="robot_automations")
    automation = models.ForeignKey(Automation, on_delete=models.CASCADE, related_name="automation_robots")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Data de Atualização")

    def __str__(self):
        return f"{self.robot.name} - {self.automation.name}"
    

class System(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, verbose_name="Nome")
    description = models.TextField(verbose_name="Descrição")
    restriction = models.BooleanField(default=False, verbose_name="Restrição")

class AutomationHasSystem(models.Model):
    automation = models.ForeignKey(Automation, on_delete=models.CASCADE, related_name="automation_systems")
    system = models.ForeignKey(System, on_delete=models.CASCADE, related_name="system_automations")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Data de Atualização")

    def __str__(self):
        return f"{self.automation.name} - {self.system.name}"

class ScheduleRestriction(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    automation = models.ForeignKey(Automation, on_delete=models.CASCADE, related_name="schedule_restrictions")
    start_time = models.DateTimeField(verbose_name="Início")
    end_time = models.DateTimeField(verbose_name="Fim")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Data de Atualização")

    def __str__(self):
        return f"{self.automation.name} - {self.start_time} a {self.end_time}"
    
class Schedule(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    automation = models.ForeignKey(Automation, on_delete=models.CASCADE, related_name="schedules")

    days_of_week = models.JSONField(default=list, verbose_name="Dias da Semana", choices=DAYS_OF_WEEK_CHOICES, help_text="Selecione um ou mais dias da semana. Ex: ['mon', 'tue', 'wed']")
    # day_of_months = models.JSONField(default=list, verbose_name="Dias do Mês", validators=[models.Min(1), models.Max(31)], help_text="Selecione um ou mais dias do mês. Ex: [1, 15, 30]")

    months = models.JSONField(default=list, verbose_name="Meses", choices=DAYS_OF_MONTH_CHOICES, help_text="Selecione um ou mais meses. Ex: [1, 2, 3]")
    # hours = models.JSONField(default=list, verbose_name="Horas", validators=[models.Min(0), models.Max(23)], help_text="Selecione um ou mais horários. Ex: [0, 12, 23]")
    # minutes = models.JSONField(default=list, verbose_name="Minutos", validators=[models.Min(0), models.Max(59)], help_text="Selecione um ou mais minutos. Ex: [0, 30, 59]")

    active = models.BooleanField(default=True, verbose_name="Ativo")
    action = models.CharField(max_length=255, verbose_name="Ação")
    business_day = models.BooleanField(default=False, verbose_name="Dia Útil")

    def __str__(self):
        return self.automation.name


class TimeRestriction(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    automation = models.ForeignKey(Automation, on_delete=models.CASCADE, related_name="time_restrictions")
    start_time = models.TimeField(verbose_name="Início")
    end_time = models.TimeField(verbose_name="Fim")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Data de Atualização")

    def __str__(self):
        return f"{self.automation.name} - {self.start_time} a {self.end_time}"