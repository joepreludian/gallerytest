from django.contrib import admin
from gallery import models


class FotoAdminInline(admin.StackedInline):
    model = models.Foto
    extra = 0


class GaleriaAdmin(admin.ModelAdmin):
    model = models.Galeria
    inlines = (FotoAdminInline, )

admin.site.register(models.Galeria, GaleriaAdmin)