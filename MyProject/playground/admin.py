from django.contrib import admin
from .models import Playground, Offer

class OfferAdmin(admin.ModelAdmin):
    list_display = ('code','discount')

class PlaygroundAdmin(admin.ModelAdmin):
    list_display = ('name','price','stock')


admin.site.register(Offer, OfferAdmin)
admin.site.register(Playground, PlaygroundAdmin)


