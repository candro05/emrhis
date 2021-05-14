from django import forms

from kepegawaian.models import Kepegawaian

# form untuk add data pegawai
class AddDataPegawaiForm(forms.ModelForm):
    class Meta:
        model = Kepegawaian
        fields = '__all__'

# form untuk edit data pegawai
class EditDataPegawaiForm(forms.ModelForm):
    class Meta:
        model = Kepegawaian
        fields = '__all__'
