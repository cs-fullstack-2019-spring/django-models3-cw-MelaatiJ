from django.contrib import admin

# Register your models here.

# from the folder models import class car
# without this step it will not display on the admins site
from .models import Car
admin.site.register(Car)
