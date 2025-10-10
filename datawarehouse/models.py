from django.db import models
import uuid

# Create your models here.
class Clientes(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="ID")
    id_cliente = models.IntegerField(unique=True, verbose_name="ID Cliente")
    uuid_cliente = models.UUIDField(editable=True, verbose_name="UUID Cliente")
    codigo_cliente = models.IntegerField(verbose_name="Código Cliente")
    nome_cliente = models.CharField(max_length=255, verbose_name="Nome Cliente")
    nome_fantasia = models.CharField(max_length=255, verbose_name="Nome Fantasia", null=True, blank=True)
    tipo_pessoa = models.CharField(max_length=2, verbose_name="Tipo Pessoa")
    cpf_cnpj = models.CharField(max_length=20, verbose_name="CPF/CNPJ")
    telefone_primario = models.CharField(max_length=20, null=True, blank=True, verbose_name="Telefone Primário")
    telefone_secundario = models.CharField(max_length=20, null=True, blank=True, verbose_name="Telefone Secundário")
    rg = models.CharField(max_length=20, null=True, blank=True, verbose_name="RG")
    rg_emissao = models.CharField(max_length=20, null=True, blank=True, verbose_name="RG Emissão")
    inscricao_municipal = models.CharField(max_length=255, null=True, blank=True, verbose_name="Inscrição Municipal")
    inscricao_estadual = models.CharField(max_length=255, null=True, blank=True, verbose_name="Inscrição Estadual")
    data_cadastro = models.DateTimeField(verbose_name="Data de Cadastro")
    data_nascimento = models.DateField(null=True, blank=True, verbose_name="Data de Nascimento")
    ativo = models.BooleanField(default=True, verbose_name="Ativo")
    origem_cliente = models.CharField(max_length=255, null=True, blank=True, verbose_name="Origem Cliente")
    data_atualizacao = models.DateTimeField(verbose_name="Data de Atualização")
    estado_civil = models.CharField(max_length=50, null=True, blank=True, verbose_name="Estado Civil")
    sexo = models.CharField(max_length=20, null=True, blank=True, verbose_name="Sexo")
    nacionalidade = models.CharField(max_length=50, null=True, blank=True, verbose_name="Nacionalidade")

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ['id_cliente']

    def __str__(self):
        return self.nome_cliente 

class Servicos(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="ID")
    id_cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE, verbose_name="Cliente")
    id_cliente_servico = models.IntegerField(verbose_name="ID Cliente Serviço")
    uuid_cliente_servico = models.UUIDField(editable=True, verbose_name="UUID Cliente Serviço")
    id_servico = models.IntegerField(verbose_name="ID Serviço")
    numero_plano = models.CharField(max_length=50, verbose_name="Número do Plano")
    nome = models.CharField(max_length=255, verbose_name="Nome")
    valor = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Valor")
    status = models.CharField(max_length=100, verbose_name="Status")
    status_prefixo = models.CharField(max_length=100, verbose_name="Status Prefixo")
    tecnologia = models.CharField(max_length=100, verbose_name="Tecnologia")
    velocidade_download = models.CharField(max_length=50, verbose_name="Velocidade Download")
    velocidade_upload = models.CharField(max_length=50, verbose_name="Velocidade Upload")
    login = models.CharField(max_length=100, null=True, blank=True, verbose_name="Login")
    senha = models.CharField(max_length=100, null=True, blank=True, verbose_name="Senha")
    mac_addr = models.CharField(max_length=50, null=True, blank=True, verbose_name="MAC Address")
    id_motivo_cancelamento = models.IntegerField(null=True, blank=True, verbose_name="ID Motivo Cancelamento")
    data_cancelamento = models.DateTimeField(null=True, blank=True, verbose_name="Data de Cancelamento")
    motivo_cancelamento = models.CharField(max_length=255, null=True, blank=True, verbose_name="Motivo Cancelamento")
    motivo_cancelamento_prefixo = models.CharField(max_length=255, null=True, blank=True, verbose_name="Motivo Cancelamento Prefixo")
    data_cadastro = models.DateTimeField(verbose_name="Data de Cadastro")
    data_habilitacao = models.DateTimeField(null=True, blank=True, verbose_name="Data de Habilitação")
    data_venda = models.DateTimeField(null=True, blank=True, verbose_name="Data de Venda")
    data_atualizacao = models.DateTimeField(verbose_name="Data de Atualização")
    data_inicio_contrato = models.DateField(null=True, blank=True, verbose_name="Data Início Contrato")
    data_fim_contrato = models.DateField(null=True, blank=True, verbose_name="Data Fim Contrato")
    
    endereco = models.CharField(max_length=255, null=True, blank=True, verbose_name="Endereço")
    numero = models.CharField(max_length=20, null=True, blank=True, verbose_name="Número")
    complemento = models.CharField(max_length=255, null=True, blank=True, verbose_name="Complemento")
    bairro = models.CharField(max_length=100, null=True, blank=True, verbose_name="Bairro")
    cep = models.CharField(max_length=20, null=True, blank=True, verbose_name="CEP")
    cidade = models.CharField(max_length=100, null=True, blank=True, verbose_name="Cidade")
    estado = models.CharField(max_length=50, null=True, blank=True, verbose_name="Estado")
    uf = models.CharField(max_length=2, null=True, blank=True, verbose_name="UF")
    pais = models.CharField(max_length=100, null=True, blank=True, verbose_name="País")

    class Meta:
        verbose_name = "Serviço"
        verbose_name_plural = "Serviços"
        ordering = ['id_cliente', 'id_servico']

    def __str__(self):
        return f"{self.nome} - {self.numero_plano}"
    