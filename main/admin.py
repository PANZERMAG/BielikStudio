from django.contrib import admin

from .models import PortfolioItem, TechnologiesModel, TypeOfProjModel

# Register your models here.

admin.site.register(PortfolioItem)
admin.site.register(TechnologiesModel)
admin.site.register(TypeOfProjModel)
