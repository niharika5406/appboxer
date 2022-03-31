from django.contrib import admin
from .models import ZombieSurvivalSocialNetwork

# Register your models here.
admin.site.register(ZombieSurvivalSocialNetwork)

class ZombieSurvivalSocialNetworkAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'gender','location')