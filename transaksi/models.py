import uuid

from django.db import models

from pendaftaran.models import Dokter, Pasien


class Transaksi(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # buat tarif app
    jenis_transaksi = models.CharField(max_length=100)
    pasien = models.ForeignKey(Pasien, on_delete=models.CASCADE)
    dokter = models.ForeignKey(Dokter, on_delete=models.CASCADE)
    biaya = models.FloatField()
