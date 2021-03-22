from django.contrib import admin

from .models import *

admin.site.site_header = "Ramadan_qa Admin"
admin.site.site_title = "Ramadan_qa Admin Area"
admin.site.undex_title = "Welcom to the Ramadan_qa Admin"

admin.site.register(Answer)
admin.site.register(Category)

