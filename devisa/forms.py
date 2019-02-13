from django.forms import ModelForm, TextInput, Select, Textarea
from .models import Pais, Estado, Municipio, Bairro, Natureza, Escolaridade, Formacao, Entidade
from .models import Area, Atividade, Subatividade, EntidadeSubatividade, Conselho, EntidadeUnidade
from .models import Areaproducao, Classeproducao, Linhaproducao, Formaproducao


class PaisForm(ModelForm):
    class Meta:
        model = Pais
        fields = ['pais_nome']
        widgets = {
            'pais_nome': TextInput(attrs={'class': 'form-control'})
        }


class EstadoForm(ModelForm):
    class Meta:
        model = Estado
        fields = ['est_nome', 'pais']
        widgets = {
            'est_nome': TextInput(attrs={'class': 'form-control'}),
            'pais': Select(attrs={'class': 'form-control'})
        }


class MunicipioForm(ModelForm):
    class Meta:
        model = Municipio
        fields = ['mun_nome', 'estado']
        widgets = {
            'mun_nome': TextInput(attrs={'class': 'form-control'}),
            'estado': Select(attrs={'class': 'form-control'})
        }


class BairroForm(ModelForm):
    class Meta:
        model = Bairro
        fields = ['bairro_nome', 'municipio']
        widgets = {
            'bairro_nome': TextInput(attrs={'class': 'form-control'}),
            'municipio': Select(attrs={'class': 'form-control'})
        }


class NaturezaForm(ModelForm):
    class Meta:
        model = Natureza
        fields = ['nat_nome', 'nat_descricao']
        widgets = {
            'nat_nome': TextInput(attrs={'class': 'form-control'}),
            'nat_descricao': TextInput(attrs={'class': 'form-control'})
        }


class EscolaridadeForm(ModelForm):
    class Meta:
        model = Escolaridade
        fields = ['esc_nome', 'esc_descricao']
        widgets = {
            'esc_nome': TextInput(attrs={'class': 'form-control'}),
            'esc_descricao': TextInput(attrs={'class': 'form-control'})
        }


class FormacaoForm(ModelForm):
    class Meta:
        model = Formacao
        fields = ['for_nome', 'escolaridade']
        widgets = {
            'for_nome': TextInput(attrs={'class': 'form-control'}),
            'escolaridade': Select(attrs={'class': 'form-control'})
        }


class AreaForm(ModelForm):
    class Meta:
        model = Area
        fields = ['area_nome', 'area_descricao']
        widgets = {
            'area_nome': TextInput(attrs={'class': 'form-control'}),
            'area_descricao': TextInput(attrs={'class': 'form-control'})
        }


class AtividadeForm(ModelForm):
    class Meta:
        model = Atividade
        fields = ['atv_nome', 'atv_descricao', 'area']
        widgets = {
            'atv_nome': TextInput(attrs={'class': 'form-control'}),
            'atv_descricao': TextInput(attrs={'class': 'form-control'}),
            'area': Select(attrs={'class': 'form-control'})
        }


class SubatividadeForm(ModelForm):
    class Meta:
        model = Subatividade
        fields = ['sub_nome', 'atividade']
        widgets = {
            'sub_nome': TextInput(attrs={'class': 'form-control'}),
            'atividade': Select(attrs={'class': 'form-control'})
        }


class ConselhoForm(ModelForm):
    class Meta:
        model = Conselho
        fields = ['con_nome', 'con_sigla']
        widgets = {
            'con_nome': TextInput(attrs={'class': 'form-control'}),
            'con_sigla': Select(attrs={'class': 'form-control'})
        }


class EntidadeForm(ModelForm):
    class Meta:
        model = Entidade
        fields = ['ent_tipo_entidade', 'ent_cpf', 'ent_cnpj', 'ent_nome_razao', 'ent_fantasia', 'ent_insc_estadual', 'ent_insc_municipal', 'ent_cnes',
                  'ent_cep', 'ent_complemento', 'ent_endereco', 'ent_numero', 'ent_fone', 'ent_fax', 'ent_email', 'ent_dt_inicio_func', 'ent_pasta_num',
                  'ent_obj_contrato_social', 'ent_observacoes', 'ent_rg', 'ent_orgao_exp', 'ent_dt_expedicao', 'ent_registro_conselho', 'ent_especializacao',
                  'municipio', 'bairro', 'natureza_juridica_dependencia', 'escolaridade', 'formacao_profissional', 'conselho', 'uf_conselho']
        widgets = {
            'ent_tipo_entidade': TextInput(attrs={'class': 'form-control'}),
            'ent_cpf':  TextInput(attrs={'class': 'form-control cpf'}),
            'ent_cnpj': TextInput(attrs={'class': 'form-control cnpj'}),
            'ent_nome_razao':  TextInput(attrs={'class': 'form-control'}),
            'ent_fantasia':  TextInput(attrs={'class': 'form-control'}),
            'ent_insc_estadual':  TextInput(attrs={'class': 'form-control'}),
            'ent_insc_municipal':  TextInput(attrs={'class': 'form-control'}),
            'ent_cnes':  TextInput(attrs={'class': 'form-control'}),
            'ent_cep':  TextInput(attrs={'class': 'form-control cep'}),
            'ent_complemento':  TextInput(attrs={'class': 'form-control'}),
            'ent_endereco':  TextInput(attrs={'class': 'form-control'}),
            'ent_numero': TextInput(attrs={'class': 'form-control'}),
            'ent_fone':  TextInput(attrs={'class': 'form-control fone'}),
            'ent_fax':  TextInput(attrs={'class': 'form-control fone'}),
            'ent_email':  TextInput(attrs={'class': 'form-control'}),
            'ent_dt_inicio_func':  TextInput(attrs={'class': 'form-control data'}),
            'ent_pasta_num':  TextInput(attrs={'class': 'form-control'}),
            'ent_obj_contrato_social':  Textarea(attrs={'class': 'form-control', 'rows': '3'}),
            'ent_observacoes':  Textarea(attrs={'class': 'form-control', 'rows': '3'}),
            'ent_rg':  TextInput(attrs={'class': 'form-control'}),
            'ent_orgao_exp':  TextInput(attrs={'class': 'form-control'}),
            'ent_dt_expedicao':  TextInput(attrs={'class': 'form-control data'}),
            'ent_registro_conselho':  TextInput(attrs={'class': 'form-control'}),
            'ent_especializacao':  TextInput(attrs={'class': 'form-control'}),
            'municipio': Select(attrs={'class': 'form-control'}),
            'bairro': Select(attrs={'class': 'form-control'}),
            'natureza_juridica_dependencia': Select(attrs={'class': 'form-control'}),
            'escolaridade': Select(attrs={'class': 'form-control'}),
            'formacao_profissional': Select(attrs={'class': 'form-control'}),
            'conselho': Select(attrs={'class': 'form-control'}),
            'uf_conselho': Select(attrs={'class': 'form-control'})
        }



class EntidadeSubatividadeForm(ModelForm):
    class Meta:
        model = EntidadeSubatividade
        fields = ['entidade', 'subatividade']
        widgets = {
            'entidade': Select(attrs={'class': 'form-control'}),
            'subatividade': Select(attrs={'class': 'form-control'})
        }


class EntidadeUnidadeForm(ModelForm):
    class Meta:
        model = EntidadeUnidade
        fields = ['estabelecimento', 'unidade']
        widgets = {
            'estabelecimento': TextInput(attrs={'class': 'form-control'}),
            'unidade': Select(attrs={'class': 'form-control'})
        }


class AreaproducaoForm(ModelForm):
    class Meta:
        model = Areaproducao
        fields = ['ap_nome', 'ap_descricao']
        widgets = {
            'ap_nome': TextInput(attrs={'class': 'form-control'}),
            'ap_descricao': TextInput(attrs={'class': 'form-control'})
        }


class ClasseproducaoForm(ModelForm):
    class Meta:
        model = Classeproducao
        fields = ['cp_nome', 'cp_descricao', 'area_producao']
        widgets = {
            'cp_nome': TextInput(attrs={'class': 'form-control'}),
            'cp_descricao': TextInput(attrs={'class': 'form-control'}),
            'area_producao': Select(attrs={'class': 'form-control'})
        }


class LinhaproducaoForm(ModelForm):
    class Meta:
        model = Linhaproducao
        fields = ['lp_nome', 'lp_descricao', 'area_producao']
        widgets = {
            'lp_nome': TextInput(attrs={'class': 'form-control'}),
            'lp_descricao': TextInput(attrs={'class': 'form-control'}),
            'area_producao': Select(attrs={'class': 'form-control'})
        }


class FormaproducaoForm(ModelForm):
    class Meta:
        model = Formaproducao
        fields = ['fp_nome', 'fp_descricao', 'linha_producao']
        widgets = {
            'fp_nome': TextInput(attrs={'class': 'form-control'}),
            'fp_descricao': TextInput(attrs={'class': 'form-control'}),
            'linha_producao': Select(attrs={'class': 'form-control'})
        }