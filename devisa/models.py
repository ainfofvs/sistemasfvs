from django.db import models


# Create your models here.
class Pais(models.Model):
    pais_nome = models.CharField(verbose_name='País', max_length=100)

    class Meta:
        permissions = (
            ('pais_list', 'Pode listar país'),
            ('pais_create', 'Pode cadastrar país'),
            ('pais_update', 'Pode editar país'),
            ('pais_view', 'Pode ver país'),
            ('pais_delete', 'Pode deletar país')
        )

    def __str__(self):
        return self.pais_nome


class Estado(models.Model):
    est_nome = models.CharField(verbose_name='Estado', max_length=100)
    pais = models.ForeignKey(Pais,on_delete=models.PROTECT)

    class Meta:
        permissions = (
            ('estado_list', 'Pode listar estado'),
            ('estado_create', 'Pode cadastrar estado'),
            ('estado_update', 'Pode editar estado'),
            ('estado_view', 'Pode ver estado'),
            ('estado_delete', 'Pode deletar estado')
        )

    def __str__(self):
        return self.est_nome


class Municipio(models.Model):
    mun_nome = models.CharField(verbose_name='municipio', max_length=100)
    estado = models.ForeignKey(Estado, on_delete=models.PROTECT)

    class Meta:
        permissions = (
            ('municipio_list', 'Pode listar município'),
            ('municipio_create', 'Pode cadastrar município'),
            ('municipio_update', 'Pode editar município'),
            ('municipio_view', 'Pode ver município'),
            ('municipio_delete', 'Pode deletar município')
        )

    def __str__(self):
        return self.mun_nome


class Bairro(models.Model):
    bairro_nome = models.CharField(verbose_name='bairro', max_length=100)
    municipio = models.ForeignKey(Municipio, on_delete=models.PROTECT)

    class Meta:
        permissions = (
            ('bairro_list', 'Pode listar bairro'),
            ('bairro_create', 'Pode cadastrar bairro'),
            ('bairro_update', 'Pode editar bairro'),
            ('bairro_view', 'Pode ver bairro'),
            ('bairro_delete', 'Pode deletar bairro')
        )

    def __str__(self):
        return self.bairro_nome


class Natureza(models.Model):
    nat_nome = models.CharField(verbose_name='natureza Jurídica / Dependência Administrativa', max_length=100)
    nat_descricao = models.CharField(verbose_name='Descrição', max_length=200)

    class Meta:
        permissions = (
            ('natureza_list', 'Pode listar natureza'),
            ('natureza_create', 'Pode cadastrar natureza'),
            ('natureza_update', 'Pode editar natureza'),
            ('natureza_view', 'Pode ver natureza'),
            ('natureza_delete', 'Pode deletar natureza')
        )

    def __str__(self):
        return self.nat_nome


class Escolaridade(models.Model):
    esc_nome = models.CharField(verbose_name='Nome', max_length=100)
    esc_descricao = models.CharField(verbose_name='Descrição', max_length=200)

    class Meta:
        permissions = (
            ('escolaridade_list', 'Pode listar escolaridade'),
            ('escolaridade_create', 'Pode cadastrar escolaridade'),
            ('escolaridade_update', 'Pode editar escolaridade'),
            ('escolaridade_view', 'Pode ver escolaridade'),
            ('escolaridade_delete', 'Pode deletar escolaridade')
        )

    def __str__(self):
        return self.esc_nome


class Formacao(models.Model):
    for_nome = models.CharField(verbose_name='Nome', max_length=100)
    escolaridade = models.ForeignKey(Escolaridade, on_delete=models.PROTECT)

    class Meta:
        permissions = (
            ('formacao_list', 'Pode listar formação'),
            ('formacao_create', 'Pode cadastrar formação'),
            ('formacao_update', 'Pode editar formação'),
            ('formacao_view', 'Pode ver formação'),
            ('formacao_delete', 'Pode deletar formação')
        )

    def __str__(self):
        return self.for_nome


class Conselho(models.Model):
    con_nome = models.CharField(verbose_name='Nome', max_length=100)
    con_sigla = models.CharField(verbose_name='Sigla', max_length=100)

    class Meta:
        permissions = (
            ('conselho_list', 'Pode listar conselho'),
            ('conselho_create', 'Pode cadastrar conselho'),
            ('conselho_update', 'Pode editar conselho'),
            ('conselho_view', 'Pode ver conselho'),
            ('conselho_delete', 'Pode deletar conselho')
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
    municipio = models.ForeignKey(Municipio, on_delete=models.SET_NULL, null=True, blank=True)
    bairro = models.ForeignKey(Bairro, on_delete=models.SET_NULL, null=True, blank=True)
    natureza_juridica_dependencia = models.ForeignKey(Natureza, on_delete=models.SET_NULL, null=True, blank=True)
    escolaridade = models.ForeignKey(Escolaridade, on_delete=models.SET_NULL, null=True, blank=True)
    formacao_profissional = models.ForeignKey(Formacao, on_delete=models.SET_NULL, null=True, blank=True)
    conselho = models.ForeignKey(Conselho, on_delete=models.SET_NULL, null=True, blank=True)
    uf_conselho = models.CharField(verbose_name='UF', max_length=2, blank=True)

    class Meta:
        permissions = (
            ('entidade_list', 'Pode listar entidade'),
            ('entidade_create', 'Pode cadastrar entidade'),
            ('entidade_update', 'Pode editar entidade'),
            ('entidade_view', 'Pode ver entidade'),
            ('entidade_delete', 'Pode deletar entidade'),
            ('cnpj_validacao', 'Pode validar CNPJ'),
            ('cnpj', 'Pode informar CNPJ para validação'),
            ('cnpj_update', 'Pode editar CNPJ'),
            ('cnpj_view', 'Pode ver CNPJ'),
            ('cnpj_delete', 'Pode deletar CNPJ')
        )

    def __str__(self):
        return self.ent_nome_razao


class Area(models.Model):
    area_nome = models.CharField(verbose_name='Nome', max_length=100)
    area_descricao = models.CharField(verbose_name='Descrição', max_length=200)

    class Meta:
        permissions = (
            ('area_list', 'Pode listar área'),
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
            ('atividade_list', 'Pode listar atividade'),
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
            ('subatividade_list', 'Pode listar subatividade'),
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
            ('entsub_list', 'Pode listar subatividades do estabelecimento'),
            ('entsub_create', 'Pode incluir subatividades do estabelecimento'),
            ('entsub_delete', 'Pode deletar subatividades do estabelecimento')
        )

    def __str__(self):
        return self.self.subatividade



class EntidadeResponsavel(models.Model):
    entidade = models.ForeignKey(Entidade, related_name="entidade", on_delete=models.PROTECT)
    responsavel = models.ForeignKey(Entidade, related_name="responsavel", on_delete=models.PROTECT)

    class Meta:
        permissions = (
            ('entresp_list', 'Pode listar responsável legal do estabelecimento'),
            ('entresp_create', 'Pode incluir responsável legal do estabelecimento'),
            ('entresp_delete', 'Pode deletar responsável legal do estabelecimento')
        )

    def __str__(self):
        return self.entidade + ' / ' + self.responsavel


class EntidadeUnidade(models.Model):
    estabelecimento = models.ForeignKey(Entidade, related_name='estabelecimento', on_delete=models.PROTECT)
    unidade = models.ForeignKey(Entidade, related_name='unidade', on_delete=models.PROTECT)

    def __str__(self):
        return self.estabelecimento


class Areaproducao(models.Model):
    ap_nome = models.CharField(verbose_name='nome', max_length=200, default='')
    ap_descricao = models.CharField(verbose_name='descrição', max_length=400, default='')

    class Meta:
        permissions = (
            ('area_producao_list', 'Pode listar área de produção'),
            ('area_producao_create', 'Pode cadastrar área de produção'),
            ('area_producao_update', 'Pode editar área de produção'),
            ('area_producao_view', 'Pode ver área de produção'),
            ('area_producao_delete', 'Pode deletar área de produção')
        )

    def __str__(self):
        return self.ap_nome


class Classeproducao(models.Model):
    cp_nome = models.CharField(verbose_name='nome', max_length=200, default='')
    cp_descricao = models.CharField(verbose_name='descrição', max_length=400, default='')
    area_producao = models.ForeignKey(Areaproducao, on_delete=models.PROTECT)

    class Meta:
        permissions = (
            ('classe_producao_list', 'Pode listar classe de produção'),
            ('classe_producao_create', 'Pode cadastrar classe de produção'),
            ('classe_producao_update', 'Pode editar classe de produção'),
            ('classe_producao_view', 'Pode ver classe de produção'),
            ('classe_producao_delete', 'Pode deletar classe de produção')
        )

    def __str__(self):
        return self.cp_nome


class Linhaproducao(models.Model):
    lp_nome = models.CharField(verbose_name='nome', max_length=200, default='')
    lp_descricao = models.CharField(verbose_name='descrição', max_length=400, default='')
    area_producao = models.ForeignKey(Areaproducao, on_delete=models.PROTECT)

    class Meta:
        permissions = (
            ('linha_producao_list', 'Pode listar linha de produção'),
            ('linha_producao_create', 'Pode cadastrar linha de produção'),
            ('linha_producao_update', 'Pode editar linha de produção'),
            ('linha_producao_view', 'Pode ver linha de produção'),
            ('linha_producao_delete', 'Pode deletar linha de produção')
        )

    def __str__(self):
        return self.lp_nome


class Formaproducao(models.Model):
    fp_nome = models.CharField(verbose_name='nome', max_length=200, default='')
    fp_descricao = models.CharField(verbose_name='descrição', max_length=400, default='')
    linha_producao = models.ForeignKey(Linhaproducao, on_delete=models.PROTECT)

    class Meta:
        permissions = (
            ('forma_producao_list', 'Pode listar forma de produção'),
            ('forma_producao_create', 'Pode cadastrar forma de produção'),
            ('forma_producao_update', 'Pode editar forma de produção'),
            ('forma_producao_view', 'Pode ver forma de produção'),
            ('forma_producao_delete', 'Pode deletar forma de produção')
        )

    def __str__(self):
        return self.fp_nome


class EntidadeFormaproducao(models.Model):
    entidade = models.ForeignKey(Entidade, on_delete=models.PROTECT)
    forma_producao = models.ForeignKey(Formaproducao, on_delete=models.PROTECT, related_name='forma_producao')

    def __str__(self):
        return self.self.forma_producao


class EntidadeClasseproducao(models.Model):
    entidade = models.ForeignKey(Entidade, on_delete=models.PROTECT)
    classe_producao = models.ForeignKey(Classeproducao, on_delete=models.PROTECT, related_name='classe_producao')

    def __str__(self):
        return self.self.classe_producao
