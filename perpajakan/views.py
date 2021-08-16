from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import ModelWajib, Modelkecamatan, Modeljenis, ModelObjek, Modelbangunan, Modelbumi, Modelsppt, Modelpembayaranpajak, ModeUpload
from .forms import FormWajib, FormKecamatan, FormJenis, FormObjek, FormBangunan, FormBumi, FormSPPT, FormUpload

IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']

def index(request):
	context = {
	'page_title':'Login',
	}
	#print(request.user)
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('Home')
		else:
			return redirect('index')

	return render(request, 'index.html',  context)

def HomeView(request):
	context = {
	'page_title':'Home',
	}
	return render(request, 'Home.html',  context)

def LogoutView(request):
	context = {
	'page_title':'logout',
	}
	if request.method == "POST":
		if request.POST["logout"] == "Submit":	
			logout(request)

		return redirect('index')

	return render(request, 'logout.html',  context)
#---------------------------
#------------------ Wajib Pajak
def WajibView(request):
	tampil_data = ModelWajib.objects.all()
	context = {
	'page_title':'Wajib',
	'tampil_data': tampil_data,
	}
	return render(request, 'Master_data/Data_wajib/tabel.html',  context)
def TambahWajibView(request):
	if request.method == 'POST':
		ModelWajib.objects.create(
			nama_lengkap = request.POST['nama_lengkap'],
			alamat = request.POST['alamat'],
			jenis_kelamin = request.POST['jk'],
			pekerjaan = request.POST['pekerjaan'],
			no_hp = request.POST['no_hp'],			
			)
		return HttpResponseRedirect("/wajib/")
	context = {
	'page_title':'Wajib',
	
	}
	return render(request, 'Master_data/Data_wajib/input.html',  context)	
def hapuswajibView(request, hapusj_id):
	ModelWajib.objects.filter(id=hapusj_id).delete()
	return redirect('wajib')	
def EditwajibView(request, editw_id):	
	Edit_wajib = ModelWajib.objects.get(id=editw_id)

	data = {
		'nama_lengkap'	: Edit_wajib.nama_lengkap,		
		'alamat'	: Edit_wajib.alamat,		
		'jenis_kelamin'	: Edit_wajib.jenis_kelamin,		
		'pekerjaan'	: Edit_wajib.pekerjaan,		
		'no_hp'	: Edit_wajib.no_hp,		
	}
	akun_form = FormWajib(request.POST or None, initial=data, instance=Edit_wajib)

	if request.method == 'POST':
		if akun_form.is_valid():
			akun_form.save()
			return redirect('wajib')

	#post_form = PostForm()
	context = {
	'page_title':'Tabel',	
	'akun_form':akun_form,
	}
	return render(request, 'Master_data/Data_wajib/edit.html',  context)	
	#---------------------------
#------------------ Wajib Pajak
def KecamatanView(request):
	tampil_kecamatan = Modelkecamatan.objects.all()
	context = {
	'page_title':'Kecamatan',
	'tampil_kecamatan': tampil_kecamatan,
	}
	return render(request, 'Master_data/Data_kecamatan/tabel.html',  context)
def TambahkecamatanView(request):
	if request.method == 'POST':
		Modelkecamatan.objects.create(
			nama_kecamatan = request.POST['nama_kecamatan'],
			nama_kelurahan = request.POST['nama_kelurahan'],
			tanggal = request.POST['tanggal'],			
			)
		return HttpResponseRedirect("/kecamatan/")
	context = {
	'page_title':'Wajib',
	
	}
	return render(request, 'Master_data/Data_kecamatan/input.html',  context)		
def hapuskecamatanView(request, hapusk_id):
	Modelkecamatan.objects.filter(id=hapusk_id).delete()
	return redirect('kecamatan')		
def EditkecamatanView(request, editk_id):	
	Edit_kecamatan = Modelkecamatan.objects.get(id=editk_id)

	data = {
		'nama_kecamatan'	: Edit_kecamatan.nama_kecamatan,		
		'nama_kelurahan'	: Edit_kecamatan.nama_kelurahan,		
		'tanggal'	: Edit_kecamatan.tanggal,		
	}
	form_kecamatan = FormKecamatan(request.POST or None, initial=data, instance=Edit_kecamatan)

	if request.method == 'POST':
		if form_kecamatan.is_valid():
			form_kecamatan.save()
			return redirect('kecamatan')

	context = {
	'page_title':'Tabel',	
	'form_kecamatan':form_kecamatan,
	}
	return render(request, 'Master_data/Data_kecamatan/edit.html',  context)		

#------------------ Wajib jenis
def JenisView(request):
	tampil_jenis = Modeljenis.objects.all()
	context = {
	'page_title':'Tabel',
	'tampil_jenis': tampil_jenis,
	}
	return render(request, 'Master_data/Data_jenis/tabel.html',  context)	

def hapusjenisView(request, hapusje_id):
	Modeljenis.objects.filter(id=hapusje_id).delete()
	return redirect('jenis')		

def TambahjenisView(request):
	if request.method == 'POST':
		Modeljenis.objects.create(
			nama_jenis = request.POST['nama_jenis'],
			pembayaran_pajak = request.POST['pembayaran'],
			keterangan = request.POST['keterangan'],			
			)
		return HttpResponseRedirect("/jenis/")
	context = {
	'page_title':'jenis',
	
	}
	return render(request, 'Master_data/Data_jenis/input.html',  context)		

def EditJenisView(request, editj_id):	
	Edit_jenis = Modeljenis.objects.get(id=editj_id)

	data = {
		'nama_jenis'	: Edit_jenis.nama_jenis,		
		'pembayaran_pajak'	: Edit_jenis.pembayaran_pajak,		
		'keterangan'	: Edit_jenis.keterangan,		
	}
	form_jenis = FormJenis(request.POST or None, initial=data, instance=Edit_jenis)

	if request.method == 'POST':
		if form_jenis.is_valid():
			form_jenis.save()
			return redirect('jenis')

	context = {
	'page_title':'Tabel',	
	'form_jenis':form_jenis,
	}
	return render(request, 'Master_data/Data_jenis/edit.html',  context)		

#------------------ Obejct
def ObjekView(request):
	tampil_objek = ModelObjek.objects.all()
	context = {
	'page_title':'Tabel',
	'tampil_objek': tampil_objek,
	}
	return render(request, 'Master_data/Data_objek/tabel.html',  context)	

def TambahobjekView(request):
	select_kecamatan = Modelkecamatan.objects.all()
	if request.method == 'POST':
		ModelObjek.objects.create(
			no_pajak = request.POST['no_pajak'],
			nama_pajak = request.POST['nama_pajak'],
			lokasi = request.POST['lokasi'],			
			kecamatan = request.POST['kecamatan'],			
			kelurahan = request.POST['kelurahan'],			
			tanggal = request.POST['tanggal'],			
			)
		return HttpResponseRedirect("/objek/")
	context = {
	'page_title':'objek',
	'select_kecamatan':select_kecamatan,
	
	}
	return render(request, 'Master_data/Data_objek/input.html',  context)		

def hapusobjekView(request, hapuso_id):
	ModelObjek.objects.filter(id=hapuso_id).delete()
	return redirect('objek')		



def EditObjekView(request, edito_id):	
	Edit_objek = ModelObjek.objects.get(id=edito_id)

	data = {
		'no_pajak'	: Edit_objek.no_pajak,		
		'nama_pajak'	: Edit_objek.nama_pajak,		
		'lokasi'	: Edit_objek.lokasi,		
		'kecamatan'	: Edit_objek.kecamatan,		
		'kelurahan'	: Edit_objek.kelurahan,		
		'tanggal'	: Edit_objek.tanggal,		
	}
	form_objek = FormObjek(request.POST or None, initial=data, instance=Edit_objek)

	if request.method == 'POST':
		if form_objek.is_valid():
			form_objek.save()
			return redirect('objek')

	context = {
	'page_title':'Tabel',	
	'form_objek':form_objek,
	}
	return render(request, 'Master_data/Data_objek/edit.html',  context)		
#----------------bangunan
def BangunankView(request):
	tampil_bangunan = Modelbangunan.objects.all()
	context = {
	'page_title':'Tabel',
	'tampil_bangunan': tampil_bangunan,
	}
	return render(request, 'Master_data/Data_bangunan/tabel.html',  context)		

def TambahbangunanView(request):	
	if request.method == 'POST':
		Modelbangunan.objects.create(
			nama_bangunan = request.POST['nama_bangunan'],
			nilai_jual = request.POST['nilai_jual'],
			keterangan = request.POST['keterangan'],			
			)
		return HttpResponseRedirect("/bangunan/")
	context = {
	'page_title':'bangunan',	
	
	}
	return render(request, 'Master_data/Data_bangunan/input.html',  context)		
def hapusbangunanView(request, hapusb_id):
	Modelbangunan.objects.filter(id=hapusb_id).delete()
	return redirect('bangunan')		

def EditbangunanView(request, editb_id):	
	Edit_bangunan = Modelbangunan.objects.get(id=editb_id)

	data = {
		'nama_bangunan'	: Edit_bangunan.nama_bangunan,		
		'nilai_jual'	: Edit_bangunan.nilai_jual,		
		'keterangan'	: Edit_bangunan.keterangan,		
	}
	form_bangunan = FormBangunan(request.POST or None, initial=data, instance=Edit_bangunan)

	if request.method == 'POST':
		if form_bangunan.is_valid():
			form_bangunan.save()
			return redirect('bangunan')

	context = {
	'page_title':'Tabel',	
	'form_bangunan':form_bangunan,
	}
	return render(request, 'Master_data/Data_bangunan/edit.html',  context)			

#----------------bangunan
def BumiView(request):
	tampil_bumi = Modelbumi.objects.all()
	context = {
	'page_title':'Tabel',
	'tampil_bumi': tampil_bumi,
	}
	return render(request, 'Master_data/Data_bumi/tabel.html',  context)			

def TambahBumiView(request):	
	if request.method == 'POST':
		Modelbumi.objects.create(
			nama_kelompok = request.POST['nama_kelompok'],
			luas = request.POST['luas'],
			nilai_jual = request.POST['nilai_jual'],			
			keterangan = request.POST['keterangan'],			
			)
		return HttpResponseRedirect("/bumi/")
	context = {
	'page_title':'Tambah',	
	
	}
	return render(request, 'Master_data/Data_bumi/input.html',  context)			
def hapusBumiView(request, hapusbu_id):
	Modelbumi.objects.filter(id=hapusbu_id).delete()
	return redirect('bumi')		

def EditbumiView(request, editbu_id):	
	Edit_bumi = Modelbumi.objects.get(id=editbu_id)

	data = {
		'nama_kelompok'	: Edit_bumi.nama_kelompok,		
		'luas'	: Edit_bumi.luas,	
		'nilai_jual'	: Edit_bumi.nilai_jual,		
		'keterangan'	: Edit_bumi.keterangan,		
	}
	form_bumi = FormBumi(request.POST or None, initial=data, instance=Edit_bumi)

	if request.method == 'POST':
		if form_bumi.is_valid():
			form_bumi.save()
			return redirect('bumi')

	context = {
	'page_title':'Edit',	
	'form_bumi':form_bumi,
	}
	return render(request, 'Master_data/Data_bumi/edit.html',  context)			

#----------------SPPT
def SPPTView(request):
	tampil_sppt = Modelsppt.objects.all()
	context = {
	'page_title':'Tabel',
	'tampil_sppt': tampil_sppt,
	}
	return render(request, 'Master_data/Data_sppt/tabel.html',  context)			
def TambahSPPTView(request):
	select_wajib = ModelWajib.objects.all()		
	select_pajak = ModelObjek.objects.all()		
	select_bangunan = Modelbangunan.objects.all()			
	select_bumi = Modelbumi.objects.all()			

	if 'cari_wajib' in request.GET:
		cari_wajib=request.GET['cari_wajib']
		post_wajib = ModelWajib.objects.filter(id=cari_wajib)
	else:
		post_wajib = ModelWajib.objects.filter(id=None)		

	if 'cari_no_pajak' in request.GET:
		cari_no_pajak=request.GET['cari_no_pajak']
		post_pajak = ModelObjek.objects.filter(no_pajak=cari_no_pajak)
	else:
		post_pajak = ModelObjek.objects.filter(no_pajak=None)				

	if 'cari_bangunan' in request.GET:
		cari_bangunan=request.GET['cari_bangunan']
		post_bangunan = Modelbangunan.objects.filter(id=cari_bangunan)
	else:
		post_bangunan = Modelbangunan.objects.filter(id=None)				

	if request.method == 'POST':
		Modelsppt.objects.create(
			nama_lengkap = request.POST['nama_lengkap'],
			nomor_pajak = request.POST['nomor_pajak'],
			nama_pajak = request.POST['nama_pajak'],			
			luas_bumi = request.POST['luas_bumi'],			
			luas_bangunan = request.POST['luas_bangunan'],			
			nama_bangunan = request.POST['nama_bangunan'],			
			nilai_jual = request.POST['nilai_jual'],			
			)
		return HttpResponseRedirect("/sppt/")
	context = {
	'page_title':'Tambah',	
	
	}
	context = {
	'page_title':'Tabel',
	'select_wajib': select_wajib,
	'select_pajak': select_pajak,
	'select_bangunan': select_bangunan,
	'select_bumi': select_bumi,
	'post_wajib': post_wajib,
	'post_pajak': post_pajak,
	'post_bangunan': post_bangunan,
	}
	return render(request, 'Master_data/Data_sppt/input.html',  context)				

def hapusSPPTView(request, hapussppt_id):
	Modelsppt.objects.filter(id=hapussppt_id).delete()
	return redirect('sppt')			

#----------------pembayaran
def PembayaraView(request):
	tampil_pembayaran = Modelpembayaranpajak.objects.all()	
	context = {
	'page_title':'Tabel',
	'tampil_pembayaran': tampil_pembayaran,
	}
	return render(request, 'Master_data/Data_pembayaran/tabel.html',  context)				
def CetakPembayaraView(request):
	if 'cetak' in request.GET:
		cetak=request.GET['cetak']
		cetak_bayar = Modelpembayaranpajak.objects.filter(id=cetak)
	else:
		cetak_bayar = Modelpembayaranpajak.objects.filter(id=None)						
	context = {
	'page_title':'Tabel',
	'cetak_bayar': cetak_bayar,
	}
	return render(request, 'Master_data/Data_pembayaran/cetak.html',  context)					

def TambahPembayaraView(request):
	select_pajak1 = Modelsppt.objects.all()		
	select_jenis = Modeljenis.objects.all()	

	if 'cari_no_pajak1' in request.GET:
		cari_no_pajak1=request.GET['cari_no_pajak1']
		post_pajak = Modelsppt.objects.filter(nomor_pajak=cari_no_pajak1)
	else:
		post_pajak = Modelsppt.objects.filter(id=None)				

	if 'cari_jenis_p' in request.GET:
		cari_jenis_p=request.GET['cari_jenis_p']
		post_jen = Modeljenis.objects.filter(id=cari_jenis_p)
	else:
		post_jen = Modeljenis.objects.filter(id=None)						

	if request.method == 'POST':
		Modelpembayaranpajak.objects.create(
			nama_lengkap = request.POST['nama_lengkap'],
			jumlah_pembayaran = request.POST['jumlah_pembayaran'],
			nomor_pajak = request.POST['nomor_pajak'],
			nama_pajak = request.POST['nama_pajak'],			
			luas_bumi = request.POST['luas_bumi'],			
			luas_bangunan = request.POST['luas_bangunan'],			
			tahun_pajak = request.POST['tahun_pajak'],			
			jatuh_tempo = request.POST['jatuh_tempo'],			
			denda = request.POST['denda'],			
			total_bayar = request.POST['total_bayar'],			
			tanggal = request.POST['tanggal'],			
			status = request.POST['status'],			
			)
		return HttpResponseRedirect("/pembayaran/")


	context = {
	'page_title':'Tabel',	
	'select_pajak1': select_pajak1,
	'select_jenis': select_jenis,
	'post_pajak': post_pajak,
	'post_jen': post_jen,
	
	}
	return render(request, 'Master_data/Data_pembayaran/input.html',  context)					
def hapusBayarView(request, hapusby_id):
	Modelpembayaranpajak.objects.filter(id=hapusby_id).delete()	
	return redirect('pembayaran')			

#----------------berkas 
def BerkasView(request):
	tampil_berkas = ModeUpload.objects.all()	
	context = {
	'page_title':'Tabel',
	'tampil_berkas': tampil_berkas,
	}
	return render(request, 'Master_data/Data_berkas/tabel.html',  context)					
def TambahBerkasView(request):	
	formberkas = FormUpload()	
	if request.method == 'POST':
		formberkas = FormUpload(request.POST,  request.FILES)
		if formberkas.is_valid():
			formberkas.save()
			return redirect('berkas')

	context = {
	'page_title':'Tabel',	
	'formberkas': formberkas,
	}
	return render(request, 'Master_data/Data_berkas/input.html',  context)						
def hapusBerkasView(request, hapusberkas_id):
	ModeUpload.objects.filter(id=hapusberkas_id).delete()
	return redirect('berkas')			
def EditBerkasView(request, editberkas_id):	
	Edit_berkas = ModeUpload.objects.get(id=editberkas_id)

	data = {
		'nama_lengkap'	: Edit_berkas.nama_lengkap,		
		'nom_pajak'	: Edit_berkas.nom_pajak,	
		'nama_pajak'	: Edit_berkas.nama_pajak,		
		'upload'	: Edit_berkas.upload,		
	}
	form_upload = FormUpload(request.POST or None, request.FILES, initial=data, instance=Edit_berkas)

	if request.method == 'POST':
		if form_upload.is_valid():
			form_upload.save()
			return redirect('berkas')

	context = {
	'page_title':'Edit',	
	'form_upload':form_upload,
	}
	return render(request, 'Master_data/Data_berkas/edit.html',  context)			







#----------------menu laporan
def MenuView(request):	
	context = {
	'page_title':'Tabel',	
	}
	return render(request, 'Master_data/Laporan/menu.html',  context)						

def LPWajibView(request):
	lp_data = ModelWajib.objects.all()
	context = {
	'page_title':'Wajib',
	'lp_data': lp_data,
	}
	return render(request, 'Master_data/Laporan/lp_wajib.html',  context)	
def LPPembayaraView(request):
	lp_pembayaran = Modelpembayaranpajak.objects.all()	
	context = {
	'page_title':'Tabel',
	'lp_pembayaran': lp_pembayaran,
	}
	return render(request, 'Master_data/Laporan/lp_pembayaran.html',  context)					
def LPSPPTView(request):
	lp_sppt = Modelsppt.objects.all()
	context = {
	'page_title':'Tabel',
	'lp_sppt': lp_sppt,
	}
	return render(request, 'Master_data/Laporan/lp_sppt.html',  context)				





#-----------WEBSITE PERPAJAKAN---------------------------
def WEBSITE(request):
	#lp_sppt = Modelsppt.objects.all()
	context = {
	'page_title':'Tabel',	
	}
	return render(request, 'WEBSITE/website.html',  context)				
def caridata(request):
	if 'c_ok' in request.GET:
		c_ok=request.GET['c_ok']
		cari_dt = Modelsppt.objects.filter(nomor_pajak=c_ok)
	else:
		cari_dt = Modelsppt.objects.filter(nomor_pajak=None)
								
	context = {
	'page_title':'Tabel',	
	'cari_dt': cari_dt,
	}
	return render(request, 'WEBSITE/cari_data.html',  context)					