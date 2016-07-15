from django.contrib import admin

# Register your models here.
from .models import Interest, User
admin.site.register(Interest)
admin.site.register(User)
