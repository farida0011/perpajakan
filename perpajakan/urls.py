from django.conf.urls import url, include
from django.conf.urls.static import static
from perpajakan import settings
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views
from django.contrib import admin
from django.urls import path
from . import views
from .views import index, HomeView, LogoutView, WajibView, TambahWajibView, hapuswajibView, EditwajibView, KecamatanView, TambahkecamatanView, hapuskecamatanView, EditkecamatanView, JenisView, hapusjenisView, TambahjenisView, EditJenisView, ObjekView, TambahobjekView, hapusobjekView, EditObjekView, BangunankView, TambahbangunanView, hapusbangunanView, EditbangunanView, BumiView, TambahBumiView, hapusBumiView, EditbumiView, SPPTView, TambahSPPTView, hapusSPPTView, PembayaraView, TambahPembayaraView, hapusBayarView, BerkasView, MenuView, CetakPembayaraView, LPWajibView, LPPembayaraView, LPSPPTView, TambahBerkasView, hapusBerkasView, EditBerkasView, WEBSITE, caridata

urlpatterns = [
    url(r'^$',index, name="index"),
    url(r'^Home/$', HomeView, name="Home"),
    url(r'^logout/$',LogoutView, name="logout"),
    
    #------------wajib bayar
    url(r'^wajib/$', WajibView, name="wajib"),    
    url(r'^t_wajib/$', TambahWajibView, name="t_wajib"),    
    url(r'^hapusj_id/(?P<hapusj_id>[0-9]+)$',hapuswajibView, name="hapusj_id"),
    url(r'^editw_id/(?P<editw_id>[0-9]+)$',EditwajibView, name="editw_id"),

    #------------wajib bayar
    url(r'^kecamatan/$', KecamatanView, name="kecamatan"),    
    url(r'^t_kecamatan/$', TambahkecamatanView, name="t_kecamatan"),    
    url(r'^hapusk_id/(?P<hapusk_id>[0-9]+)$',hapuskecamatanView, name="hapusk_id"),    
    url(r'^edit_kecamatan/(?P<editk_id>[0-9]+)$',EditkecamatanView, name="edit_kecamatan"),        

#------------jenis
    url(r'^jenis/$', JenisView, name="jenis"),        
    url(r'^hapus_jenis/(?P<hapusje_id>[0-9]+)$',hapusjenisView, name="hapus_jenis"),        
    url(r'^t_jenis/$', TambahjenisView, name="t_jenis"),            
    url(r'^edit_jenis/(?P<editj_id>[0-9]+)$',EditJenisView, name="edit_jenis"),            

#------------objek
    url(r'^objek/$', ObjekView, name="objek"),        
    url(r'^t_objek/$', TambahobjekView, name="t_objek"),            
    url(r'^hapus_objek/(?P<hapuso_id>[0-9]+)$',hapusobjekView, name="hapus_objek"),            
    url(r'^edit_objek/(?P<edito_id>[0-9]+)$',EditObjekView, name="edit_objek"),            

#------------bangunan
    url(r'^bangunan/$', BangunankView, name="bangunan"),            
    url(r'^t_bangunan/$', TambahbangunanView, name="t_bangunan"),                
    url(r'^hapus_bangunan/(?P<hapusb_id>[0-9]+)$',hapusbangunanView, name="hapus_bangunan"),                
    url(r'^edit_bangunan/(?P<editb_id>[0-9]+)$',EditbangunanView, name="edit_bangunan"),                
#------------kelompok bumi
    url(r'^bumi/$', BumiView, name="bumi"),                
    url(r'^t_bumi/$', TambahBumiView, name="t_bumi"),                
    url(r'^hapus_bumi/(?P<hapusbu_id>[0-9]+)$',hapusBumiView, name="hapus_bumi"),                    
    url(r'^edit_bumi/(?P<editbu_id>[0-9]+)$',EditbumiView, name="edit_bumi"),                        

#------------SPPT
    url(r'^sppt/$', SPPTView, name="sppt"),                    
    url(r'^t_sppt/$', TambahSPPTView, name="t_sppt"),               
    url(r'^hapus_sppt/(?P<hapussppt_id>[0-9]+)$',hapusSPPTView, name="hapus_sppt"),                             

#------------pembayaran
    url(r'^pembayaran/$', PembayaraView, name="pembayaran"),                    
    url(r'^t_pembayaran/$', TambahPembayaraView, name="t_pembayaran"),                        
    url(r'^hapus_bayar/(?P<hapusby_id>[0-9]+)$',hapusBayarView, name="hapus_bayar"),  
    url(r'^cetak/$', CetakPembayaraView, name="cetak"),                        

#------------berkas
    url(r'^berkas/$', BerkasView, name="berkas"),                    
    url(r'^t_berkas/$', TambahBerkasView, name="t_berkas"),                    
    url(r'^hapus_berkas/(?P<hapusberkas_id>[0-9]+)$',hapusBerkasView, name="hapus_berkas"),      
    url(r'^edit_berkas/(?P<editberkas_id>[0-9]+)$',EditBerkasView, name="edit_berkas"),      


#------------menu laporan
    url(r'^menu/$', MenuView, name="menu"),                        
    url(r'^lp_wajib/$', LPWajibView, name="lp_wajib"),                            
    url(r'^lp_pembayaran/$', LPPembayaraView, name="lp_pembayaran"),                                
    url(r'^lp_sppt/$', LPSPPTView, name="lp_sppt"),                                    




#-----------MY WEBSITE------------------
    url(r'^website/$', WEBSITE, name="website"),                                    
    url(r'^c_data/$', caridata, name="c_data"),                                    
    
    
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    #urlpatterns += static(settings.STATIC_URL, document_root = None )
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    