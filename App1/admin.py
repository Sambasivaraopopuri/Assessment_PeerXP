from django.contrib import admin

# Register your models here.
from .models import Login,Ticket

admin.site.register(Login)
admin.site.register(Ticket)
