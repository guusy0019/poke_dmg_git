from django.contrib import admin
from .models import PokeModel, PokeMove

# Register your models here.
admin.site.register(PokeModel)
admin.site.register(PokeMove)
