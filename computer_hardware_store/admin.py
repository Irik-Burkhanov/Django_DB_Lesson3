from django.contrib import admin
from computer_hardware_store import models
# Register your models here.

@admin.register(models.Computer)
class ComputerAdmin(admin.ModelAdmin):
    list_display = ('title','builder')

@admin.register(models.Builder)
class BuilderAdmin(admin.ModelAdmin):
    list_display = ('first_name','surname')

@admin.register(models.CPU)
class CPUAdmin(admin.ModelAdmin):
    list_display = ('CPU_model',)

@admin.register(models.GPU)
class GPUAdmin(admin.ModelAdmin):
    list_display = ('GPU_model',)

@admin.register(models.Storage)
class StorageAdmin(admin.ModelAdmin):
    list_display = ('amount',)