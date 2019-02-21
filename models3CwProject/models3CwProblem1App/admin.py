from django.contrib import admin

# Register your models here.


#from models file import class Book
#without this step it will not display on the admins page
from .models import Book
admin.site.register(Book)
