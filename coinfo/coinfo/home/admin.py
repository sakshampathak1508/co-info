from django.contrib import admin
from . models import Oxygen,Hospital,Plasma,Medicine
# Register your models here.



@admin.register(Hospital)
class PostAdmin(admin.ModelAdmin):
    # class Media:
        # js= ('/static/js/tinyinject.js',)
    list_display = ('type_of_bed','name','number_of_beds','time_stamp')
    list_filter = ('type_of_bed','number_of_beds','city','state')
    list_editable = ('time_stamp',)
    ordering = ('name','type_of_bed')
    
@admin.register(Oxygen)
class PostAdmin(admin.ModelAdmin):
    # class Media:
        # js= ('/static/js/tinyinject.js',)
    list_display = ('type_of_facility','name','quantity','time_stamp')
    list_editable = ('time_stamp','quantity')
    list_filter = ('type_of_facility','quantity','city','state')
    ordering = ('type_of_facility','name')

@admin.register(Plasma)
class PostAdmin(admin.ModelAdmin):
    # class Media:
        # js= ('/static/js/tinyinject.js',)
    list_display = ('blood_group','name')
    # list_editable = ('','','',)
    # ordering = ('','-',)

@admin.register(Medicine)
class PostAdmin(admin.ModelAdmin):
    list_display = ('name',)
    # list_editable = ('','','',)
    # ordering = ('','-',)


