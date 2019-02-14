from django.db import models


# Create your models here.
class Pais(models.Model):
    pais_nome = models.CharField(verbose_name='País', max_length=100)

    class Meta:
        permissions = (
            ('pais_list', 'Pode listar países'),
            ('pais_create', 'Pode cadastrar país'),
            ('pais_update', 'Pode editar país'),
            ('pais_view', 'Pode ver país'),
            ('pais_delete', 'Pode excluir país')
        )

    def __str__(self):
        return self.pais_nome


class Estado(models.Model):
    est_nome = models.CharField(verbose_name='Estado', max_length=100)
    pais = models.ForeignKey(Pais,on_delete=models.PROTECT)

    class Meta:
        permissions = (
            ('estado_list', 'Pode listar estados'),
            ('estado_create', 'Pode cadastrar estado'),
            ('estado_update', 'Pode editar estado'),
            ('estado_view', 'Pode ver estado'),
            ('estado_delete', 'Pode excluir estado')
        )

    def __str__(self):
        return self.est_nome


class Municipio(models.Model):
    mun_nome = models.CharField(verbose_name='municipio', max_length=100)
    estado = models.ForeignKey(Estado, on_delete=models.PROTECT)

    class Meta:
        permissions = (
            ('municipio_list', 'Pode listar municípios'),
            ('municipio_create', 'Pode cadastrar município'),
            ('municipio_update', 'Pode editar município'),
            ('municipio_view', 'Pode ver município'),
            ('municipio_delete', 'Pode excluir município')
        )

    def __str__(self):
        return self.mun_nome


class Bairro(models.Model):
    bairro_nome = models.CharField(verbose_name='bairro', max_length=100)
    municipio = models.ForeignKey(Municipio, on_delete=models.PROTECT)

    class Meta:
        permissions = (
            ('bairro_list', 'Pode listar bairros'),
            ('bairro_create', 'Pode cadastrar bairro'),
            ('bairro_update', 'Pode editar bairro'),
            ('bairro_view', 'Pode ver bairro'),
            ('bairro_delete', 'Pode excluir bairro')
        )

    def __str__(self):
        return self.bairro_nome


class Natureza(models.Model):
    nat_nome = models.CharField(verbose_name='natureza Jurídica / Dependência Administrativa', max_length=100)
    nat_descricao = models.CharField(verbose_name='Descrição', max_length=200)

    class Meta:
        permissions = (
            ('natureza_list', 'Pode listar naturezas jurídicas / dependências administrativas'),
            ('natureza_create', 'Pode cadastrar natureza jurídica / dependência administrativa'),
            ('natureza_update', 'Pode editar natureza jurídica / dependência administrativa'),
            ('natureza_view', 'Pode ver natureza jurídica / dependência administrativa'),
            ('natureza_delete', 'Pode excluir natureza jurídica / dependência administrativa')
        )

    def __str__(self):
        return self.nat_nome


class Escolaridade(models.Model):
    esc_nome = models.CharField(verbose_name='Nome', max_length=100)
    esc_descricao = models.CharField(verbose_name='Descrição', max_length=200)

    class Meta:
        permissions = (
            ('escolaridade_list', 'Pode listar escolaridades'),
            ('escolaridade_create', 'Pode cadastrar escolaridade'),
            ('escolaridade_update', 'Pode editar escolaridade'),
            ('escolaridade_view', 'Pode ver escolaridade'),
            ('escolaridade_delete', 'Pode excluir escolaridade')
        )

    def __str__(self):
        return self.esc_nome


class Formacao(models.Model):
    for_nome = models.CharField(verbose_name='Nome', max_length=100)
    escolaridade = models.ForeignKey(Escolaridade, on_delete=models.PROTECT)

    class Meta:
        permissions = (
            ('formacao_list', 'Pode listar formações'),
            ('formacao_create', 'Pode cadastrar formação'),
            ('formacao_update', 'Pode editar formação'),
            ('formacao_view', 'Pode ver formação'),
            ('formacao_delete', 'Pode excluir formação')
        )

    def __str__(self):
        return self.for_nome


class Conselho(models.Model):
    con_nome = models.CharField(verbose_name='Nome', max_length=100)
    con_sigla = models.CharField(verbose_name='Sigla', max_length=100)

    class Meta:
        permissions = (
            ('conselho_list', 'Pode listar conselhos'),
            ('conselho_create', 'Pode cadastrar conselho'),
            ('conselho_update', 'Pode editar conselho'),
            ('conselho_view', 'Pode ver conselho'),
            ('conselho_delete', 'Pode excluir conselho')
        )

    def __str__(self):
        return self.con_sigla



class Entidade(models.Model):
    ent_tipo_entidade = models.CharField(verbose_name='tipo de entidade', max_length=2, default=1)  # required
    ent_cpf = models.CharField(verbose_name='CPF', max_length=20, null=True, default='', blank=True)
    ent_cnpj = models.CharField(verbose_name='CNPJ', max_length=30, null=True, default='', blank=True)
    ent_nome_razao = models.CharField(verbose_name='nome / Razão Social', max_length=300)  # required
    ent_fantasia = models.CharField(verbose_name='nome Fantasia', max_length=200, blank=True, default='', null=True)
    ent_insc_estadual = models.CharField(verbose_name='Inscrição Estadual', max_length=100, blank=True, default='',
                                         null=True)
    ent_insc_municipal = models.CharField(verbose_name='Inscrição Municipal', max_length=100, blank=True, default='',
                                          null=True)
    ent_cnes = models.CharField(verbose_name='CNES (Estabelecimentos de Saúde)', max_length=100, blank=True, default='',
                                null=True)
    ent_cep = models.CharField(verbose_name='CEP', max_length=20, blank=True, default='', null=False)
    ent_complemento = models.CharField(verbose_name='Complemento', max_length=300, blank=True, default='', null=True)
    ent_endereco = models.CharField(verbose_name='Endereço', max_length=300, blank=True, default='', null=False)
    ent_numero = models.CharField(verbose_name='Endereço', max_length=6, blank=True, default='', null=False)
    ent_fone = models.CharField(verbose_name='Telefone', max_length=20, blank=True, default='', null=True)
    ent_fax = models.CharField(verbose_name='Fax', max_length=20, blank=True, default='', null=True)
    ent_email = models.CharField(verbose_name='E-mail', max_length=200, blank=True, default='', null=True)
    ent_dt_inicio_func = models.CharField(verbose_name='Data de Início do Funcionamento', max_length=20, blank=True,
                                          default='', null=False)
    ent_pasta_num = models.CharField(verbose_name='Número da Pasta', max_length=200, blank=True, default='', null=True)
    ent_obj_contrato_social = models.CharField(verbose_name='Objetivo Contrato Social', max_length=500, blank=True,
                                               default='', null=True)
    ent_observacoes = models.CharField(verbose_name='Observações', max_length=500, blank=True, default='', null=True)
    ent_rg = models.CharField(verbose_name='RG', max_length=20, blank=True, default='', null=True)
    ent_orgao_exp = models.CharField(verbose_name='Órgão Expedidor', max_length=100, blank=True, default='', null=True)
    ent_dt_expedicao = models.CharField(verbose_name='Data de Expedição', max_length=20, blank=True, default='',
                                        null=True)
    ent_registro_conselho = models.CharField(verbose_name='Registro no Conselho', max_length=100, blank=True, default=''
                                             , null=True)
    ent_especializacao = models.CharField(verbose_name='Especialização', max_length=200, blank=True, default='',
                                          null=True)
    municipio = models.ForeignKey(Municipio, on_delete=models.SET_NULL, blank=True, null=True)
    bairro = models.ForeignKey(Bairro, on_delete=models.SET_NULL, blank=True, null=True)
    natureza_juridica_dependencia = models.ForeignKey(Natureza, on_delete=models.SET_NULL, blank=True, null=True)
    escolaridade = models.ForeignKey(Escolaridade, on_delete=models.SET_NULL, blank=True, null=True)
    formacao_profissional = models.ForeignKey(Formacao, on_delete=models.SET_NULL, blank=True, null=True)
    conselho = models.ForeignKey(Conselho, on_delete=models.SET_NULL, blank=True, null=True)
    uf_conselho = models.CharField(verbose_name='UF', max_length=2, blank=True)

    class Meta:
        permissions = (
            ('entidade_list', 'Pode listar entidades'),
            ('entidade_create', 'Pode cadastrar entidade'),
            ('entidade_update', 'Pode editar entidade'),
            ('entidade_view', 'Pode ver entidade'),
            ('entidade_delete', 'Pode excluir entidade'),

            ('cpf_autonomo', 'Pode listar profissionais autônomos'),
            ('cpf_autonomo_validacao', 'Pode validar CPF de profissional autônomo'),
            ('cpf_autonomo_create', 'Pode cadastrar profissional autônomo'),
            ('cpf_autonomo_update', 'Pode editar profissional autônomo'),
            ('cpf_autonomo_view', 'Pode ver profissional autônomo'),
            ('cpf_autonomo_delete', 'Pode excluir profissional autônomo'),

            ('cpf_liberal', 'Pode listar profissionais liberais'),
            ('cpf_liberal_validacao', 'Pode validar CPF de profissional liberal'),
            ('cpf_liberal_create', 'Pode cadastrar profissional liberal'),
            ('cpf_liberal_update', 'Pode editar profissional liberal'),
            ('cpf_liberal_view', 'Pode ver profissional liberal'),
            ('cpf_liberal_delete', 'Pode excluir profissional liberal'),

            ('cnpj', 'Pode listar estabelecimentos'),
            ('cnpj_validacao', 'Pode validar CNPJ de estabelecimento'),
            ('cnpj_create', 'Pode cadastrar estabelecimento'),
            ('cnpj_update', 'Pode editar estabelecimento'),
            ('cnpj_view', 'Pode ver estabelecimento'),
            ('cnpj_delete', 'Pode excluir estabelecimento')
        )

    def __str__(self):
        return self.ent_nome_razao


class Area(models.Model):
    area_nome = models.CharField(verbose_name='Nome', max_length=100)
    area_descricao = models.CharField(verbose_name='Descrição', max_length=200)

    class Meta:
        permissions = (
            ('area_list', 'Pode listar áreas'),
            ('area_create', 'Pode cadastrar área'),
            ('area_update', 'Pode editar área'),
            ('area_view', 'Pode ver área'),
            ('area_delete', 'Pode deletar área')
        )

    def __str__(self):
        return self.area_nome


class Atividade(models.Model):
    atv_nome = models.CharField(verbose_name='Nome', max_length=100)
    atv_descricao = models.CharField(verbose_name='Descrição', max_length=200)
    area = models.ForeignKey(Area, on_delete=models.PROTECT)

    class Meta:
        permissions = (
            ('atividade_list', 'Pode listar atividades'),
            ('atividade_create', 'Pode cadastrar atividade'),
            ('atividade_update', 'Pode editar atividade'),
            ('atividade_view', 'Pode ver atividade'),
            ('atividade_delete', 'Pode deletar atividade')
        )

    def __str__(self):
        return self.atv_nome


class Subatividade(models.Model):
    sub_nome = models.CharField(verbose_name='Nome', max_length=100)
    atividade = models.ForeignKey(Atividade, on_delete=models.PROTECT)
    entidades = models.ManyToManyField(Entidade)

    class Meta:
        permissions = (
            ('subatividade_list', 'Pode listar subatividades'),
            ('subatividade_create', 'Pode cadastrar subatividade'),
            ('subatividade_update', 'Pode editar subatividade'),
            ('subatividade_view', 'Pode ver subatividade'),
            ('subatividade_delete', 'Pode deletar subatividade')
        )

    def __str__(self):
        return self.sub_nome


class EntidadeSubatividade(models.Model):
    entidade = models.ForeignKey(Entidade, on_delete=models.PROTECT)
    subatividade = models.ForeignKey(Subatividade, on_delete=models.PROTECT, related_name='subatividade')
    responsavel_tecnico = models.ForeignKey(Entidade, on_delete=models.PROTECT, related_name='responsavel_tecnico', blank=True,
                                    default='', null=True)
    terceirizado = models.ForeignKey(Entidade, on_delete=models.PROTECT, related_name='terceirizado', blank=True, default='', null=True)

    class Meta:
        permissions = (
            ('entsub_list', 'Pode listar atividades do estabelecimento'),
            ('entsub_liberal_list', 'Pode listar atividades do profissional liberal'),
            ('entsub_autonomo_list', 'Pode listar atividades do profissional autônomo'),

            ('entsub_create', 'Pode vincular atividades ao estabelecimento'),
            ('entsub_liberal_create', 'Pode vincular atividades ao profissional liberal'),
            ('entsub_autonomo_create', 'Pode vincular atividades ao profissional autônomo'),

            ('entsub_delete', 'Pode desvincular atividades do estabelecimento'),
            ('entsub_liberal_delete', 'Pode desvincular atividades do profissional liberal'),
            ('entsub_autonomo_delete', 'Pode desvincular atividades do profissional autônomo'),

            ('entresptec_list', 'Pode listar responsáveis técnicos'),
            ('entresptec_create', 'Pode validar o CPF do responsável técnico'),
            ('cpf_responsaveltec_create', 'Pode cadastrar responsável técnico'),
            ('cpf_responsaveltec_update', 'Pode editar responsável técnico'),
            ('entresptec_vincula_atvs', 'Pode vincular responsável técnico às atividades do estabelecimento'),
            ('entresptec_delete', 'Pode excluir responsável técnico'),

            ('terceirizada_list', 'Pode listar atividades terceirizadas do estabelecimento'),
            ('terceirizada_create', 'Pode validar o CNPJ da empresa terceirizada'),
            ('cnpj_terceirizada_create', 'Pode cadastrar empresa terceirizada'),
            ('cnpj_terceirizada_update', 'Pode editar empresa terceirizada'),
            ('terceirizada_vincula_atvs', 'Pode vincular empresa terceirizada às atividades do estabelecimento'),
            ('terceirizada_delete', 'Pode retirar terceirzação de atividade')

        )

    def __str__(self):
        return self.self.subatividade



class EntidadeResponsavel(models.Model):
    entidade = models.ForeignKey(Entidade, related_name="entidade", on_delete=models.PROTECT)
    responsavel = models.ForeignKey(Entidade, related_name="responsavel", on_delete=models.PROTECT)

    class Meta:
        permissions = (
            ('entresp_list', 'Pode listar responsáveis legais do estabelecimento'),
            ('entresp_create', 'Pode validar o CPF do responsável legal'),
            ('cpf_responsavel_create', 'Pode cadastrar responsável legal do estabelecimento'),
            ('cpf_responsavel_update', 'Pode editar responsável legal do estabelecimento'),
            ('entresp_delete', 'Pode excluir responsável legal do estabelecimento')
        )

    def __str__(self):
        return self.entidade + ' / ' + self.responsavel


class EntidadeUnidade(models.Model):
    estabelecimento = models.ForeignKey(Entidade, related_name='estabelecimento', on_delete=models.PROTECT)
    unidade = models.ForeignKey(Entidade, related_name='unidade', on_delete=models.PROTECT)

    class Meta:
        permissions = (
            ('unid_list', 'Pode listar unidades do estabelecimento'),
            ('unid_create', 'Pode cadastrar unidade do estabelecimento'),
            ('unid_update', 'Pode editar unidade do estabelecimento'),
            ('unid_view', 'Pode ver unidade do estabelecimento'),
            ('unid_delete', 'Pode excluir unidade do estabelecimento'),

            ('unid_liberal_list', 'Pode listar unidades do profissional liberal'),
            ('unid_liberal_create', 'Pode cadastrar unidade do profissional liberal'),
            ('unid_liberal_update', 'Pode editar unidade do profissional liberal'),
            ('unid_liberal_view', 'Pode ver unidade do profissional liberal'),
            ('unid_liberal_delete', 'Pode excluir unidade do profissional liberal'),

            ('unid_autonomo_list', 'Pode listar unidades do profissional autônomo'),
            ('unid_autonomo_create', 'Pode cadastrar unidade do profissional autônomo'),
            ('unid_autonomo_update', 'Pode editar unidade do profissional autônomo'),
            ('unid_autonomo_view', 'Pode ver unidade do profissional autônomo'),
            ('unid_autonomo_delete', 'Pode excluir unidade do profissional autônomo')
        )

    def __str__(self):
        return self.estabelecimento


class Areaproducao(models.Model):
    ap_nome = models.CharField(verbose_name='nome', max_length=200, default='')
    ap_descricao = models.CharField(verbose_name='descrição', max_length=400, default='')

    class Meta:
        permissions = (
            ('area_producao_list', 'Pode listar áreas de produção'),
            ('area_producao_create', 'Pode cadastrar área de produção'),
            ('area_producao_update', 'Pode editar área de produção'),
            ('area_producao_view', 'Pode ver área de produção'),
            ('area_producao_delete', 'Pode excluir área de produção')
        )

    def __str__(self):
        return self.ap_nome


class Classeproducao(models.Model):
    cp_nome = models.CharField(verbose_name='nome', max_length=200, default='')
    cp_descricao = models.CharField(verbose_name='descrição', max_length=400, default='')
    area_producao = models.ForeignKey(Areaproducao, on_delete=models.PROTECT)

    class Meta:
        permissions = (
            ('classe_producao_list', 'Pode listar classes de produção'),
            ('classe_producao_create', 'Pode cadastrar classe de produção'),
            ('classe_producao_update', 'Pode editar classe de produção'),
            ('classe_producao_view', 'Pode ver classe de produção'),
            ('classe_producao_delete', 'Pode excluir classe de produção')
        )

    def __str__(self):
        return self.cp_nome


class Linhaproducao(models.Model):
    lp_nome = models.CharField(verbose_name='nome', max_length=200, default='')
    lp_descricao = models.CharField(verbose_name='descrição', max_length=400, default='')
    area_producao = models.ForeignKey(Areaproducao, on_delete=models.PROTECT)

    class Meta:
        permissions = (
            ('linha_producao_list', 'Pode listar linhas de produção'),
            ('linha_producao_create', 'Pode cadastrar linha de produção'),
            ('linha_producao_update', 'Pode editar linha de produção'),
            ('linha_producao_view', 'Pode ver linha de produção'),
            ('linha_producao_delete', 'Pode excluir linha de produção')
        )

    def __str__(self):
        return self.lp_nome


class Formaproducao(models.Model):
    fp_nome = models.CharField(verbose_name='nome', max_length=200, default='')
    fp_descricao = models.CharField(verbose_name='descrição', max_length=400, default='')
    linha_producao = models.ForeignKey(Linhaproducao, on_delete=models.PROTECT)

    class Meta:
        permissions = (
            ('forma_producao_list', 'Pode listar formas de produção'),
            ('forma_producao_create', 'Pode cadastrar forma de produção'),
            ('forma_producao_update', 'Pode editar forma de produção'),
            ('forma_producao_view', 'Pode ver forma de produção'),
            ('forma_producao_delete', 'Pode excluir forma de produção')
        )

    def __str__(self):
        return self.fp_nome


class EntidadeFormaproducao(models.Model):
    entidade = models.ForeignKey(Entidade, on_delete=models.PROTECT)
    forma_producao = models.ForeignKey(Formaproducao, on_delete=models.PROTECT, related_name='forma_producao')

    class Meta:
        permissions = (
            ('ent_linha_producao_list', 'Pode ver formas/classes de produção do estabelecimento'),
            ('ent_forma_producao_create', 'Pode vincular forma de produção'),
            ('ent_forma_producao_delete', 'Pode desvincular forma de produção')
        )

    def __str__(self):
        return self.forma_producao


class EntidadeClasseproducao(models.Model):
    entidade = models.ForeignKey(Entidade, on_delete=models.PROTECT)
    classe_producao = models.ForeignKey(Classeproducao, on_delete=models.PROTECT, related_name='classe_producao')

    class Meta:
        permissions = (
            ('ent_classe_producao_create', 'Pode vincular classe de produção'),
            ('ent_classe_producao_delete', 'Pode desvincular classe de produção')
        )

    def __str__(self):
        return self.classe_producao
