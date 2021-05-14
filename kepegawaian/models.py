from django.db import models


class Pendidikan(models.Model):
    jenjang_pendidikan = models.CharField(max_length=100)
    nama_institusi = models.CharField(max_length=100)
    jurusan = models.CharField(max_length=100)
    tanggal_ijazah = models.DateField()
    gelar = models.CharField(max_length=100)
    tahun_tamat = models.CharField(max_length=4)
    lampiran = models.FileField(upload_to='/media')

    def __str__(self):
        return '{} - {}'.format(self.nama_institusi, self.tahun_tamat)


class AlamatSaatIni(models.Model):
    alamat = models.CharField(max_length=500)
    kodepos = models.CharField(max_length=100)
    provinsi = models.CharField(max_length=100)
    kabupaten_kota = models.CharField(max_length=100)
    kecamatan = models.CharField(max_length=100)
    kelurahan = models.CharField(max_length=100)
    rt = models.CharField(max_length=3, default='000')
    rw = models.CharField(max_length=3, default='000')

    def __str__(self):
        return '{}, {}, {}, {}, {}, {}, {}, {}'.format(self.alamat, self.rt, self.rw, self.kelurahan, self.kecamatan,
                                                       self.kabupaten_kota, self.provinsi, self.kodepos)


class AlamatKTP(models.Model):
    alamat = models.CharField(max_length=500)
    rt = models.CharField(max_length=3, default='000')
    rw = models.CharField(max_length=3, default='000')
    kelurahan = models.CharField(max_length=100)
    kecamatan = models.CharField(max_length=100)
    kabupaten_kota = models.CharField(max_length=100)
    provinsi = models.CharField(max_length=100)
    kodepos = models.CharField(max_length=100)

    def __str__(self):
        return '{}, {}, {}, {}, {}, {}, {}, {}'.format(self.alamat, self.rt, self.rw, self.kelurahan, self.kecamatan,
                                                       self.kabupaten_kota, self.provinsi, self.kodepos)


class Kepegawaian(models.Model):
    nomor_pegawai = models.CharField(max_length=100)
    nik = models.CharField(max_length=15)
    nama_depan = models.CharField(max_length=200)
    nama_tengah = models.CharField(max_length=200)
    nama_belakang = models.CharField(max_length=200)
    nama_panggilan = models.CharField(max_length=100)
    tempat_lahir = models.CharField(max_length=100)
    tanggal_lahir = models.DateField()
    jenis_kelamin = models.CharField(max_length=100)
    gelar_depan = models.CharField(max_length=100)
    gelar_belakang = models.CharField(max_length=100)
    kewarganegaraan = models.CharField(max_length=3)
    suku_bangsa = models.CharField(max_length=100)
    alamat_saat_ini = models.ForeignKey(AlamatSaatIni, on_delete=models.CASCADE)
    alamat_KTP = models.ForeignKey(AlamatKTP, on_delete=models.CASCADE)
    agama = models.CharField(max_length=50)
    status_kawin = models.CharField(max_length=100)
    status_kepegawaian = models.CharField(max_length=100)
    pendidikan = models.ForeignKey(Pendidikan, on_delete=models.CASCADE)
    aktif = models.BooleanField(default=True)

    def __str__(self):
        return '{} - {}'.format(self.nomor_pegawai, self.nama_depan + ' ' + self.nama_belakang)

    def save(self, *args, **kwargs):
        return super(self, Kepegawaian).save(*args, **kwargs)
