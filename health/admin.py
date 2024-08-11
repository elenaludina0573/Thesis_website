from django.contrib import admin

from health.models import Client, Record, Diagnostics


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'surname', 'phone', 'email', 'address', 'birth_date', 'created_at']


@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ['pk', 'client', 'record_date', 'record_time', 'doctor']


# @admin.register(Diagnostics)
# class DiagnosticsAdmin(admin.ModelAdmin):
#     list_display = ['pk', 'record', 'name', 'result', 'diagnosis']
