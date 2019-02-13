from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.utils.translation import ugettext as _
from .forms import StatusForm, FaseForm, SistemaForm, DocumentoForm, SistemaFaseForm, ProfileForm
from django.contrib import messages
from .models import Status, Fase, Sistema, Documento, SistemaFase, Profile
from django.conf import settings
import os
from django.contrib.auth.models import Permission, Group, User




# Create your views here.
@login_required
def home(request):
    return render(request, 'index.html')


def my_logout(request):
    logout(request)
    return redirect('home')


@login_required
@permission_required('sistemasfvs.perfil')
def perfil(request):
    user = request.user
    perms = Permission.objects.filter(user=user)
    groups = Group.objects.filter(user=user)

    if request.GET:
        usuario = get_object_or_404(User, pk=user.id)
        usuario.email = request.GET.get('email')
        usuario.first_name = request.GET.get('first_name')
        usuario.last_name = request.GET.get('last_name')
        usuario.save()
        messages.success(request, 'Informações do perfil salvas com sucesso!')
        return redirect('perfil')

    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, _('Your password was successfully updated!'))
            return redirect('perfil')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        form = PasswordChangeForm(request.user)

    return render(request, 'perfil.html', {'perms': perms, 'groups': groups, 'form': form, 'perfil': perfil})


# @login_required
# @permission_required('sistemasfvs.perfil_altera_senha')
# def perfil_altera_senha(request):
#
#     if request.method == 'POST':
#         form = PasswordChangeForm(request.user, request.POST)
#         if form.is_valid():
#             user = form.save()
#             update_session_auth_hash(request, user)
#             messages.success(request, _('Your password was successfully updated!'))
#             return redirect('perfil')
#         else:
#             messages.error(request, _('Please correct the error below.'))
#     else:
#         form = PasswordChangeForm(request.user)
#
#     # return render(request, 'accounts/change_password.html', {'form': form})


# ------------- STATUS ---------------- #
@login_required
@permission_required('sistemasfvs.status_list')
def status_list(request):
    model = Status.objects.all()
    q = request.GET.get('pesquisar_por')
    if q is not None:
        model = model.filter(Q(st_nome__icontains=q) | Q(st_descricao__icontains=q))

    return render(request, 'status/status_list.html', {'status': model})


@login_required
@permission_required('sistemasfvs.status_view')
def status_view(request, id):
    model = get_object_or_404(Status, pk=id)
    return render(request, 'status/status_view.html', {'status': model})


@login_required
@permission_required('sistemasfvs.status_create')
def status_create(request):
    form = StatusForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        messages.success(request, 'Status cadastrado com sucesso!')
        return redirect('/status_list')
    return render(request, 'status/status_create.html', {'form': form})


@login_required
@permission_required('sistemasfvs.status_update')
def status_update(request,id):
    model = get_object_or_404(Status, pk=id)
    form = StatusForm(request.POST or None, request.FILES or None, instance=model)

    if form.is_valid():
        form.save()
        messages.success(request, 'Status alterado com sucesso!')
        return redirect('/status_list')

    return render(request, 'status/status_update.html', {'form': form})


@login_required
@permission_required('sistemasfvs.status_delete')
def status_delete(request, id):
    model = get_object_or_404(Status, pk=id)

    if request.method == 'POST':
        model.delete()
        messages.success(request, 'Status excluído com sucesso!')
        return redirect('/status_list')

    return render(request, 'status/status_delete.html', {'model': model})


# ------------ FASE --------------- #
@login_required
@permission_required('sistemasfvs.fase_list')
def fase_list(request):
    model = Fase.objects.all()
    q = request.GET.get('pesquisar_por')
    if q is not None:
        model = model.filter(Q(fase_nome__icontains=q) | Q(fase_descricao__icontains=q))

    return render(request, 'fase/fase_list.html', {'fases': model})


@login_required
@permission_required('sistemasfvs.fase_view')
def fase_view(request,id):
    model = get_object_or_404(Fase, pk=id)
    return render(request, 'fase/fase_view.html', {'fase': model})


@login_required
@permission_required('sistemasfvs.fase_create')
def fase_create(request):
    form = FaseForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        messages.success(request, 'Fase cadastrada com sucesso!')
        return redirect('/fase_list')
    return render(request, 'fase/fase_create.html', {'form': form})


@login_required
@permission_required('sistemasfvs.fase_add')
def fase_add(request,id):
    form = SistemaFaseForm(request.POST or None, request.FILES or None)
    sistema = get_object_or_404(Sistema, pk=id)

    if form.is_valid():
        form.save()
        messages.success(request, 'Fase do projeto alterada com sucesso!')
        return redirect('sistema_fases',id=id)
    return render(request, 'fase/fase_add.html', {'form': form, 'sistema': sistema})


@login_required
@permission_required('sistemasfvs.fase_sf_delete')
def fase_sf_delete(request,id):
    model = get_object_or_404(SistemaFase, pk=id)
    idsistema = model.sistema.id

    if request.method == 'POST':
        model.delete()
        messages.success(request, 'Fase excluída do projeto com sucesso!')
        return redirect('sistema_fases',id=idsistema)

    return render(request, 'fase/fase_sf_delete.html', {'model': model})


@login_required
@permission_required('sistemasfvs.fase_sf_update')
def fase_sf_update(request,id):
    model = get_object_or_404(SistemaFase, pk=id)
    form = SistemaFaseForm(request.POST or None, request.FILES or None, instance=model)

    if form.is_valid():
        form.save()
        messages.success(request, 'Fase do projeto alterada com sucesso!')
        return redirect('sistema_fases',id=model.sistema.id)

    return render(request, 'fase/fase_sf_update.html', {'form': form, 'model': model})


@login_required
@permission_required('sistemasfvs.fase_update')
def fase_update(request,id):
    model = get_object_or_404(Fase, pk=id)
    form = FaseForm(request.POST or None, request.FILES or None, instance=model)

    if form.is_valid():
        form.save()
        messages.success(request, 'Fase alterada com sucesso!')
        return redirect('/fase_list')

    return render(request, 'fase/fase_update.html', {'form': form})


@login_required
@permission_required('sistemasfvs.fase_delete')
def fase_delete(request,id):
    model = get_object_or_404(Fase, pk=id)

    if request.method == 'POST':
        model.delete()
        messages.success(request, 'Fase excluída com sucesso!')
        return redirect('/fase_list')

    return render(request, 'fase/fase_delete.html', {'model': model})



# ------------ SISTEMA --------------- #
@login_required
@permission_required('sistemasfvs.sistema_list')
def sistema_list(request):
    model = Sistema.objects.all()
    q = request.GET.get('pesquisar_por')
    if q is not None:
        model = model.filter(Q(sis_nome__icontains=q) | Q(sis_descricao__icontains=q))

    return render(request, 'sistema/sistema_list.html', {'sistemas': model})


@login_required
@permission_required('sistemasfvs.sistema_view')
def sistema_view(request,id):
    model = get_object_or_404(Sistema, pk=id)
    return render(request, 'sistema/sistema_view.html', {'sistema': model})


@login_required
@permission_required('sistemasfvs.sistema_create')
def sistema_create(request):
    form = SistemaForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        messages.success(request, 'Sistema cadastrado com sucesso!')
        return redirect('/sistema_list')
    return render(request, 'sistema/sistema_create.html', {'form': form})


@login_required
@permission_required('sistemasfvs.sistema_update')
def sistema_update(request,id):
    model = get_object_or_404(Sistema, pk=id)
    form = SistemaForm(request.POST or None, request.FILES or None, instance=model)

    if form.is_valid():
        form.save()
        messages.success(request, 'Sistema alterado com sucesso!')
        return redirect('/sistema_list')

    return render(request, 'sistema/sistema_update.html', {'form': form})


@login_required
@permission_required('sistemasfvs.sistema_delete')
def sistema_delete(request,id):
    model = get_object_or_404(Sistema, pk=id)

    if request.method == 'POST':
        model.delete()
        messages.success(request, 'Sistema excluído com sucesso!')
        return redirect('/sistema_list')

    return render(request, 'sistema/sistema_delete.html', {'model': model})


@login_required
@permission_required('sistemasfvs.sistema_doctos')
def sistema_doctos(request,id):
    model = get_object_or_404(Sistema, pk=id)
    documentos = Documento.objects.all().filter(sistema_cod_fk=id)

    return render(request, 'sistema/sistema_doctos.html', {'model': model, 'documentos': documentos})


@login_required
@permission_required('sistemasfvs.sistema_fases')
def sistema_fases(request, id):
    model = get_object_or_404(Sistema, pk=id)
    sisfases = SistemaFase.objects.all().filter(sistema=id)

    return render(request, 'sistema/sistema_fases.html', {'model': model, 'sisfases': sisfases})



# ---------------- DOCUMENTOS -------------------- #
@login_required
@permission_required('sistemasfvs.documento_create')
def documento_create(request,id):
    form = DocumentoForm(request.POST or None, request.FILES or None)
    model = get_object_or_404(Sistema, pk=id)

    if form.is_valid():
        form.save()
        messages.success(request, 'Documento cadastrado com sucesso!')
        return redirect('sistema_doctos', id=id)

    return render(request, 'documento/documento_create.html', {'form': form, 'model': model})


@login_required
@permission_required('sistemasfvs.documento_view')
def documento_view(request,sis_id,id):
    model = get_object_or_404(Documento, pk=id)
    sistema = get_object_or_404(Sistema, pk=sis_id)
    return render(request, 'documento/documento_view.html', {'documento': model, 'sis': sistema})


@login_required
@permission_required('sistemasfvs.documento_update')
def documento_update(request,sis_id,id):
    model = get_object_or_404(Documento, pk=id)
    sistema = get_object_or_404(Sistema, pk=sis_id)
    form = DocumentoForm(request.POST or None, request.FILES or None, instance=model)

    if form.is_valid():
        form.save()
        messages.success(request, 'Documento alterado com sucesso!')
        return redirect('sistema_doctos',id=sis_id)

    return render(request, 'documento/documento_update.html', {'form': form, 'sis': sistema, 'model': model})


@login_required
@permission_required('sistemasfvs.documento_delete')
def documento_delete(request,sis_id,id):
    model = get_object_or_404(Documento, pk=id)
    sistema = get_object_or_404(Sistema, pk=sis_id)

    if request.method == 'POST':
        os.remove(os.path.join(settings.MEDIA_ROOT, model.doc_file.name))
        model.delete()
        messages.success(request, 'Documento excluído com sucesso!')
        return redirect('sistema_doctos',id=sis_id)

    return render(request, 'documento/documento_delete.html', {'model': model, 'sistema': sistema})



@login_required
@permission_required('sistemasfvs.altera_foto')
def altera_foto(request):
    perfil = get_object_or_404(Profile, pk=request.user.id)
    form = ProfileForm(request.POST or None, request.FILES or None, instance=perfil)

    if form.is_valid():
        form.save()
        messages.success(request, 'Foto do perfil alterada com sucesso!')
        return redirect('perfil')

    return redirect('perfil')