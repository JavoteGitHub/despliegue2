from django.contrib import admin
from .models import TejidoMama 

class TejidoMamaAdmin(admin.ModelAdmin):
    list_display = ('partP','temperatura','color','inflamacion',)



admin.site.register (TejidoMama,TejidoMamaAdmin)