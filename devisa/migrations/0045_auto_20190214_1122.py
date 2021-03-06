# Generated by Django 2.1.4 on 2019-02-14 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('devisa', '0044_entidadeclasseproducao'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='area',
            options={'permissions': (('area_list', 'Pode listar áreas'), ('area_create', 'Pode cadastrar área'), ('area_update', 'Pode editar área'), ('area_view', 'Pode ver área'), ('area_delete', 'Pode deletar área'))},
        ),
        migrations.AlterModelOptions(
            name='areaproducao',
            options={'permissions': (('area_producao_list', 'Pode listar áreas de produção'), ('area_producao_create', 'Pode cadastrar área de produção'), ('area_producao_update', 'Pode editar área de produção'), ('area_producao_view', 'Pode ver área de produção'), ('area_producao_delete', 'Pode excluir área de produção'))},
        ),
        migrations.AlterModelOptions(
            name='atividade',
            options={'permissions': (('atividade_list', 'Pode listar atividades'), ('atividade_create', 'Pode cadastrar atividade'), ('atividade_update', 'Pode editar atividade'), ('atividade_view', 'Pode ver atividade'), ('atividade_delete', 'Pode deletar atividade'))},
        ),
        migrations.AlterModelOptions(
            name='bairro',
            options={'permissions': (('bairro_list', 'Pode listar bairros'), ('bairro_create', 'Pode cadastrar bairro'), ('bairro_update', 'Pode editar bairro'), ('bairro_view', 'Pode ver bairro'), ('bairro_delete', 'Pode excluir bairro'))},
        ),
        migrations.AlterModelOptions(
            name='classeproducao',
            options={'permissions': (('classe_producao_list', 'Pode listar classes de produção'), ('classe_producao_create', 'Pode cadastrar classe de produção'), ('classe_producao_update', 'Pode editar classe de produção'), ('classe_producao_view', 'Pode ver classe de produção'), ('classe_producao_delete', 'Pode excluir classe de produção'))},
        ),
        migrations.AlterModelOptions(
            name='conselho',
            options={'permissions': (('conselho_list', 'Pode listar conselhos'), ('conselho_create', 'Pode cadastrar conselho'), ('conselho_update', 'Pode editar conselho'), ('conselho_view', 'Pode ver conselho'), ('conselho_delete', 'Pode excluir conselho'))},
        ),
        migrations.AlterModelOptions(
            name='entidade',
            options={'permissions': (('entidade_list', 'Pode listar entidades'), ('entidade_create', 'Pode cadastrar entidade'), ('entidade_update', 'Pode editar entidade'), ('entidade_view', 'Pode ver entidade'), ('entidade_delete', 'Pode excluir entidade'), ('cpf_autonomo', 'Pode listar profissionais autônomos'), ('cpf_autonomo_validacao', 'Pode validar CPF de profissional autônomo'), ('cpf_autonomo_create', 'Pode cadastrar profissional autônomo'), ('cpf_autonomo_update', 'Pode editar profissional autônomo'), ('cpf_autonomo_view', 'Pode ver profissional autônomo'), ('cpf_autonomo_delete', 'Pode excluir profissional autônomo'), ('cpf_liberal', 'Pode listar profissionais liberais'), ('cpf_liberal_validacao', 'Pode validar CPF de profissional liberal'), ('cpf_liberal_create', 'Pode cadastrar profissional liberal'), ('cpf_liberal_update', 'Pode editar profissional liberal'), ('cpf_liberal_view', 'Pode ver profissional liberal'), ('cpf_liberal_delete', 'Pode excluir profissional liberal'), ('cnpj', 'Pode listar estabelecimentos'), ('cnpj_validacao', 'Pode validar CNPJ de estabelecimento'), ('cnpj_create', 'Pode cadastrar estabelecimento'), ('cnpj_update', 'Pode editar estabelecimento'), ('cnpj_view', 'Pode ver estabelecimento'), ('cnpj_delete', 'Pode excluir estabelecimento'))},
        ),
        migrations.AlterModelOptions(
            name='entidadeclasseproducao',
            options={'permissions': (('ent_classe_producao_create', 'Pode vincular classe de produção'), ('ent_classe_producao_delete', 'Pode desvincular classe de produção'))},
        ),
        migrations.AlterModelOptions(
            name='entidadeformaproducao',
            options={'permissions': (('ent_linha_producao_list', 'Pode ver formas/classes de produção do estabelecimento'), ('ent_forma_producao_create', 'Pode vincular forma de produção'), ('ent_forma_producao_delete', 'Pode desvincular forma de produção'))},
        ),
        migrations.AlterModelOptions(
            name='entidaderesponsavel',
            options={'permissions': (('entresp_list', 'Pode listar responsáveis legais do estabelecimento'), ('entresp_create', 'Pode validar o CPF do responsável legal'), ('cpf_responsavel_create', 'Pode cadastrar responsável legal do estabelecimento'), ('cpf_responsavel_update', 'Pode editar responsável legal do estabelecimento'), ('entresp_delete', 'Pode excluir responsável legal do estabelecimento'))},
        ),
        migrations.AlterModelOptions(
            name='entidadesubatividade',
            options={'permissions': (('entsub_list', 'Pode listar atividades do estabelecimento'), ('entsub_liberal_list', 'Pode listar atividades do profissional liberal'), ('entsub_autonomo_list', 'Pode listar atividades do profissional autônomo'), ('entsub_create', 'Pode vincular atividades ao estabelecimento'), ('entsub_liberal_create', 'Pode vincular atividades ao profissional liberal'), ('entsub_autonomo_create', 'Pode vincular atividades ao profissional autônomo'), ('entsub_delete', 'Pode desvincular atividades do estabelecimento'), ('entsub_liberal_delete', 'Pode desvincular atividades do profissional liberal'), ('entsub_autonomo_delete', 'Pode desvincular atividades do profissional autônomo'), ('entresptec_list', 'Pode listar responsáveis técnicos'), ('entresptec_create', 'Pode validar o CPF do responsável técnico'), ('cpf_responsaveltec_create', 'Pode cadastrar responsável técnico'), ('cpf_responsaveltec_update', 'Pode editar responsável técnico'), ('entresptec_vincula_atvs', 'Pode vincular responsável técnico às atividades do estabelecimento'), ('entresptec_delete', 'Pode excluir responsável técnico'), ('terceirizada_list', 'Pode listar atividades terceirizadas do estabelecimento'), ('terceirizada_create', 'Pode validar o CNPJ da empresa terceirizada'), ('cnpj_terceirizada_create', 'Pode cadastrar empresa terceirizada'), ('cnpj_terceirizada_update', 'Pode editar empresa terceirizada'), ('terceirizada_vincula_atvs', 'Pode vincular empresa terceirizada às atividades do estabelecimento'), ('terceirizada_delete', 'Pode retirar terceirzação de atividade'))},
        ),
        migrations.AlterModelOptions(
            name='entidadeunidade',
            options={'permissions': (('unid_list', 'Pode listar unidades do estabelecimento'), ('unid_create', 'Pode cadastrar unidade do estabelecimento'), ('unid_update', 'Pode editar unidade do estabelecimento'), ('unid_view', 'Pode ver unidade do estabelecimento'), ('unid_delete', 'Pode excluir unidade do estabelecimento'), ('unid_liberal_list', 'Pode listar unidades do profissional liberal'), ('unid_liberal_create', 'Pode cadastrar unidade do profissional liberal'), ('unid_liberal_update', 'Pode editar unidade do profissional liberal'), ('unid_liberal_view', 'Pode ver unidade do profissional liberal'), ('unid_liberal_delete', 'Pode excluir unidade do profissional liberal'), ('unid_autonomo_list', 'Pode listar unidades do profissional autônomo'), ('unid_autonomo_create', 'Pode cadastrar unidade do profissional autônomo'), ('unid_autonomo_update', 'Pode editar unidade do profissional autônomo'), ('unid_autonomo_view', 'Pode ver unidade do profissional autônomo'), ('unid_autonomo_delete', 'Pode excluir unidade do profissional autônomo'))},
        ),
        migrations.AlterModelOptions(
            name='escolaridade',
            options={'permissions': (('escolaridade_list', 'Pode listar escolaridades'), ('escolaridade_create', 'Pode cadastrar escolaridade'), ('escolaridade_update', 'Pode editar escolaridade'), ('escolaridade_view', 'Pode ver escolaridade'), ('escolaridade_delete', 'Pode excluir escolaridade'))},
        ),
        migrations.AlterModelOptions(
            name='estado',
            options={'permissions': (('estado_list', 'Pode listar estados'), ('estado_create', 'Pode cadastrar estado'), ('estado_update', 'Pode editar estado'), ('estado_view', 'Pode ver estado'), ('estado_delete', 'Pode excluir estado'))},
        ),
        migrations.AlterModelOptions(
            name='formacao',
            options={'permissions': (('formacao_list', 'Pode listar formações'), ('formacao_create', 'Pode cadastrar formação'), ('formacao_update', 'Pode editar formação'), ('formacao_view', 'Pode ver formação'), ('formacao_delete', 'Pode excluir formação'))},
        ),
        migrations.AlterModelOptions(
            name='formaproducao',
            options={'permissions': (('forma_producao_list', 'Pode listar formas de produção'), ('forma_producao_create', 'Pode cadastrar forma de produção'), ('forma_producao_update', 'Pode editar forma de produção'), ('forma_producao_view', 'Pode ver forma de produção'), ('forma_producao_delete', 'Pode excluir forma de produção'))},
        ),
        migrations.AlterModelOptions(
            name='linhaproducao',
            options={'permissions': (('linha_producao_list', 'Pode listar linhas de produção'), ('linha_producao_create', 'Pode cadastrar linha de produção'), ('linha_producao_update', 'Pode editar linha de produção'), ('linha_producao_view', 'Pode ver linha de produção'), ('linha_producao_delete', 'Pode excluir linha de produção'))},
        ),
        migrations.AlterModelOptions(
            name='municipio',
            options={'permissions': (('municipio_list', 'Pode listar municípios'), ('municipio_create', 'Pode cadastrar município'), ('municipio_update', 'Pode editar município'), ('municipio_view', 'Pode ver município'), ('municipio_delete', 'Pode excluir município'))},
        ),
        migrations.AlterModelOptions(
            name='natureza',
            options={'permissions': (('natureza_list', 'Pode listar naturezas jurídicas / dependências administrativas'), ('natureza_create', 'Pode cadastrar natureza jurídica / dependência administrativa'), ('natureza_update', 'Pode editar natureza jurídica / dependência administrativa'), ('natureza_view', 'Pode ver natureza jurídica / dependência administrativa'), ('natureza_delete', 'Pode excluir natureza jurídica / dependência administrativa'))},
        ),
        migrations.AlterModelOptions(
            name='pais',
            options={'permissions': (('pais_list', 'Pode listar países'), ('pais_create', 'Pode cadastrar país'), ('pais_update', 'Pode editar país'), ('pais_view', 'Pode ver país'), ('pais_delete', 'Pode excluir país'))},
        ),
        migrations.AlterModelOptions(
            name='subatividade',
            options={'permissions': (('subatividade_list', 'Pode listar subatividades'), ('subatividade_create', 'Pode cadastrar subatividade'), ('subatividade_update', 'Pode editar subatividade'), ('subatividade_view', 'Pode ver subatividade'), ('subatividade_delete', 'Pode deletar subatividade'))},
        ),
        migrations.AlterField(
            model_name='entidade',
            name='bairro',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='devisa.Bairro'),
        ),
        migrations.AlterField(
            model_name='entidade',
            name='conselho',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.PROTECT, to='devisa.Conselho'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='entidade',
            name='escolaridade',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.PROTECT, to='devisa.Escolaridade'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='entidade',
            name='formacao_profissional',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.PROTECT, to='devisa.Formacao'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='entidade',
            name='municipio',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.PROTECT, to='devisa.Municipio'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='entidade',
            name='natureza_juridica_dependencia',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.PROTECT, to='devisa.Natureza'),
            preserve_default=False,
        ),
    ]
