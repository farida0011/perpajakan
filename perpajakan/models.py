from django.db import models
from django.utils.text import slugify
from django.utils.timezone import now
from django.contrib.auth.models import User
# Create your models here.
class ModelWajib(models.Model):
	nama_lengkap	= models.CharField(max_length = 200)
	alamat	=models.CharField(max_length = 200)
	jenis_kelamin	=models.CharField(max_length = 25)
	pekerjaan	=models.CharField(max_length = 200)
	no_hp	=models.CharField(max_length = 14)

	published = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)
			
	def __str__(self):
		return "{}.{}".format(self.id, self.nama_lengkap)

		
class Modelkecamatan(models.Model):
	nama_kecamatan	= models.CharField(max_length = 200)
	nama_kelurahan	=models.CharField(max_length = 200)
	tanggal	=models.CharField(max_length = 13)

	published = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)
			
	def __str__(self):
		return "{}.{}".format(self.id, self.nama_kecamatan)

class Modeljenis(models.Model):
	nama_jenis	= models.CharField(max_length = 200)
	pembayaran_pajak	=models.CharField(max_length = 20)
	keterangan	=models.CharField(max_length = 1000)

	published = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)
			
	def __str__(self):
		return "{}.{}".format(self.id, self.nama_jenis)		

class ModelObjek(models.Model):
	no_pajak	= models.CharField(max_length = 200)
	nama_pajak	=models.CharField(max_length = 200)
	lokasi	=models.CharField(max_length = 200)
	kecamatan	=models.CharField(max_length = 200)
	kelurahan	=models.CharField(max_length = 200)
	tanggal	=models.CharField(max_length = 12)

	published = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)
			
	def __str__(self):
		return "{}.{}".format(self.id, self.no_pajak)		

class Modelbangunan(models.Model):
	nama_bangunan	= models.CharField(max_length = 200)
	nilai_jual	=models.CharField(max_length = 200)
	keterangan	=models.CharField(max_length = 1000)

	published = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)
			
	def __str__(self):
		return "{}.{}".format(self.id, self.nama_bangunan)				

class Modelbumi(models.Model):
	nama_kelompok	= models.CharField(max_length = 200)
	luas	=models.CharField(max_length = 200)
	nilai_jual	=models.CharField(max_length = 200)
	keterangan	=models.CharField(max_length = 1000)

	published = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)
			
	def __str__(self):
		return "{}.{}".format(self.id, self.nama_kelompok)						

class Modelsppt(models.Model):
	nama_lengkap	= models.CharField(max_length = 1000)
	nomor_pajak	=models.CharField(max_length = 200)
	nama_pajak	=models.CharField(max_length = 1000)
	luas_bumi	=models.CharField(max_length = 25)
	luas_bangunan	=models.CharField(max_length = 25)
	nama_bangunan	=models.CharField(max_length = 1000)
	nilai_jual	=models.CharField(max_length = 12)

	published = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)
			
	def __str__(self):
		return "{}.{}".format(self.id, self.nama_lengkap)								

class Modelpembayaranpajak(models.Model):
	nama_lengkap	= models.CharField(max_length = 1000)	
	jumlah_pembayaran	=models.CharField(max_length = 12)	
	nomor_pajak	=models.CharField(max_length = 200)	
	nama_pajak	=models.CharField(max_length = 1000)
	luas_bumi	=models.CharField(max_length = 25)
	luas_bangunan	=models.CharField(max_length = 25)		
	tahun_pajak	=models.CharField(max_length = 12)
	jatuh_tempo	=models.CharField(max_length = 12)
	denda	=models.CharField(max_length = 12)
	total_bayar	=models.CharField(max_length = 12)
	tanggal	=models.CharField(max_length = 12)
	status	=models.CharField(max_length = 50)

	published = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)
			
	def __str__(self):
		return "{}.{}".format(self.id, self.nama_lengkap)										


class ModeUpload(models.Model):
	nama_lengkap	= models.CharField(max_length = 200)
	nom_pajak	=models.CharField(max_length = 200)
	nama_pajak	=models.CharField(max_length = 500)
	upload	=models.ImageField(upload_to ='cover/', null=True)	

	published = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)
			
	def __str__(self):
		return "{}.{}".format(self.id, self.nama_lengkap)


#cara membuat model/atau database pada django

class ModelCoba(models.Model):
	nama_lengkap	= models.CharField(max_length = 200)
	nohp = models.CharField(max_length =12)

	published = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)
			
	def __str__(self):
		return "{}.{}".format(self.id, self.nama_lengkap)

	#def save(self):
	#	self.slug = slugify(self.nama_barang)
	#	super(Postmodel, self).save()

	#def get_absolute_url(self):
	#	url_slug = {
	#		'slug':self.slug,
	#	}
