# -*- coding: utf-8 -*-

import datetime

from django.contrib import admin
from django.http import HttpResponseRedirect
from django import forms

from .models import *

# class OpinioniInline(admin.TabularInline):
#     model = Opinione
#     extra = 0

# class NotiziaModelForm( forms.ModelForm ):
#     descrizione = forms.CharField( widget=forms.Textarea(attrs={
#         'cols': 100,
#         'rows': 12
#         }))
#     class Meta:
#         model = Notizia

# class NotiziaAdmin(admin.ModelAdmin):
#     form = NotiziaModelForm
#     prepopulated_fields = {"parametro": ("titolo", )}
#     inlines = [
#         OpinioniInline,
#     ]

#     list_display = ('titolo', 'stato', 'data_inserimento', 'data_ultima_modifica')
#     actions = ['anticipa', 'posticipa', 'set_fase1']


#     def save_model(self, request, obj, form, change):

#         obj.save()

#         if change == False:
#             obj.parametro = obj.parametro + "-" + unicode(obj.id).zfill(3)
#             obj.save()

#     #def anticipa(self, request, queryset):
#         #selected = request.POST.getlist(admin.ACTION_CHECKBOX_NAME)
#         #return HttpResponseRedirect("/admin/notizie/anticipa?ids=%s" % (",".join(selected)))

#     #def posticipa(self, request, queryset):
#         #selected = request.POST.getlist(admin.ACTION_CHECKBOX_NAME)
#         #return HttpResponseRedirect("/admin/notizie/posticipa?ids=%s" % (",".join(selected)))

#     #def set_fase1(self, request, queryset):
#         #selected = request.POST.getlist(admin.ACTION_CHECKBOX_NAME)
#         #return HttpResponseRedirect("/admin/notizie/posticipa?ids=%s" % (",".join(selected)))

#     #set_fase1.short_description = "Riporta in fase 1"

# class OpinioneAdmin(admin.ModelAdmin):
#     prepopulated_fields = {"parametro": ("titolo", )}

# class MetaVariabiliInline(admin.TabularInline):
#     readonly_fields = ('variabile', 'descrizione')
#     can_delete = False
#     model = MetaVariabile
#     extra = 0

# class MetaRegolaModelForm( forms.ModelForm ):
#     view = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
#     meta_title = forms.CharField(widget=forms.TextInput(attrs={'size':'65'}))
#     meta_description = forms.CharField( widget=forms.Textarea(attrs={
#         'cols': 100,
#         'rows': 5
#         }))
#     class Meta:
#         model = MetaRegola

# class MetaRegolaAdmin(admin.ModelAdmin):
#     form = MetaRegolaModelForm
#     inlines = [
#         MetaVariabiliInline,
#     ]


admin.site.register(Azienda)
admin.site.register(Prodotto)
admin.site.register(Tag)
