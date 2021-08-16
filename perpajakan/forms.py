from django import forms
from .models import ModelWajib, Modelkecamatan, Modeljenis, ModelObjek, Modelbangunan, Modelbumi, Modelsppt, Modelpembayaranpajak, ModeUpload

class FormWajib(forms.ModelForm):
	class Meta:
		model = ModelWajib
		fields = [
			'nama_lengkap',
			'alamat',
			'jenis_kelamin',
			'pekerjaan',
			'no_hp',
		]

class FormKecamatan(forms.ModelForm):
	class Meta:
		model = Modelkecamatan
		fields = [
			'nama_kecamatan',
			'nama_kelurahan',
			'tanggal',
		]	
			
class FormJenis(forms.ModelForm):
	class Meta:
		model = Modeljenis
		fields = [
			'nama_jenis',
			'pembayaran_pajak',
			'keterangan',
		]				
class FormObjek(forms.ModelForm):
	class Meta:
		model = ModelObjek
		fields = [
			'no_pajak',
			'nama_pajak',
			'lokasi',
			'kecamatan',
			'kelurahan',
			'tanggal',
		]						

class FormBangunan(forms.ModelForm):
	class Meta:
		model = Modelbangunan
		fields = [
			'nama_bangunan',
			'nilai_jual',
			'keterangan',
		]								

class FormBumi(forms.ModelForm):
	class Meta:
		model = Modelbumi
		fields = [
			'nama_kelompok',
			'luas',
			'nilai_jual',
			'keterangan',
		]								
class FormSPPT(forms.ModelForm):
	class Meta:
		model = Modelsppt
		fields = [
			'nama_lengkap',
			'nomor_pajak',
			'nama_pajak',
			'luas_bumi',
			'luas_bangunan',
			'nama_bangunan',
			'nilai_jual',
		]
class Formpembayaran(forms.ModelForm):
	class Meta:
		model = Modelpembayaranpajak
		fields = [
			'nama_lengkap',			
			'jumlah_pembayaran',			
			'nomor_pajak',			
			'nama_pajak',
			'luas_bumi',
			'luas_bangunan',			
			'tahun_pajak',
			'jatuh_tempo',
			'denda',
			'total_bayar',
			'tanggal',
			'status',
		]

class FormUpload(forms.ModelForm):
	class Meta:
		model = ModeUpload
		fields = [
			'nama_lengkap',			
			'nom_pajak',			
			'nama_pajak',
			'upload',			
		]





