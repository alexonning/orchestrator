from django.contrib import admin
from .models import Clientes, Servicos
from unfold.admin import ModelAdmin

# Register your models here.
@admin.register(Clientes)
class ClientesAdmin(ModelAdmin):
    list_display = (
        "id_cliente", "nome_cliente", "nome_fantasia", "tipo_pessoa", "cpf_cnpj", "ativo", "data_cadastro", "data_atualizacao"
    )
    search_fields = ("nome_cliente", "nome_fantasia", "cpf_cnpj", "codigo_cliente")
    list_filter = ("ativo", "tipo_pessoa", "estado_civil", "sexo", "nacionalidade")
    fieldsets = (
        ("Identificação", {
            "fields": (
                "id", "id_cliente", "uuid_cliente", "codigo_cliente", "nome_cliente", "nome_fantasia", "tipo_pessoa", "cpf_cnpj"
            )
        }),
        ("Contato", {
            "fields": (
                "telefone_primario", "telefone_secundario"
            )
        }),
        ("Documentos", {
            "fields": (
                "rg", "rg_emissao", "inscricao_municipal", "inscricao_estadual"
            )
        }),
        ("Informações Pessoais", {
            "fields": (
                "data_nascimento", "estado_civil", "sexo", "nacionalidade"
            )
        }),
        ("Status", {
            "fields": (
                "ativo", "origem_cliente"
            )
        }),
        ("Datas", {
            "fields": (
                "data_cadastro", "data_atualizacao"
            )
        }),
    )
    readonly_fields = ("id", "id_cliente", "uuid_cliente", "data_cadastro", "data_atualizacao")

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
    list_per_page = 12


    # Display cancel button in submit line in changeform
    change_form_show_cancel_button = True # show/hide cancel button in changeform, default: False


@admin.register(Servicos)
class ServicosAdmin(ModelAdmin):
    list_display = (
        "id_cliente", "id_servico", "nome", "numero_plano", "status", "tecnologia", "valor", "data_cadastro", "data_atualizacao"
    )
    search_fields = ("nome", "numero_plano", "status", "tecnologia", "login", "mac_addr")
    list_filter = ("status", "tecnologia", "status_prefixo", "motivo_cancelamento_prefixo", "data_cancelamento")
    fieldsets = (
        ("Identificação do Serviço", {
            "fields": (
                "id_cliente", "id_cliente_servico", "uuid_cliente_servico", "id_servico", "numero_plano", "nome"
            )
        }),
        ("Status e Tecnologia", {
            "fields": (
                "status", "status_prefixo", "tecnologia", "valor"
            )
        }),
        ("Velocidades", {
            "fields": (
                "velocidade_download", "velocidade_upload"
            )
        }),
        ("Acesso", {
            "fields": (
                "login", "senha", "mac_addr"
            )
        }),
        ("Cancelamento", {
            "fields": (
                "id_motivo_cancelamento", "data_cancelamento", "motivo_cancelamento", "motivo_cancelamento_prefixo"
            )
        }),
        ("Datas", {
            "fields": (
                "data_inicio_contrato", "data_fim_contrato", "data_cadastro", "data_habilitacao", "data_venda", "data_atualizacao"
            )
        }),
        ("Endereço", {
            "fields": (
                "endereco", "numero", "complemento", "bairro", "cep", "cidade", "estado", "uf", "pais"
            )
        }),
    )
    readonly_fields = ("data_cadastro", "data_atualizacao")

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
