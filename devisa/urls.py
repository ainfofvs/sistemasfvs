from django.urls import path
from .views import devisa, cnpj, cnpj_create, cnpj_update, cnpj_delete, cnpj_view, cnpj_validacao
from .views import atividade_list, atividade_create, atividade_update, atividade_view, atividade_delete
from .views import pais_list, pais_create, pais_update, pais_view, pais_delete
from .views import estado_list, estado_create, estado_update, estado_view, estado_delete
from .views import municipio_list, municipio_create, municipio_update, municipio_view, municipio_delete
from .views import bairro_list, bairro_create, bairro_update, bairro_view, bairro_delete
from .views import area_list, area_create, area_update, area_view, area_delete
from .views import subatividade_list, subatividade_create, subatividade_update, subatividade_view, subatividade_delete
from .views import escolaridade_list, escolaridade_create, escolaridade_update, escolaridade_view, escolaridade_delete
from .views import formacao_list, formacao_create, formacao_update, formacao_view, formacao_delete
from .views import natureza_list, natureza_create, natureza_update, natureza_view, natureza_delete
from .views import conselho_list, conselho_create, conselho_update, conselho_view, conselho_delete
from .views import entidade_list, entidade_create, entidade_update, entidade_view, entidade_delete
from .views import cpf_liberal, cpf_liberal_validacao, cpf_liberal_create, cpf_liberal_view, cpf_liberal_update, cpf_liberal_delete
from .views import cpf_autonomo, cpf_autonomo_validacao, cpf_autonomo_create, cpf_autonomo_view, cpf_autonomo_update, cpf_autonomo_delete
from .views import entsub_list, entsub_create, entsub_delete, entresp_list, entresp_create, entresp_delete, cpf_responsavel_create, cpf_responsavel_update
from .views import entsub_liberal_list, entsub_liberal_create, entsub_liberal_delete
from .views import entsub_autonomo_list, entsub_autonomo_create, entsub_autonomo_delete
from .views import entresptec_list, entresptec_create, entresptec_delete, cpf_responsaveltec_create, cpf_responsaveltec_update, entresptec_vincula_atvs
from .views import unid_list, unid_create, unid_update, unid_delete, unid_view
from .views import unid_liberal_list, unid_liberal_create, unid_liberal_update, unid_liberal_delete, unid_liberal_view
from .views import unid_autonomo_list, unid_autonomo_create, unid_autonomo_update, unid_autonomo_delete, unid_autonomo_view
from .views import terceirizada_list, terceirizada_create, cnpj_terceirizada_create, terceirizada_vincula_atvs
from .views import cnpj_terceirizada_update, terceirizada_delete
from .views import areaproducao_list, areaproducao_create, areaproducao_update, areaproducao_view, areaproducao_delete
from .views import classeproducao_list, classeproducao_create, classeproducao_update, classeproducao_view, classeproducao_delete
from .views import linhaproducao_list, linhaproducao_create, linhaproducao_update, linhaproducao_view, linhaproducao_delete
from .views import formaproducao_list, formaproducao_create, formaproducao_update, formaproducao_view, formaproducao_delete
from .views import ent_linha_producao_list, ent_forma_producao_create, ent_classe_producao_create
from .views import ent_forma_producao_delete, ent_classe_producao_delete



urlpatterns = [
    path('devisa', devisa, name="devisa"),

    path('ent_linha_producao_list/<int:id>', ent_linha_producao_list, name="ent_linha_producao_list"),
    path('ent_forma_producao_create/<int:id>', ent_forma_producao_create, name="ent_forma_producao_create"),
    path('ent_classe_producao_create/<int:id>', ent_classe_producao_create, name="ent_classe_producao_create"),
    path('ent_forma_producao_delete/<int:id>', ent_forma_producao_delete, name="ent_forma_producao_delete"),
    path('ent_classe_producao_delete/<int:id>', ent_classe_producao_delete, name="ent_classe_producao_delete"),

    path('formaproducao_list', formaproducao_list, name="formaproducao_list"),
    path('formaproducao_view/<int:id>', formaproducao_view, name="formaproducao_view"),
    path('formaproducao_create', formaproducao_create, name="formaproducao_create"),
    path('formaproducao_update/<int:id>', formaproducao_update, name="formaproducao_update"),
    path('formaproducao_delete/<int:id>', formaproducao_delete, name="formaproducao_delete"),

    path('linhaproducao_list', linhaproducao_list, name="linhaproducao_list"),
    path('linhaproducao_view/<int:id>', linhaproducao_view, name="linhaproducao_view"),
    path('linhaproducao_create', linhaproducao_create, name="linhaproducao_create"),
    path('linhaproducao_update/<int:id>', linhaproducao_update, name="linhaproducao_update"),
    path('linhaproducao_delete/<int:id>', linhaproducao_delete, name="linhaproducao_delete"),

    path('classeproducao_list', classeproducao_list, name="classeproducao_list"),
    path('classeproducao_view/<int:id>', classeproducao_view, name="classeproducao_view"),
    path('classeproducao_create', classeproducao_create, name="classeproducao_create"),
    path('classeproducao_update/<int:id>', classeproducao_update, name="classeproducao_update"),
    path('classeproducao_delete/<int:id>', classeproducao_delete, name="classeproducao_delete"),

    path('areaproducao_list', areaproducao_list, name="areaproducao_list"),
    path('areaproducao_view/<int:id>', areaproducao_view, name="areaproducao_view"),
    path('areaproducao_create', areaproducao_create, name="areaproducao_create"),
    path('areaproducao_update/<int:id>', areaproducao_update, name="areaproducao_update"),
    path('areaproducao_delete/<int:id>', areaproducao_delete, name="areaproducao_delete"),

    path('terceirizada_list/<int:id>', terceirizada_list, name="terceirizada_list"),
    path('terceirizada_create/<int:id>', terceirizada_create, name="terceirizada_create"),
    path('terceirizada_delete/<int:id>', terceirizada_delete, name="terceirizada_delete"),
    path('cnpj_terceirizada_create/<int:id>/<str:cnpj>', cnpj_terceirizada_create, name="cnpj_terceirizada_create"),
    path('cnpj_terceirizada_update/<int:id>/<int:terc_id>', cnpj_terceirizada_update, name="cnpj_terceirizada_update"),
    path('terceirizada_vincula_atvs/<int:id>/<int:terc_id>', terceirizada_vincula_atvs, name="terceirizada_vincula_atvs"),

    path('unid_list/<int:id>', unid_list, name="unid_list"),
    path('unid_liberal_list/<int:id>', unid_liberal_list, name="unid_liberal_list"),
    path('unid_autonomo_list/<int:id>', unid_autonomo_list, name="unid_autonomo_list"),
    path('unid_create/<int:id>', unid_create, name="unid_create"),
    path('unid_liberal_create/<int:id>', unid_liberal_create, name="unid_liberal_create"),
    path('unid_autonomo_create/<int:id>', unid_autonomo_create, name="unid_autonomo_create"),
    path('unid_update/<int:id>', unid_update, name="unid_update"),
    path('unid_liberal_update/<int:id>', unid_liberal_update, name="unid_liberal_update"),
    path('unid_autonomo_update/<int:id>', unid_autonomo_update, name="unid_autonomo_update"),
    path('unid_delete/<int:id>', unid_delete, name="unid_delete"),
    path('unid_liberal_delete/<int:id>', unid_liberal_delete, name="unid_liberal_delete"),
    path('unid_autonomo_delete/<int:id>', unid_autonomo_delete, name="unid_autonomo_delete"),
    path('unid_view/<int:id>', unid_view, name="unid_view"),
    path('unid_liberal_view/<int:id>', unid_liberal_view, name="unid_liberal_view"),
    path('unid_autonomo_view/<int:id>', unid_autonomo_view, name="unid_autonomo_view"),


    path('entresptec_list/<int:id>', entresptec_list, name="entresptec_list"),
    path('entresptec_create/<int:id>', entresptec_create, name="entresptec_create"),
    path('entresptec_delete/<int:id>', entresptec_delete, name="entresptec_delete"),
    path('cpf_responsaveltec_create/<int:id>/<str:cpf>', cpf_responsaveltec_create, name="cpf_responsaveltec_create"),
    path('cpf_responsaveltec_update/<int:id>/<int:resp>', cpf_responsaveltec_update, name="cpf_responsaveltec_update"),
    path('entresptec_vincula_atvs/<int:id>/<str:cpf>', entresptec_vincula_atvs, name="entresptec_vincula_atvs"),

    path('entsub_list/<int:id>', entsub_list, name="entsub_list"),
    path('entsub_liberal_list/<int:id>', entsub_liberal_list, name="entsub_liberal_list"),
    path('entsub_autonomo_list/<int:id>', entsub_autonomo_list, name="entsub_autonomo_list"),
    path('entsub_create/<int:id>', entsub_create, name="entsub_create"),
    path('entsub_liberal_create/<int:id>', entsub_liberal_create, name="entsub_liberal_create"),
    path('entsub_autonomo_create/<int:id>', entsub_autonomo_create, name="entsub_autonomo_create"),
    path('entsub_delete/<int:id>', entsub_delete, name="entsub_delete"),
    path('entsub_liberal_delete/<int:id>', entsub_liberal_delete, name="entsub_liberal_delete"),
    path('entsub_autonomo_delete/<int:id>', entsub_autonomo_delete, name="entsub_autonomo_delete"),

    path('entresp_list/<int:id>', entresp_list, name="entresp_list"),
    path('entresp_create/<int:id>', entresp_create, name="entresp_create"),
    path('entresp_delete/<int:id>/<int:estab>', entresp_delete, name="entresp_delete"),
    path('cpf_responsavel_create/<int:id>/<str:cpf>', cpf_responsavel_create, name="cpf_responsavel_create"),
    path('cpf_responsavel_update/<int:id>/<int:resp>', cpf_responsavel_update, name="cpf_responsavel_update"),


    path('cpf_liberal', cpf_liberal, name="cpf_liberal"),
    path('cpf_liberal_validacao', cpf_liberal_validacao, name="cpf_liberal_validacao"),
    path('cpf_liberal_create/<str:cpf>', cpf_liberal_create, name="cpf_liberal_create"),
    path('cpf_liberal_view/<int:id>', cpf_liberal_view, name="cpf_liberal_view"),
    path('cpf_liberal_update/<int:id>', cpf_liberal_update, name="cpf_liberal_update"),
    path('cpf_liberal_delete/<int:id>', cpf_liberal_delete, name="cpf_liberal_delete"),

    path('cpf_autonomo', cpf_autonomo, name="cpf_autonomo"),
    path('cpf_autonomo_validacao', cpf_autonomo_validacao, name="cpf_autonomo_validacao"),
    path('cpf_autonomo_create/<str:cpf>', cpf_autonomo_create, name="cpf_autonomo_create"),
    path('cpf_autonomo_view/<int:id>', cpf_autonomo_view, name="cpf_autonomo_view"),
    path('cpf_autonomo_update/<int:id>', cpf_autonomo_update, name="cpf_autonomo_update"),
    path('cpf_autonomo_delete/<int:id>', cpf_autonomo_delete, name="cpf_autonomo_delete"),

    path('cnpj', cnpj, name="cnpj"),
    path('cnpj_view/<int:id>', cnpj_view, name="cnpj_view"),
    path('cnpj_create/<str:cnpj>', cnpj_create, name="cnpj_create"),
    path('cnpj_update/<int:id>', cnpj_update, name="cnpj_update"),
    path('cnpj_delete/<int:id>', cnpj_delete, name="cnpj_delete"),
    path('cnpj_validacao', cnpj_validacao, name="cnpj_validacao"),

    path('atividade_list', atividade_list, name="atividade_list"),
    path('atividade_view/<int:id>', atividade_view, name="atividade_view"),
    path('atividade_create', atividade_create, name="atividade_create"),
    path('atividade_update/<int:id>', atividade_update, name="atividade_update"),
    path('atividade_delete/<int:id>', atividade_delete, name="atividade_delete"),

    path('pais_list', pais_list, name="pais_list"),
    path('pais_view/<int:id>', pais_view, name="pais_view"),
    path('pais_create', pais_create, name="pais_create"),
    path('pais_update/<int:id>', pais_update, name="pais_update"),
    path('pais_delete/<int:id>', pais_delete, name="pais_delete"),

    path('estado_list', estado_list, name="estado_list"),
    path('estado_view/<int:id>', estado_view, name="estado_view"),
    path('estado_create', estado_create, name="estado_create"),
    path('estado_update/<int:id>', estado_update, name="estado_update"),
    path('estado_delete/<int:id>', estado_delete, name="estado_delete"),

    path('municipio_list', municipio_list, name="municipio_list"),
    path('municipio_view/<int:id>', municipio_view, name="municipio_view"),
    path('municipio_create', municipio_create, name="municipio_create"),
    path('municipio_update/<int:id>', municipio_update, name="municipio_update"),
    path('municipio_delete/<int:id>', municipio_delete, name="municipio_delete"),

    path('bairro_list', bairro_list, name="bairro_list"),
    path('bairro_view/<int:id>', bairro_view, name="bairro_view"),
    path('bairro_create', bairro_create, name="bairro_create"),
    path('bairro_update/<int:id>', bairro_update, name="bairro_update"),
    path('bairro_delete/<int:id>', bairro_delete, name="bairro_delete"),

    path('area_list', area_list, name="area_list"),
    path('area_view/<int:id>', area_view, name="area_view"),
    path('area_create', area_create, name="area_create"),
    path('area_update/<int:id>', area_update, name="area_update"),
    path('area_delete/<int:id>', area_delete, name="area_delete"),

    path('subatividade_list', subatividade_list, name="subatividade_list"),
    path('subatividade_view/<int:id>', subatividade_view, name="subatividade_view"),
    path('subatividade_create', subatividade_create, name="subatividade_create"),
    path('subatividade_update/<int:id>', subatividade_update, name="subatividade_update"),
    path('subatividade_delete/<int:id>', subatividade_delete, name="subatividade_delete"),

    path('escolaridade_list', escolaridade_list, name="escolaridade_list"),
    path('escolaridade_view/<int:id>', escolaridade_view, name="escolaridade_view"),
    path('escolaridade_create', escolaridade_create, name="escolaridade_create"),
    path('escolaridade_update/<int:id>', escolaridade_update, name="escolaridade_update"),
    path('escolaridade_delete/<int:id>', escolaridade_delete, name="escolaridade_delete"),

    path('formacao_list', formacao_list, name="formacao_list"),
    path('formacao_view/<int:id>', formacao_view, name="formacao_view"),
    path('formacao_create', formacao_create, name="formacao_create"),
    path('formacao_update/<int:id>', formacao_update, name="formacao_update"),
    path('formacao_delete/<int:id>', formacao_delete, name="formacao_delete"),

    path('natureza_list', natureza_list, name="natureza_list"),
    path('natureza_view/<int:id>', natureza_view, name="natureza_view"),
    path('natureza_create', natureza_create, name="natureza_create"),
    path('natureza_update/<int:id>', natureza_update, name="natureza_update"),
    path('natureza_delete/<int:id>', natureza_delete, name="natureza_delete"),

    path('conselho_list', conselho_list, name="conselho_list"),
    path('conselho_view/<int:id>', conselho_view, name="conselho_view"),
    path('conselho_create', conselho_create, name="conselho_create"),
    path('conselho_update/<int:id>', conselho_update, name="conselho_update"),
    path('conselho_delete/<int:id>', conselho_delete, name="conselho_delete"),

    path('entidade_list', entidade_list, name="entidade_list"),
    path('entidade_view/<int:id>', entidade_view, name="entidade_view"),
    path('entidade_create', entidade_create, name="entidade_create"),
    path('entidade_update/<int:id>', entidade_update, name="entidade_update"),
    path('entidade_delete/<int:id>', entidade_delete, name="entidade_delete")

]