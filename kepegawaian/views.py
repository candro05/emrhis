from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from emrhis.decorators import allowed_users
from kepegawaian.forms import AddDataPegawaiForm, EditDataPegawaiForm
from kepegawaian.models import Kepegawaian

# list data pegawai
@login_required(login_url='/login')
@allowed_users(allowed_roles=[])
def data_pegawai(request):
    queryset = Kepegawaian.objects.all()
    context = {
        'queryset':queryset,
    }
    return render(request, 'Kepegawaian/', context)

# tambah data pegawai
@login_required(login_url='/login')
@allowed_users(allowed_roles=[])
def add_data_pegawai(request):
    form = AddDataPegawaiForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'form':form,
    }
    return render(request, 'kepegawaian/', context)

# edit data pegawai
@login_required(login_url='/login')
@allowed_users(allowed_roles=[])
def edit_data_pegawai(request, id):
    data_pegawai = get_object_or_404(Kepegawaian, id=id)
    form = EditDataPegawaiForm(request.POST or None)
    if form.is_valid():
        form.save()
        return data_pegawai(request)

    context = {
        'form':form,
    }
    return render(request, 'kepegawaian/', context)

# delete data pegawai
@login_required(login_url='/login')
@allowed_users(allowed_roles=[])
def delete_data_pegawai(request, id):
    data_pegawai = get_object_or_404(Kepegawaian, id=id)
    if request.method == 'POST':
        data_pegawai.delete()
        return data_pegawai(request)
    context = {}
    return render(request, 'kepegawaian/', context)
