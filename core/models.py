import uuid
from django.db import models
from multiselectfield import MultiSelectField

# Create your models here.
PRIORITY_CHOICES = [(i, str(i)) for i in range(0, 10)]

STATUS_AUTOMATION_CHOICES = [
    ('roadmap', 'Roadmap'),
    ('in_progress', 'Em Progresso'),
    ('development', 'Desenvolvimento'),
    ('homologation', 'Homologação'),
    ('production', 'Produção'),
    ('discontinued', 'Descontinuado'),
]

STATUS_ROBOT_CHOICES = [
    ('idle', 'Ocioso'),
    ('working', 'Trabalhando'),
    ('error', 'Erro'),
    ('shutting_down_systems', 'Encerrando Sistemas'),
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
    ('1', 'Janeiro'),
    ('2', 'Fevereiro'),
    ('3', 'Março'),
    ('4', 'Abril'),
    ('5', 'Maio'),
    ('6', 'Junho'),
    ('7', 'Julho'),
    ('8', 'Agosto'),
    ('9', 'Setembro'),
    ('10', 'Outubro'),
    ('11', 'Novembro'),
    ('12', 'Dezembro'),
]

class Automation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, verbose_name="Nome")
    description = models.TextField(blank=True, verbose_name="Descrição")
    status = models.CharField(max_length=25, choices=STATUS_AUTOMATION_CHOICES, default='roadmap', verbose_name="Status")
    priority = models.IntegerField(default=0, verbose_name="Prioridade", choices=PRIORITY_CHOICES)
    business_day_only = models.BooleanField(default=False, verbose_name="Apenas Dias Úteis")
    executor_time = models.DurationField(blank=True, null=True, verbose_name="Tempo do Executor", help_text="Tempo do executor em segundos.")
    average_executor_cost = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True, verbose_name="Custo Médio do Executor")
    limit_attempts = models.IntegerField(default=3, verbose_name="Limite de Tentativas")
    system_restriction = models.BooleanField(default=False, verbose_name="Restrição do Sistema")
    project_type = models.CharField(max_length=25, verbose_name="Tipo de Projeto", choices=[('Python', 'Python'), ('Java', 'Java')], help_text="Informe o tipo de projeto. Ex: Python, Java")
    git_project_url = models.CharField(max_length=255, verbose_name="URL do Projeto Git", help_text="Informe a URL do repositório Git.")
    project_name = models.CharField(max_length=255, verbose_name="Nome do Projeto", help_text="Informe o nome do projeto.")
    project_version = models.CharField(max_length=50, verbose_name="Versão do Projeto", help_text="Informe a versão do projeto.")
    project_file_start = models.CharField(max_length=255, verbose_name="Arquivo de Início do Projeto", help_text="Informe o caminho do arquivo de início do projeto.")
    table_name_schema = models.CharField(max_length=255, verbose_name="Schema da Tabela", help_text="Informe o nome do schema da tabela no banco de dados.")
    table_name = models.CharField(max_length=255, verbose_name="Nome da Tabela", help_text="Informe o nome da tabela no banco de dados.")
    by_pass = models.BooleanField(default=False, verbose_name="Bypass")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Data de Atualização")

    class Meta:
        verbose_name = "Automação"
        verbose_name_plural = "Automações"
        ordering = ['-created_at', 'name']

    def __str__(self):
        return self.project_name

class Robot(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, verbose_name="Nome")
    automation = models.ForeignKey(Automation, null=True, blank=True, on_delete=models.DO_NOTHING, related_name="robots")
    type = models.CharField(max_length=20, verbose_name="Tipo", choices=[('Robot', 'Robô'), ('Developer', 'Desenvolvedor')], help_text="Informe o tipo do robô.")
    host_name = models.CharField(max_length=255, verbose_name="Nome do Host")
    host_ip = models.CharField(max_length=255, verbose_name="IP do Host")
    status = models.CharField(max_length=25, choices=STATUS_ROBOT_CHOICES, default='idle', verbose_name="Status")
    active = models.BooleanField(default=True, verbose_name="Ativo")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Data de Atualização")

    class Meta:
        verbose_name = "Robô"
        verbose_name_plural = "Robôs"
        ordering = ['-created_at', 'name']

    def __str__(self):
        return self.name
    
class RobotHasAutomation(models.Model):
    robot = models.ForeignKey(Robot, on_delete=models.CASCADE, related_name="robot_automations", verbose_name="Robô")
    automation = models.ForeignKey(Automation, on_delete=models.CASCADE, related_name="automation_robots", verbose_name="Automação")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Data de Atualização")

    class Meta:
        verbose_name = "Robô por Automação"
        verbose_name_plural = "Robôs por Automações"
        unique_together = ('robot', 'automation')
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.robot.name} - {self.automation.name}"
    
class System(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, verbose_name="Nome")
    description = models.TextField(verbose_name="Descrição")
    restriction = models.BooleanField(default=False, verbose_name="Restrição")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Data de Atualização")

    class Meta:
        verbose_name = "Sistema"
        verbose_name_plural = "Sistemas"
        ordering = ['-created_at', 'name']
    
    def __str__(self):
        return self.name

class AutomationHasSystem(models.Model):
    automation = models.ForeignKey(Automation, on_delete=models.CASCADE, related_name="automation_systems")
    system = models.ForeignKey(System, on_delete=models.CASCADE, related_name="system_automations")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Data de Atualização")

    class Meta:
        verbose_name = "Sistema por Automação"
        verbose_name_plural = "Sistemas por Automações"
        unique_together = ('automation', 'system')
        ordering = ['-created_at']
        
    def __str__(self):
        return f"{self.automation.name} - {self.system.name}"

class ScheduleRestriction(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    automation = models.ForeignKey(Automation, on_delete=models.CASCADE, related_name="schedule_restrictions")
    start_time = models.TimeField(verbose_name="Início")
    end_time = models.TimeField(verbose_name="Fim")
    active = models.BooleanField(default=True, verbose_name="Ativo")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Data de Atualização")

    class Meta:
        verbose_name = "Restrição de Agendamento"
        verbose_name_plural = "Restrições de Agendamento"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.automation.name} - {self.start_time} a {self.end_time}"
    
class Schedule(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    automation = models.ForeignKey(Automation, on_delete=models.CASCADE, related_name="schedules")

    days_of_week = MultiSelectField(default=list, verbose_name="Dias da Semana", choices=DAYS_OF_WEEK_CHOICES, help_text="Selecione um ou mais dias da semana. Ex: ['mon', 'tue', 'wed']")
    # day_of_months = models.JSONField(default=list, verbose_name="Dias do Mês", validators=[models.Min(1), models.Max(31)], help_text="Selecione um ou mais dias do mês. Ex: [1, 15, 30]")

    months = MultiSelectField(default=list, verbose_name="Meses", choices=DAYS_OF_MONTH_CHOICES, help_text="Selecione um ou mais meses. Ex: [1, 2, 3]")
    hours = models.JSONField(default=list, verbose_name="Horas", help_text="Selecione um ou mais horários. Ex: [0, 12, 23]")
    minutes = models.JSONField(default=list, verbose_name="Minutos", help_text="Selecione um ou mais minutos. Ex: [0, 30, 59]")

    active = models.BooleanField(default=True, verbose_name="Ativo", blank=False, null=False)
    action = models.CharField(max_length=255, verbose_name="Ação")
    business_day = models.BooleanField(default=False, verbose_name="Dia Útil")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Data de Atualização")

    class Meta:
        verbose_name = "Agendamento"
        verbose_name_plural = "Agendamentos"
        ordering = ['-created_at']

    def __str__(self):
        return self.automation.name

class Agenda(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    automation = models.ForeignKey(Automation, on_delete=models.CASCADE, related_name="agendas")
    date_execution = models.DateTimeField(verbose_name="Data de Execução")
    created_task = models.BooleanField(default=False, verbose_name="Tarefa Criada")
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação")

    class Meta:
        verbose_name = "Agenda"
        verbose_name_plural = "Agendas"
        ordering = ['-created_at']
        unique_together = ('automation', 'date_execution')

    def __str__(self):
        return self.id.__str__()

class Task(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    automation = models.ForeignKey(Automation, on_delete=models.CASCADE, related_name="tasks")
    agenda = models.ForeignKey(Agenda, null=True, blank=True, on_delete=models.SET_NULL, related_name="tasks")
    total_rotinas = models.IntegerField(default=0, verbose_name="Total de Rotinas")
    rotinas_pendentes = models.IntegerField(default=0, verbose_name="Rotinas Pendentes")
    rotinas_processando = models.IntegerField(default=0, verbose_name="Rotinas em Processamento")
    rotinas_erros = models.IntegerField(default=0, verbose_name="Rotinas com Erros")
    rotinas_outros = models.IntegerField(default=0, verbose_name="Outros Status de Rotinas")
    priority = models.IntegerField(verbose_name="Prioridade da Automação", editable=False, null=True, blank=True)
    
    date_task = models.DateField(verbose_name="Data da Tarefa", auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Data de Atualização")

    class Meta:
        verbose_name = "Tarefa"
        verbose_name_plural = "Tarefas"
        ordering = ['-created_at']
        unique_together = ['agenda']

    def save(self, *args, **kwargs):
        # Garante que a Automation esteja carregada antes de salvar
        if self.automation_id:
            # Sincroniza o valor da prioridade da Automation para a Task
            self.priority = self.automation.priority
            
        super().save(*args, **kwargs)

    def __str__(self):
        return self.id.__str__()