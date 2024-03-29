from django.contrib import admin
from todo.models import Todo

class todoAdmin(admin.ModelAdmin):
    a = ['title','details','date']
admin.site.register(Todo,todoAdmin)
# Register your models here.
