from django.contrib import admin
from .models import User
#admin.site._registry(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'password', 'email')
admin.site.register(User,UserAdmin)
#admin.site.registry(User,UserAdmin)

# Register your models here.
