from django.db import models
from django.contrib.auth.models import User
import time
import os



class Karyawan(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True) 
    nama = models.CharField(max_length=100, blank=True, null=True)
    NIP = models.CharField(max_length=20, blank=True, null=True)
    PRIA = 'PR'
    WANITA = 'WN'
    JK_CHOICES  = (
        (PRIA, 'Pria'),
        (WANITA, 'Wanita'),

    )
    jenis_kelamin = models.CharField(
        max_length=2,
        choices=JK_CHOICES,
        default=PRIA,
    )
    born_date = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    agama = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.nama

    class Meta:
        db_table = 'karyawan'
        ordering = ['id']

class Kecerdasan(models.Model):
    karyawan = models.OneToOneField(Karyawan, on_delete=models.CASCADE, related_name='kecerdasans', blank=True, null=True)     
    sistematika_berfikir = models.CharField(max_length=5)
    konsentrasi = models.IntegerField(max_length=5, blank=True, null=True)
    logika_praktis = models.IntegerField(max_length=5, blank=True, null=True)
    imajinasi_kreatif = models.IntegerField(max_length=5, blank=True, null=True)
    antisipasi = models.IntegerField(max_length=5, blank=True, null=True)

    def __str__(self):
        return self.karyawan.nama

    class Meta:
        db_table = 'kecerdasan'
        ordering = ['id']


class MasaKerja(models.Model):
    karyawan = models.OneToOneField(Karyawan, on_delete=models.CASCADE, related_name='masakerjas', blank=True, null=True) 
    nol_sd_empat = models.CharField(max_length=5, blank=True, null=True)
    lima_sd_delapan = models.IntegerField(max_length=5, blank=True, null=True)
    sembilan_sd_tigaenam= models.IntegerField(max_length=5, blank=True, null=True)
    tigabelas_sd_enambelas = models.IntegerField(max_length=5, blank=True, null=True)
    tujuhbelas_sd_duapuluh = models.IntegerField(max_length=5, blank=True, null=True)
    duasatu_sd_duaempat = models.IntegerField(max_length=5, blank=True, null=True)
    dualima_sd_duadelapan = models.IntegerField(max_length=5, blank=True, null=True)
    duasembilan_sd_tigadua = models.IntegerField(max_length=5, blank=True, null=True)
    tigatiga_sd_tigaenam = models.IntegerField(max_length=5, blank=True, null=True)

    def __str__(self):
        return self.karyawan.nama

    class Meta:
        db_table = 'masakerja'
        ordering = ['id']


class PendidikanTerakhir(models.Model):
    karyawan = models.OneToOneField(Karyawan, on_delete=models.CASCADE, related_name='pendidikanterakhirs', blank=True, null=True) 
    SD = models.CharField(max_length=5, blank=True, null=True)
    SMP = models.IntegerField(max_length=5, blank=True, null=True)
    SMA = models.IntegerField(max_length=5, blank=True, null=True)
    DIII = models.IntegerField(max_length=5, blank=True, null=True)
    Strata_satu = models.IntegerField(max_length=5, blank=True, null=True)
    Strata_dua = models.IntegerField(max_length=5, blank=True, null=True)

    def __str__(self):
        return self.karyawan.nama

    class Meta:
        db_table = 'pendidikanterakhir'
        ordering = ['id']

class Prilaku(models.Model):
    karyawan = models.OneToOneField(Karyawan, on_delete=models.CASCADE, related_name='prilakus', blank=True, null=True) 
    dominance = models.CharField(max_length=5, blank=True, null=True)
    influences = models.IntegerField(max_length=5, blank=True, null=True)
    steadines = models.IntegerField(max_length=5, blank=True, null=True)
    compliance = models.IntegerField(max_length=5, blank=True, null=True)

    def __str__(self):
        return self.karyawan.nama

    class Meta:
        db_table = 'prilaku'
        ordering = ['id']

class SikapKerja(models.Model):
    karyawan = models.OneToOneField(Karyawan, on_delete=models.CASCADE, related_name='sikapkerjas', blank=True, null=True) 
    energi_psikis = models.CharField(max_length=5, blank=True, null=True)
    ketelitian = models.IntegerField(max_length=5, blank=True, null=True)
    kehati_hatian = models.IntegerField(max_length=5, blank=True, null=True)
    pengendalian_prasaan = models.IntegerField(max_length=5, blank=True, null=True)
    dorongan_berprestasi = models.IntegerField(max_length=5, blank=True, null=True)

    def __str__(self):
        return self.karyawan.nama

    class Meta:
        db_table = 'sikapkerja'
        ordering = ['id'] 


class PDF(models.Model):
    pdf = models.FileField(upload_to='pdffiles/', blank=True, null=True)





