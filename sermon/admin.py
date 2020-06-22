from django.contrib import admin
from .models import Sermon

class SermonAdmin(admin.ModelAdmin):
	models = Sermon
	prepopulated_fields = { "slug": ('title',)}
admin.site.register(Sermon, SermonAdmin)
# Register your models here.
