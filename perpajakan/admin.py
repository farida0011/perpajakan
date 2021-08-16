from django.contrib import admin

# Register your models here. daftar model yang telah kita buat
from .models import ModelWajib, Modelkecamatan, Modeljenis, ModelObjek, Modelbangunan, Modelbumi, Modelsppt, Modelpembayaranpajak, ModeUpload, ModelCoba

admin.site.register(ModelWajib)
admin.site.register(Modelkecamatan)
admin.site.register(Modeljenis)
admin.site.register(ModelObjek)
admin.site.register(Modelbangunan)
admin.site.register(Modelbumi)
admin.site.register(Modelsppt)
admin.site.register(Modelpembayaranpajak)
admin.site.register(ModeUpload)
admin.site.register(ModelCoba)