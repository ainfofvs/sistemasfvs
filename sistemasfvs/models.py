from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Status(models.Model):
    st_nome = models.CharField(verbose_name='nome', max_length=200, default='')
    st_descricao = models.CharField(verbose_name='descrição', max_length=400, default='')
    st_cor = models.CharField(verbose_name='cor', max_length=20, default='')

    class Meta:
        permissions = (
            ('status_list', 'Pode listar status'),
            ('status_create', 'Pode cadastrar status'),
            ('status_update', 'Pode editar status'),
            ('status_view', 'Pode ver status'),
            ('status_delete', 'Pode deletar status')
        )

    def __str__(self):
        return self.st_nome


class Fase(models.Model):
    fase_nome = models.CharField(verbose_name='nome', max_length=200, default='')
    fase_descricao = models.CharField(verbose_name='descrição', max_length=400, default='')

    class Meta:
        permissions = (
            ('fase_list', 'Pode listar fase'),
            ('fase_create', 'Pode cadastrar fase'),
            ('fase_add', 'Pode alterar fase de projeto'),
            ('fase_sf_delete', 'Pode excluir fase de projeto'),
            ('fase_sf_update', 'Pode alterar fase de projeto'),
            ('fase_update', 'Pode editar fase'),
            ('fase_view', 'Pode ver fase'),
            ('fase_delete', 'Pode deletar fase')
        )

    def __str__(self):
        return self.fase_nome


class Sistema(models.Model):
    sis_nome = models.CharField(verbose_name='nome',max_length=200, default='')
    sis_descricao = models.CharField(verbose_name='descrição',max_length=400, default='')
    sis_setor_cliente = models.CharField(verbose_name='setor Solicitante', max_length=300, default='')
    sis_dt_criacao = models.DateField(verbose_name='data Criação')
    status_cod_fk = models.ForeignKey(Status,on_delete=models.PROTECT)
    fases = models.ManyToManyField(Fase, through='SistemaFase')

    class Meta:
        permissions = (
            ('sistema_list', 'Pode listar projeto'),
            ('sistema_create', 'Pode cadastrar projeto'),
            ('sistema_update', 'Pode editar projeto'),
            ('sistema_view', 'Pode ver projeto'),
            ('sistema_delete', 'Pode deletar projeto'),
            ('sistema_doctos', 'Pode ver documentos do projeto'),
            ('sistema_fases', 'Pode ver fases do projeto'),
        )

    def __str__(self):
        return self.sis_nome


class SistemaFase(models.Model):
    sistema = models.ForeignKey(Sistema,on_delete=models.CASCADE)
    fase = models.ForeignKey(Fase,on_delete=models.CASCADE)
    sf_dt_inicio = models.DateField(verbose_name='data de Início')
    sf_dt_termino = models.DateField(verbose_name='data de Término')
    sf_situacao = models.CharField(verbose_name="situação", choices=(('Ativo','Ativo'),('Finalizada','Finalizada')), default='Ativo', max_length=12)

    class Meta:
        permissions = (
            ('sistemafase_list', 'Pode listar sistemafase'),
            ('sistemafase_create', 'Pode cadastrar sistemafase'),
            ('sistemafase_update', 'Pode editar sistemafase'),
            ('sistemafase_view', 'Pode ver sistemafase'),
            ('sistemafase_delete', 'Pode deletar sistemafase')
        )

    def __str__(self):
        return self.sf_situacao


class Documento(models.Model):
    doc_titulo = models.CharField(verbose_name='Título',max_length=200, default='')
    doc_descricao = models.CharField(verbose_name='Descrição',max_length=300, default='')
    doc_path = models.CharField(verbose_name='Caminho', max_length=600, default='')
    doc_dt_cad = models.DateField(verbose_name='Data Cadastro')
    doc_usuario = models.CharField(verbose_name='Quem Cadastrou',max_length=300, default='')
    sistema_cod_fk = models.ForeignKey(Sistema,on_delete=models.PROTECT)
    doc_file = models.FileField(upload_to='doctos_files/', null=True, blank=True)

    class Meta:
        permissions = (
            ('documento_list', 'Pode listar documento'),
            ('documento_create', 'Pode cadastrar documento'),
            ('documento_update', 'Pode editar documento'),
            ('documento_view', 'Pode ver documento'),
            ('documento_delete', 'Pode deletar documento')
        )

    def __str__(self):
        return self.doc_titulo


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT, related_name='profile')
    foto = models.FileField(upload_to='fotos_perfil/', null=True, blank=True)

    def __str__(self):
        return self.user
