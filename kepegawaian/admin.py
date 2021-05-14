from django.contrib import admin

from .models import Pendidikan, AlamatSaatIni, AlamatKTP, Kepegawaian

admin.site.register(Pendidikan, AlamatSaatIni, AlamatKTP, Kepegawaian)