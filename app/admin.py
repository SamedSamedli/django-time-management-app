from django.contrib import admin
from app.models import TODO, Blocklist
# Register your models here.
admin.site.register(TODO)
admin.site.register(Blocklist)