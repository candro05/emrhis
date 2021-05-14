from django.contrib import admin
from .models import Pasien, Registrasi, Poliklinik,Dokter

admin.site.register(Pasien)
admin.site.register(Registrasi)
admin.site.register(Poliklinik)
admin.site.register(Dokter)