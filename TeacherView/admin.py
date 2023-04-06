from django.contrib import admin
from .models import *
admin.site.register(Experiment)
admin.site.register(Equipment)
admin.site.register(Chemicals)
admin.site.register(Steps)