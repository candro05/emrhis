import uuid

from django.db import models
from simple_history.models import HistoricalRecords

GENDER_CHOICES = (
    ('L', 'Laki-Laki'),
    ('P', 'Perempuan'),
)

AGAMA_CHOICES = (
    ('I', 'Islam'),
    ('K', 'Khatolik'),
    ('P', 'Protestan'),
    ('H', 'Hindu'),
    ('B', 'Budha'),
    ('L', 'Lain-Lain'),
)

STATUS_PERIKSA_CHOICES = (
    ('55', 'Sudah Diperiksa'),
    ('99', 'Batal'),
    ('00', 'Belum Diperiksa'),
)

STATUS_ANAMNESE_CHOICES = (
    ('00', 'Belum Anemnese Perawat'),
    ('55', 'Sudah Anamnese Perawat'),
)


class Provinsi(models.Model):
    nama = models.CharField(max_length=100)

    def __str__(self):
        return self.nama


class KabupatenKota(models.Model):
    nama = models.CharField(max_length=100)

    def __str__(self):
        return self.nama


class Kelurahan(models.Model):
    nama = models.CharField(max_length=100)

    def __str__(self):
        return self.nama


class Pasien(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    rekam_medis = models.CharField(max_length=6)
    nama = models.CharField(max_length=200)
    nik = models.CharField(max_length=16)
    tempat_lahir = models.CharField(max_length=200)
    tgl_lahir = models.DateField()
    no_bpjs = models.CharField(max_length=13)
    no_asuransi = models.CharField(max_length=15)
    jenis_kelamin = models.CharField(max_length=10, choices=GENDER_CHOICES)
    status_kawin = models.CharField(max_length=50)
    agama = models.CharField(max_length=10, choices=AGAMA_CHOICES)
    suku = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, blank=True, null=True)
    alamat_KTP = models.CharField(max_length=200)
    alamat_domisili = models.CharField(max_length=200)
    propinsi = models.CharField(max_length=10)
    kab_kota = models.CharField(max_length=10)
    kecamatan = models.CharField(max_length=10)
    kelurahan = models.CharField(max_length=10)
    kode_pos = models.CharField(max_length=10)
    rt = models.CharField(max_length=10)
    rw = models.CharField(max_length=10)
    pekerjaan = models.CharField(max_length=200)
    pendidikan = models.CharField(max_length=100)
    aktif = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    user_created = models.CharField(max_length=100)
    history = HistoricalRecords()

    def __str__(self):
        return self.nama

    def save(self, *args, **kwargs):
        return super(self, Pasien).save(*args, **kwargs)

class Registrasi(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    transaksi = models.ForeignKey(Transaksi, on_delete=models.CASCADE)
    no_pedaftaran = models.CharField(max_length=10)
    rekam_medis = models.CharField(max_length=10)
    kode_dokter = models.CharField(max_length=16)
    kode_klinik = models.CharField(max_length=200)
    tgl_daftar = models.DateField(null=True)
    no_antrian = models.CharField(max_length=15)
    status_periksa = models.CharField(max_length=10, choices=STATUS_PERIKSA_CHOICES)
    status_anamnese = models.CharField(max_length=10, choices=STATUS_ANAMNESE_CHOICES)
    penjamin = models.CharField(max_length=10)
    aktif = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    user_created = models.CharField(max_length=100)
    history = HistoricalRecords()

    def __str__(self):
        return self.no_pedaftaran

    def save(self, *args, **kwargs):
        return super(self, Registrasi).save(*args, **kwargs)

       
class Poliklinik(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    kode_klinik = models.CharField(max_length=10)
    nama_klinik = models.CharField(max_length=100)
    nomor_ruang = models.CharField(max_length=10)
    poli_bpjs = models.CharField(max_length=10)
    aktif = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    user_created = models.CharField(max_length=100)
    history = HistoricalRecords()


    def __str__(self):
        return self.nama_klinik


class Dokter(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    kode_dokter = models.CharField(max_length=10)
    nama_dokter = models.CharField(max_length=100)
    no_sip = models.CharField(max_length=20)
    kode_klinik = models.CharField(max_length=10)
    alamat = models.CharField(max_length=100)
    no_telp = models.CharField(max_length=12)
    aktif = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    user_created = models.CharField(max_length=100)
    history = HistoricalRecords()


    def __str__(self):
        return self.nama_dokter
  