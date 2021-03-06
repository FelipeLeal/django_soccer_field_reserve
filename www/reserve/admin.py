from django.contrib import admin
from django import forms
from .models import FieldType, Field, Price, Block, Reserve
from django.core import mail
from pprint import pprint
from soccer_field_reserve.settings import EMAIL_USE_TLS, EMAIL_HOST, EMAIL_BACKEND

import os


# Register your models here.
class FieldTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    ordering = ['id']


class FieldAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'field_type')
    ordering = ['id']


class PriceAdmin(admin.ModelAdmin):
    list_display = ('id', 'price', 'reservation_time', 'field')
    ordering = ['id']


class BlockAdmin(admin.ModelAdmin):
    list_display = ('id', 'start_time', 'end_time')
    ordering = ['id']

    # def has_add_permission(self, request, obj=None):
    #     return False
    #
    # def has_change_permission(self, request, obj=None):
    #     return False


class ReserveForm(forms.ModelForm):
    # day = forms.DateField(help_text="Enter a date between now and 4 weeks.")

    class Meta:
        model = Reserve
        fields = ['user', 'day', 'block', 'reserve_price']

    # def clean_day(self):
    #     date = self.cleaned_data.get('day')
    #     if date < datetime.date.today():
    #         raise forms.ValidationError(
    #             'Invalid value - renewal in past'
    #         )
    #     return self.cleaned_data


class ReserveAdmin(admin.ModelAdmin):
    form = ReserveForm
    fields = [('day', 'block'), 'reserve_price']
    list_display = ('user', 'day', 'block', 'reserve_price')

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        mail.send_mail(
            subject='Confimarción reserva',
            message=f"Estimado {obj.user.username}, Su reserva se ha realizado con éxito.",
            from_email=os.getenv('EMAIL_HOST_USER'),
            recipient_list=[obj.user.email]
        )
        super(ReserveAdmin, self).save_model(request, obj, form, change)


admin.site.register(FieldType, FieldTypeAdmin)
admin.site.register(Field, FieldAdmin)
admin.site.register(Price, PriceAdmin)
admin.site.register(Block, BlockAdmin)
admin.site.register(Reserve, ReserveAdmin)
