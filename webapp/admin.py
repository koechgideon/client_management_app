from django.contrib import admin


from .models import Client,Product,Tag,Order

admin.site.register(Client)
admin.site.register(Product)
admin.site.register(Tag)
admin.site.register(Order)