from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from .models import Pais, Estado, Municipio, Bairro, Area, Atividade, Subatividade, Escolaridade
from .models import Formacao, Natureza, Entidade, EntidadeSubatividade, EntidadeResponsavel, Conselho, EntidadeUnidade
from .models import Areaproducao, Classeproducao, Linhaproducao, Formaproducao, EntidadeFormaproducao, EntidadeClasseproducao
from .forms import PaisForm, EstadoForm, MunicipioForm, BairroForm, AreaForm, EntidadeForm
from .forms import AtividadeForm, SubatividadeForm, EscolaridadeForm, FormacaoForm, NaturezaForm, ConselhoForm, EntidadeUnidadeForm
from .forms import AreaproducaoForm, ClasseproducaoForm, LinhaproducaoForm, FormaproducaoForm
from django.contrib import messages
import re
from django.core.validators import EMPTY_VALUES
from django.forms import ValidationError
from django.utils.translation import ugettext_lazy as _
from django import template

register = template.Library()


error_messages = {
    'invalid': _("Invalid number."),
    'digits_only': _("This field requires only numbers."),
    'max_digits': _("This field requires exactly 11 digits."),
}


def DV_maker(v):
    if v >= 2:
        return 11 - v
    return 0


def validate_CPF(value):
    """
    Value can be either a string in the format XXX.XXX.XXX-XX or an
    11-digit number.
    """
    flag = 1

    if value in EMPTY_VALUES:
        return u''
    if not value.isdigit():
        value = re.sub("[-\.]", "", value)
    orig_value = value[:]
    try:
        int(value)
    except ValueError:
        #raise ValidationError(error_messages['digits_only'])
        flag = -1
    if len(value) != 11:
        #raise ValidationError(error_messages['max_digits'])
        flag = -2
    orig_dv = value[-2:]

    new_1dv = sum([i * int(value[idx]) for idx, i in enumerate(range(10, 1, -1))])
    new_1dv = DV_maker(new_1dv % 11)
    value = value[:-2] + str(new_1dv) + value[-1]
    new_2dv = sum([i * int(value[idx]) for idx, i in enumerate(range(11, 1, -1))])
    new_2dv = DV_maker(new_2dv % 11)
    value = value[:-1] + str(new_2dv)
    if value[-2:] != orig_dv:
        #raise ValidationError(error_messages['invalid'])
        flag = -3

    #return orig_value
    return flag

def validate_CNPJ(value):
    """
    Value can be either a string in the format XX.XXX.XXX/XXXX-XX or a
    group of 14 characters.
    :type value: object
    """
    flg = 1
    value = str(value)
    if value in EMPTY_VALUES:
        return u''
    if not value.isdigit():
        value = re.sub("[-/\.]", "", value)
    orig_value = value[:]
    try:
        int(value)
    except ValueError:
        #raise ValidationError(error_messages['digits_only'])
        flg = -1
    if len(value) > 14:
        #raise ValidationError(error_messages['max_digits'])
        flg = -2
    orig_dv = value[-2:]

    new_1dv = sum([i * int(value[idx]) for idx, i in enumerate(list(range(5, 1, -1)) + list(range(9, 1, -1)))])
    new_1dv = DV_maker(new_1dv % 11)
    value = value[:-2] + str(new_1dv) + value[-1]
    new_2dv = sum([i * int(value[idx]) for idx, i in enumerate(list(range(6, 1, -1)) + list(range(9, 1, -1)))])
    new_2dv = DV_maker(new_2dv % 11)
    value = value[:-1] + str(new_2dv)
    if value[-2:] != orig_dv:
        #raise ValidationError(error_messages['invalid'])
        flg = -3

    #return orig_value
    return flg


@login_required
def devisa(request):
    return render(request, 'devisa.html')



# ------------- CPF - Autônomo ------------------- #
@login_required
@permission_required('devisa.cpf_autonomo_validacao')
def cpf_autonomo_validacao(request):
    form = EntidadeForm(request.POST or None, request.FILES or None)

    if request.POST:
        ent_cpf = request.POST['ent_cpf']
        ent_cpf2 = re.sub("[-/\.]", "", ent_cpf)
        if validate_CPF(ent_cpf) == 1:
            model = Entidade.objects.filter(ent_cpf=ent_cpf)
            if not model:
                return redirect('cpf_autonomo_create', cpf=ent_cpf2)
            else:
                entidade = Entidade.objects.get(ent_cpf=ent_cpf)
                messages.info(request, 'O CPF informado já está cadastrado!')
                return redirect('cpf_autonomo_update', id=entidade.id)

        else:
            messages.error(request, 'O CPF informado é inválido!')
            return redirect('cpf_autonomo_validacao')

    return render(request, 'entidade/cpf_autonomo_validacao.html', {'form': form})


@login_required
@permission_required('devisa.cpf_autonomo')
def cpf_autonomo(request):
    model = Entidade.objects.filter(ent_tipo_entidade=5)
    # q = request.GET.get('pesquisar_por')
    # if q is not None:
    #     model = model.filter(Q(ent_cpf__icontains=q) | Q(ent_nome_razao__icontains=q))

    return render(request, 'entidade/cpf_autonomo.html', {'entidades': model})


@login_required
@permission_required('devisa.cpf_autonomo_update')
def cpf_autonomo_update(request, id):
    model = get_object_or_404(Entidade, pk=id)
    form = EntidadeForm(request.POST or None, request.FILES or None, instance=model)

    if form.is_valid():
        form.save()
        messages.success(request, 'Profissional autônomo alterado com sucesso!')
        return redirect('cpf_autonomo')

    return render(request, 'entidade/cpf_autonomo_update.html', {'form': form})


@login_required
@permission_required('devisa.cpf_autonomo_delete')
def cpf_autonomo_delete(request, id):
    model = get_object_or_404(Entidade, pk=id)

    if request.method == 'POST':
        model.delete()
        messages.success(request, 'Profissional autônomo excluído com sucesso!')
        return redirect('cpf_autonomo')

    return render(request, 'entidade/cpf_autonomo_delete.html', {'model': model})


@login_required
@permission_required('devisa.cpf_autonomo_create')
def cpf_autonomo_create(request, cpf):
    form = EntidadeForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        messages.success(request, 'Profissional autônomo cadastrado com sucesso!')
        return redirect('cpf_autonomo')
    return render(request, 'entidade/cpf_autonomo_create.html', {'cpf': cpf, 'form': form})


@login_required
@permission_required('devisa.cpf_autonomo_view')
def cpf_autonomo_view(request, id):
    model = get_object_or_404(Entidade, pk=id)
    return render(request, 'entidade/cpf_autonomo_view.html', {'entidade': model})

# ------------- Fim CPF - Autônomo ------------------- #


# ------------- CPF - Profissional Liberal ------------------- #
@login_required
@permission_required('devisa.cpf_liberal_validacao')
def cpf_liberal_validacao(request):
    form = EntidadeForm(request.POST or None, request.FILES or None)

    if request.POST:
        ent_cpf = request.POST['ent_cpf']
        ent_cpf2 = re.sub("[-/\.]", "", ent_cpf)
        if validate_CPF(ent_cpf) == 1:
            model = Entidade.objects.filter(ent_cpf=ent_cpf)
            if not model:
                return redirect('cpf_liberal_create', cpf=ent_cpf2)
            else:
                entidade = Entidade.objects.get(ent_cpf=ent_cpf)
                messages.info(request, 'O CPF informado já está cadastrado!')
                return redirect('cpf_liberal_update', id=entidade.id)

        else:
            messages.error(request, 'O CPF informado é inválido!')
            return redirect('cpf_liberal_validacao')

    return render(request, 'entidade/cpf_liberal_validacao.html', {'form': form})


@login_required
@permission_required('devisa.cpf_liberal')
def cpf_liberal(request):
    model = Entidade.objects.filter(ent_tipo_entidade=4)
    # q = request.GET.get('pesquisar_por')
    # if q is not None:
    #     model = model.filter(Q(ent_cpf__icontains=q) | Q(ent_nome_razao__icontains=q))

    return render(request, 'entidade/cpf_liberal.html', {'entidades': model})


@login_required
@permission_required('devisa.cpf_liberal_update')
def cpf_liberal_update(request,id):
    model = get_object_or_404(Entidade, pk=id)
    form = EntidadeForm(request.POST or None, request.FILES or None, instance=model)

    if form.is_valid():
        form.save()
        messages.success(request, 'Profissional liberal alterado com sucesso!')
        return redirect('cpf_liberal')

    return render(request, 'entidade/cpf_liberal_update.html', {'form': form})


@login_required
@permission_required('devisa.cpf_liberal_delete')
def cpf_liberal_delete(request, id):
    model = get_object_or_404(Entidade, pk=id)

    if request.method == 'POST':
        model.delete()
        messages.success(request, 'Profissional liberal excluído com sucesso!')
        return redirect('cpf_liberal')

    return render(request, 'entidade/cpf_liberal_delete.html', {'model': model})


@login_required
@permission_required('devisa.cpf_liberal_create')
def cpf_liberal_create(request, cpf):
    form = EntidadeForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        messages.success(request, 'Profissional liberal cadastrado com sucesso!')
        return redirect('cpf_liberal')
    return render(request, 'entidade/cpf_liberal_create.html', {'cpf': cpf, 'form': form})


@login_required
@permission_required('devisa.cpf_liberal_view')
def cpf_liberal_view(request, id):
    model = get_object_or_404(Entidade, pk=id)
    return render(request, 'entidade/cpf_liberal_view.html', {'entidade': model})

# ------------- Fim CPF - Profissional Liberal ------------------- #


# ------------- CNPJ - Estabelecimento ------------------- #
@login_required
@permission_required('devisa.cnpj_validacao')
def cnpj_validacao(request):
    form = EntidadeForm(request.POST or None, request.FILES or None)

    if request.POST:
        ent_cnpj = request.POST['ent_cnpj']
        ent_cnpj2 = re.sub("[-/\.]", "", ent_cnpj)
        if validate_CNPJ(ent_cnpj) == 1:
            model = Entidade.objects.filter(ent_cnpj=ent_cnpj)
            if not model:
                return redirect('cnpj_create', cnpj=ent_cnpj2)
            else:
                entidade = Entidade.objects.get(ent_cnpj=ent_cnpj)
                messages.info(request, 'O CNPJ informado já estava cadastrado!')
                return redirect('cnpj_update', id=entidade.id)

        else:
            messages.error(request, 'O CNPJ informado é inválido!')
            return redirect('cnpj_validacao')

    return render(request, 'entidade/cnpj_validacao.html', {'form': form})


@login_required
@permission_required('devisa.cnpj')
def cnpj(request):
    model = Entidade.objects.filter(ent_tipo_entidade=1)
    # q = request.GET.get('pesquisar_por')
    # if q is not None:
    #     model = model.filter(Q(ent_cnpj__icontains=q) | Q(ent_nome_razao__icontains=q))

    return render(request, 'entidade/cnpj.html', {'entidades': model})


@login_required
@permission_required('devisa.cnpj_view')
def cnpj_view(request, id):
    model = get_object_or_404(Entidade, pk=id)
    return render(request, 'entidade/cnpj_view.html', {'entidade': model})


@login_required
@permission_required('devisa.cnpj_create')
def cnpj_create(request, cnpj):
    form = EntidadeForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        messages.success(request, 'Estabelecimento cadastrado com sucesso!')
        return redirect('cnpj')
    return render(request, 'entidade/cnpj_create.html', {'cnpj': cnpj, 'form': form})


@login_required
@permission_required('devisa.cnpj_update')
def cnpj_update(request,id):
    model = get_object_or_404(Entidade, pk=id)
    form = EntidadeForm(request.POST or None, request.FILES or None, instance=model)

    if form.is_valid():
        form.save()
        messages.success(request, 'Estabelecimento alterado com sucesso!')
        return redirect('cnpj')

    return render(request, 'entidade/cnpj_update.html', {'form': form})


@login_required
@permission_required('devisa.cnpj_delete')
def cnpj_delete(request, id):
    model = get_object_or_404(Entidade, pk=id)

    if request.method == 'POST':
        model.delete()
        messages.success(request, 'Estabelecimento excluído com sucesso!')
        return redirect('cnpj')

    return render(request, 'entidade/cnpj_delete.html', {'model': model})

# ------------- Fim CNPJ - Estabelecimento ------------------- #


# ------------- PAÍS ---------------- #
@login_required
@permission_required('devisa.pais_list')
def pais_list(request):
    model = Pais.objects.all()
    q = request.GET.get('pesquisar_por')
    if q is not None:
        model = model.filter(Q(pais_nome__icontains=q))

    return render(request, 'pais/pais_list.html', {'paises': model})


@login_required
@permission_required('devisa.pais_view')
def pais_view(request, id):
    model = get_object_or_404(Pais, pk=id)
    return render(request, 'pais/pais_view.html', {'pais': model})


@login_required
@permission_required('devisa.pais_create')
def pais_create(request):
    form = PaisForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        messages.success(request, 'País cadastrado com sucesso!')
        return redirect('pais_list')
    return render(request, 'pais/pais_create.html', {'form': form})


@login_required
@permission_required('devisa.pais_update')
def pais_update(request,id):
    model = get_object_or_404(Pais, pk=id)
    form = PaisForm(request.POST or None, request.FILES or None, instance=model)

    if form.is_valid():
        form.save()
        messages.success(request, 'País alterado com sucesso!')
        return redirect('pais_list')

    return render(request, 'pais/pais_update.html', {'form': form})


@login_required
@permission_required('devisa.pais_delete')
def pais_delete(request, id):
    model = get_object_or_404(Pais, pk=id)

    if request.method == 'POST':
        model.delete()
        messages.success(request, 'País excluído com sucesso!')
        return redirect('pais_list')

    return render(request, 'pais/pais_delete.html', {'model': model})
# ------------- FIM PAÍS ---------------- #

# ------------- ESTADO ---------------- #
@login_required
@permission_required('devisa.estado_list')
def estado_list(request):
    model = Estado.objects.all()
    q = request.GET.get('pesquisar_por')
    if q is not None:
        model = model.filter(Q(est_nome__icontains=q) | Q(pais__icontains=q))

    return render(request, 'estado/estado_list.html', {'estados': model})


@login_required
@permission_required('devisa.estado_view')
def estado_view(request, id):
    model = get_object_or_404(Estado, pk=id)
    return render(request, 'estado/estado_view.html', {'estado': model})


@login_required
@permission_required('devisa.estado_create')
def estado_create(request):
    form = EstadoForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        messages.success(request, 'Estado cadastrado com sucesso!')
        return redirect('estado_list')
    return render(request, 'estado/estado_create.html', {'form': form})


@login_required
@permission_required('devisa.estado_update')
def estado_update(request,id):
    model = get_object_or_404(Estado, pk=id)
    form = EstadoForm(request.POST or None, request.FILES or None, instance=model)

    if form.is_valid():
        form.save()
        messages.success(request, 'Estado alterado com sucesso!')
        return redirect('estado_list')

    return render(request, 'estado/estado_update.html', {'form': form})


@login_required
@permission_required('devisa.estado_delete')
def estado_delete(request, id):
    model = get_object_or_404(Estado, pk=id)

    if request.method == 'POST':
        model.delete()
        messages.success(request, 'Estado excluído com sucesso!')
        return redirect('estado_list')

    return render(request, 'estado/estado_delete.html', {'model': model})
# ------------- FIM ESTADO ---------------- #


# ------------- MUNICÍPIO ---------------- #
@login_required
@permission_required('devisa.municipio_list')
def municipio_list(request):
    model = Municipio.objects.all()
    q = request.GET.get('pesquisar_por')
    if q is not None:
        model = model.filter(Q(mun_nome__icontains=q) | Q(estado__icontains=q))

    return render(request, 'municipio/municipio_list.html', {'municipios': model})


@login_required
@permission_required('devisa.municipio_view')
def municipio_view(request, id):
    model = get_object_or_404(Municipio, pk=id)
    return render(request, 'municipio/municipio_view.html', {'municipio': model})


@login_required
@permission_required('devisa.municipio_create')
def municipio_create(request):
    form = MunicipioForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        messages.success(request, 'Município cadastrado com sucesso!')
        return redirect('municipio_list')
    return render(request, 'municipio/municipio_create.html', {'form': form})


@login_required
@permission_required('devisa.municipio_update')
def municipio_update(request,id):
    model = get_object_or_404(Municipio, pk=id)
    form = MunicipioForm(request.POST or None, request.FILES or None, instance=model)

    if form.is_valid():
        form.save()
        messages.success(request, 'Município alterado com sucesso!')
        return redirect('municipio_list')

    return render(request, 'municipio/municipio_update.html', {'form': form})


@login_required
@permission_required('devisa.municipio_delete')
def municipio_delete(request, id):
    model = get_object_or_404(Municipio, pk=id)

    if request.method == 'POST':
        model.delete()
        messages.success(request, 'Município excluído com sucesso!')
        return redirect('municipio_list')

    return render(request, 'municipio/municipio_delete.html', {'model': model})
# ------------- FIM MUNICÍPIO ---------------- #


# ------------- BAIRRO ---------------- #
@login_required
@permission_required('devisa.bairro_list')
def bairro_list(request):
    model = Bairro.objects.all()
    q = request.GET.get('pesquisar_por')
    if q is not None:
        model = model.filter(Q(bairro_nome__icontains=q) | Q(municipio__icontains=q))

    return render(request, 'bairro/bairro_list.html', {'bairros': model})


@login_required
@permission_required('devisa.bairro_view')
def bairro_view(request, id):
    model = get_object_or_404(Bairro, pk=id)
    return render(request, 'bairro/bairro_view.html', {'bairro': model})


@login_required
@permission_required('devisa.bairro_create')
def bairro_create(request):
    form = BairroForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        messages.success(request, 'Bairro cadastrado com sucesso!')
        return redirect('bairro_list')
    return render(request, 'bairro/bairro_create.html', {'form': form})


@login_required
@permission_required('devisa.bairro_update')
def bairro_update(request,id):
    model = get_object_or_404(Bairro, pk=id)
    form = BairroForm(request.POST or None, request.FILES or None, instance=model)

    if form.is_valid():
        form.save()
        messages.success(request, 'Bairro alterado com sucesso!')
        return redirect('bairro_list')

    return render(request, 'bairro/bairro_update.html', {'form': form})


@login_required
@permission_required('devisa.bairro_delete')
def bairro_delete(request, id):
    model = get_object_or_404(Bairro, pk=id)

    if request.method == 'POST':
        model.delete()
        messages.success(request, 'Bairro excluído com sucesso!')
        return redirect('bairro_list')

    return render(request, 'bairro/bairro_delete.html', {'model': model})
# ------------- FIM BAIRRO ---------------- #

# ------------- AREA ---------------- #
@login_required
@permission_required('devisa.area_list')
def area_list(request):
    model = Area.objects.all()
    q = request.GET.get('pesquisar_por')
    if q is not None:
        model = model.filter(Q(area_nome__icontains=q) | Q(area_descricao__icontains=q))

    return render(request, 'area/area_list.html', {'areas': model})


@login_required
@permission_required('devisa.area_view')
def area_view(request, id):
    model = get_object_or_404(Area, pk=id)
    return render(request, 'area/area_view.html', {'area': model})


@login_required
@permission_required('devisa.area_create')
def area_create(request):
    form = AreaForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        messages.success(request, 'Área cadastrada com sucesso!')
        return redirect('area_list')
    return render(request, 'area/area_create.html', {'form': form})


@login_required
@permission_required('devisa.area_update')
def area_update(request,id):
    model = get_object_or_404(Area, pk=id)
    form = AreaForm(request.POST or None, request.FILES or None, instance=model)

    if form.is_valid():
        form.save()
        messages.success(request, 'Área alterada com sucesso!')
        return redirect('area_list')

    return render(request, 'area/area_update.html', {'form': form})


@login_required
@permission_required('devisa.area_delete')
def area_delete(request, id):
    model = get_object_or_404(Area, pk=id)

    if request.method == 'POST':
        model.delete()
        messages.success(request, 'Área excluída com sucesso!')
        return redirect('area_list')

    return render(request, 'area/area_delete.html', {'model': model})
# ------------- FIM AREA ---------------- #


# ------------- ATIVIDADE ---------------- #
@login_required
@permission_required('devisa.atividade_list')
def atividade_list(request):
    model = Atividade.objects.all()
    q = request.GET.get('pesquisar_por')
    if q is not None:
        model = model.filter(Q(atv_nome__icontains=q) | Q(atv_descricao__icontains=q)| Q(area__icontains=q))

    return render(request, 'atividade/atividade_list.html', {'atividades': model})


@login_required
@permission_required('devisa.atividade_view')
def atividade_view(request, id):
    model = get_object_or_404(Atividade, pk=id)
    return render(request, 'atividade/atividade_view.html', {'atividade': model})


@login_required
@permission_required('devisa.atividade_create')
def atividade_create(request):
    form = AtividadeForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        messages.success(request, 'Atividade cadastrada com sucesso!')
        return redirect('atividade_list')
    return render(request, 'atividade/atividade_create.html', {'form': form})


@login_required
@permission_required('devisa.atividade_update')
def atividade_update(request,id):
    model = get_object_or_404(Atividade, pk=id)
    form = AtividadeForm(request.POST or None, request.FILES or None, instance=model)

    if form.is_valid():
        form.save()
        messages.success(request, 'Atividade alterada com sucesso!')
        return redirect('atividade_list')

    return render(request, 'atividade/atividade_update.html', {'form': form})


@login_required
@permission_required('devisa.atividade_delete')
def atividade_delete(request, id):
    model = get_object_or_404(Atividade, pk=id)

    if request.method == 'POST':
        model.delete()
        messages.success(request, 'Atividade excluída com sucesso!')
        return redirect('atividade_list')

    return render(request, 'atividade/atividade_delete.html', {'model': model})
# ------------- FIM ATIVIDADE ---------------- #


# ------------- SUBATIVIDADE ---------------- #
@login_required
@permission_required('devisa.subatividade_list')
def subatividade_list(request):
    model = Subatividade.objects.all()
    q = request.GET.get('pesquisar_por')
    if q is not None:
        model = model.filter(Q(sub_nome__icontains=q) | Q(atividade__icontains=q))

    return render(request, 'subatividade/subatividade_list.html', {'subatividades': model})


@login_required
@permission_required('devisa.subatividade_view')
def subatividade_view(request, id):
    model = get_object_or_404(Subatividade, pk=id)
    return render(request, 'subatividade/subatividade_view.html', {'subatividade': model})


@login_required
@permission_required('devisa.subatividade_create')
def subatividade_create(request):
    form = SubatividadeForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        messages.success(request, 'Subatividade cadastrada com sucesso!')
        return redirect('subatividade_list')
    return render(request, 'subatividade/subatividade_create.html', {'form': form})


@login_required
@permission_required('devisa.subatividade_update')
def subatividade_update(request,id):
    model = get_object_or_404(Subatividade, pk=id)
    form = SubatividadeForm(request.POST or None, request.FILES or None, instance=model)

    if form.is_valid():
        form.save()
        messages.success(request, 'Subatividade alterada com sucesso!')
        return redirect('subatividade_list')

    return render(request, 'subatividade/subatividade_update.html', {'form': form})


@login_required
@permission_required('devisa.subatividade_delete')
def subatividade_delete(request, id):
    model = get_object_or_404(Subatividade, pk=id)

    if request.method == 'POST':
        model.delete()
        messages.success(request, 'Subatividade excluída com sucesso!')
        return redirect('subatividade_list')

    return render(request, 'subatividade/subatividade_delete.html', {'model': model})
# ------------- FIM SUBATIVIDADE ---------------- #

# ------------- ESCOLARIDADE ---------------- #
@login_required
@permission_required('devisa.escolaridade_list')
def escolaridade_list(request):
    model = Escolaridade.objects.all()
    q = request.GET.get('pesquisar_por')
    if q is not None:
        model = model.filter(Q(esc_nome__icontains=q) | Q(esc_descricao__icontains=q))

    return render(request, 'escolaridade/escolaridade_list.html', {'escolaridades': model})


@login_required
@permission_required('devisa.escolaridade_view')
def escolaridade_view(request, id):
    model = get_object_or_404(Escolaridade, pk=id)
    return render(request, 'escolaridade/escolaridade_view.html', {'escolaridade': model})


@login_required
@permission_required('devisa.escolaridade_create')
def escolaridade_create(request):
    form = EscolaridadeForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        messages.success(request, 'Escolaridade cadastrada com sucesso!')
        return redirect('escolaridade_list')
    return render(request, 'escolaridade/escolaridade_create.html', {'form': form})


@login_required
@permission_required('devisa.escolaridade_update')
def escolaridade_update(request,id):
    model = get_object_or_404(Escolaridade, pk=id)
    form = EscolaridadeForm(request.POST or None, request.FILES or None, instance=model)

    if form.is_valid():
        form.save()
        messages.success(request, 'Escolaridade alterada com sucesso!')
        return redirect('escolaridade_list')

    return render(request, 'escolaridade/escolaridade_update.html', {'form': form})


@login_required
@permission_required('devisa.escolaridade_delete')
def escolaridade_delete(request, id):
    model = get_object_or_404(Escolaridade, pk=id)

    if request.method == 'POST':
        model.delete()
        messages.success(request, 'Escolaridade excluída com sucesso!')
        return redirect('escolaridade_list')

    return render(request, 'escolaridade/escolaridade_delete.html', {'model': model})
# ------------- FIM ESCOLARIDADE ---------------- #


# ------------- FORMACAO ---------------- #
@login_required
@permission_required('devisa.formacao_list')
def formacao_list(request):
    model = Formacao.objects.all()
    q = request.GET.get('pesquisar_por')
    if q is not None:
        model = model.filter(Q(for_nome__icontains=q) | Q(escolaridade__icontains=q))

    return render(request, 'formacao/formacao_list.html', {'formacoes': model})


@login_required
@permission_required('devisa.formacao_view')
def formacao_view(request, id):
    model = get_object_or_404(Formacao, pk=id)
    return render(request, 'formacao/formacao_view.html', {'formacao': model})


@login_required
@permission_required('devisa.formacao_create')
def formacao_create(request):
    form = FormacaoForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        messages.success(request, 'Formação cadastrada com sucesso!')
        return redirect('formacao_list')
    return render(request, 'formacao/formacao_create.html', {'form': form})


@login_required
@permission_required('devisa.formacao_update')
def formacao_update(request,id):
    model = get_object_or_404(Formacao, pk=id)
    form = FormacaoForm(request.POST or None, request.FILES or None, instance=model)

    if form.is_valid():
        form.save()
        messages.success(request, 'Formação alterada com sucesso!')
        return redirect('formacao_list')

    return render(request, 'formacao/formacao_update.html', {'form': form})


@login_required
@permission_required('devisa.formacao_delete')
def formacao_delete(request, id):
    model = get_object_or_404(Formacao, pk=id)

    if request.method == 'POST':
        model.delete()
        messages.success(request, 'Formação excluída com sucesso!')
        return redirect('formacao_list')

    return render(request, 'formacao/formacao_delete.html', {'model': model})
# ------------- FIM FORMACAO ---------------- #

# ------------- NATUREZA ---------------- #
@login_required
@permission_required('devisa.natureza_list')
def natureza_list(request):
    model = Natureza.objects.all()
    q = request.GET.get('pesquisar_por')
    if q is not None:
        model = model.filter(Q(nat_nome__icontains=q) | Q(nat_descricao__icontains=q))

    return render(request, 'natureza/natureza_list.html', {'naturezas': model})


@login_required
@permission_required('devisa.natureza_view')
def natureza_view(request, id):
    model = get_object_or_404(Natureza, pk=id)
    return render(request, 'natureza/natureza_view.html', {'natureza': model})


@login_required
@permission_required('devisa.natureza_create')
def natureza_create(request):
    form = NaturezaForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        messages.success(request, 'Natureza cadastrada com sucesso!')
        return redirect('natureza_list')
    return render(request, 'natureza/natureza_create.html', {'form': form})


@login_required
@permission_required('devisa.natureza_update')
def natureza_update(request,id):
    model = get_object_or_404(Natureza, pk=id)
    form = NaturezaForm(request.POST or None, request.FILES or None, instance=model)

    if form.is_valid():
        form.save()
        messages.success(request, 'Natureza alterada com sucesso!')
        return redirect('natureza_list')

    return render(request, 'natureza/natureza_update.html', {'form': form})


@login_required
@permission_required('devisa.natureza_delete')
def natureza_delete(request, id):
    model = get_object_or_404(Natureza, pk=id)

    if request.method == 'POST':
        model.delete()
        messages.success(request, 'Natureza excluída com sucesso!')
        return redirect('natureza_list')

    return render(request, 'natureza/natureza_delete.html', {'model': model})
# ------------- FIM NATUREZA ---------------- #


# ------------- CONSELHO ---------------- #
@login_required
@permission_required('devisa.conselho_list')
def conselho_list(request):
    model = Conselho.objects.all()
    q = request.GET.get('pesquisar_por')
    if q is not None:
        model = model.filter(Q(con_nome__icontains=q) | Q(con_sigla__icontains=q))

    return render(request, 'conselho/conselho_list.html', {'conselhos': model})


@login_required
@permission_required('devisa.conselho_view')
def conselho_view(request, id):
    model = get_object_or_404(Conselho, pk=id)
    return render(request, 'conselho/conselho_view.html', {'conselho': model})


@login_required
@permission_required('devisa.conselho_create')
def conselho_create(request):
    form = ConselhoForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        messages.success(request, 'Conselho cadastrado com sucesso!')
        return redirect('conselho_list')
    return render(request, 'conselho/conselho_create.html', {'form': form})


@login_required
@permission_required('devisa.conselho_update')
def conselho_update(request,id):
    model = get_object_or_404(Conselho, pk=id)
    form = ConselhoForm(request.POST or None, request.FILES or None, instance=model)

    if form.is_valid():
        form.save()
        messages.success(request, 'Conselho alterado com sucesso!')
        return redirect('conselho_list')

    return render(request, 'conselho/conselho_update.html', {'form': form})


@login_required
@permission_required('devisa.conselho_delete')
def conselho_delete(request, id):
    model = get_object_or_404(Conselho, pk=id)

    if request.method == 'POST':
        model.delete()
        messages.success(request, 'Conselho excluído com sucesso!')
        return redirect('conselho_list')

    return render(request, 'conselho/conselho_delete.html', {'model': model})
# ------------- FIM CONSELHO ---------------- #


# ------------- ENTIDADE ---------------- #
@login_required
@permission_required('devisa.entidade_list')
def entidade_list(request):
    model = Entidade.objects.all()
    q = request.GET.get('pesquisar_por')
    if q is not None:
        model = model.filter(Q(ent_cpf__icontains=q) | Q(ent_cnpj__icontains=q) | Q(ent_nome_razao__icontains=q))

    return render(request, 'entidade/entidade_list.html', {'entidades': model})


@login_required
@permission_required('devisa.entidade_view')
def entidade_view(request, id):
    model = get_object_or_404(Entidade, pk=id)
    return render(request, 'entidade/entidade_view.html', {'entidade': model})


@login_required
@permission_required('devisa.entidade_create')
def entidade_create(request):
    form = EntidadeForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        messages.success(request, 'Entidade cadastrada com sucesso!')
        return redirect('entidade_list')
    return render(request, 'entidade/entidade_create.html', {'form': form})


@login_required
@permission_required('devisa.entidade_update')
def entidade_update(request,id):
    model = get_object_or_404(Entidade, pk=id)
    form = EntidadeForm(request.POST or None, request.FILES or None, instance=model)

    if form.is_valid():
        form.save()
        messages.success(request, 'Entidade alterada com sucesso!')
        return redirect('entidade_list')

    return render(request, 'entidade/entidade_update.html', {'form': form})


@login_required
@permission_required('devisa.entidade_delete')
def entidade_delete(request, id):
    model = get_object_or_404(Entidade, pk=id)

    if request.method == 'POST':
        model.delete()
        messages.success(request, 'Entidade excluída com sucesso!')
        return redirect('entidade_list')

    return render(request, 'entidade/entidade_delete.html', {'model': model})
# ------------- FIM ENTIDADE ---------------- #


# ------------- ATIVIDADES DA ENTIDADE - ENTIDADESUBATIVIDADE ---------------- #
@login_required
@permission_required('devisa.entsub_list')
def entsub_list(request, id):
    model = get_object_or_404(Entidade, pk=id)
    entsubs = EntidadeSubatividade.objects.filter(entidade=id)

    return render(request, 'entsub/entsub_list.html', {'model': model, 'entsubs': entsubs})


@login_required
@permission_required('devisa.entsub_liberal_list')
def entsub_liberal_list(request, id):
    model = get_object_or_404(Entidade, pk=id)
    entsubs = EntidadeSubatividade.objects.filter(entidade=id)

    return render(request, 'entsub/entsub_liberal_list.html', {'model': model, 'entsubs': entsubs})


@login_required
@permission_required('devisa.entsub_autonomo_list')
def entsub_autonomo_list(request, id):
    model = get_object_or_404(Entidade, pk=id)
    entsubs = EntidadeSubatividade.objects.filter(entidade=id)

    return render(request, 'entsub/entsub_autonomo_list.html', {'model': model, 'entsubs': entsubs})


@login_required
@permission_required('devisa.entsub_create')
def entsub_create(request, id):
    model = get_object_or_404(Entidade, pk=id)
    subs = Subatividade.objects.all()

    if request.POST:
        checks = request.POST.getlist('checks[]')
        for check in checks:
            sub = get_object_or_404(Subatividade, pk=check)
            entsub = EntidadeSubatividade(entidade=model, subatividade=sub)
            entsub.save()

        messages.success(request, 'Atividades vinculadas ao estabelecimento com sucesso!')
        return redirect('entsub_list', id=id)

    return render(request, 'entsub/entsub_create.html', {'model': model, 'subs': subs})


@login_required
@permission_required('devisa.entsub_liberal_create')
def entsub_liberal_create(request, id):
    model = get_object_or_404(Entidade, pk=id)
    subs = Subatividade.objects.all()

    if request.POST:
        checks = request.POST.getlist('checks[]')
        for check in checks:
            sub = get_object_or_404(Subatividade, pk=check)
            entsub = EntidadeSubatividade(entidade=model, subatividade=sub)
            entsub.save()

        messages.success(request, 'Atividades vinculadas ao profissional liberal com sucesso!')
        return redirect('entsub_liberal_list', id=id)

    return render(request, 'entsub/entsub_liberal_create.html', {'model': model, 'subs': subs})

@login_required
@permission_required('devisa.entsub_autonomo_create')
def entsub_autonomo_create(request, id):
    model = get_object_or_404(Entidade, pk=id)
    subs = Subatividade.objects.all()

    if request.POST:
        checks = request.POST.getlist('checks[]')
        for check in checks:
            sub = get_object_or_404(Subatividade, pk=check)
            entsub = EntidadeSubatividade(entidade=model, subatividade=sub)
            entsub.save()

        messages.success(request, 'Atividades vinculadas ao profissional autônomo com sucesso!')
        return redirect('entsub_autonomo_list', id=id)

    return render(request, 'entsub/entsub_autonomo_create.html', {'model': model, 'subs': subs})


@login_required
@permission_required('devisa.entsub_delete')
def entsub_delete(request, id):
    model = get_object_or_404(EntidadeSubatividade, pk=id)

    if request.method == 'POST':
        model.delete()
        messages.success(request, 'Atividade desvinculada do estabelecimento com sucesso!')
        return redirect('entsub_list', model.entidade.id)

    return render(request, 'entsub/entsub_delete.html', {'model': model})


@login_required
@permission_required('devisa.entsub_liberal_delete')
def entsub_liberal_delete(request, id):
    model = get_object_or_404(EntidadeSubatividade, pk=id)

    if request.method == 'POST':
        model.delete()
        messages.success(request, 'Atividade desvinculada do profissional liberal com sucesso!')
        return redirect('entsub_liberal_list', model.entidade.id)

    return render(request, 'entsub/entsub_liberal_delete.html', {'model': model})


@login_required
@permission_required('devisa.entsub_autonomo_delete')
def entsub_autonomo_delete(request, id):
    model = get_object_or_404(EntidadeSubatividade, pk=id)

    if request.method == 'POST':
        model.delete()
        messages.success(request, 'Atividade desvinculada do profissional autônomo com sucesso!')
        return redirect('entsub_autonomo_list', model.entidade.id)

    return render(request, 'entsub/entsub_autonomo_delete.html', {'model': model})

# ------------- FIM ATIVIDADES DA ENTIDADE - ENTIDADESUBATIVIDADE ---------------- #


# ------------- RESPONSÁVEL TÉCNICO DA ENTIDADE - ENTIDADERESPONSAVELTECNICO ---------------- #
@login_required
@permission_required('devisa.entresptec_list')
def entresptec_list(request, id):
    model = get_object_or_404(Entidade, pk=id)
    entresptecs = EntidadeSubatividade.objects.filter(entidade=id, responsavel_tecnico__isnull=False).order_by('responsavel_tecnico')

    return render(request, 'entresptec/entresptec_list.html', {'model': model, 'entresptecs': entresptecs})


@login_required
@permission_required('devisa.entresptec_create')
def entresptec_create(request, id):
    model = get_object_or_404(Entidade, pk=id)

    if request.POST:
        ent_cpf = request.POST['cpf']
        ent_cpf2 = re.sub("[-/\.]", "", ent_cpf)
        if validate_CPF(ent_cpf) == 1:
            Entidade.clean(Entidade)
            model = Entidade.objects.filter(ent_cpf=ent_cpf)
            if not model:
                return redirect('cpf_responsaveltec_create', id=id, cpf=ent_cpf2)
            else:
                entidade = Entidade.objects.get(ent_cpf=ent_cpf)
                messages.info(request, 'O CPF informado já está cadastrado!')
                return redirect('cpf_responsaveltec_update', id=id, resp=entidade.id)

        else:
            messages.error(request, 'O CPF informado é inválido!')
            return redirect('entresptec_create', model.id)

    return render(request, 'entresptec/entresptec_create.html', {'model': model})



@login_required
@permission_required('devisa.cpf_responsaveltec_create')
def cpf_responsaveltec_create(request, id, cpf):
    model = get_object_or_404(Entidade, pk=id)
    form = EntidadeForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        messages.success(request, 'Responsável Técnico cadastrado com sucesso!')
        return redirect('entresptec_vincula_atvs', id, cpf)

    return render(request, 'entresptec/cpf_responsaveltec_create.html', {'cpf': cpf, 'form': form, 'model': model})


@login_required
@permission_required('devisa.cpf_responsaveltec_update')
def cpf_responsaveltec_update(request, id, resp):
    entidade = get_object_or_404(Entidade, pk=id)
    resptec = get_object_or_404(Entidade, pk=resp)
    form = EntidadeForm(request.POST or None, request.FILES or None, instance=resptec)

    if form.is_valid():
        form.save()
        messages.success(request, 'Responsável Técnico alterado com sucesso!')
        return redirect('entresptec_vincula_atvs', id, resptec.ent_cpf)

    return render(request, 'entresptec/cpf_responsaveltec_update.html', {'form': form, 'model': entidade})



@login_required
@permission_required('devisa.entresptec_vincula_atvs')
def entresptec_vincula_atvs(request, id, cpf):
    estabelecimento = get_object_or_404(Entidade, pk=id)
    resptec = Entidade.objects.get(ent_cpf=cpf)
    entsubs = EntidadeSubatividade.objects.filter(entidade=id)

    if request.POST:
        checks = request.POST.getlist('checks[]')
        for check in checks:
            entsub = get_object_or_404(EntidadeSubatividade, pk=check)
            entsub.responsavel_tecnico = resptec
            entsub.save()

        messages.success(request, 'Atividades do estabelecimento vinculadas ao responsável técnico com sucesso!')
        return redirect('entresptec_list', id=id)

    return render(request, 'entresptec/entresptec_vincula_atvs.html', {'estabelecimento': estabelecimento,
                                                                       'resptec': resptec, 'entsubs': entsubs})



@login_required
@permission_required('devisa.entresptec_delete')
def entresptec_delete(request, id):
    entsubresp = get_object_or_404(EntidadeSubatividade, pk=id)

    if request.method == 'POST':
        entsubresp.responsavel_tecnico = None
        entsubresp.save()
        messages.success(request, 'Responsável Técnico desvinculado de estabelecimento com sucesso!')
        return redirect('entresptec_list', entsubresp.entidade.id)

    return render(request, 'entresptec/entresptec_delete.html', {'model': entsubresp})

# ------------- FIM RESPONSÁVEL TÉCNICO DA ENTIDADE - ENTIDADERESPONSAVELTECNICO ---------------- #


# ------------- RESPONSÁVEL LEGAL DO ESTABELECIMENTO - ENTIDADERESPONSAVEL ---------------- #
@login_required
@permission_required('devisa.entresp_list')
def entresp_list(request, id):
    model = get_object_or_404(Entidade, pk=id)
    entresps = EntidadeResponsavel.objects.filter(entidade=id)

    return render(request, 'entresp/entresp_list.html', {'model': model, 'entresps': entresps})


@login_required
@permission_required('devisa.entresp_create')
def entresp_create(request, id):
    model = get_object_or_404(Entidade, pk=id)

    if request.POST:
        ent_cpf = request.POST['cpf']
        ent_cpf2 = re.sub("[-/\.]", "", ent_cpf)
        if validate_CPF(ent_cpf) == 1:
            Entidade.clean(Entidade)
            model = Entidade.objects.filter(ent_cpf=ent_cpf)
            if not model:
                return redirect('cpf_responsavel_create', id=id, cpf=ent_cpf2)
            else:
                entidade = Entidade.objects.get(ent_cpf=ent_cpf)
                messages.info(request, 'O CPF informado já está cadastrado!')
                return redirect('cpf_responsavel_update', id=id, resp=entidade.id)

        else:
            messages.error(request, 'O CPF informado é inválido!')
            return redirect('entresp_create', model.id)

    return render(request, 'entresp/entresp_create.html', {'model': model})



@login_required
@permission_required('devisa.cpf_responsavel_create')
def cpf_responsavel_create(request, id, cpf):
    model = get_object_or_404(Entidade, pk=id)
    form = EntidadeForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        responsavel = Entidade.objects.create(
            ent_tipo_entidade=request.POST.get('ent_tipo_entidade'),
            ent_cpf=request.POST.get('ent_cpf'),
            ent_nome_razao=request.POST.get('ent_nome_razao'),
            ent_rg=request.POST.get('ent_rg'),
            ent_orgao_exp=request.POST.get('ent_orgao_exp'),
            ent_dt_expedicao=request.POST.get('ent_dt_expedicao')
        )
        entidade_responsavel = EntidadeResponsavel.objects.create(entidade=model, responsavel=responsavel)
        messages.success(request, 'Responsável legal do estabelecimento cadastrado com sucesso!')
        return redirect('entresp_list', id)

    return render(request, 'entresp/cpf_responsavel_create.html', {'cpf': cpf, 'form': form, 'model': model})


@login_required
@permission_required('devisa.cpf_responsavel_update')
def cpf_responsavel_update(request,id, resp):
    entidade = get_object_or_404(Entidade, pk=id)
    responsavel = get_object_or_404(Entidade, pk=resp)

    form = EntidadeForm(request.POST or None, request.FILES or None, instance=responsavel)

    if form.is_valid():
        form.save()
        model = EntidadeResponsavel.objects.filter(entidade=entidade, responsavel=responsavel)
        if not model:
            entidade_responsavel = EntidadeResponsavel.objects.create(entidade=entidade, responsavel=responsavel)

        messages.success(request, 'Responsável legal do estabelecimento alterado com sucesso!')
        return redirect('entresp_list', id)

    return render(request, 'entresp/cpf_responsavel_update.html', {'form': form, 'model': entidade})



@login_required
@permission_required('devisa.entresp_delete')
def entresp_delete(request, id, estab):
    model = get_object_or_404(EntidadeResponsavel, pk=id)

    if request.method == 'POST':
        model.delete()
        messages.success(request, 'Responsável legal do estabelecimento retirado com sucesso!')
        return redirect('entresp_list', estab)

    return render(request, 'entresp/entresp_delete.html', {'model': model})

# ------------- FIM RESPONSÁVEL LEGAL DA ENTIDADE - ENTIDADERESPONSAVEL ---------------- #


# -------------------------- UNIDADES DA ENTIDADE -------------------------------------  #
@login_required
@permission_required('devisa.unid_list')
def unid_list(request, id):
    estabelecimento = get_object_or_404(Entidade, pk=id)
    unidades = EntidadeUnidade.objects.filter(estabelecimento=estabelecimento)

    return render(request, 'unidade/unid_list.html', {'estabelecimento': estabelecimento, 'unidades': unidades})


@login_required
@permission_required('devisa.unid_liberal_list')
def unid_liberal_list(request, id):
    estabelecimento = get_object_or_404(Entidade, pk=id)
    unidades = EntidadeUnidade.objects.filter(estabelecimento=estabelecimento)

    return render(request, 'unidade/unid_liberal_list.html', {'estabelecimento': estabelecimento, 'unidades': unidades})


@login_required
@permission_required('devisa.unid_autonomo_list')
def unid_autonomo_list(request, id):
    estabelecimento = get_object_or_404(Entidade, pk=id)
    unidades = EntidadeUnidade.objects.filter(estabelecimento=estabelecimento)

    return render(request, 'unidade/unid_autonomo_list.html', {'estabelecimento': estabelecimento, 'unidades': unidades})


@login_required
@permission_required('devisa.unid_create')
def unid_create(request, id):
    estabelecimento = get_object_or_404(Entidade, pk=id)
    form = EntidadeForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        unidade = form.save()
        entidade_unidade = EntidadeUnidade.objects.create(estabelecimento=estabelecimento, unidade=unidade)
        messages.success(request, 'Unidade do estabelecimento cadastrado com sucesso!')
        return redirect('unid_list', id)

    return render(request, 'unidade/unid_create.html', {'form': form, 'model': estabelecimento})


@login_required
@permission_required('devisa.unid_liberal_create')
def unid_liberal_create(request, id):
    estabelecimento = get_object_or_404(Entidade, pk=id)
    form = EntidadeForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        unidade = form.save()
        entidade_unidade = EntidadeUnidade.objects.create(estabelecimento=estabelecimento, unidade=unidade)
        messages.success(request, 'Unidade do profissional liberal cadastrado com sucesso!')
        return redirect('unid_liberal_list', id)

    return render(request, 'unidade/unid_liberal_create.html', {'form': form, 'model': estabelecimento})


@login_required
@permission_required('devisa.unid_autonomo_create')
def unid_autonomo_create(request, id):
    estabelecimento = get_object_or_404(Entidade, pk=id)
    form = EntidadeForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        unidade = form.save()
        entidade_unidade = EntidadeUnidade.objects.create(estabelecimento=estabelecimento, unidade=unidade)
        messages.success(request, 'Unidade do profissional autônomo cadastrado com sucesso!')
        return redirect('unid_autonomo_list', id)

    return render(request, 'unidade/unid_autonomo_create.html', {'form': form, 'model': estabelecimento})



@login_required
@permission_required('devisa.unid_update')
def unid_update(request, id):
    ent_unid = get_object_or_404(EntidadeUnidade, pk=id)
    estabelecimento = get_object_or_404(Entidade, pk=ent_unid.estabelecimento.id)
    unidade = get_object_or_404(Entidade, pk=ent_unid.unidade.id)
    form = EntidadeForm(request.POST or None, request.FILES or None, instance=unidade)

    if form.is_valid():
        form.save()
        messages.success(request, 'Unidade do estabelecimento alterado com sucesso!')
        return redirect('unid_list', estabelecimento.id)

    return render(request, 'unidade/unid_update.html', {'form': form, 'model': estabelecimento})


@login_required
@permission_required('devisa.unid_liberal_update')
def unid_liberal_update(request, id):
    ent_unid = get_object_or_404(EntidadeUnidade, pk=id)
    estabelecimento = get_object_or_404(Entidade, pk=ent_unid.estabelecimento.id)
    unidade = get_object_or_404(Entidade, pk=ent_unid.unidade.id)
    form = EntidadeForm(request.POST or None, request.FILES or None, instance=unidade)

    if form.is_valid():
        form.save()
        messages.success(request, 'Unidade do profissional liberal alterado com sucesso!')
        return redirect('unid_liberal_list', estabelecimento.id)

    return render(request, 'unidade/unid_liberal_update.html', {'form': form, 'model': estabelecimento})


@login_required
@permission_required('devisa.unid_autonomo_update')
def unid_autonomo_update(request, id):
    ent_unid = get_object_or_404(EntidadeUnidade, pk=id)
    estabelecimento = get_object_or_404(Entidade, pk=ent_unid.estabelecimento.id)
    unidade = get_object_or_404(Entidade, pk=ent_unid.unidade.id)
    form = EntidadeForm(request.POST or None, request.FILES or None, instance=unidade)

    if form.is_valid():
        form.save()
        messages.success(request, 'Unidade do profissional autônomo alterado com sucesso!')
        return redirect('unid_autonomo_list', estabelecimento.id)

    return render(request, 'unidade/unid_autonomo_update.html', {'form': form, 'model': estabelecimento})


@login_required
@permission_required('devisa.unid_delete')
def unid_delete(request, id):
    model = get_object_or_404(EntidadeUnidade, pk=id)
    unidade = get_object_or_404(Entidade, pk=model.unidade.id)
    id_estab = model.estabelecimento.id

    if request.POST:
        model.delete()
        unidade.delete()
        return redirect('unid_list', id_estab)

    return render(request, 'unidade/unid_delete.html', {'model': model})


@login_required
@permission_required('devisa.unid_liberal_delete')
def unid_liberal_delete(request, id):
    model = get_object_or_404(EntidadeUnidade, pk=id)
    unidade = get_object_or_404(Entidade, pk=model.unidade.id)
    id_estab = model.estabelecimento.id

    if request.POST:
        model.delete()
        unidade.delete()
        return redirect('unid_liberal_list', id_estab)

    return render(request, 'unidade/unid_liberal_delete.html', {'model': model})


@login_required
@permission_required('devisa.unid_autonomo_delete')
def unid_autonomo_delete(request, id):
    model = get_object_or_404(EntidadeUnidade, pk=id)
    unidade = get_object_or_404(Entidade, pk=model.unidade.id)
    id_estab = model.estabelecimento.id

    if request.POST:
        model.delete()
        unidade.delete()
        return redirect('unid_autonomo_list', id_estab)

    return render(request, 'unidade/unid_autonomo_delete.html', {'model': model})


@login_required
@permission_required('devisa.unid_view')
def unid_view(request, id):
    model = get_object_or_404(EntidadeUnidade, pk=id)

    return render(request, 'unidade/unid_view.html', {'model': model})


@login_required
@permission_required('devisa.unid_liberal_view')
def unid_liberal_view(request, id):
    model = get_object_or_404(EntidadeUnidade, pk=id)

    return render(request, 'unidade/unid_liberal_view.html', {'model': model})


@login_required
@permission_required('devisa.unid_autonomo_view')
def unid_autonomo_view(request, id):
    model = get_object_or_404(EntidadeUnidade, pk=id)

    return render(request, 'unidade/unid_autonomo_view.html', {'model': model})

# ----------------------- FIM UNIDADES DA ENTIDADE ------------------------------------  #


# ------------- ATIVIDADE TERCEIRIZADA DA ENTIDADE - ENTIDADERESPONSAVELTECNICO ---------------- #
@login_required
@permission_required('devisa.terceirizada_list')
def terceirizada_list(request, id):
    model = get_object_or_404(Entidade, pk=id)
    terceirizadas = EntidadeSubatividade.objects.filter(entidade=id, terceirizado__isnull=False).order_by('terceirizado')

    return render(request, 'entterc/terceirizada_list.html', {'model': model, 'terceirizadas': terceirizadas})


@login_required
@permission_required('devisa.terceirizada_create')
def terceirizada_create(request, id):
    model = get_object_or_404(Entidade, pk=id)

    if request.POST:
        ent_cnpj = request.POST['cnpj']
        ent_cnpj2 = re.sub("[-/\.]", "", ent_cnpj)
        if validate_CNPJ(ent_cnpj) == 1:
            Entidade.clean(Entidade)
            model = Entidade.objects.filter(ent_cnpj=ent_cnpj)
            if not model:
                return redirect('cnpj_terceirizada_create', id=id, cnpj=ent_cnpj2)
            else:
                entidade = Entidade.objects.get(ent_cnpj=ent_cnpj)
                messages.info(request, 'O CNPJ informado já está cadastrado!')
                return redirect('cnpj_terceirizada_update', id=id, terc_id=entidade.id)

        else:
            messages.error(request, 'O CNPJ informado é inválido!')
            return redirect('terceirizada_create', model.id)

    return render(request, 'entterc/terceirizada_create.html', {'model': model})


@login_required
@permission_required('devisa.cnpj_terceirizada_create')
def cnpj_terceirizada_create(request, id, cnpj):
    model = get_object_or_404(Entidade, pk=id)
    form = EntidadeForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        terceirizada = form.save()
        messages.success(request, 'Empresa terceirizada cadastrada com sucesso!')
        return redirect('terceirizada_vincula_atvs', id, terceirizada.id)

    return render(request, 'entterc/cnpj_terceirizada_create.html', {'cnpj': cnpj, 'form': form, 'model': model})


@login_required
@permission_required('devisa.cnpj_terceirizada_update')
def cnpj_terceirizada_update(request, id, terc_id):
    entidade = get_object_or_404(Entidade, pk=id)
    terceirizado = get_object_or_404(Entidade, pk=terc_id)
    form = EntidadeForm(request.POST or None, request.FILES or None, instance=terceirizado)

    if form.is_valid():
        form.save()
        messages.success(request, 'Empresa terceirizada alterada com sucesso!')
        return redirect('terceirizada_vincula_atvs', id, terc_id)

    return render(request, 'entterc/cnpj_terceirizada_update.html', {'form': form, 'model': entidade})



@login_required
@permission_required('devisa.terceirizada_vincula_atvs')
def terceirizada_vincula_atvs(request, id, terc_id):
    estabelecimento = get_object_or_404(Entidade, pk=id)
    terceirizado = get_object_or_404(Entidade, pk=terc_id)
    entsubs = EntidadeSubatividade.objects.filter(entidade=id)

    if request.POST:
        checks = request.POST.getlist('checks[]')
        for check in checks:
            entsub = get_object_or_404(EntidadeSubatividade, pk=check)
            entsub.terceirizado = terceirizado
            entsub.save()

        messages.success(request, 'As atividades marcadas foram terceirizadas com sucesso!')
        return redirect('terceirizada_list', id=id)

    return render(request, 'entterc/terceirizada_vincula_atvs.html', {'estabelecimento': estabelecimento,
                                                                       'terceirizada': terceirizado, 'entsubs': entsubs})


@login_required
@permission_required('devisa.terceirizada_delete')
def terceirizada_delete(request, id):
    entsub = get_object_or_404(EntidadeSubatividade, pk=id)

    if request.method == 'POST':
        entsub.terceirizado = None
        entsub.save()
        messages.success(request, 'Atividade desvinculada de empresa terceirizada com sucesso!')
        return redirect('terceirizada_list', entsub.entidade.id)

    return render(request, 'entterc/terceirizada_delete.html', {'model': entsub})

# ------------- FIM ATIVIDADE TERCEIRIZADA DA ENTIDADE - ENTIDADERESPONSAVELTECNICO ---------------- #


# ------------- ÁREA DE PRODUÇÃO ---------------- #
@login_required
@permission_required('devisa.areaproducao_list')
def areaproducao_list(request):
    model = Areaproducao.objects.all()

    return render(request, 'areaproducao/areaproducao_list.html', {'areaproducaos': model})


@login_required
@permission_required('devisa.areaproducao_view')
def areaproducao_view(request, id):
    model = get_object_or_404(Areaproducao, pk=id)
    return render(request, 'areaproducao/areaproducao_view.html', {'areaproducao': model})


@login_required
@permission_required('devisa.areaproducao_create')
def areaproducao_create(request):
    form = AreaproducaoForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        messages.success(request, 'Área de Produção cadastrada com sucesso!')
        return redirect('areaproducao_list')
    return render(request, 'areaproducao/areaproducao_create.html', {'form': form})


@login_required
@permission_required('devisa.areaproducao_update')
def areaproducao_update(request,id):
    model = get_object_or_404(Areaproducao, pk=id)
    form = AreaproducaoForm(request.POST or None, request.FILES or None, instance=model)

    if form.is_valid():
        form.save()
        messages.success(request, 'Área de Produção alterada com sucesso!')
        return redirect('areaproducao_list')

    return render(request, 'areaproducao/areaproducao_update.html', {'form': form})


@login_required
@permission_required('devisa.areaproducao_delete')
def areaproducao_delete(request, id):
    model = get_object_or_404(Areaproducao, pk=id)

    if request.method == 'POST':
        model.delete()
        messages.success(request, 'Área de Produção excluída com sucesso!')
        return redirect('areaproducao_list')

    return render(request, 'areaproducao/areaproducao_delete.html', {'model': model})
# ------------- FIM AREA DE PRODUÇÃO ---------------- #


# ------------- CLASSE DE PRODUÇÃO ---------------- #
@login_required
@permission_required('devisa.classeproducao_list')
def classeproducao_list(request):
    model = Classeproducao.objects.all()

    return render(request, 'classeproducao/classeproducao_list.html', {'classeproducaos': model})


@login_required
@permission_required('devisa.classeproducao_view')
def classeproducao_view(request, id):
    model = get_object_or_404(Classeproducao, pk=id)
    return render(request, 'classeproducao/classeproducao_view.html', {'classeproducao': model})


@login_required
@permission_required('devisa.classeproducao_create')
def classeproducao_create(request):
    form = ClasseproducaoForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        messages.success(request, 'Classe de Produção cadastrada com sucesso!')
        return redirect('classeproducao_list')
    return render(request, 'classeproducao/classeproducao_create.html', {'form': form})


@login_required
@permission_required('devisa.classeproducao_update')
def classeproducao_update(request,id):
    model = get_object_or_404(Classeproducao, pk=id)
    form = ClasseproducaoForm(request.POST or None, request.FILES or None, instance=model)

    if form.is_valid():
        form.save()
        messages.success(request, 'Classe de Produção alterada com sucesso!')
        return redirect('classeproducao_list')

    return render(request, 'classeproducao/classeproducao_update.html', {'form': form})


@login_required
@permission_required('devisa.classeproducao_delete')
def classeproducao_delete(request, id):
    model = get_object_or_404(Classeproducao, pk=id)

    if request.method == 'POST':
        model.delete()
        messages.success(request, 'Classe de Produção excluída com sucesso!')
        return redirect('classeproducao_list')

    return render(request, 'classeproducao/classeproducao_delete.html', {'model': model})

# ------------- FIM CLASSE DE PRODUÇÃO ---------------- #


# ------------- LINHA DE PRODUÇÃO ---------------- #
@login_required
@permission_required('devisa.linhaproducao_list')
def linhaproducao_list(request):
    model = Linhaproducao.objects.all()

    return render(request, 'linhaproducao/linhaproducao_list.html', {'linhaproducaos': model})


@login_required
@permission_required('devisa.linhaproducao_view')
def linhaproducao_view(request, id):
    model = get_object_or_404(Linhaproducao, pk=id)
    return render(request, 'linhaproducao/linhaproducao_view.html', {'linhaproducao': model})


@login_required
@permission_required('devisa.linhaproducao_create')
def linhaproducao_create(request):
    form = LinhaproducaoForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        messages.success(request, 'Linha de Produção cadastrada com sucesso!')
        return redirect('linhaproducao_list')
    return render(request, 'linhaproducao/linhaproducao_create.html', {'form': form})


@login_required
@permission_required('devisa.linhaproducao_update')
def linhaproducao_update(request,id):
    model = get_object_or_404(Linhaproducao, pk=id)
    form = LinhaproducaoForm(request.POST or None, request.FILES or None, instance=model)

    if form.is_valid():
        form.save()
        messages.success(request, 'Linha de Produção alterada com sucesso!')
        return redirect('linhaproducao_list')

    return render(request, 'linhaproducao/linhaproducao_update.html', {'form': form})


@login_required
@permission_required('devisa.linhaproducao_delete')
def linhaproducao_delete(request, id):
    model = get_object_or_404(Linhaproducao, pk=id)

    if request.method == 'POST':
        model.delete()
        messages.success(request, 'Linha de Produção excluída com sucesso!')
        return redirect('linhaproducao_list')

    return render(request, 'linhaproducao/linhaproducao_delete.html', {'model': model})

# ------------- FIM LINHA DE PRODUÇÃO ---------------- #


# ------------- FORMA DE PRODUÇÃO ---------------- #
@login_required
@permission_required('devisa.formaproducao_list')
def formaproducao_list(request):
    model = Formaproducao.objects.all()

    return render(request, 'formaproducao/formaproducao_list.html', {'formaproducaos': model})


@login_required
@permission_required('devisa.formaproducao_view')
def formaproducao_view(request, id):
    model = get_object_or_404(Formaproducao, pk=id)
    return render(request, 'formaproducao/formaproducao_view.html', {'formaproducao': model})


@login_required
@permission_required('devisa.formaproducao_create')
def formaproducao_create(request):
    form = FormaproducaoForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        messages.success(request, 'Forma de Produção cadastrada com sucesso!')
        return redirect('formaproducao_list')
    return render(request, 'formaproducao/formaproducao_create.html', {'form': form})


@login_required
@permission_required('devisa.formaproducao_update')
def formaproducao_update(request, id):
    model = get_object_or_404(Formaproducao, pk=id)
    form = FormaproducaoForm(request.POST or None, request.FILES or None, instance=model)

    if form.is_valid():
        form.save()
        messages.success(request, 'Forma de Produção alterada com sucesso!')
        return redirect('formaproducao_list')

    return render(request, 'formaproducao/formaproducao_update.html', {'form': form})


@login_required
@permission_required('devisa.formaproducao_delete')
def formaproducao_delete(request, id):
    model = get_object_or_404(Formaproducao, pk=id)

    if request.method == 'POST':
        model.delete()
        messages.success(request, 'Forma de Produção excluída com sucesso!')
        return redirect('formaproducao_list')

    return render(request, 'formaproducao/formaproducao_delete.html', {'model': model})

# ------------- FIM FORMA DE PRODUÇÃO ---------------- #


# ---------------------- ENTIDADE - LINHA DE PRODUÇÃO DA ENTIDADE ----------------------- #
@login_required
@permission_required('devisa.ent_linha_producao_list')
def ent_linha_producao_list(request, id):
    model = get_object_or_404(Entidade, pk=id)
    entfps = EntidadeFormaproducao.objects.filter(entidade=id)
    entcps = EntidadeClasseproducao.objects.filter(entidade=id)

    return render(request, 'entlp/ent_linha_producao_list.html', {'model': model, 'entfps': entfps, 'entcps': entcps})


@login_required
@permission_required('devisa.ent_forma_producao_create')
def ent_forma_producao_create(request, id):
    model = get_object_or_404(Entidade, pk=id)
    fps = Formaproducao.objects.all()

    if request.POST:
        checks = request.POST.getlist('checks[]')
        for check in checks:
            fp = get_object_or_404(Formaproducao, pk=check)
            entfp = EntidadeFormaproducao(entidade=model, forma_producao=fp)
            entfp.save()

        messages.success(request, 'Formas de Produção vinculadas ao estabelecimento com sucesso!')
        return redirect('ent_linha_producao_list', id=id)

    return render(request, 'entlp/ent_forma_producao_create.html', {'model': model, 'fps': fps})


@login_required
@permission_required('devisa.ent_classe_producao_create')
def ent_classe_producao_create(request, id):
    model = get_object_or_404(Entidade, pk=id)
    cps = Classeproducao.objects.all()

    if request.POST:
        checks = request.POST.getlist('checks[]')
        for check in checks:
            cp = get_object_or_404(Classeproducao, pk=check)
            entcp = EntidadeClasseproducao(entidade=model, classe_producao=cp)
            entcp.save()

        messages.success(request, 'Classes de Produção vinculadas ao estabelecimento com sucesso!')
        return redirect('ent_linha_producao_list', id=id)

    return render(request, 'entlp/ent_classe_producao_create.html', {'model': model, 'cps': cps})


@login_required
@permission_required('devisa.ent_forma_producao_delete')
def ent_forma_producao_delete(request, id):
    model = get_object_or_404(EntidadeFormaproducao, pk=id)

    if request.method == 'POST':
        model.delete()
        messages.success(request, 'Forma de Produção desvinculada do estabelecimento com sucesso!')
        return redirect('ent_linha_producao_list', model.entidade.id)

    return render(request, 'entlp/ent_forma_producao_delete.html', {'model': model})


@login_required
@permission_required('devisa.ent_classe_producao_delete')
def ent_classe_producao_delete(request, id):
    model = get_object_or_404(EntidadeClasseproducao, pk=id)

    if request.method == 'POST':
        model.delete()
        messages.success(request, 'Classe de Produção desvinculada do estabelecimento com sucesso!')
        return redirect('ent_linha_producao_list', model.entidade.id)

    return render(request, 'entlp/ent_classe_producao_delete.html', {'model': model})

# ------------------- FIM LINHA DE PRODUÇÃO DA ENTIDADE ---------------------- #