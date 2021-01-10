from django.contrib import admin
from .models import Image, Contact
# Register your models here.
@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = [ 'title', 'created']
    list_filter = ['created']

admin.site.register(Contact)