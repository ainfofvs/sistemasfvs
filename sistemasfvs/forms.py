from django.forms import ModelForm, TextInput, Select
from .models import Status, Fase, Sistema, Documento, SistemaFase, Profile

class StatusForm(ModelForm):
    class Meta:
        model = Status
        fields = ['st_nome', 'st_descricao', 'st_cor']
        widgets = {
            'st_nome': TextInput(attrs={'class': 'form-control'}),
            'st_descricao': TextInput(attrs={'class': 'form-control'}),
        }

class FaseForm(ModelForm):
    class Meta:
        model = Fase
        fields = ['fase_nome', 'fase_descricao']
        widgets = {
            'fase_nome': TextInput(attrs={'class': 'form-control'}),
            'fase_descricao': TextInput(attrs={'class': 'form-control'}),
        }

class SistemaForm(ModelForm):
    class Meta:
        model = Sistema
        fields = ['sis_nome', 'sis_descricao',  'sis_setor_cliente', 'sis_dt_criacao',  'status_cod_fk']
        widgets = {
            'sis_nome': TextInput(attrs={'class': 'form-control'}),
            'sis_descricao': TextInput(attrs={'class': 'form-control'}),
            'sis_setor_cliente': TextInput(attrs={'class': 'form-control'}),
            'sis_dt_criacao': TextInput(attrs={'class': 'form-control'}),
            'status_cod_fk': Select(attrs={'class': 'form-control'})
        }


class DocumentoForm(ModelForm):
    class Meta:
        model = Documento
        fields = ['doc_titulo', 'doc_descricao',  'doc_path', 'doc_dt_cad',  'doc_usuario',  'sistema_cod_fk',  'doc_file']
        widgets = {
            'doc_titulo': TextInput(attrs={'class': 'form-control'}),
            'doc_descricao': TextInput(attrs={'class': 'form-control'}),
            'doc_path': TextInput(attrs={'class': 'form-control'}),
            'doc_dt_cad': TextInput(attrs={'class': 'form-control'}),
            'doc_usuario': TextInput(attrs={'class': 'form-control'}),
            'sistema_cod_fk': Select(attrs={'class': 'form-control'})
        }



class SistemaFaseForm(ModelForm):
    class Meta:
        model = SistemaFase
        fields = ['sistema', 'fase',  'sf_dt_inicio', 'sf_dt_termino',  'sf_situacao']
        widgets = {
            'sistema': Select(attrs={'class': 'form-control'}),
            'fase': Select(attrs={'class': 'form-control'}),
            'sf_dt_inicio': TextInput(attrs={'class': 'form-control'}),
            'sf_dt_termino': TextInput(attrs={'class': 'form-control'}),
            'sf_situacao': Select(attrs={'class': 'form-control'})
        }


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['user', 'foto']
        widgets = {
            'user': TextInput(attrs={'class': 'form-control'}),
            'foto': TextInput(attrs={'class': 'form-control'})
        }
