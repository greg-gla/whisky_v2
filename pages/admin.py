from django.contrib import admin
from pages.models import Distillery, Whisky, Rating

# Register your models here.
admin.site.register(Distillery)
admin.site.register(Whisky)
admin.site.register(Rating)